---
name: genz-pilot
description: Designs a proportionate test of one food and beverage change, separating feasibility and uptake from causal business impact. Specifies baseline, comparison, contribution, capacity, uncertainty and keep/tweak/stop/inconclusive decisions. Use when an owner asks how to try or evaluate a change.
---

# Genz pilot — learn what this test can actually show

Read the proposed move and relevant profile fields, `../genzfy/references/patterns.md` and
`../genzfy/references/claim-ledger.md`. A standalone test does not require full intake. Collect
only missing baseline, costs, eligible exposure, tools, operating constraints and decision needs.

## 1. Choose the question and design

- **Feasibility/adoption:** can staff deliver it, do customers understand/use it, does it stay
  within service and cost limits? A small short run can answer this without proving sales lift.
- **Causal effect:** did the change improve an outcome versus what would otherwise have happened?
  Prefer a concurrent randomized or suitable comparison when feasible. State allocation unit,
  eligibility, exposure, contamination and dependency assumptions.
- **Descriptive before/after:** useful when comparison is impractical, but log weather, holidays,
  other campaigns, prices, hours, stockouts and customer mix. Do not label change incremental.

Use one clearly defined intervention. A bundle can be tested as a bundle, but its components cannot
then be individually credited. Multiple interventions need a design that separates their effects.

## 2. Establish baseline and the worthwhile result

Record outcome, denominator, baseline period and comparable units (orders per eligible hour,
conversion among eligible visitors, contribution per shift). Obtain only tools confirmed available:
paper tallies may suffice. Check baseline variation across periods and capacity, not totals alone.

Set a practical minimum worthwhile result from contribution and effort. This is a business decision
threshold, **not a detectable effect** or proof of statistical significance. There is no reliable
power rule based only on 100, 500 or any other event count. A power/sample-size calculation needs
baseline rate or variance, meaningful effect, allocation, significance/power assumptions,
independence or clustering, attrition and repeated-testing plan. If unavailable, say power is
unknown and use a feasibility question or plan more data; never fabricate a detectable percentage.

New channel orders from a zero baseline establish use of that channel. They may be migration,
substitution or new demand. A code redemption is attribution, not necessarily incrementality.
Track total relevant demand and contribution where feasible and use a comparison to estimate
incrementality. Zero-baseline data cannot rescue an underpowered causal test.

## 3. Account for full economics and harms

State setup and recurring labor/cash separately. Compare revenue, retained revenue and contribution
using net sales excluding pass-through taxes and explicit costs, including discounts, packaging,
fees, delivery, refunds, waste and support.
Check cannibalization and displacement. Flat alcohol sales plus NA sales is not “pure gain”.
Guardrails can include contribution floor, queue time, stockouts, complaints and staff burden.

Use aggregate outcomes by default. Do not estimate age from appearance, require customer identity
tracking, or collect unnecessary sensitive data. If demographic analysis is actually needed, use
lawful, voluntary self-report with clear purpose and minimal retention. Compare cohorts directly;
significance in one subgroup and not another does not itself show a between-group difference.

## 4. Predefine the decision and window

Match timing to the question: a short run may test operations, whereas repeat visits, retention or
seasonality may need longer. Use real dates once a start date is known, verifying weekdays. If it
isn't agreed, use offsets labelled provisional rather than inventing a calendar commitment.

Specify **keep**, **tweak**, **stop** and **inconclusive** conditions before launch. Include both
business thresholds and guardrails. Keep can mean continue a feasible trial, not “causal success”.
Missing exposure, confounding, insufficient precision or failed implementation can make a result
inconclusive. A negative-contribution intervention can be stopped even with strong uptake. Do not
keep extending until a positive result appears; predefine one bounded extension or a new design.

## Output

Write `genzfy-workspace/<slug>/pilot.md`:

```markdown
# Pilot: <intervention>
question: <feasibility/adoption | causal effect | descriptive before/after>
window: <dates or provisional offsets; feasibility versus longer outcome follow-up>
owner: <person and time/capacity>
hypothesis: <outcome and minimum worthwhile result; labelled business threshold>
alternative: <migration, mix, calendar or other explanation>

## Before launch
- Baseline, period, variation, eligible exposure and source: <known/unknown>
- Comparison/allocation and limitations: <design>
- Costs, contribution calculation and measurement tool: <confirmed inputs>
- Setup, team instructions and permissions: <checklist>

## During
<Daily/shift measures, exposure, implementation, confounder and guardrail log>

## Decision
Keep / tweak / stop / inconclusive: <predefined conditions and decision date>
<What this design cannot establish; bounded next step and reversal>

## Outcome
<Observed counts/rates with denominators, costs, contribution, uncertainty and conclusion>
```

Afterwards update `profile.md` under `## What we tried`. Keep the distinction between adoption,
commercial performance and causal evidence in the summary, not just in a footnote.
