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

1. `benchspec-ops` `audit.md` for identity, physical condition, configuration, inclusions, completed tests and test boundaries;
2. manufacturer/product documentation explicitly recorded or referenced by the audit for technical specifications;
3. `benchspec-ops` `pricing.md` for the current internal pricing decision when relevant to page preparation;
4. the live selling channel for current public price, availability, delivery, returns and transaction terms;
5. the existing site page only as the current presentation state.

Do not infer, embellish or strengthen a claim beyond the Ops audit. If the audit and site disagree, fix the site or flag the conflict; do not silently rewrite the audit from the site.

If no durable Ops record can be found, stop and flag that before publishing material factual claims.

## Read first

Before editing a product page, read:

- `AGENTS.md`;
- `CATALOGUE_GUIDE.md`;
- the corresponding `benchspec-ops` `audit.md`;
- `pricing.md` if present and relevant;
- retained actual-item images / image notes;
- the current product page, if one exists.

## Core writing rule

**Write the audit formally; write the catalogue page naturally.**

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

A clearly described test often defines its own scope. Do not automatically add a negative sentence about pressure, vacuum, flow, calibration or other unmeasured characteristics simply because the audit records that boundary. Include a test limitation on the public page only when omitting it could reasonably cause a technical buyer to over-read the claim.

Do not repeat the same verification in the summary, condition section and technical section unless each occurrence serves a distinct purpose.

## Page workflow

### 1. Confirm exact identity and sale unit

Confirm manufacturer, exact model/MPN, variant and BenchSpec reference from Ops. Confirm whether the offered unit is a single item, assembly, pair, quantity listing or batch.

### 2. Build search-visible identity

Keep exact searchable identifiers in the page title, H1, visible specification block, meta description and structured data where appropriate.

Do not shorten exact identifiers merely for visual neatness.

### 3. Write the top summary

The top summary should answer quickly:

- what the item is;
- the important included configuration;
- the strongest useful verification result.

Keep it concise. Avoid a second miniature audit.

### 4. Write condition and verification

Use natural prose, normally one or two short paragraphs.

State the strongest defensible condition first. Then describe the completed test in plain technical language.

A good pattern for a tested industrial component is:

`Very clean used condition. Tested at 24 V DC with the supplied controller and operating normally.`

`The pump starts normally, draws approximately 3 A at startup and settles at approximately 1.5 A running unloaded.`

Only add a verification-boundary sentence when it materially prevents an overclaim that the positive wording would otherwise imply. Do not add routine `not measured` statements merely to mirror the audit.

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
- Is any sentence merely restating another sentence?
- Has formal audit phrasing leaked into the public page?
- Are the useful test results easy to understand?
- Is any limitation actually needed, or is it present only because the audit recorded it?
- Could any buyer-facing claim be traced back to the Ops audit or documented product evidence?

If not, simplify the copy before publishing.

For wording examples, read `references/voice-examples.md`.
