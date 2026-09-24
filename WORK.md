# Work record — catalogue v1

Status: first slice implemented with actual-item photographs; **not merged or deployed**. The live eBay offer recheck and separate launch checks remain outstanding. Approved by Craig on 24 September 2026, including the subsequent heading/copy/photo amendments.

Current finalisation state: approved context, contact/business identity, logo/favicon and condition wording are implemented on `feat/catalogue-v1`. Normal/publication site checks, HTML validation and responsive/sold-state browser checks pass. The old literal-“untested” validation failure is resolved; there is no current local validation exception. See “Current finalisation validation” below for the authoritative final results. No merge or deployment has occurred. The prior visual/positioning/copy refinements were committed and pushed as `7c2411450ab3ddd95e431ce210b2f628d8673d92`; their review-time notes below are historical, not the current status.

## Objective and scope

Build a small, replaceable public catalogue for specialist technical equipment and parts. First slice: an available-stock homepage and one permanent Infinity Fluids product page. Homepage entries link to BenchSpec product pages; product pages direct purchase traffic to the existing eBay listing.

The CRES-ILB-12-0010-K-XP-PTC inline heater (BS-INFI-002 / audit 13020) is the intentionally selected first product, confirmed by Craig. It is not a substitute for the separate PTC controller.

- Branch: `feat/catalogue-v1`.
- Production origin: `https://benchspec.com.au`.
- Publishable directory: `site/`; ordinary static HTML/CSS and local product photographs, without a build step.
- Primary facts: BenchSpec audit and dated pricing records in `cbeveridge68/erpnext-ops`; never infer completed tests from a testing plan.
- Visual direction: navy header/footer and white/light neutral body, system fonts, subtle rules, compact specification tables, restrained controls, actual equipment photography and exact identification. Approved BenchSpec SVG logo; descriptor: Specialist technical equipment — new surplus, decommissioned and fully specified.
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

## Current finalisation validation — 24 September 2026

This record supersedes the historical review-time statuses above. The previous refinements were committed/pushed as `7c24114`. The latest remote standards (`7175aa6`) and approved logo (`1ab5184`) were incorporated before this bounded finalisation pass.

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

The containing finalisation commit is on `feat/catalogue-v1`; its SHA and remote-branch verification are reported in the handoff. Unused controller originals remain untracked and untouched. No merge to `main`, deployment or DNS changes are included.
