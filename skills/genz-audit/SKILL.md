---
name: genz-audit
description: Reviews a food and beverage venue across seven customer-journey dimensions using venue evidence and bounded research. Produces supported concerns, alternatives and unknowns rather than a predictive Gen Z score. Use for a customer diagnosis after a profile or enough equivalent context exists.
---

# Genz audit — findings before prescriptions

Read the profile (or supplied equivalent), `../genzfy/references/patterns.md`,
`../genzfy/references/claim-ledger.md` and `references/rubric.md`. If essential references cannot be
read, report the limitation rather than cite them from memory. If venue context is missing, use
`genzfy` to collect only what matters.

## Filter by use case, not stereotype

List applicable patterns and exclusions with reasons, based on service mix, occasion, market and
operating model. A mixed dine-in/pickup business needs separate channel checks. Alcohol status may
change P11's priority; P14 flavors is independent. Nonalcoholic drinks can matter at a venue that
sells no alcohol. Minor alcohol share does not quantify a nonalcoholic opportunity.

Match a study's actual geography, age definition, question, denominator and outcome. An adolescent
alcohol survey cannot establish legal-age customer demand. A local market variant is external
research, not venue evidence, and does not win automatically over a better-designed source.

## Review seven dimensions

Use the statuses and questions in `references/rubric.md`. Do not generate a total, grade or 0–3
score. This is an unvalidated diagnostic checklist, not a predictive instrument. For each dimension:

- State **supported concern**, **no concern established**, **mixed**, **unknown**, or **not applicable**.
- Quote or describe the actual venue evidence, its date, source and label: measured,
  owner-reported, calculated or inferred. An owner's phone check is owner-reported observation.
- Name relevant pattern/claim IDs and their limits. No evidence means unknown, not failure.
- Separate the observed issue from its possible cause. Give competing explanations where plausible.
- Identify what would change the finding, and a proportionate check if it affects a decision.

Combine mixed evidence explicitly. If hours are verified wrong but photos are unobserved, report a
supported hours concern and unknown photos; do not generalize to the whole discovery journey.
An old social post alone does not show lost demand. No loyalty scheme, events or Wi-Fi is not a
failure when the venue serves its intended occasion well.

## Rank the decision needs

Rank supported issues by plausible business impact, confidence, urgency, cost to investigate and
operational constraints. Do not convert pattern confidence into a causal venue diagnosis. Known
incorrect hours or a broken order link can be corrected without proving a cohort-specific effect.
Keep Now to at most three important concerns or checks. Larger uncertainty can justify measurement
before investment. No change recommended is valid. Do not manufacture a strength or gap.

An unsuccessful campaign does not prove awareness was adequate. Check exposure, targeting, offer,
tracking, purchase friction, price, quality and capacity before assigning cause. Likewise,
simultaneous staffing and service problems may be related but are not automatically one cause.

## Output

Write `genzfy-workspace/<slug>/audit.md`:

```markdown
# <Venue> — customer journey audit
date: <YYYY-MM-DD>
method: unvalidated diagnostic checklist; no overall score

## Dimension findings
| Dimension | Status | Venue evidence and limits |
|---|---|---|
<D1–D7; expand material findings with evidence label, pattern/claim, alternatives and falsifying check>

## What is supported
<Strengths or concerns actually evidenced; say none established if appropriate>

## Decision needs, ranked
### Now
<Up to three supported concerns or important checks, not a shopping list>
### Next
### Later

## Unknowns and contradictions
<What is missing, what conflicts, and a check that would change the decision>

## Applicable and excluded evidence
<Pattern IDs and reasons; population/market/design limits>

## Conclusion
<What can and cannot be diagnosed; non-generational explanation/no change if warranted>
```

Hand supported priorities to `genz-playbook`. If the owner disputes a finding, inspect the new
evidence, update or mark mixed/unknown. The checklist does not outrank the venue's observed facts.
