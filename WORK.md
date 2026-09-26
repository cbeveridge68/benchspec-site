# Work record — catalogue v1

## Current work — editorial review and image-source correction, 25 September 2026

Scope: a wording-only review of the homepage and all five published product pages, including meta descriptions, Open Graph descriptions and JSON-LD descriptions, before carrying the batch to a clean branch. Work remains local on `feat/catalogue-v1`; no branch transfer, commit, push, merge or deployment is included in this pass. The 24 September batch record below is historical wherever its copy or validation status has been superseded.

Changes: removed redundant caption explanations of per-unit pricing, changed the count to “5 equipment listings”, removed “pre-owned” from descriptions of apparently unused stock, and replaced mechanical inspection fragments with natural technical prose. Positive physical condition leads the verification detail and the specific testing limitation. Shortened repeated purchase/quantity explanations, clarified the controller's manual-and-binder wording and kept descriptions aligned across visible copy and metadata. The existing CRES condition and handling statements remain intact.

MAG-VIEW source rechecked: current `BenchSpec_Lot31_Audit.csv`, blob `a1e0c991f08e95d820e76b3972807234043ef478`, audit 13011, states that the original MVM-Q user's guide is included with the two-meter stock; it does not specify a guide per meter. Visible and JSON-LD wording now says “An original MVM-Q user's guide is included with the stock.” The inclusion heading no longer implies that every meter has a guide. No allocation or extra manual was invented; clarification has been requested separately.

Factual invariants: exact identifiers, ratings, quantities, serial numbers, prices, Offer fields, testing limitations, links, actual photographs and shipping availability are unchanged. The entire structured Product object excluding its editorial description, specification tables, key specifications and visible status/price blocks were compared with commit `05895b6`. CSS, logo/favicon, sitemap, robots and validator are unchanged. No “appears unused” observation has been upgraded into an unsupported new-condition or functional-test claim.

Final validation: normal and publication site checks pass for all six pages; HTML Validate passes; all 40 verification-boundary regression tests pass; `git diff --check` passes. Chrome checks pass on every page at 390 px and 1440 px: no horizontal overflow or header crowding, images and links resolve, keyboard/skip-link navigation works and JavaScript-disabled purchase navigation remains available. All five independent sold-state rehearsals pass, retaining permanent HTTP 200 URLs, technical content, photographs and sitemap entries. Fresh review screenshots are in `.qa/editorial-2026-09-25/`; representative desktop/mobile captures were visually inspected. No new Lighthouse run was performed for these wording-only changes; earlier scores remain historical. Changes remain uncommitted on the existing branch for the subsequent clean-branch step.

### Current photo state: processed replacements applied

Craig updated the descriptively named top-level sources after the renaming pass. The processed Perma Pure, MAG-VIEW and Spirax photographs are now applied to the website: ten selected source images, each with full-size and 480 px WebP outputs (20 changed assets). Unlike the earlier identical-source pass, these replacements visibly change the photographs. The following table is the current source mapping and supersedes the earlier image-source status.

| Source directly in `raw-images/` | Asset under `site/assets/` | Full-size dimensions |
| --- | --- | --- |
| `perma-pure-humidifier1-overview.jpeg` | `perma-pure-fc125-240-5mp/overview.webp` | 1215 × 1600 |
| `perma-pure-humidifier2-serial-011.jpeg` | `perma-pure-fc125-240-5mp/serial-011.webp` | 1253 × 1600 |
| `perma-pure-humidifier3-serial-010.jpeg` | `perma-pure-fc125-240-5mp/serial-010.webp` | 1380 × 1600 |
| `perma-pure-humidifier4-pair-alternate.jpeg` | `perma-pure-fc125-240-5mp/pair.webp` | 1096 × 1386 |
| `mag-view-flowmeter1-overview-processed.jpg` | `mag-view-mvm-050-q/overview.webp` | 1277 × 1600 |
| `mag-view-flowmeter2-packaged.jpeg` | `mag-view-mvm-050-q/packaged.webp` | 1384 × 1600 |
| `spirax-trap1-overview.jpeg` | `spirax-sarco-fa-150-71497/overview.webp` | 1191 × 1600 |
| `spirax-trap2-ratings.jpeg` | `spirax-sarco-fa-150-71497/ratings.webp` | 1509 × 1600 |
| `spirax-trap3-body.jpeg` | `spirax-sarco-fa-150-71497/body.webp` | 1461 × 1600 |
| `spirax-trap4-audit-label.jpeg` | `spirax-sarco-fa-150-71497/audit-label.webp` | 1600 × 1380 |

The current Perma Pure pair photograph replaces the previous pair view whose top-level source was removed by the operator. Its alt text now describes the two humidifiers without referring to an audit label absent from the new crop. Homepage/product image dimensions and responsive width descriptors match the replacement files. No product facts, prices, condition/verification prose, eBay destinations, JSON-LD, sitemap, CSS or architecture changed in this photo pass. Heater/controller assets and the existing MAG-VIEW manual asset remain unchanged. No source files were edited, restored from the subfolder or removed by this pass.

Validation: normal/publication site checks, HTML validation, all 40 verification-boundary regressions and `git diff --check` pass. Independent re-encoding confirms all 20 outputs match their current top-level sources. Chrome checks on the homepage and all three affected product pages pass at 390 px and 1440 px: images decode, full-size image links resolve, no horizontal overflow or header crowding. Updated screenshots are in `.qa/updated-photos-2026-09-25/`; desktop Spirax and mobile Perma Pure captures were visually reviewed. These current results supersede the earlier unchanged-image findings below. Work remains local and uncommitted; no push, branch transfer, merge or deployment.

### Historical follow-up: descriptive source filenames

Renamed all 24 image files directly in `raw-images/` to item-based numbered names at Craig's request; the timestamped subfolder is untouched. The map below supersedes top-level filenames in earlier source records while retaining original names for provenance. Image bytes and extensions are preserved. No website assets or pages changed in this rename pass.

Two new processed MAG-VIEW `.jpg` files were present alongside the older `.jpeg` files. Both sets are retained; processed variants are explicitly labelled `-processed`. These newly supplied processed variants have not yet been incorporated into the website. Earlier findings about identical MAG-VIEW sources applied to the older `.jpeg` files, not these new `.jpg` exports.

Validation: SHA-256 comparisons confirm every renamed photo is unchanged, every file in the timestamped subfolder is unchanged, and the entire `site/` tree is unchanged. Normal and publication site checks pass. No commit, push, merge or deployment.

| Current filename in immediate `raw-images/` | Previous filename |
| --- | --- |
| `controller1-overview.jpg` | `2026-09-13_16-32-22_AEST_01_IMG_8A225C25-AFCD-46D2-B5C1-6C2F82B73CC8.jpg` |
| `controller2-interior.jpg` | `2026-09-13_16-32-22_AEST_02_IMG_1841ACFD-E95E-4483-A29F-6F20C927459D.jpg` |
| `controller3-enclosure.jpg` | `2026-09-13_16-32-22_AEST_03_IMG_32C1F8A3-AE64-49A7-A39F-6D4FF6956111.jpg` |
| `controller4-manual.jpg` | `2026-09-13_16-33-44_AEST_01_IMG_D620011F-A2EE-48B6-8C4D-2ECA550D937A.jpg` |
| `heater1-overview.jpg` | `IMG_51F35372-0313-4A4E-B6D3-100239975F70.jpg` |
| `heater2-nameplate.jpg` | `IMG_4D0A9114-AF7A-4A73-97B1-2A5DD999ABDA.jpg` |
| `heater3-probe.jpg` | `IMG_D21A390C-ED98-451A-9CAF-58BDF78FC229.jpg` |
| `heater4-enclosure.jpg` | `IMG_BE5F2EC9-0E18-4230-8E76-CC850EEB452F.jpg` |
| `mag-view-flowmeter1-overview-processed.jpg` | `2026-09-13_16-22-29_AEST_01_IMG_87737F7E-6927-4AE9-AEA3-B9E47F89C89E.jpg` |
| `mag-view-flowmeter1-overview.jpeg` | `2026-09-13_16-22-29_AEST_01_IMG_87737F7E-6927-4AE9-AEA3-B9E47F89C89E.jpeg` |
| `mag-view-flowmeter2-packaged-processed.jpg` | `2026-09-13_16-22-29_AEST_02_IMG_78E6698E-04F4-4730-8441-4E203FAA4431.jpg` |
| `mag-view-flowmeter2-packaged.jpeg` | `2026-09-13_16-22-29_AEST_02_IMG_78E6698E-04F4-4730-8441-4E203FAA4431.jpeg` |
| `perma-pure-humidifier1-overview.jpeg` | `2026-09-13_15-44-01_AEST_01_IMG_BA98A548-3187-47A6-AEB5-1C89A1577C78.jpeg` |
| `perma-pure-humidifier2-serial-011.jpeg` | `2026-09-13_15-44-01_AEST_02_IMG_D6F0E637-AB54-4359-80FE-F8BDBEFE04C5.jpeg` |
| `perma-pure-humidifier3-serial-010.jpeg` | `2026-09-13_15-44-01_AEST_03_IMG_B06B7882-6A4D-4BE3-A75C-90FFFEC76296.jpeg` |
| `perma-pure-humidifier4-pair-alternate.jpeg` | `2026-09-13_15-44-01_AEST_04_IMG_A6D85AC7-0069-4BFF-B163-9A0A0027E84E.jpeg` |
| `perma-pure-humidifier5-pair.jpeg` | `2026-09-13_15-44-01_AEST_05_IMG_56335BA1-6691-4BE7-8FF8-6E12DF451021.jpeg` |
| `spirax-trap1-overview.jpeg` | `2026-09-13_16-28-38_AEST_01_IMG_C80DAA47-8619-4E69-AAE5-A80C59D7AE70.jpeg` |
| `spirax-trap2-ratings.jpeg` | `2026-09-13_16-28-38_AEST_02_IMG_179024FD-D66E-4952-874A-C124B8EBAF49.jpeg` |
| `spirax-trap3-body.jpeg` | `2026-09-13_16-28-38_AEST_03_IMG_1F24E332-4A0E-47C1-A276-55329130A731.jpeg` |
| `spirax-trap4-audit-label.jpeg` | `2026-09-13_16-28-38_AEST_04_IMG_6126D38B-38A4-4A13-9EB9-BC272153FA11.jpeg` |
| `swagelok-check-valve1.jpg` | `31002-1.jpg` |
| `swagelok-check-valve2.jpg` | `31002-2.jpg` |
| `swagelok-check-valve3.jpg` | `31002-3.jpg` |

### Follow-up: immediate `raw-images/` sources (before descriptive renaming)

Craig supplied the Spirax, MAG-VIEW and Perma Pure photographs directly in this repository's `raw-images/` and instructed that these take precedence over the timestamped subfolder. The selected source filenames are unchanged from the historical provenance table, but their current source directory is now **`raw-images/`**, with no subfolder:

- Perma Pure: `2026-09-13_15-44-01_AEST_01`, `_02`, `_03` and `_05` photographs → overview, serial -011, serial -010 and pair assets.
- MAG-VIEW: `2026-09-13_16-22-29_AEST_01` and `_02` photographs → overview and packaged assets.
- Spirax: `2026-09-13_16-28-38_AEST_01` through `_04` photographs → overview, ratings, body and audit-label assets.

The ten selected top-level originals were inspected and compared with their archived counterparts: each is byte-identical, with dimensions 1152 × 1536. Consequently this changes source provenance, not the visual appearance. The supplied files are preserved unchanged outside `site/`; full-size and 480 px WebP assets are re-encoded directly from these top-level sources. The additional Perma Pure `_04` photograph is not needed to duplicate the existing pair view.

Exception: the MAG-VIEW user's-guide photograph (`2026-09-13_16-34-15_AEST_01_IMG_65B55FBA-E478-496A-BB15-75AFE4D26A4A.jpeg`) has not been supplied at the top level. Its existing supporting asset is retained unchanged; it is not represented as a new processed replacement. Controller and heater images already use their approved top-level originals. Editorial changes and all product facts remain intact.

Follow-up validation: all 20 WebP outputs (ten full-size plus ten responsive variants) match independent encodings of the selected top-level source files. They are also byte-identical to the prior deployed assets, so no image dimension, HTML, JSON-LD or CSS change is necessary. Normal/publication site checks, HTML validation and `git diff --check` pass. Fresh Chrome checks on the homepage and all three affected product pages pass at 390 and 1440 px: all images decode, full-size links resolve, and there is no horizontal overflow or header crowding. Refreshed screenshots are in `.qa/raw-image-sources-2026-09-25/`; the desktop trap capture was visually checked. No commit, push or branch transfer was made.

## Historical work — first Lot 31 catalogue batch, 24 September 2026

Status: bounded implementation and validation complete on `feat/catalogue-v1`: four additional product pages, five saleable product pages in total. TSI and Swagelok KPR are withheld because Craig confirmed they are not yet listed on eBay. The containing commit SHA and remote push verification are reported in the handoff. **Not merged or deployed.** This section supersedes the first-slice status and validation records below, which are historical.

Bounded scope: six requested items only (BS-INFI-001, BS-TSI-001, BS-PPUR-001, BS-MAGV-001, BS-SWAG-004 and BS-SPIR-001), using hand-authored pages and the existing layout. Publish only items with actual photographs, an established public asking price and a positively identified current BenchSpec eBay destination. Keep incomplete items outside `site/`, with exact blockers recorded here. Never infer completed testing from plans or publish private commercial figures.

Primary evidence: current `cbeveridge68/erpnext-ops` main at `5cafd9b3d7a4f873d10cbaa65f81d5add254cf8f`; `benchspec/auctions/grays lot31/BenchSpec_Lot31_Audit.csv` (blob `a1e0c991f08e95d820e76b3972807234043ef478`) and `Lot31_Pricing_Strategy_2026-09-17.md` (blob `b9fa7881478ae512e8a44a13c3b9890fd461b873`). The source checkout's unrelated changes remain untouched.

Live [BenchSpec eBay store](https://www.ebay.com.au/str/benchspec) inspected in Chrome on 24 September: exact controller, Perma Pure, MAG-VIEW and Spirax listings found. Craig explicitly approved using the current live Perma Pure A$795, MAG-VIEW A$400 and Spirax A$725 asking prices instead of the older commercial-record prices. Controller remains A$1,995. Actual photographs for all six requested items have been located in the supplied `raw-images/` archive; selected originals will remain outside the deployed tree.

Acceptance: normal/publication site checks; HTML validation; visible/JSON-LD, canonical/sitemap and exact eBay-link agreement; actual-image review; desktop and 390 px mobile screenshots with no overflow; preserved brand/contact/footer and no application JavaScript; sold-state rehearsal; `git diff --check`; commit and push this branch only. Final item disposition and fresh results will be recorded here before handoff.

### Implemented pages and public offer evidence

| Permanent product path under `/products/` | Audit / SKU | Public asking price | Exact BenchSpec eBay destination |
| --- | --- | --- | --- |
| `infinity-fluids-ptc-12-20-1p/` | 13014 / BS-INFI-001 | A$1,995 | [198658139207](https://www.ebay.com.au/itm/198658139207) |
| `perma-pure-fc125-240-5mp/` | 31006 / BS-PPUR-001 | A$795 each | [198644525062](https://www.ebay.com.au/itm/198644525062) |
| `mag-view-mvm-050-q/` | 13011 / BS-MAGV-001 | A$400 each | [198645719640](https://www.ebay.com.au/itm/198645719640) |
| `spirax-sarco-fa-150-71497/` | 13013 / BS-SPIR-001 | A$725 | [198646864549](https://www.ebay.com.au/itm/198646864549) |

The live store returned HTTP 200 in Chrome and supplied these exact item links, exact model titles and AUD prices. Later direct-item retrieval encountered eBay HTTP 403/verification challenges; these were not bypassed. Destination identity and asking prices are established by the successfully retrieved live seller store, not invented links or other sellers' offers. The individual listings' shipping coverage and manual allocation could not be independently re-read: new pages therefore say “International shipping enquiries welcome”, direct transaction terms to eBay, and do not promise a manual with each MAG-VIEW unit. Quantities follow the current audit (controller 1, Perma Pure 2, MAG-VIEW 2, Spirax 1); recheck live quantity and destination-specific delivery immediately before deployment.

The existing [CRES heater listing](https://www.ebay.com.au/itm/198659547917) was successfully retrieved directly: BenchSpec, exact MPN, A$1,495 and an active Buy It Now offer. This resolves the historical inability to read that live offer on this review date; it does not remove normal pre-launch stock checks.

Changes remain bounded: four manually authored HTML pages, four homepage entries (five total), four sitemap entries and accurate two-way Infinity related-equipment links. Header/footer, logo/favicon, navy/white CSS, contact details, homepage positioning, robots and no-JavaScript architecture are unchanged. No test plan is represented as a completed test. Optional unrecorded weights/dimensions and MAG-VIEW connection size are omitted. The apparently unused items retain that qualified physical-condition description; their conservative `UsedCondition` metadata describes pre-owned surplus, not a claim of new or function-tested stock.

The existing checker now recognises the specific process-testing, dry-flow and wet/pressure-test boundaries for this batch, requiring the same explicit limitation in visible text and structured Test status. A bare “Untested” label still fails. No dependency, build step or product-data layer was added. README now describes the five-product catalogue and item-specific publication gating.

### Withheld items — exact blockers

- **TSI 4140D / BS-TSI-001 / audit 13021:** Craig confirmed no current eBay listing exists. The commercial record provides a non-tested/open-box asking range, not a single verified live asking price. Required before publication: the exact live BenchSpec listing and its chosen non-tested public BIN price. Actual kit, instrument, historical calibration label and filter photographs are available and selected originals are retained. Calibration dated 04/08/2014 is historical only; no completed power/display/zero-flow test is recorded. The Infinite Filter 14SX remains an unverified third-party accessory, not a claimed calibrated/matched TSI component. No page, card, sitemap entry, Offer or purchase action was published.
- **Swagelok KPR1DRF412A20000 / BS-SWAG-004 / audit 13012:** Craig confirmed no current eBay listing exists. A$649 remains the provisional public asking position in the inspected commercial record, not a verified live offer. Required before publication: exact live BenchSpec listing and confirmation of its public BIN price. Four actual package/marking photographs are retained. Preserve the intentionally unopened package and fitted protective caps; do not claim factory-sealed packaging or completed pressure testing. No page, card, sitemap entry, Offer or purchase action was published.

### Selected actual-item photograph provenance

Controller web assets use **only the four processed `.jpg` files immediately inside this repository's `raw-images/`**, as explicitly directed by Craig during review. The older controller `.jpeg` files in the timestamped subfolder are not used. The selected processed files are preserved unchanged; only WebP encodings and 480 px derivatives are deployed.

| Controller web asset | Source in immediate `raw-images/` | Source dimensions |
| --- | --- | --- |
| `overview.webp` | `2026-09-13_16-32-22_AEST_01_IMG_8A225C25-AFCD-46D2-B5C1-6C2F82B73CC8.jpg` | 1312 × 1600 |
| `interior.webp` | `2026-09-13_16-32-22_AEST_02_IMG_1841ACFD-E95E-4483-A29F-6F20C927459D.jpg` | 1600 × 1148 |
| `enclosure.webp` | `2026-09-13_16-32-22_AEST_03_IMG_32C1F8A3-AE64-49A7-A39F-6D4FF6956111.jpg` | 1155 × 1600 |
| `manual.webp` | `2026-09-13_16-33-44_AEST_01_IMG_D620011F-A2EE-48B6-8C4D-2ECA550D937A.jpg` | 1203 × 1600 |

Other selected sources are unchanged files inside `raw-images/BenchSpec_Grays_Lot31_Audit_Images_Timestamped/`. Each timestamp/sequence prefix below identifies one original unambiguously; original UUID filenames are retained. All deployed sources below are 1152 × 1536. Full-size WebP quality 86 and 480 px quality 82 derivatives retain the supplied framing; no substitute imagery or AI processing was used.

| Product / web asset | Original filename prefix (all dated 2026-09-13) |
| --- | --- |
| Perma Pure / `overview.webp` | `2026-09-13_15-44-01_AEST_01_IMG_` |
| Perma Pure / `serial-011.webp` | `2026-09-13_15-44-01_AEST_02_IMG_` |
| Perma Pure / `serial-010.webp` | `2026-09-13_15-44-01_AEST_03_IMG_` |
| Perma Pure / `pair.webp` | `2026-09-13_15-44-01_AEST_05_IMG_` |
| MAG-VIEW / `overview.webp` | `2026-09-13_16-22-29_AEST_01_IMG_` |
| MAG-VIEW / `packaged.webp` | `2026-09-13_16-22-29_AEST_02_IMG_` |
| MAG-VIEW / `manual.webp` | `2026-09-13_16-34-15_AEST_01_IMG_` |
| Spirax / `overview.webp` | `2026-09-13_16-28-38_AEST_01_IMG_` |
| Spirax / `ratings.webp` | `2026-09-13_16-28-38_AEST_02_IMG_` |
| Spirax / `body.webp` | `2026-09-13_16-28-38_AEST_03_IMG_` |
| Spirax / `audit-label.webp` | `2026-09-13_16-28-38_AEST_04_IMG_` |

For the withheld items, preserve the four `2026-09-13_16-26-03_AEST_01` through `_04` KPR photographs and TSI sources `IMG_2B67D908-35B9-43D7-A932-42038DC4AB82.jpeg` (kit), `IMG_43F218E7-0F1C-44B0-B93C-770210CCF5CB.jpeg` (instrument), `IMG_C7DDB484-78EA-420F-AAD1-452D2DADFC07.jpeg` (model/serial/historical calibration) and `IMG_B3BF9F9B-9403-4822-91FE-6579BE5A3EEB.jpeg` (filter). These eight files remain outside the deployed tree and are not used by any public page. Other unrelated supplied images remain untouched and untracked.

### Final batch validation — after processed controller-photo replacement

- `python3 tools/check_site.py` and `python3 tools/check_site.py --publication`: **PASS**, all six HTML pages. Exact visible/structured identifiers, asking prices, status and purchase URLs agree; local images/links resolve; sitemap has exactly the six self-canonical URLs. Blocked products are absent from the deployable tree.
- HTML Validate 11.16.0: **PASS**, all six pages. `xmllint --noout site/sitemap.xml site/assets/benchspec-logo.svg site/assets/favicon.svg`: **PASS**. `git diff --check`: **PASS**.
- Chrome at **390, 768 and 1440 px**, every page: **PASS**. No horizontal overflow or header crowding; all photographs decode and full-size photo links return HTTP 200; no application scripts; header/footer identity and exact email destinations intact. Forward/reverse keyboard navigation, visible focus, skip links and JavaScript-disabled product navigation pass. Mail links were checked without sending email or claiming mailbox deliverability.
- Desktop/mobile screenshots visually reviewed, including corrected controller framing/orientation. Final captures are `.qa/lot31/homepage-{desktop,mobile}.png` and `.qa/lot31/<product-slug>-{desktop,mobile}.png` for all five products, with tablet captures and `browser-results.json` alongside. QA outputs are ignored local review artifacts, outside `site/`.
- Available-to-sold rehearsal: **PASS for each of the five products independently**, on disposable copies only. Sold/SoldOut agree, purchase action and buying instructions are removed, last asking price is labelled, only the sold item's homepage card is removed, and technical content/photos/sitemap remain intact. Each permanent URL still returns HTTP 200; unknown paths return HTTP 404. Actual repository state remains available.
- Verification-boundary regression checks: **40 PASS** across the five products and both checker modes. Whitespace-wrapped exact limitations are accepted; removing the visible limitation while retaining JSON-LD, replacing it with a bare “Untested” label, or claiming successful testing is rejected.
- Additional local mobile Lighthouse 13.5.0 checks: homepage **98 performance / 100 accessibility / 100 best practices / 100 SEO**, LCP 2.1 s, CLS 0; processed-photo controller page **91 / 100 / 100 / 100**, LCP 1.7 s, CLS 0. Both meet the ≥90 performance target. These are local-preview results, not production-host measurements; browser validation was also running during these measurements.
- The catalogue-guide checklist was applied to each new page: exact identity, actual photographs, approved current public price, audited quantity, known-condition-first language, specific recorded test boundary, item-specific eBay terms and conservative shipping wording. No factory-sealed, calibrated, refurbished, completed functional-test or tested-pairing claim was introduced. Public price changes were explicitly approved by Craig. Exact eBay destinations were positively identified in the live BenchSpec store, with the direct-item access limitation documented above.

Remaining items: two unlisted products require their own verified live offers before pages can be published; MAG-VIEW manual allocation remains item-specific; stock/delivery terms require the routine launch recheck. Hosting/DNS, Search Console and public-host checks remain a separate authorised launch step. No source-system, eBay listing, merge, deployment or DNS changes were made.

## Historical first-slice record

Status: first slice implemented with actual-item photographs; **not merged or deployed**. The live eBay offer recheck and separate launch checks remain outstanding. Approved by Craig on 24 September 2026, including the subsequent heading/copy/photo amendments.

Current approved state: the header logo reads **SPECIFIED • VERIFIED** and the heater short condition reads **Used item in very clean physical condition. Visually inspected and verified complete as offered.** Visible copy, metadata, JSON-LD and `CATALOGUE_GUIDE.md` agree. Fresh normal/publication, HTML/XML and responsive/sold-state checks pass with no local validation exception. See “Current approved-state validation” below for the authoritative results. All earlier review/validation sections are historical. Branch: `feat/catalogue-v1`; no merge or deployment.

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

## Current approved-state validation — 24 September 2026

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
