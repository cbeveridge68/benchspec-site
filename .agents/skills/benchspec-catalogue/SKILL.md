---
name: benchspec-catalogue
description: Create or revise BenchSpec catalogue product pages from the durable BenchSpec Ops audit/source record, current commercial facts and actual-item photography.
---

# BenchSpec Catalogue

Use this skill whenever the task is to create, revise, review or finalise a BenchSpec product page in `benchspec-site`.

## Source-of-truth guardrail

The public catalogue page is a presentation layer. It must not become the primary source for product facts.

For every product page, identify the corresponding durable item record in `cbeveridge68/benchspec-ops` and use that record as the factual source of truth.

Use this precedence:

1. `benchspec-ops` `audit.md` for identity, product positioning/context, physical condition, configuration, inclusions, completed tests and test boundaries;
2. manufacturer/product documentation explicitly recorded or referenced by the audit for technical specifications;
3. `benchspec-ops` `listing.md` for the current approved sale-unit wording/data where useful;
4. `benchspec-ops` `pricing.md` for the current internal pricing decision when relevant to page preparation;
5. the live selling channel for current public price, availability, delivery, returns and transaction terms;
6. the existing site page only as the current presentation state.

Do not infer, embellish or strengthen a claim beyond the Ops evidence. If the audit and site disagree, fix the site or flag the conflict; do not silently rewrite the audit from the site.

Do not introduce new manufacturer specifications into a site page from ad-hoc web research. New technical facts should first be established in the durable Ops record. If a useful specification is not in Ops, omit it from the site rather than improvising it.

If no durable Ops record can be found, stop and flag that before publishing material factual claims.

## Read first

Before editing a product page, read:

- `AGENTS.md`;
- `CATALOGUE_GUIDE.md`;
- the corresponding `benchspec-ops` `audit.md`;
- the corresponding Ops `listing.md` when present;
- `pricing.md` if present and relevant;
- retained actual-item images / image notes;
- the current product page, if one exists.

## Autonomous completion loop

Do not treat the first generated page as finished. Complete the following loop without asking Craig to arbitrate normal wording or presentation choices.

### Pass 1 — evidence map

Before changing HTML, build a temporary internal evidence map from the durable sources. It is working state only and does not need to be committed.

Capture:

- exact identity / MPN / variant;
- sale unit and included components;
- product class and positioning terms supported by the audit;
- manufacturer-backed specifications;
- observed condition;
- completed functional tests and their results;
- specific known defects / exclusions / safety facts, if any;
- public price / availability / quantity;
- approved actual-item images.

Every numeric technical claim intended for the page must be traceable to this evidence map. If a number cannot be traced, do not publish it.

### Pass 2 — buyer-facing draft

Create or revise the page from the evidence map, not by copying the audit prose.

The first visible screen should work for both kinds of buyer:

1. someone searching the exact manufacturer/model/MPN; and
2. someone searching by equipment class, application or technical need who does not yet know the exact part.

Where the audit contains product positioning/context, carry the useful class/application terms into the H1, subheading, catalogue card or opening copy naturally. Do not manufacture marketing adjectives such as `premium`, `rare` or `high-value`.

### Pass 3 — factual QA

Re-read the completed visible page, metadata and structured data against the evidence map.

Check every:

- model / MPN;
- technical number;
- performance figure;
- electrical rating;
- condition claim;
- test claim;
- inclusion / exclusion;
- price / availability statement.

Remove or correct anything that is not supported by the durable sources.

Pay particular attention to plausible-looking numbers. A technically plausible figure is still wrong if it is not the supported figure for this exact item/variant.

### Pass 4 — editorial QA

Read the page as a technical buyer rather than as its author.

Check that:

- the exact part identity is obvious;
- the generic equipment class / application is also obvious where supported;
- the equipment type is obvious without a lengthy explanation of how it is used;
- the wording sounds like BenchSpec selling the item, not writing an audit or manufacturer's brochure;
- audit/test-report phrasing has not leaked into public copy;
- the same fact is not repeated across card, hero, condition and technical sections without purpose;
- negative statements describe known facts, not speculative possibilities;
- routine unperformed tests have not become public disclaimers;
- condition prose sounds natural and confident;
- headings and specification labels use buyer language rather than internal workflow language.

Rewrite until these checks pass.

### Pass 5 — visual QA

When local render/browser/screenshot tooling is available, render the changed page and inspect it before finishing.

Check at least:

- desktop layout;
- mobile layout where practical;
- H1 wrapping and hierarchy;
- lead-image crop / orientation;
- card-to-detail consistency;
- price / availability prominence;
- technical-table readability;
- thumbnail captions and image order.

Fix visible presentation problems rather than reporting them back for Craig to resolve.

### Pass 6 — final consistency pass

Compare the catalogue card, product page, SEO title/meta and structured data one final time. They must describe the same product, positioning, price, condition and availability.

Only consider the task complete after the factual, editorial and visual passes are clean.

Ask Craig only when there is a genuine unresolved source conflict, a material business decision, or missing information that cannot safely be omitted. Do not ask for approval of routine wording choices that can be resolved by this skill.

## Core writing rule

**Write the audit formally; write the catalogue page naturally.**

**The voice matters more than the volume of technical detail.** A BenchSpec page is a simple, credible sales listing for people who usually know the part they want. Use direct, everyday English; stay accurate and matter-of-fact. Do not make the reader work through an internal audit report, specifications essay or long disclaimer. Prefer `Used, in good physical condition` over `externally intact`; prefer `Powered on at 24 V DC with status LEDs checked` over lab-report language. State the completed checks and stop. Do not routinely append `Safety functions have not been tested` (or any other `not tested` sentence) after a clear power-on/LED test statement, including for safety I/O modules. Disclose a specific material safety issue or other required limitation when genuinely necessary, without adding boilerplate. Avoid `recorded sale configuration`, `audited batch`, `verification boundary` and `safety-function validation` in public copy.

When several units share the same model and series, describe the **buyer-facing sale unit** simply. Do not expose revisions, date codes, origin or batch tracking just because those details exist in Ops, unless material to compatibility, condition or what is actually offered.

The audit is evidence, not copy. Translate verified facts into concise technical prose that sounds like a competent specialist describing the item to another technical buyer.

Prefer:

- `Very clean used condition. Tested at 24 V DC with the supplied controller and operating normally.`
- `The pump starts normally, draws about 3 A at startup and settles at about 1.5 A running unloaded.`

Avoid copying audit language such as:

- `no abnormal behaviour reported`;
- `continuous unloaded operation confirmed`;
- `visual identity / condition check passed`;
- `no obvious burnt components, damaged connectors or other visible electrical damage` unless a specific observed defect comparison is genuinely useful to the buyer;
- routine statements listing performance characteristics that were not measured.

## Negative statements

Buyer-facing copy should be evidence-led, not defensive.

Use negative wording when it describes a **specific known fact** that matters to the buyer, for example:

- visible damage or a missing component;
- an actual failed or negative test result;
- a known material exclusion;
- an expired calibration status where calibration matters;
- a specific safety limitation.

Do **not** introduce speculative negative statements about things that might be wrong, might fail, might be incompatible or were simply not investigated. Do not turn every unperformed audit test into a public disclaimer.

A clearly scoped positive statement normally defines the verification boundary. For example, `Tested at 24 V DC and operating normally unloaded` does not require an added sentence listing pressure, vacuum or flow measurements that were not taken. Likewise `Powered on at 24 V DC with status LEDs checked` should **not** be followed by `Safety functions have not been tested.` A specific material issue or necessary safety disclosure is different from reciting a routine unperformed test.

Only surface an unperformed-test boundary when omitting it would materially mislead a reasonable technical buyer about what BenchSpec verified.

Do not repeat the same verification in the summary, condition section and technical section unless each occurrence serves a distinct purpose.

## Page workflow

### 1. Confirm exact identity and sale unit

Confirm manufacturer, exact model/MPN, variant and BenchSpec reference from Ops. Confirm whether the offered unit is a single item, assembly, pair, quantity listing or batch.

### 2. Build search-visible identity

Keep exact searchable identifiers in the page title, H1, visible specification block, meta description and structured data where appropriate.

Also surface supported equipment-class / application language so the page is discoverable by buyers who know the need but not the exact part number.

Do not shorten exact identifiers merely for visual neatness.

### 3. Write the top summary

The top summary should answer quickly:

- what the item is;
- what technical class/application it serves, where supported;
- the important included configuration;
- the strongest useful verification result.

Keep it concise. Avoid a second miniature audit.

### 4. Write condition and verification

Use natural prose, normally one or two short paragraphs.

State the strongest defensible condition first. Then describe the completed test in plain technical language.

A good pattern for a tested industrial component is:

`Very clean used condition. Tested at 24 V DC with the supplied controller and operating normally.`

`The pump starts normally, draws approximately 3 A at startup and settles at approximately 1.5 A running unloaded.`

Do not reproduce every visual inspection observation from the audit unless it materially helps a buyer assess the item.

### 5. Technical specifications

Use exact supported values only. Preserve useful MPNs, ratings, interfaces and controller/accessory identities.

Do not publish unsupported values such as `Unknown` or `Not verified`; omit them unless the absence itself is materially useful.

### 6. Inclusions and exclusions

List only meaningful supplied components and material exclusions. Avoid boilerplate such as `only what is pictured is included` when the page already clearly enumerates the supplied assembly.

### 7. Commercial facts

Keep public price, stock status, quantity, eBay destination, shipping and transaction terms consistent with the live selling channel.

Use Ops pricing as internal decision evidence, not as permission to publish internal floors, targets, acquisition cost or margin notes.

### 8. Photography

Use actual-item photography only. Prefer overall view, identity/nameplate, interfaces/configuration, included accessories and useful condition details.

Do not use troubleshooting or temporary test-setup images unless they materially improve buyer confidence and do not make the offered item look improvised.

### 9. SEO and structured data

Ensure title, meta description, visible copy and structured data describe the same item, condition and availability. Do not add unsupported technical claims for SEO.

### 10. Sold-state handling

Preserve useful permanent pages after sale. Update stock state and structured availability, remove the purchase action, and retain the technical record and actual photography according to `CATALOGUE_GUIDE.md`.

## Voice check

Before finishing, read the visible product copy as a technical buyer would.

Ask:

- Does this sound like a human specialist rather than an audit report?
- Can both an exact-part buyer and a category/application buyer understand the item quickly?
- Could the main description be said naturally to a buyer in two short sentences?
- Are there formal phrases that could be replaced with plain English without losing accuracy?
- Is any sentence merely restating another sentence?
- Has formal audit phrasing leaked into the public page?
- Are the useful test results easy to understand?
- Did we append a negative `not tested` sentence to a complete, scoped positive test result? Remove it unless a specific material disclosure requires it.
- Is any negative statement a specific known fact, or is it speculative/defensive?
- Could every technical claim be traced back to the Ops audit or documented product evidence?

If not, simplify or correct the copy before publishing.

For wording examples, read `references/voice-examples.md`.
