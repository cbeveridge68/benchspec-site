# Work record — Lot 31 catalogue batch 1

## Current batch — 25 September 2026

Branch: `feat/lot31-catalogue-batch-1`, created directly from fetched `origin/main` at `f8df5ffaf60520e2732c230e975ef6b1d1f0074b`. The old diverged `feat/catalogue-v1` was not merged or cherry-picked. Only the approved four-product batch, its current actual-item photographs, associated homepage/sitemap/cross-links, and required README/checker/work records were transferred. The original dirty worktree and unrelated raw images remain untouched. A separate worktree isolates this branch.

### Scope and factual corrections

- Four new hand-authored product pages: Infinity PTC controller, Perma Pure humidifier, MAG-VIEW flow meter and Spirax Sarco drain trap. The original CRES heater remains available; all five pages and the homepage receive the requested editorial/shipping review. No catalogue expansion beyond these items.
- Perma Pure source correction supplied by Craig on 25 September: the units are **not capped**. Earlier closure/protection claims are withdrawn, not replaced with another inference. Current wording records very good physical condition with minimal signs of prior use; model and serial numbers verified; physical condition inspected; kept dry. The specific boundary remains: “Units have not been dismantled, wetted or pressure-tested.”
- Lot 31 physical appearance does not establish an unused history. All item-level descriptions use observed physical condition, followed by recorded verification and the specific functional-test boundary. Unsupported history implications have been removed from cards, visible copy, metadata and JSON-LD. The general BenchSpec brand descriptor is not a condition claim about these items.
- MAG-VIEW: model, ratings and serial numbers verified; physical condition inspected. Dry condition and the explicit flow-test boundary are retained. One original MVM-Q user's guide is recorded with the stock; allocation is not fixed. The page refers buyers to the eBay listing for the inclusions supplied with the selected unit, without promising a guide with each meter.
- Spirax: excellent physical condition with minor handling marks. Protective caps and exact pressure/temperature ratings are retained. Wet or pressure testing has not been performed; ports remain capped.
- Both Infinity pages retain the 120 V safety warning and process-testing limitation. Related-equipment cross-links state that the controller and heater are separate offers from the same lot and have not been functionally tested together.
- Removed repetitive quantity/pricing captions and mechanical inspection prose. Count: “5 equipment listings”. Image dimensions, responsive descriptors and Open Graph image dimensions match the operator-supplied processed photographs.
- International shipping is affirmative under Craig's stated operating policy: “Stock in Melbourne, Australia · Ready for international shipping” or the corresponding full sentence. No free-shipping, logistics-cost, warranty or destination-specific promise was added. These instructions supersede older shipping guidance; README records the rule for subsequent Lot 31 work.
- Plain static HTML/CSS, logo/tagline, navy/white design, contact/ABN, eBay handoff and sold-page behaviour are preserved. No new architecture, application scripts, dependencies or tracked generation/QA tooling.

### Evidence and public offers

Original batch facts were drawn from `cbeveridge68/erpnext-ops` revision `5cafd9b3d7a4f873d10cbaa65f81d5add254cf8f`: `benchspec/auctions/grays lot31/BenchSpec_Lot31_Audit.csv` (blob `a1e0c991f08e95d820e76b3972807234043ef478`) and `Lot31_Pricing_Strategy_2026-09-17.md` (blob `b9fa7881478ae512e8a44a13c3b9890fd461b873`). Craig's subsequent factual corrections, public-price approvals and shipping policy govern this batch. No completed testing is inferred from a testing plan; private commercial figures are not published.

The live [BenchSpec eBay store](https://www.ebay.com.au/str/benchspec) returned HTTP 200 in Chrome on 25 September and positively identified all five exact item links, model titles and public asking prices below. The CRES item page was also readable. The other direct item pages could not be independently retrieved by the web reader; no access challenge was bypassed. Quantities and serials remain the audited values, not a claim that the store index exposes remaining quantity. Local evidence is retained in ignored `.qa/ebay-offer-evidence.json`.

| Product | SKU / audit | Quantity | Public asking price | Exact eBay item |
| --- | --- | --- | --- | --- |
| Infinity Fluids CRES-ILB-12-0010-K-XP-PTC | BS-INFI-002 / 13020 | 1 | A$1,495 | [198659547917](https://www.ebay.com.au/itm/198659547917) |
| Infinity Fluids PTC-12-20-1P | BS-INFI-001 / 13014 | 1 | A$1,995 | [198658139207](https://www.ebay.com.au/itm/198658139207) |
| Perma Pure FC125-240-5MP | BS-PPUR-001 / 31006 | 2 | A$795 each | [198644525062](https://www.ebay.com.au/itm/198644525062) |
| MAG-VIEW MVM-050-Q | BS-MAGV-001 / 13011 | 2 | A$400 each | [198645719640](https://www.ebay.com.au/itm/198645719640) |
| Spirax Sarco FA-150 / 71497 | BS-SPIR-001 / 13013 | 1 | A$725 | [198646864549](https://www.ebay.com.au/itm/198646864549) |

### Current photo sources

The following originals are preserved directly in `raw-images/`, outside the deployed tree. Current processed exports take precedence over older timestamped copies. WebP full-size quality 86 and 480 px quality 82 derivatives preserve their framing; no substitute/generated imagery is used. CRES assets and its original sources are unchanged from main.

| Product / web asset | Current top-level source |
| --- | --- |
| Infinity controller / `overview.webp` | `controller1-overview.jpg` |
| Infinity controller / `interior.webp` | `controller2-interior.jpg` |
| Infinity controller / `enclosure.webp` | `controller3-enclosure.jpg` |
| Infinity controller / `manual.webp` | `controller4-manual.jpg` |
| perma-pure-fc125-240-5mp / `overview.webp` | `perma-pure-humidifier1-overview.jpeg` |
| perma-pure-fc125-240-5mp / `serial-011.webp` | `perma-pure-humidifier2-serial-011.jpeg` |
| perma-pure-fc125-240-5mp / `serial-010.webp` | `perma-pure-humidifier3-serial-010.jpeg` |
| perma-pure-fc125-240-5mp / `pair.webp` | `perma-pure-humidifier4-pair-alternate.jpeg` |
| mag-view-mvm-050-q / `overview.webp` | `mag-view-flowmeter1-overview-processed.jpg` |
| mag-view-mvm-050-q / `packaged.webp` | `mag-view-flowmeter2-packaged.jpeg` |
| spirax-sarco-fa-150-71497 / `overview.webp` | `spirax-trap1-overview.jpeg` |
| spirax-sarco-fa-150-71497 / `ratings.webp` | `spirax-trap2-ratings.jpeg` |
| spirax-sarco-fa-150-71497 / `body.webp` | `spirax-trap3-body.jpeg` |
| spirax-sarco-fa-150-71497 / `audit-label.webp` | `spirax-trap4-audit-label.jpeg` |

The MAG-VIEW manual remains sourced from `raw-images/BenchSpec_Grays_Lot31_Audit_Images_Timestamped/2026-09-13_16-34-15_AEST_01_IMG_65B55FBA-E478-496A-BB15-75AFE4D26A4A.jpeg`. No unrelated archive images or check-valve photographs were included.

### Withheld products

- **TSI 4140D / BS-TSI-001 / audit 13021:** Craig confirmed it is not listed. Publication requires an exact live BenchSpec eBay URL and its chosen non-tested public asking price. Historical calibration dated 04/08/2014 is not current calibration; no completed functional test is recorded. The Infinite Filter 14SX remains an unverified third-party accessory, not a claimed calibrated/matched TSI component. Preserve kit, instrument, historical-calibration-label and filter photos: `IMG_2B67D908-35B9-43D7-A932-42038DC4AB82.jpeg`, `IMG_43F218E7-0F1C-44B0-B93C-770210CCF5CB.jpeg`, `IMG_C7DDB484-78EA-420F-AAD1-452D2DADFC07.jpeg`, `IMG_B3BF9F9B-9403-4822-91FE-6579BE5A3EEB.jpeg`.
- **Swagelok KPR1DRF412A20000 / BS-SWAG-004 / audit 13012:** Craig confirmed it is not listed. Publication requires an exact live BenchSpec URL and confirmed public asking price; A$649 was provisional, not a live offer. Its package intentionally remains unopened; do not infer factory-sealed condition or pressure testing. Preserve the four timestamped `2026-09-13_16-26-03_AEST_01` through `_04` package/marking photos.
- These eight originals remain in the timestamped raw-image subfolder. Neither withheld product has a public page, card, sitemap entry, structured offer or purchase action.

### Validation and final state

- `python3 tools/check_site.py` and `python3 tools/check_site.py --publication`: **PASS** for six HTML pages. Internal links/assets, canonical metadata, JSON-LD, visible price/status consistency, available-state behaviour and sitemap membership pass.
- HTML Validate: **PASS** for all six pages. `xmllint --noout` passes for `site/sitemap.xml`, `site/assets/benchspec-logo.svg` and `site/assets/favicon.svg`. `git diff --check`: **PASS**.
- Independent editorial/factual checks: **PASS**. Exact identifiers, serials, quantities, offer prices/URLs, specification tables, key safety statements and structured Offer values match the reviewed batch. Perma Pure is the sole intentional source correction: its storage record is now `Kept dry`, with no capped claim. All item copy, metadata and JSON-LD exclude unsupported unused/open-surplus/pre-owned language; published pages contain no TSI or KPR references.
- Image provenance: **PASS**. The 23 selected preserved raw originals on this branch match the reviewed worktree byte-for-byte. Independent WebP encoding checks pass for all 30 Lot 31 assets (full-size plus 480 px variants); responsive/OG dimensions match the files.
- Public offer review: **PASS**. The BenchSpec eBay store returned HTTP 200 in Chrome on 25 September and confirmed the exact five URLs, titles and public asking prices recorded above. The site button and JSON-LD URL match each confirmed item.
- Browser review: **PASS** at 390, 768 and 1440 px for homepage plus every product page. No horizontal overflow or header crowding; all images decode; full-size image and internal links resolve; mailto links, favicon and logo resolve; forward/reverse keyboard navigation, visible focus, skip links and no-JavaScript product navigation pass. Updated captures are ignored local artifacts in `.qa/final-review/`.
- Sold-state rehearsal: **PASS** independently for every published product on disposable copies. Each permanent product URL returns HTTP 200 with technical content, photos and sitemap retained; visible state/structured availability become Sold/SoldOut; active purchase action and homepage card are removed; last asking price is labelled.
- Verification-boundary regression: **PASS**, 40 cases across five product pages and both checker modes. Removing the exact visible/structured test boundary, replacing it with a bare `Untested` label or claiming successful testing fails the checker.
- Scope comparison: **PASS** against `origin/main` at `f8df5ffaf60520e2732c230e975ef6b1d1f0074b`. The branch changes only the four approved pages, their assets/raw originals, homepage/sitemap, factual cross-links, checker/README/work record and necessary editorial updates to the original heater. No TSI/KPR public page, card, sitemap entry, offer or purchase action is present.

Final branch state is ready for commit and push only; it is not merged or deployed.

### Remaining external items

The external Perma Pure eBay title still uses legacy condition terminology. The catalogue uses Craig's corrected observed-condition wording; changing the eBay listing is outside this repository task. No website publication blocker is created by that legacy title.

Hosting, DNS publication, Search Console setup and final pre-launch stock/offer recheck remain separate. No merge or deployment is performed by this batch.

## Historical first-slice record from main

Everything below is retained solely as historical evidence. Its old branch/status, shipping wording and validation statements are not the current batch state; the current record above is authoritative.

Status: first slice implemented with actual-item photographs; **not merged or deployed**. The live eBay offer recheck and separate launch checks remain outstanding. Approved by Craig on 24 September 2026, including the subsequent heading/copy/photo amendments.

Historical approved state: the header logo reads **SPECIFIED • VERIFIED** and the heater short condition reads **Used item in very clean physical condition. Visually inspected and verified complete as offered.** Visible copy, metadata, JSON-LD and `CATALOGUE_GUIDE.md` agree. Fresh normal/publication, HTML/XML and responsive/sold-state checks pass with no local validation exception. See “Historical approved-state validation” below for the authoritative results. All earlier review/validation sections are historical. Branch: `feat/catalogue-v1`; no merge or deployment.

## Objective and scope

Build a small, replaceable public catalogue for specialist technical equipment and parts. First slice: an available-stock homepage and one permanent Infinity Fluids product page. Homepage entries link to BenchSpec product pages; product pages direct purchase traffic to the existing eBay listing.

The CRES-ILB-12-0010-K-XP-PTC inline heater (BS-INFI-002 / audit 13020) is the intentionally selected first product, confirmed by Craig. It is not a substitute for the separate PTC controller.

- Branch: `feat/catalogue-v1`.
- Production origin: `https://benchspec.com.au`.
- Publishable directory: `site/`; ordinary static HTML/CSS and local product photographs, without a build step.
- Primary facts: BenchSpec audit and dated pricing records in `cbeveridge68/erpnext-ops`; never infer completed tests from a testing plan.
- Visual direction: navy header/footer and white/light neutral body, system fonts, subtle rules, compact specification tables, restrained controls, actual equipment photography and exact identification. Approved BenchSpec SVG logo with “SPECIFIED • VERIFIED”; live descriptor: Specialist technical equipment — new surplus, decommissioned and fully specified.
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
- `tools/check_site.py`: existing optional dependency-free consistency checks, not a build step or product-data layer. Its `--publication` mode rejects missing required images and marked blockers. The approved finalisation amendment replaces the literal-“untested” check with the explicit process-testing boundary; no dependency or site-architecture expansion was made.
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

## Historical validation evidence — initial image-backed implementation

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

## Historical visual refinement — review record, 24 September 2026

One restrained pass, left uncommitted on `feat/catalogue-v1` (base `3d87627`):

- Shared dark navy header/footer, white wordmark and restrained light secondary text/navigation; predominantly white body retained.
- Homepage inventory entry grouped by a subtle neutral surface and border, with the existing A$1,495 asking price (AUD, excluding postage) and unchanged availability indicator.
- Lower homepage explanation combined into one compact paragraph. Product image/offer/specification hierarchy retained; complete product HTML and both pages' head/SEO content verified byte-for-byte unchanged.
- No catalogue expansion, architecture, content-model, tooling, application-script or deployment changes. Unused controller originals remain untouched.
- Publication checker, HTML validation, 320/390/768/1440 px browser checks, image/link checks, keyboard navigation and sold-state rehearsal pass. Navy-frame text contrast is 8.44:1 or higher. `git diff --check` passes.
- Desktop screenshots captured at 1440 px and visually inspected: `.qa/visual-refinement/homepage-desktop.png` and `.qa/visual-refinement/product-desktop.png`. These are local ignored review artifacts, not website assets.
- No new Lighthouse run for this visual-only pass; the image-backed scores above belong to the preceding `3d87627` implementation.

Awaiting visual review before committing this pass. No push, merge or deployment performed.

## Historical positioning pass — review record, 24 September 2026

Applied on `feat/catalogue-v1`, preserving the preceding uncommitted visual pass:

- Broader BenchSpec descriptor on both headers; homepage H1 “Specialist technical equipment” and the requested stock-in-Melbourne/international-shipping introduction. Section/navigation labels now say “Available equipment”; the count says “01 item available”.
- Heater primary condition is “Used · Visually inspected”. Detailed copy states that BenchSpec has confirmed the model, ratings, included components and visible condition, while functional operation remains untested under the fluid, flow and control conditions required for proper operation. Service-history and compatibility limits remain explicit. No refurbishment or successful functional-test claim was introduced.
- Added “Condition and warranty are stated per item.” The heater directs buyers to eBay for current purchase, delivery, returns, warranty and destination-specific shipping terms; no item warranty or blanket returns promise was invented.
- International-shipping basis: the [indexed BenchSpec eBay offer](https://www.ebay.com.au/itm/198659547917), retrieved on 24 September, shows Australia Post International Standard and delivery to a US destination. This supports “International shipping available”, not guaranteed worldwide coverage. Direct-page access still returned an error; destination eligibility and current terms must be rechecked at launch.
- Existing title/description strings were aligned with visible positioning/condition; SEO mechanisms, exact product title/H1, canonicals and JSON-LD structure are unchanged. JSON-LD changes are limited to descriptive and test-status wording; Offer, price, currency, stock, URL and image fields remain unchanged.
- CSS changes for this pass are confined to header padding, descriptor width/line-height and flex sizing so the longer descriptor wraps without crowding navigation. No page sections, photo treatment, navy/white identity, architecture, tooling, sitemap or robots changes.

Validation: existing publication checker and HTML Validate pass; sitemap XML and `git diff --check` pass. Browser checks at 320/390/768/1440 px, full forward/reverse keyboard navigation, image/link loading, JavaScript-disabled navigation and sold-state rehearsal pass. Additional 390/768/1440 px assertions confirm header separation and correct revised wording. Page sections/links/images and schema structure were compared with the pre-positioning files; tools, sitemap, robots and image assets were verified unchanged from HEAD.

Final review screenshots are in `.qa/final-positioning/`: `homepage-desktop.png`, `homepage-mobile.png`, `product-desktop.png`, `product-mobile.png`, plus both tablet views. All six were visually inspected; no overflow or header crowding was found. These remain local ignored artifacts outside `site/`.

Mobile Lighthouse 13.5.0 rerun: both pages score 100/100/100/100 for performance/accessibility/best practices/SEO. Homepage LCP 1.2 s; product LCP 1.7 s; both CLS 0. These are local results, not production-host measurements.

Both refinement passes remain uncommitted for final visual review. No catalogue expansion, push, merge or deployment performed.

## Historical copy refinement — review record, 24 September 2026

Applied the final requested wording on `feat/catalogue-v1`, preserving all preceding uncommitted refinements:

- Both header descriptors now read “Specialist technical equipment — new surplus, decommissioned and fully specified”. The homepage H1, “Available equipment” heading and global-availability introduction remain unchanged. The catalogue note uses the exact requested shorter wording.
- The detailed heater condition now reads: “Very clean physical condition. BenchSpec has confirmed the model, ratings, included components and visible condition. Functional operation has not been tested under process conditions.” Removed the controller/process compatibility sentence without adding another disclaimer. The specific recorded unknown service history remains.
- Electrical and handling copy now reads: “120 V equipment. Do not connect directly to Australian 230 V mains. Functional testing requires appropriate fluid flow and control conditions.” The primary condition remains “Used · Visually inspected”; no successful functional testing or refurbishment is implied.
- Aligned only the existing homepage meta-description text and Product description/test-status strings with the revised copy. Product/Offer structure, identifiers, price, availability, eBay destination, canonical URLs and image fields remain unchanged.
- Recorded the general catalogue rule in README maintenance guidance: state identified facts, visual inspection, actual functional testing if any, and specific material limitations; avoid hypothetical untested scenarios unless directly relevant to safe use or accurate representation.
- No CSS or layout adjustment was needed. Architecture, page/SEO structure, tooling, image treatment, sitemap, robots and overall visual identity are unchanged in this pass. Unused controller originals remain untouched.

Validation performed after these changes:

- Both `python3 tools/check_site.py` and `python3 tools/check_site.py --publication` were rerun. Both exit 1 with exactly one reported failure: `verification limits missing`, caused by the hardcoded literal-word check described above. The checker was not modified, bypassed or reported as passing. All its other assertions reported no failures, including local targets, canonicals, sitemap and Product/Offer consistency.
- HTML Validate 11.16.0 passes both pages; sitemap XML and `git diff --check` pass. Comparing both HTML files with the pre-pass snapshot confirms the same tag/attribute structure, links and images except the requested homepage description text. JSON-LD is unchanged except its description/test-status values. CSS is byte-identical to the pre-pass snapshot; repository tooling, sitemap, robots and image assets match HEAD.
- Chrome checks pass at 320, 390, 768 and 1440 px: HTTP 200, no horizontal overflow or header crowding, exact requested copy, all images decoded, internal/photo links resolving, correct eBay handoff, skip links and full forward/reverse keyboard navigation. JavaScript-disabled homepage-to-product navigation and the eBay link pass.
- Disposable sold-state browser rehearsal passes: `Sold` / `SoldOut` agree, product URL returns HTTP 200, active purchase action and homepage item are removed, technical content and sitemap remain, and an unknown URL returns HTTP 404. The sold-copy publication checker reports the same single literal-word failure, not a clean pass. The repository remains in the available state.
- Fresh full-page screenshots at 1440 px desktop, 390 px mobile and 768 px tablet were visually inspected. `.qa/final-copy/` contains `homepage-desktop.png`, `homepage-mobile.png`, `product-desktop.png`, `product-mobile.png`, `homepage-tablet.png` and `product-tablet.png`. These are local ignored review artifacts, not deployed assets.
- Fresh mobile Lighthouse 13.5.0: both pages score **100/100/100/100** for performance/accessibility/best practices/SEO. Homepage LCP 1.2 s; product LCP 1.7 s; both CLS 0. Local results only; production-host checks remain a separate launch step.

Branch: `feat/catalogue-v1`; existing HEAD: `3d87627`. This copy pass and the earlier visual/positioning refinements remain uncommitted for final review. No push, merge, deployment or catalogue expansion performed.

## Historical finalisation validation — 24 September 2026 (`f737df7`)

Historical result for `f737df7`, before the approved logo tagline and “complete as offered” amendments. The previous refinements were committed/pushed as `7c24114`. The then-current remote standards (`7175aa6`) and approved logo (`1ab5184`) were incorporated before that pass.

Changes:

- Added the small homepage contextual eyebrow: “Direct catalogue — specialist equipment available from stock”. Kept the approved H1, global-availability intro, “Available equipment” heading and full brand descriptor unchanged.
- Added `sales@benchspec.com.au` as header/footer `mailto:` links on both pages and a quiet item-enquiry line immediately beneath the eBay action. Added the operator-approved footer identity “BenchSpec · Operated by PartsLab · ABN 14 525 874 055”. eBay remains the primary purchase route; no direct checkout or new warranty promise was introduced.
- Incorporated the operator-supplied `site/assets/benchspec-logo.svg` from remote commit `1ab5184`. Its original canvas clipped the tagline and bottom of the icon; only the viewBox bounds were expanded from `0 0 1080 360` to `0 0 1146 384` (plus an end-of-file newline). All supplied artwork, paths and text are unchanged. CSS renders it white at a restrained size on the existing navy header and restores the original colour for printing. `site/assets/favicon.svg` reuses the exact five supplied icon paths on a square canvas.
- Homepage/product short condition now reads “Used item in very clean physical condition. Visually inspected and verified complete.” This is the operator-approved wording, consistent with the latest guide. The detailed condition retains the explicit process-testing boundary, specific 120 V handling wording, known service-history limitation and separate-controller exclusion. No functional-test success, refurbishment or generic compatibility claim was added. Descriptive metadata and JSON-LD wording match the visible condition; Offer structure, price, availability and destination are unchanged.
- The existing validator now requires the explicit “Functional operation has not been tested under process conditions” statement, with case/whitespace normalisation. It no longer accepts a bare “untested” label. No check was disabled and no new tooling dependency was introduced.
- `CATALOGUE_GUIDE.md` already contains the approved short condition wording; it now also records use of the approved logo/derived favicon. README points maintainers to the guide. WORK.md distinguishes the current passing results from the historical literal-word failure.
- No new product, page architecture, framework, build step, application script, analytics, hosting or integration. Product URL, photography/treatment, canonical URLs, sitemap and robots remain unchanged. CSS adjustments are confined to the logo, eyebrow spacing, quiet contact/footer text and a 24 px minimum header-link target height; the latter fixes the touch-spacing issue exposed when the email link was added.

Final validation:

- `python3 tools/check_site.py` and `python3 tools/check_site.py --publication`: pass for both pages, including JSON-LD/visible identifiers, price, availability, destination, local assets, canonical URLs and sitemap consistency. HTML Validate 11.16.0 passes both pages; sitemap and both SVG files parse as XML; `git diff --check` passes.
- Verification-limit regression checks pass in normal and publication modes: approved wording and wrapped whitespace are accepted; deleting the visible limitation (even while retaining it in JSON-LD), using only “Untested”, using a vague non-verification statement, or claiming functional testing are all rejected. No weakening of the explicit disclosure requirement.
- Chrome checks pass at 320, 390, 768 and 1440 px: HTTP 200, no horizontal overflow or header crowding, exact approved copy, all images decoded, internal/full-size photo links resolved, and complete forward/reverse keyboard navigation with visible focus. JavaScript-disabled catalogue navigation and eBay handoff remain available.
- Logo and favicon return HTTP 200 with SVG content types and decode successfully. Comparison with the supplied SVG confirms unchanged artwork and identical favicon icon paths. All five email anchors use exactly `mailto:sales@benchspec.com.au`; keyboard access is verified. No email was sent and mailbox deliverability was not tested.
- Visible eBay action and structured Offer still point to `https://www.ebay.com.au/itm/198659547917`. Correct target consistency is verified locally; live offer/price/stock and destination-specific shipping remain a pre-launch recheck, as recorded above.
- Disposable sold-state rehearsal passes the publication validator and browser checks: `Sold` / `SoldOut` agree, buying instructions and purchase action are removed, homepage stock entry is removed, permanent product URL remains HTTP 200, technical content/photos/sitemap remain, and unknown paths return HTTP 404. The repository retains the available state.
- Review screenshots at 1440 px desktop and 390 px mobile are `.qa/finalisation/homepage-desktop.png`, `homepage-mobile.png`, `product-desktop.png` and `product-mobile.png`; both 768 px tablet captures are retained alongside them. These are ignored local review artifacts, outside the deployable site.
- Final desktop/mobile screenshots were visually inspected after the header touch-target adjustment. Fresh mobile Lighthouse 13.5.0 scores are **100/100/100/100** for performance/accessibility/best practices/SEO on both pages. Homepage LCP 1.5 s; product LCP 1.7 s; both CLS 0. These are local preview results, not production-host measurements.

That finalisation was committed and pushed as `f737df78170c3e541144c1b79ab45fc7cb92a82e`. Unused controller originals were left untracked and untouched. No merge to `main`, deployment or DNS changes were included.

## Historical approved-state validation — 24 September 2026

Reconciled against the latest approved remote revision `8d5c98a`. Its existing commits already supply the “SPECIFIED • VERIFIED” logo, “verified complete as offered” wording on both pages and in descriptive metadata/JSON-LD, and the matching catalogue guide. They were fast-forwarded locally and validated without further website, CSS, asset or tooling edits. The only new repository change in this pass is this reconciled work record.

Confirmed final state:

- Header uses `site/assets/benchspec-logo.svg` with the exact approved logo tagline; `site/assets/favicon.svg` remains the favicon. The longer live descriptor, homepage contextual eyebrow, H1, intro, “Available equipment” heading, public email and PartsLab/ABN footer identity retain their exact approved wording.
- Product short condition is exactly “Used item in very clean physical condition. Visually inspected and verified complete as offered.” The homepage, product meta/OG descriptions and JSON-LD description/test status consistently use “verified complete as offered”.
- Detailed verification and 120 V handling wording remain unchanged and exact. No prohibited primary label, generic compatibility disclaimer, speculative non-test disclaimer or functional-test success claim has been introduced. eBay remains the primary transaction route.
- Existing explicit process-testing-limit validation is unchanged. CSS, favicon, product photographs, sitemap, robots and validator are byte-identical to `f737df7`; architecture, page hierarchy and catalogue scope are unchanged.

Fresh validation results:

- `python3 tools/check_site.py`: **pass**. `python3 tools/check_site.py --publication`: **pass**. JSON-LD parses and agrees with visible identifiers, price, status and destination; canonical URLs and sitemap membership agree.
- HTML Validate 11.16.0: **pass** for both HTML pages. `xmllint --noout site/sitemap.xml site/assets/benchspec-logo.svg site/assets/favicon.svg`: **pass**. `git diff --check`: **pass**.
- Chrome checks at 1440 px desktop and 390 px mobile (also 320/768 px): **pass**. No horizontal overflow or header crowding. All images decode, local links resolve, exact text assertions pass, full forward/reverse keyboard navigation and skip links pass, and JavaScript-disabled product navigation remains functional.
- Logo/favicon: **pass**, HTTP 200 with SVG content types and successful decoding. SVG text is exactly “BenchSpec” / “SPECIFIED • VERIFIED”; measured artwork fits inside the viewBox without clipping. Desktop/mobile screenshots were visually inspected.
- All five `mailto:sales@benchspec.com.au` anchors have the correct address/text and are keyboard accessible. No email was sent or mailbox deliverability claimed. Visible and structured eBay destinations both remain `https://www.ebay.com.au/itm/198659547917`; the separate live-offer launch recheck remains outstanding.
- Sold-state rehearsal on a disposable copy: **pass**, including the publication checker, Sold/SoldOut agreement, removal from the homepage and removal of the purchase action, permanent URL HTTP 200, retained specifications/photos/sitemap, and unknown-route HTTP 404. Repository stock remains available.
- Fresh validator regression checks in both modes accept the approved process-testing statement and reject its removal, a bare “Untested” replacement or an opposite successful-test statement. The limitation left in JSON-LD alone does not satisfy the visible-content check.
- Updated screenshots: `.qa/approved-final-state/homepage-desktop.png`, `homepage-mobile.png`, `product-desktop.png` and `product-mobile.png`, with tablet captures alongside. These remain ignored local review artifacts outside `site/`. No new Lighthouse run was requested or performed for this confirmation pass; all earlier Lighthouse scores above are explicitly historical.

The containing validation-record commit is on `feat/catalogue-v1`; the final SHA and remote verification are reported in the handoff. Unused controller originals remain untracked and untouched. No merge, deployment or DNS changes. Remaining launch checks are unchanged under “Unresolved items”.
