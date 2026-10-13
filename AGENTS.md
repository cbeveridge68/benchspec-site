# BenchSpec agent instructions

Before creating or editing any BenchSpec catalogue page, read and apply `CATALOGUE_GUIDE.md` and use the repo-local `benchspec-catalogue` skill in `.agents/skills/benchspec-catalogue/`.

Treat `CATALOGUE_GUIDE.md` as the governing editorial, brand, condition-language, visual and catalogue standard for this repository.

## Product source-of-truth guardrail

The public site is a presentation layer, not the primary product record.

For every catalogue item, identify the corresponding durable record in `cbeveridge68/benchspec-ops` and ground product claims in that record. In particular:

- use the Ops `audit.md` for identity, product positioning/context, condition, configuration, included components, completed tests and verification boundaries;
- use the Ops `listing.md` for the current approved sale-unit wording/data where useful;
- use manufacturer/product documentation only where it is explicitly recorded or reliably identified in the durable Ops record;
- use Ops `pricing.md` as internal pricing evidence where relevant, while keeping public commercial facts consistent with the live selling channel;
- do not strengthen, infer or embellish a site claim beyond the Ops evidence;
- do not add new technical specifications from ad-hoc web research directly to the site — establish them in Ops first or omit them;
- if the site and Ops record conflict, correct the site or flag the conflict rather than silently changing the meaning of the audit;
- if no durable Ops record can be found, flag that before publishing material factual claims.

## Autonomous completion expectation

For product-page work, do not stop after generating a first draft and hand normal editorial cleanup back to Craig.

Follow the full self-review loop in the `benchspec-catalogue` skill:

1. build an internal evidence map from Ops;
2. draft the buyer-facing page;
3. verify every technical/numeric claim against the evidence map;
4. perform an editorial pass for discoverability, repetition, tone and speculative negatives;
5. render and visually inspect desktop/mobile where tooling is available;
6. repair issues and repeat until clean;
7. confirm catalogue card, detail page, SEO metadata and structured data are consistent.

Ask Craig only for a genuine unresolved source conflict, material commercial decision, or missing fact that cannot safely be omitted. Routine wording, compression, positioning and layout decisions should be resolved by the agent using the repo rules.

When working on catalogue content:

- preserve exact manufacturer/model/MPN identifiers;
- make the item discoverable both by exact part number and by supported equipment class/application terms;
- use actual-item photography only;
- translate formal audit evidence into natural technical buyer-facing language rather than copying audit/test-report wording;
- state what BenchSpec has verified rather than listing hypothetical things it has not;
- keep test limitations specific and non-defensive;
- do not introduce generic compatibility disclaimers unless a specific material issue exists;
- do not imply refurbishment, calibration or functional testing unless documented;
- keep commercial facts consistent with the live selling channel;
- keep the implementation intentionally lean and static unless the operator explicitly approves a broader change.

If a requested change conflicts with `CATALOGUE_GUIDE.md`, flag the conflict rather than silently departing from the guide.

For each new or materially updated product page, apply the review checklist in `CATALOGUE_GUIDE.md` before considering the work complete.
