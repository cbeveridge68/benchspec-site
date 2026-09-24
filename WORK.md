# Work record — catalogue v1

Status: first slice implemented with actual-item photographs; **not merged or deployed**. The live eBay offer recheck and separate launch checks remain outstanding. Approved by Craig on 24 September 2026, including the subsequent heading/copy/photo amendments.

## Objective and scope

Build a small, replaceable public catalogue for specialist laboratory and process equipment. First slice: a current-stock homepage and one permanent Infinity Fluids product page. Homepage entries link to BenchSpec product pages; product pages direct purchase traffic to the existing eBay listing.

The CRES-ILB-12-0010-K-XP-PTC inline heater (BS-INFI-002 / audit 13020) is the intentionally selected first product, confirmed by Craig. It is not a substitute for the separate PTC controller.

- Branch: `feat/catalogue-v1`.
- Production origin: `https://benchspec.com.au`.
- Publishable directory: `site/`; ordinary static HTML/CSS and local product photographs, without a build step.
- Primary facts: BenchSpec audit and dated pricing records in `cbeveridge68/erpnext-ops`; never infer completed tests from a testing plan.
- Visual direction: white/light neutral background, charcoal/navy text, system fonts, subtle rules, compact specification tables, restrained controls, actual equipment photography and exact identification. Text wordmark: BenchSpec; descriptor: Specialist technical equipment.
- No framework, application JavaScript, database, CMS, product-data layer, ERPNext integration, eBay API, checkout, search/filtering, analytics scripts, animation, stock imagery or full brand system.
- Cloudflare/DNS publication and Search Console verification are separate launch tasks. No publication is authorised by this work record itself.

## Implementation and acceptance

- [x] Hand-author homepage and the first product page with shared CSS.
- [x] Identify manufacturer/model/MPN prominently; include supported specifications, audited condition/test limits and inclusions; omit optional unknowns.
- [x] Include Melbourne location, one-unit stock status and the existing eBay destination, with source/access limits below.
- [x] Include verified actual-item photographs and validate their rendering, links and image metadata.
- [x] Use exact identifiers in title/H1/copy, unique descriptions, absolute self-canonical URLs and matching Product/Offer JSON-LD.
- [x] Supply sitemap.xml and robots.txt for the production origin.
- [x] Validate image-backed mobile/desktop rendering, keyboard access, internal links, HTML, JSON-LD consistency and canonical/sitemap consistency.
- [x] Rehearse sale: preserve product URL/HTTP 200/technical content/sitemap entry; update visible status and structured availability; remove the active purchase action and current-stock card.
- [x] Confirm mobile Lighthouse performance >=90 after the actual photographs are included. Final image-backed scores are recorded below.
- [x] Document local preview, manual product/price/status maintenance and separate launch checks.
- [x] Record validation and unresolved items here. Branch/commit and push outcome are reported in the handoff; no merge or deployment is included.

## Changes

- `site/index.html`: one-item current-stock catalogue linking to the permanent BenchSpec product page; shortened introduction and reduced introductory spacing keep the equipment prominent.
- `site/products/infinity-fluids-cres-ilb-12-0010-k-xp-ptc/index.html`: H1 contains manufacturer, exact MPN and “Inline Heater”; audited specifications/condition/inclusions, manual offer and eBay handoff, canonical and Product/Offer JSON-LD.
- `raw-images/`: four unchanged heater originals. `site/assets/infinity-fluids-cres-ilb-12-0010-k-xp-ptc/`: four full-resolution WebP images and four 480 px responsive variants. Actual-item overview, nameplate, probe and enclosure appear in the page and structured image metadata. No placeholder panels remain.
- `site/assets/site.css`: shared responsive, restrained technical presentation; visible keyboard focus and skip links; system fonts. No application JavaScript or third-party assets.
- `site/sitemap.xml` and `site/robots.txt`: production-origin crawl metadata.
- `tools/check_site.py`: existing optional dependency-free consistency checks, not a build step or product-data layer. Its `--publication` mode rejects missing required images and marked blockers. No tooling or site-architecture expansion was made for the amendments.
- `README.md`: preview, manual maintenance, sold-state procedure and separate launch checklist. Only `site/` is the deployable web root.

## Source evidence

Primary source: `cbeveridge68/erpnext-ops`, remote main inspected at commit [`5cafd9b3d7a4f873d10cbaa65f81d5add254cf8f`](https://github.com/cbeveridge68/erpnext-ops/tree/5cafd9b3d7a4f873d10cbaa65f81d5add254cf8f). The local `../erpnext` checkout at `3c1d8bd` was older; the newer remote audit was used. Unrelated local edits and all source records were left unchanged.

- `benchspec/auctions/grays lot31/BenchSpec_Lot31_Audit.csv`, audit 13020 / BS-INFI-002: Infinity Fluids CRES-ILB-12-0010-K-XP-PTC inline heater; 120 V, 1000 W, single phase; stainless body, electrical termination enclosure and attached wiring; separate temperature-probe assembly and lead; labelled Made in U.S.A.; very clean, service history unknown, untested. No direct 230 V connection or dry firing. The related controller is a separate item, BS-INFI-001; functional pairing is not verified.
- `benchspec/auctions/grays lot31/Lot31_Pricing_Strategy_2026-09-17.md`: public asking price A$1,495 excluding postage. Private negotiation targets/floors are not catalogue content.
- Existing public listing: [eBay item 198659547917](https://www.ebay.com.au/itm/198659547917). Search-indexed listing identifies BenchSpec, the exact model/MPN, A$1,495 and Greensborough VIC. Direct retrieval returned HTTP 403/access errors, including in a fresh browser; a live listing check is still required before launch. The visible purchase link and JSON-LD use this same destination.
- A one-time read-only stock check on 24 September 2026 corroborated one unit of BS-INFI-002, with none reserved. No ERPNext integration, writes or stock synchronisation were introduced. Price and availability must be reviewed manually before publication and when the listing changes.
- Dimensions are not recorded. The audit's approximate 1.5 kg working weight is pending scale verification and is omitted, as are other optional unknowns. No testing-plan procedure is represented as a completed test.
- The repository's original 60-image Lot31 timestamped archive supplied controller photographs, not heater photographs. The follow-up search located additional heater images under the local `Evo/PartsLab/BenchTest/Lot031/` project assets, including audit-label evidence `13020` and a matching heater nameplate. Craig then moved the selected exports into this repository's `raw-images/`; checksums confirmed the four heater exports are byte-identical to the inspected local files. That resolves the earlier photo blocker recorded in commit `790b317`.

### Selected photograph provenance

All sources below are in `raw-images/`. The exact MPN, 120 V, 1000 W, single-phase rating and Infinity Fluids Corp. marking are legible in the nameplate photograph. The overview and detail photographs show the same enclosure, body, wiring and separate probe. Separate PTC-controller images were not used or modified.

| Web asset | Source original | Original dimensions |
| --- | --- | --- |
| `overview.webp` | `IMG_51F35372-0313-4A4E-B6D3-100239975F70.jpg` | 985 × 1537 |
| `nameplate.webp` | `IMG_4D0A9114-AF7A-4A73-97B1-2A5DD999ABDA.jpg` | 1600 × 1519 |
| `probe.webp` | `IMG_D21A390C-ED98-451A-9CAF-58BDF78FC229.jpg` | 1139 × 1600 |
| `enclosure.webp` | `IMG_BE5F2EC9-0E18-4230-8E76-CC850EEB452F.jpg` | 1520 × 1600 |

Web copies were encoded using the existing `cwebp` utility (quality 86 full-resolution, 82 for 480 px variants; metadata removed). No additional retouching, cropping, generated content or substitute imagery was used. Source originals are unchanged and outside the deployed web root. Full-size image links work without JavaScript. Responsive thumbnail files are approximately 13–24 kB each; full-resolution copies are approximately 65–141 kB each. No image-processing dependency or build step was added to the project.

## Unresolved items

- No missing source photograph remains for the selected heater. Optional unverified dimensions/weight remain omitted.
- Recheck the live eBay destination, public price and stock before launch; the destination is corroborated by indexed evidence, not a successful live listing load.
- Production publication, DNS/host validation and Search Console ownership/submission remain separate launch tasks.

## Validation evidence

Checks performed on 24 September 2026 against a local static server, not the production domain:

- `python3 tools/check_site.py` and `python3 tools/check_site.py --publication`: pass for both image-backed pages. Checks local URLs/fragments/assets, canonical URLs, unique descriptions, Product/Offer consistency, visible price/status/identifiers, required images and sitemap membership. No marked publication blocker remains in the HTML. This is a static-content gate, not a replacement for the outstanding live-offer/host checks.
- HTML Validate 11.16.0: both HTML files pass. `xmllint --noout site/sitemap.xml`: pass. JSON-LD parses as JSON and matches visible content; this is not a claim that Google's live Rich Results Test has passed.
- Chrome browser checks at 320, 390, 768 and 1440 px: both pages return HTTP 200, no horizontal overflow, all actual-item images decode, internal links and full-size photo links resolve, skip links work. Desktop/mobile screenshots with the actual photography were visually inspected. Image dimensions/alt text/srcsets and structured image URLs are present; web images contain no EXIF metadata.
- Complete forward/reverse keyboard navigation and visible focus pass across all six homepage links and ten product-page links, including all four photograph links. The product H1 was asserted to read “Infinity Fluids CRES-ILB-12-0010-K-XP-PTC Inline Heater”.
- JavaScript-disabled navigation from homepage to product and the visible eBay link: pass. No application script is present.
- Sold-state rehearsal on a disposable copy with photography: publication validator passes; `Sold` and `SoldOut` agree; purchase action and current-stock card removed; product URL remains HTTP 200; photographs, technical content and sitemap remain; unknown paths return HTTP 404. Repository content remains in the verified available state.
- Mobile Lighthouse 13.5.0 with actual photography: **both pages scored 100/100/100/100** for performance/accessibility/best practices/SEO. Homepage LCP 1.2 s; product LCP 1.7 s; both CLS 0. The >=90 mobile performance target is met locally. Repeat on the production host at launch; local Python hosting does not represent production caching/compression.
- QA dependencies and generated screenshots/reports were kept outside the repository; the website has no runtime/build dependencies. The existing consistency checker is unchanged. `git diff --cached --check`: pass.

Not performed: public-host HTTP/HTTPS checks, live Google Rich Results Test, Search Console setup/submission, deployment, DNS changes or any merge to `main`.
