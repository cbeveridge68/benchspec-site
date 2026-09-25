#!/usr/bin/env python3
"""Dependency-free checks for the hand-authored catalogue; not a site generator."""

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ORIGIN = "https://benchspec.com.au"


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.tags = []
        self.text = []
        self.jsonld = []
        self.active_json = None
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.active_json = []

    def handle_data(self, data):
        if self.active_json is not None:
            self.active_json.append(data)
        else:
            self.text.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.active_json is not None:
            self.jsonld.append(json.loads("".join(self.active_json)))
            self.active_json = None

    def select(self, tag, **attrs):
        return [a for t, a in self.tags if t == tag and all(a.get(k) == v for k, v in attrs.items())]


def check(root, publication=False):
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    pages = {p: Page(p) for p in root.rglob("*.html")}
    require(bool(pages), "No HTML pages found")
    canonicals = set()
    descriptions = set()
    for path, page in pages.items():
        rel = path.relative_to(root).as_posix()
        route = "/" + rel.removesuffix("index.html") if path.name == "index.html" else "/" + rel
        expected = ORIGIN + route
        prefix = f"{rel}: "
        blockers = [a["data-publication-blocker"] for _, a in page.tags if "data-publication-blocker" in a]
        if blockers:
            message = prefix + "publication blocked: " + ", ".join(blockers)
            if publication:
                require(False, message)
            else:
                print("OPEN:", message)
        canonical = page.select("link", rel="canonical")
        require(len(canonical) == 1 and canonical[0].get("href") == expected, prefix + "incorrect canonical")
        canonicals.add(expected)
        require(len(page.select("h1")) == 1, prefix + "expected one H1")
        require(bool(page.select("meta", name="viewport")), prefix + "viewport missing")
        require(bool(page.select("html", lang="en-AU")), prefix + "language missing")
        desc = page.select("meta", name="description")
        require(len(desc) == 1 and bool(desc[0].get("content")), prefix + "description missing")
        if desc:
            require(desc[0]["content"] not in descriptions, prefix + "duplicate description")
            descriptions.add(desc[0]["content"])
        ids = [a["id"] for _, a in page.tags if "id" in a]
        require(len(ids) == len(set(ids)), prefix + "duplicate IDs")
        require(all(a.get("type") == "application/ld+json" and "src" not in a for a in page.select("script")), prefix + "application script present")
        for tag, attrs in page.tags:
            if tag == "img":
                require(bool(attrs.get("alt")), prefix + "image needs descriptive alt text")
                require("width" in attrs and "height" in attrs, prefix + "image dimensions missing")
            urls = [attrs[k] for k in ("href", "src") if k in attrs]
            urls += [part.strip().split()[0] for part in attrs.get("srcset", "").split(",") if part.strip()]
            for url in urls:
                parsed = urlsplit(urljoin(expected, url))
                if parsed.netloc != "benchspec.com.au":
                    continue
                target = root / unquote(parsed.path).lstrip("/")
                if parsed.path.endswith("/"):
                    target /= "index.html"
                require(target.is_file(), prefix + f"missing internal target: {url}")
                if parsed.fragment and target in pages:
                    require(any(a.get("id") == parsed.fragment for _, a in pages[target].tags), prefix + f"missing fragment: {url}")
        for data in page.jsonld:
            require(data.get("@context") == "https://schema.org", prefix + "invalid JSON-LD context")
            if data.get("@type") != "Product":
                continue
            if publication:
                require(bool(data.get("image")) and bool(page.select("img")), prefix + "actual-item images required before publication")
            visible = " ".join(page.text)
            for field in ("mpn", "model", "sku"):
                require(bool(data.get(field)) and data[field] in visible, prefix + f"{field} disagrees with page")
            require(data.get("url") == expected, prefix + "Product URL mismatch")
            require(data.get("@id") == expected + "#product", prefix + "Product ID mismatch")
            offer = data.get("offers", {})
            require(offer.get("@type") == "Offer", prefix + "Offer missing")
            require(offer.get("priceCurrency") == "AUD", prefix + "unexpected currency")
            require(float(offer.get("price", 0)) > 0, prefix + "price missing")
            price = float(offer.get("price", 0))
            amount = f"A${price:,.0f}" if price.is_integer() else f"A${price:,.2f}"
            require(amount in visible, prefix + "visible/structured price mismatch")
            require(offer.get("itemCondition") == "https://schema.org/UsedCondition", prefix + "condition mismatch")
            # Specific recorded boundaries for the current catalogue, not a bare
            # "untested" label. Keep the same explicit disclosure in both places.
            verification_limits = (
                "functional operation has not been tested under process conditions",
                "units have not been dismantled, wetted or pressure-tested",
                "functional flow testing has not been performed; both meters remain dry",
                "wet or pressure testing has not been performed; ports remain capped",
                "packaging seals have been intentionally preserved. no functional or pressure testing has been performed",
                "no pressure or calibration test has been performed",
                "no loop or zero test has been performed",
                "no electrical or pressure test has been performed",
            )
            visible_normalised = " ".join(visible.lower().split())
            test_status = " ".join(
                str(prop.get("value", "")) for prop in data.get("additionalProperty", [])
                if prop.get("name") == "Test status"
            )
            test_normalised = " ".join(test_status.lower().split())
            require(any(limit in visible_normalised and limit in test_normalised
                        for limit in verification_limits),
                    prefix + "specific visible/structured verification limits missing or inconsistent")
            for url in data.get("image", []):
                require(url.startswith(ORIGIN + "/") and (root / urlsplit(url).path.lstrip("/")).is_file(), prefix + "invalid structured image: " + url)
            purchase = [a for a in page.select("a") if "purchase" in a.get("class", "").split()]
            if offer.get("availability") == "https://schema.org/InStock":
                require("Available" in visible, prefix + "available status missing")
                require(len(purchase) == 1 and purchase[0].get("href") == offer.get("url"), prefix + "purchase/Offer URL mismatch")
            elif offer.get("availability") == "https://schema.org/SoldOut":
                require("Sold" in visible and not purchase, prefix + "sold page retains purchase action or lacks sold status")
                homepage = pages[root / "index.html"]
                require(not any(a.get("href") == route for a in homepage.select("a")), prefix + "sold item remains in current stock")
            else:
                require(False, prefix + "unknown availability")
    sitemap = ET.parse(root / "sitemap.xml")
    urls = [node.text for node in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    require(set(urls) == canonicals and len(urls) == len(set(urls)), "Sitemap and canonical page URLs differ")
    robots = (root / "robots.txt").read_text()
    require(f"Sitemap: {ORIGIN}/sitemap.xml" in robots, "robots.txt sitemap differs")
    require("Disallow: /" not in robots, "robots.txt blocks crawling")
    for error in errors:
        print("FAIL:", error)
    if not errors:
        print(f"PASS: {len(pages)} HTML pages; internal links/assets, metadata, JSON-LD consistency, availability and sitemap")
    return bool(errors)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1] / "site")
    parser.add_argument("--publication", action="store_true", help="also reject missing required photographs and marked publication blockers")
    args = parser.parse_args()
    sys.exit(check(args.root.resolve(), args.publication))
