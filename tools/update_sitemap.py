#!/usr/bin/env python3
"""Rebuild sitemap.xml from canonical catalogue pages and product review dates."""

import argparse
import sys
from datetime import date
from html.parser import HTMLParser
from pathlib import Path


class PageMetadata(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.canonicals = []
        self.review_dates = []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "link" and attrs.get("rel") == "canonical" and attrs.get("href"):
            self.canonicals.append(attrs["href"])
        if tag == "time" and attrs.get("datetime"):
            self.review_dates.append(attrs["datetime"])


def sitemap_entries(root):
    entries = []
    for path in sorted(root.rglob("index.html")):
        rel = path.relative_to(root).as_posix()
        metadata = PageMetadata(path)
        if len(metadata.canonicals) != 1:
            raise ValueError(f"{rel}: expected exactly one canonical URL")

        canonical = metadata.canonicals[0]
        review_date = None
        if rel.startswith("products/"):
            if len(metadata.review_dates) != 1:
                raise ValueError(f"{rel}: expected exactly one catalogue review date")
            review_date = metadata.review_dates[0]
            date.fromisoformat(review_date)

        entries.append((canonical, review_date))
    return entries


def render(entries):
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for canonical, review_date in entries:
        lines.append("  <url>")
        lines.append(f"    <loc>{canonical}</loc>")
        if review_date:
            lines.append(f"    <lastmod>{review_date}</lastmod>")
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def main(root):
    entries = sitemap_entries(root)
    target = root / "sitemap.xml"
    target.write_text(render(entries), encoding="utf-8")
    product_count = sum(1 for _, review_date in entries if review_date)
    print(f"WROTE: {target} ({len(entries)} URLs; {product_count} product lastmod dates)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1] / "site")
    args = parser.parse_args()
    try:
        main(args.root.resolve())
    except (OSError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
