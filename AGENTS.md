# BenchSpec agent instructions

Before creating or editing any BenchSpec catalogue page, read and apply `CATALOGUE_GUIDE.md` and use the repo-local `benchspec-catalogue` skill in `.agents/skills/benchspec-catalogue/`.

Treat `CATALOGUE_GUIDE.md` as the governing editorial, brand, condition-language, visual and catalogue standard for this repository.

## Product source-of-truth guardrail

The public site is a presentation layer, not the primary product record.

For every catalogue item, identify the corresponding durable record in `cbeveridge68/benchspec-ops` and ground product claims in that record. In particular:

- use the Ops `audit.md` for identity, condition, configuration, included components, completed tests and verification boundaries;
- use manufacturer/product documentation only where it is explicitly recorded or reliably identified;
- use Ops `pricing.md` as internal pricing evidence where relevant, while keeping public commercial facts consistent with the live selling channel;
- do not strengthen, infer or embellish a site claim beyond the Ops evidence;
- if the site and Ops record conflict, correct the site or flag the conflict rather than silently changing the meaning of the audit;
- if no durable Ops record can be found, flag that before publishing material factual claims.

When working on catalogue content:

- preserve exact manufacturer/model/MPN identifiers;
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
