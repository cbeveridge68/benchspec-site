# BenchSpec catalogue voice examples

These examples show how to translate a formal Ops audit into natural public catalogue copy without weakening the evidence boundary.

## Thomas 118ZC20/24UV pump + SK604530 controller

### Too audit-like

> Very clean and appears near-new or very lightly used. The pump head and body show no obvious damage. Protective red port caps are fitted. The controller PCB is clean, with no obvious burnt components, damaged connectors or other visible electrical damage.
>
> BenchSpec connected the supplied controller to this pump and powered the assembly from a current-limited 24 V DC bench supply. The pump started and continued running unloaded, with no abnormal behaviour reported. Approximately 3 A available was required for reliable startup; running current settled at approximately 1.5 A unloaded.
>
> No calibrated pressure, vacuum or airflow performance test has been performed.

Problems:

- copies the audit observation sequence instead of summarising buyer-relevant condition;
- `no obvious burnt components...` is inspection-report language;
- `no abnormal behaviour reported` is passive and procedural;
- `approximately 3 A available was required` is awkward;
- the final negative test statement is unnecessary here because the positive wording already says exactly what was tested.

### Preferred catalogue wording

> Very clean used condition. Supplied with the matching SK604530 controller and wiring harness.
>
> Tested together at 24 V DC and operating normally. The pump starts at approximately 3 A and settles at approximately 1.5 A running unloaded.

This stays inside the audit boundary while sounding like a specialist seller rather than a test report. The wording describes the completed test without turning every unperformed test into buyer-facing copy.

### Short top-of-page summary

> Thomas 118ZC20/24UV 24 V DC diaphragm pump supplied with its matching SK604530 controller and complete interconnecting harness. Tested together at 24 V DC and operating normally.

## General transformations

Audit-style:

> Visual identity / condition check: PASS.

Catalogue:

> Very clean used condition.

Audit-style:

> Continuous unloaded operation confirmed.

Catalogue:

> Tested and operating normally unloaded.

Audit boundary:

> Pressure / vacuum / calibrated airflow test: NOT PERFORMED.

Catalogue, normally:

> Omit it when the public wording already makes the actual test scope clear.

Only surface a negative test boundary when omitting it could reasonably mislead a technical buyer about what BenchSpec verified.

Audit-style:

> Controller PCB is clean with no obvious burnt components, damaged connectors or other visible electrical damage.

Catalogue, normally:

> Controller and wiring are clean and complete as supplied.

Only retain detailed absence-of-damage wording where the specific area is commercially important or where a buyer would reasonably expect disclosure.
