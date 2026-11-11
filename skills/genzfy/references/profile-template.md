# Profile template

Keep these field names stable. Use unknown rather than invented values. Add only fields relevant
to the request. Mixed formats and multiple occasions are valid.

```markdown
# <Venue> — Genzfy profile
last_updated: <YYYY-MM-DD>
venue_format: <takeaway | sit-down | cafe | bar | bakery | truck | delivery-only | mixed: details>
what_they_sell: <description>
market: <city, country>
currency: <currency>
channel_split: <shares, period, source | unknown>
alcohol: <central | minor | none>
current_customers: <occasion/needs; age only with source and uncertainty>
problem_definition: <outcome that changed, comparison period, evidence | unknown>
target_occasion: <who needs what, when, budget/constraints | unknown>
team_size: <including owner | unknown>
available_time: <person-hours, skills, owner | unknown>
budget_band: <none | low | medium | high; actual amount and recurring limit>
baseline: <metric, value, denominator, period, source | unknown>
contribution: <price less product/packaging/payment/channel/variable labor costs; inputs | unknown>
measurement_tools: <confirmed tools and accessible measures | unknown>
capacity: <spare capacity, queues, staffing, fulfillment limits | unknown>
already_tried: <change, dates, measured outcome; explanation separately>
owner_words: "<useful exact quote, or not supplied>"

## Observed
google_listing: <who/when/channel/result | unobserved | not applicable>
menu: <who/when/price accuracy/legibility/availability | unobserved>
written_path: <who/when/order or booking journey, response and accessibility | unobserved>
last_social_post: <date/platform/source | unobserved | not applicable>

## Evidence labels and conflicts
<For each material item: measured | owner-reported | calculated (inputs) | inferred.
Preserve contradictions, missing dates, ambiguous denominators and alternative explanations.>

## Evidence caveat
market_is_us: <yes | no>
market_has_local_evidence: <relevant pattern/claim IDs, or none>
<What matches this market, population and occasion; what cannot be assumed to transfer.>

## What we tried
<Move, dates, baseline, outcome, comparison, costs, uncertainty, kept/tweaked/stopped/inconclusive.>
```

Read `references/patterns.md` and `references/claim-ledger.md` for evidence scope. No profile field
is evidence that a generation caused the problem. Keep live business and employee details private;
collect only what the decision needs, preferably aggregate data.
