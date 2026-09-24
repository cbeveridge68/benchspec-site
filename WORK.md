# Work record — catalogue v1

Status: review draft implemented; **not ready for publication**. Actual-item heater photographs remain required. Approved by Craig on 24 September 2026, including the amendments in the task conversation.

## Objective and scope

Build a small, replaceable public catalogue for specialist laboratory and process equipment. First slice: a current-stock homepage and one permanent Infinity Fluids product page. Homepage entries link to BenchSpec product pages; product pages direct purchase traffic to the existing eBay listing.

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
- [ ] Include verified actual-item photographs and validate their rendering, links and image metadata.
- [x] Use exact identifiers in title/H1/copy, unique descriptions, absolute self-canonical URLs and matching Product/Offer JSON-LD.
- [x] Supply sitemap.xml and robots.txt for the production origin.
- [x] Validate draft mobile/desktop rendering, keyboard access, internal links, HTML, JSON-LD consistency and canonical/sitemap consistency.
- [x] Rehearse sale: preserve product URL/HTTP 200/technical content/sitemap entry; update visible status and structured availability; remove the active purchase action and current-stock card.
- [ ] Confirm mobile Lighthouse performance >=90 after the actual photographs are included. Draft scores are recorded below, not final photographic-page acceptance.
- [x] Document local preview, manual product/price/status maintenance and separate launch checks.
- [x] Record validation and unresolved items here. Branch/commit and push outcome are reported in the handoff; no merge or deployment is included.

## Changes

- `site/index.html`: one-item current-stock catalogue linking to the permanent BenchSpec product page.
- `site/products/infinity-fluids-cres-ilb-12-0010-k-xp-ptc/index.html`: exact identification, audited specifications/condition/inclusions, manual offer and eBay handoff, canonical and Product/Offer JSON-LD.
- `site/assets/site.css`: shared responsive, restrained technical presentation; visible keyboard focus and skip links; system fonts. No application JavaScript or third-party assets.
- `site/sitemap.xml` and `site/robots.txt`: production-origin crawl metadata.
- `tools/check_site.py`: optional dependency-free consistency checks, not a build step or product-data layer. Its `--publication` mode rejects the known photo blockers.
- `README.md`: preview, manual maintenance, sold-state procedure and separate launch checklist. Only `site/` is the deployable web root.

## Source evidence

Primary source: `cbeveridge68/erpnext-ops`, remote main inspected at commit [`5cafd9b3d7a4f873d10cbaa65f81d5add254cf8f`](https://github.com/cbeveridge68/erpnext-ops/tree/5cafd9b3d7a4f873d10cbaa65f81d5add254cf8f). The local `../erpnext` checkout at `3c1d8bd` was older; the newer remote audit was used. Unrelated local edits and all source records were left unchanged.

- `benchspec/auctions/grays lot31/BenchSpec_Lot31_Audit.csv`, audit 13020 / BS-INFI-002: Infinity Fluids CRES-ILB-12-0010-K-XP-PTC inline heater; 120 V, 1000 W, single phase; stainless body, electrical termination enclosure and attached wiring; separate temperature-probe assembly and lead; labelled Made in U.S.A.; very clean, service history unknown, untested. No direct 230 V connection or dry firing. The related controller is a separate item, BS-INFI-001; functional pairing is not verified.
- `benchspec/auctions/grays lot31/Lot31_Pricing_Strategy_2026-09-17.md`: public asking price A$1,495 excluding postage. Private negotiation targets/floors are not catalogue content.
- Existing public listing: [eBay item 198659547917](https://www.ebay.com.au/itm/198659547917). Search-indexed listing identifies BenchSpec, the exact model/MPN, A$1,495 and Greensborough VIC. Direct retrieval returned HTTP 403/access errors, including in a fresh browser; a live listing check is still required before launch. The visible purchase link and JSON-LD use this same destination.
- A one-time read-only stock check on 24 September 2026 corroborated one unit of BS-INFI-002, with none reserved. No ERPNext integration, writes or stock synchronisation were introduced. Price and availability must be reviewed manually before publication and when the listing changes.
- Dimensions are not recorded. The audit's approximate 1.5 kg working weight is pending scale verification and is omitted, as are other optional unknowns. No testing-plan procedure is represented as a completed test.
- The Lot31 timestamped image archive was inspected; its Infinity photographs show the separate PTC controller, not this heater. No verified actual-heater photograph was located. Neither substitute photography nor generated imagery was used.

## Unresolved items

- **Publication/completion blocker:** provide access to the actual-item heater photographs (a local folder path is sufficient). The existing audit, price and stock facts have already been obtained; they do not need to be re-entered. eBay image retrieval was blocked, and the source archive did not supply verified heater images. Both pages visibly mark photography as pending; the Product image property is deliberately omitted rather than fabricated.
- After photographs are available: inspect their identity, add optimised local images/responsive variants and descriptive alt text, update structured/social image metadata, remove the two photo-blocker panels, and rerun image/browser/performance and `--publication` checks.
- Recheck the live eBay destination, public price and stock before launch; the destination is corroborated by indexed evidence, not a successful live listing load.
- Production publication, DNS/host validation and Search Console ownership/submission remain separate launch tasks.

## Validation evidence

Checks performed on 24 September 2026 against a local static server, not the production domain:

- `python3 tools/check_site.py`: pass for both pages; reports the known photography blockers explicitly. Checks local URLs/fragments/assets, canonical URLs, unique descriptions, Product/Offer consistency, visible price/status/identifiers and sitemap membership.
- `python3 tools/check_site.py --publication`: expected failure for the two marked photo blockers and missing Product images. This is an unresolved acceptance condition, not a passing release gate.
- HTML Validate 11.16.0: both HTML files pass. `xmllint --noout site/sitemap.xml`: pass. JSON-LD parses as JSON and matches visible content; this is not a claim that Google's live Rich Results Test has passed.
- Chrome browser checks at 320, 390, 768 and 1440 px: both pages return HTTP 200, no horizontal overflow, internal links resolve, skip links work. Forward/reverse keyboard navigation and visible focus were checked across all six links on each page. Desktop/mobile screenshots were visually inspected. A tablet-width overflow found during testing was fixed. No actual images exist yet, so photographic rendering is **not validated**.
- JavaScript-disabled navigation from homepage to product and the visible eBay link: pass. No application script is present.
- Sold-state rehearsal on a disposable copy: `Sold` and `SoldOut` agree; purchase action and current-stock card removed; product URL remains HTTP 200; technical content and sitemap are unchanged; unknown paths return HTTP 404. Repository content remains in the verified available state.
- Mobile Lighthouse 13.5.0 on the local draft: **both homepage and product page scored 100/100/100/100** for performance/accessibility/best practices/SEO. These are provisional, image-free results; repeat with final photos and on the production host. Local Python hosting does not represent production caching/compression.
- QA dependencies and generated screenshots/reports were kept outside the repository; the website has no runtime/build dependencies. `git diff --cached --check`: pass after removing a trailing blank line in `.gitignore`.

Not performed: public-host HTTP/HTTPS checks, actual-photo validation, live Google Rich Results Test, Search Console setup/submission, deployment, DNS changes or any merge to `main`.
