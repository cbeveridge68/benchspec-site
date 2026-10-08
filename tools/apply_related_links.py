from pathlib import Path
import re

ROOT = Path("site")
PRODUCT_ROOT = ROOT / "products"

CANDIDATES = {
    "infinity-fluids-cres-ilb-12-0010-k-xp-ptc": [
        ("/products/infinity-fluids-ptc-12-20-1p/", "Infinity Fluids PTC-12-20-1P temperature control system"),
        ("/products/perma-pure-fc125-240-5mp/", "Perma Pure FC125-240-5MP gas humidifier"),
        ("/products/mag-view-mvm-050-q/", "MAG-VIEW MVM-050-Q magnetic flow meter"),
        ("/products/omega-px2300-0-5bdi/", "OMEGA PX2300-0.5BDI differential pressure transmitter"),
    ],
    "infinity-fluids-ptc-12-20-1p": [
        ("/products/infinity-fluids-cres-ilb-12-0010-k-xp-ptc/", "Infinity Fluids CRES-ILB-12-0010-K-XP-PTC inline heater"),
        ("/products/perma-pure-fc125-240-5mp/", "Perma Pure FC125-240-5MP gas humidifier"),
        ("/products/mag-view-mvm-050-q/", "MAG-VIEW MVM-050-Q magnetic flow meter"),
        ("/products/omega-px2300-0-5bdi/", "OMEGA PX2300-0.5BDI differential pressure transmitter"),
    ],
    "mag-view-mvm-050-q": [
        ("/products/tsi-4140d/", "TSI 4140D thermal mass flow meter — sold catalogue record"),
        ("/products/omega-px2300-0-5bdi/", "OMEGA PX2300-0.5BDI differential pressure transmitter"),
        ("/products/sensortechnics-ctu7001gy7c2/", "SensorTechnics CTU7001GY7C2 pressure transmitter"),
        ("/products/perma-pure-fc125-240-5mp/", "Perma Pure FC125-240-5MP gas humidifier"),
    ],
    "omega-px2300-0-5bdi": [
        ("/products/sensortechnics-ctu7001gy7c2/", "SensorTechnics CTU7001GY7C2 pressure transmitter"),
        ("/products/swagelok-pgi-63s-pg300-la01/", "Swagelok PGI-63S-PG300-LA01 pressure gauge"),
        ("/products/mag-view-mvm-050-q/", "MAG-VIEW MVM-050-Q magnetic flow meter"),
        ("/products/tsi-4140d/", "TSI 4140D thermal mass flow meter — sold catalogue record"),
    ],
    "perma-pure-fc125-240-5mp": [
        ("/products/mag-view-mvm-050-q/", "MAG-VIEW MVM-050-Q magnetic flow meter"),
        ("/products/omega-px2300-0-5bdi/", "OMEGA PX2300-0.5BDI differential pressure transmitter"),
        ("/products/spirax-sarco-fa-150-71497/", "Spirax Sarco FA-150 / 71497 drain trap"),
        ("/products/infinity-fluids-cres-ilb-12-0010-k-xp-ptc/", "Infinity Fluids CRES-ILB-12-0010-K-XP-PTC inline heater"),
    ],
    "sensortechnics-ctu7001gy7c2": [
        ("/products/omega-px2300-0-5bdi/", "OMEGA PX2300-0.5BDI differential pressure transmitter"),
        ("/products/swagelok-pgi-63s-pg300-la01/", "Swagelok PGI-63S-PG300-LA01 pressure gauge"),
        ("/products/mag-view-mvm-050-q/", "MAG-VIEW MVM-050-Q magnetic flow meter"),
        ("/products/tsi-4140d/", "TSI 4140D thermal mass flow meter — sold catalogue record"),
    ],
    "spirax-sarco-fa-150-71497": [
        ("/products/swagelok-pgi-63s-pg300-la01/", "Swagelok PGI-63S-PG300-LA01 pressure gauge"),
        ("/products/swagelok-6lv-cw4bw4/", "Swagelok 6LV-CW4BW4 high-purity check valve"),
        ("/products/swagelok-ss-dltw4/", "Swagelok SS-DLTW4 high-purity diaphragm valve"),
        ("/products/perma-pure-fc125-240-5mp/", "Perma Pure FC125-240-5MP gas humidifier"),
    ],
    "swagelok-6lv-cw4bw4": [
        ("/products/swagelok-ss-dltw4/", "Swagelok SS-DLTW4 high-purity diaphragm valve"),
        ("/products/swagelok-pgi-63s-pg300-la01/", "Swagelok PGI-63S-PG300-LA01 pressure gauge"),
        ("/products/spirax-sarco-fa-150-71497/", "Spirax Sarco FA-150 / 71497 drain trap"),
        ("/products/perma-pure-fc125-240-5mp/", "Perma Pure FC125-240-5MP gas humidifier"),
    ],
    "swagelok-pgi-63s-pg300-la01": [
        ("/products/omega-px2300-0-5bdi/", "OMEGA PX2300-0.5BDI differential pressure transmitter"),
        ("/products/sensortechnics-ctu7001gy7c2/", "SensorTechnics CTU7001GY7C2 pressure transmitter"),
        ("/products/swagelok-6lv-cw4bw4/", "Swagelok 6LV-CW4BW4 high-purity check valve"),
        ("/products/swagelok-ss-dltw4/", "Swagelok SS-DLTW4 high-purity diaphragm valve"),
    ],
    "swagelok-ss-dltw4": [
        ("/products/swagelok-6lv-cw4bw4/", "Swagelok 6LV-CW4BW4 high-purity check valve"),
        ("/products/swagelok-pgi-63s-pg300-la01/", "Swagelok PGI-63S-PG300-LA01 pressure gauge"),
        ("/products/spirax-sarco-fa-150-71497/", "Spirax Sarco FA-150 / 71497 drain trap"),
        ("/products/perma-pure-fc125-240-5mp/", "Perma Pure FC125-240-5MP gas humidifier"),
    ],
    "tsi-4140d": [
        ("/products/mag-view-mvm-050-q/", "MAG-VIEW MVM-050-Q magnetic flow meter"),
        ("/products/omega-px2300-0-5bdi/", "OMEGA PX2300-0.5BDI differential pressure transmitter"),
        ("/products/sensortechnics-ctu7001gy7c2/", "SensorTechnics CTU7001GY7C2 pressure transmitter"),
        ("/products/perma-pure-fc125-240-5mp/", "Perma Pure FC125-240-5MP gas humidifier"),
    ],
}

HREF_RE = re.compile(r'href="(/products/[^\"]+/)"')


def product_links(text, self_url):
    urls = []
    for href in HREF_RE.findall(text):
        if href != self_url and href not in urls:
            urls.append(href)
    return urls


def add_related_section(path, slug):
    text = path.read_text(encoding="utf-8")
    if 'class="related-equipment"' in text:
        raise SystemExit(f"Related equipment section already present: {path}")

    self_url = f"/products/{slug}/"
    existing = product_links(text, self_url)
    needed = max(0, 3 - len(existing))

    additions = []
    for href, label in CANDIDATES[slug]:
        if href in existing or href == self_url:
            continue
        additions.append((href, label))
        if len(additions) == needed:
            break

    if len(additions) != needed:
        raise SystemExit(f"Not enough unique related links for {slug}: need {needed}, found {len(additions)}")

    if additions:
        block = "\n".join([
            '    <section class="related-equipment" aria-labelledby="related-equipment">',
            '      <h2 id="related-equipment">Related equipment</h2>',
            '      <ul>',
            *(f'        <li><a href="{href}">{label}</a></li>' for href, label in additions),
            '      </ul>',
            '    </section>',
        ]) + "\n"

        if text.count("</main>") != 1:
            raise SystemExit(f"Expected one closing main tag in {path}")
        text = text.replace("</main>", block + "</main>")
        path.write_text(text, encoding="utf-8")

    updated_links = product_links(path.read_text(encoding="utf-8"), self_url)
    if len(updated_links) < 3:
        raise SystemExit(f"{slug} has only {len(updated_links)} unique product cross-links")

    print(f"{slug}: {len(existing)} existing + {len(additions)} added = {len(updated_links)} product cross-links")


def add_css():
    path = ROOT / "assets" / "site.css"
    css = path.read_text(encoding="utf-8")
    if ".related-equipment" in css:
        raise SystemExit("Related equipment CSS already present")

    rules = (
        ".related-equipment { border-top: 1px solid var(--rule); padding: 24px 0 56px; }\n"
        ".related-equipment h2 { margin-bottom: 14px; }\n"
        ".related-equipment ul { margin: 0; padding-left: 20px; font-size: .94rem; }\n"
        ".related-equipment li + li { margin-top: 5px; }\n"
    )
    marker = ".site-footer {"
    if css.count(marker) != 1:
        raise SystemExit("Expected one site-footer CSS rule")
    path.write_text(css.replace(marker, rules + marker), encoding="utf-8")


def main():
    pages = {path.parent.name: path for path in PRODUCT_ROOT.glob("*/index.html")}
    if set(pages) != set(CANDIDATES):
        missing = sorted(set(pages) - set(CANDIDATES))
        extra = sorted(set(CANDIDATES) - set(pages))
        raise SystemExit(f"Related-link mapping mismatch. Unmapped pages={missing}; missing pages={extra}")

    for slug, path in sorted(pages.items()):
        add_related_section(path, slug)
    add_css()


if __name__ == "__main__":
    main()
