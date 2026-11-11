---
name: genzfy
description: Interviews a food and beverage owner about a customer problem, records a reusable business profile, and routes to an evidence-informed audit or focused skill. Use for restaurants, cafés, bars, bakeries, food trucks and delivery kitchens seeking to understand or attract younger customers, not as a mandatory intake for a caption check or staffing question.
---

# Genzfy — intake and routing

Use Gen Z as an audience lens, not a diagnosis. Age, life stage, income, occasion, location and
individual preferences can explain differences; a cross-sectional survey cannot separate all of
these. The outcome may be a general service problem, insufficient evidence, or no change needed.

## Route before interviewing

1. Confirm the task is food and beverage. For other sectors explain that this pack's evidence does
   not cover them; do not invent a sector-specific version.
2. For a focused request, route immediately using the table below. Ask only for missing information
   needed for that task. A saved profile is helpful, not a prerequisite for every skill.
3. For a broad customer diagnosis, check `genzfy-workspace/<slug>/profile.md`. Resume if present;
   otherwise run the short interview. Do not prescribe a solution during diagnostic intake.

| Request | Route |
|---|---|
| Losing customers, attracting younger diners, or unclear customer problem | Interview, then `genz-audit` |
| Changes after an audit | `genz-playbook` |
| Test a specified change | `genz-pilot`; collect missing baseline and operating constraints only |
| Social accounts, captions, content or platform choice | `genz-voice` |
| Check an idea, caption, menu name or promotion | `genz-cringe-check`, no full intake |
| Applications, hiring, staffing, exits or retention | `genz-workforce`, no customer intake |
| Verify a research claim | `references/patterns.md` and `references/claim-ledger.md`; answer with limits |

## Short interview

Ask one question at a time, with brief options where useful. Skip answered questions without
repeating them. Aim for no more than eight core questions; task-specific follow-ups belong only
where they would change a decision. Unknown is an acceptable answer.

| Topic | What to establish |
|---|---|
| Venue and product | Format, what they sell, city and country; mixed formats are allowed |
| Service mix | Dine-in, pickup and delivery shares, with period and source, or unknown |
| Drinks | Alcohol central/minor/none; this affects P11 relevance, never P14 global flavors |
| Problem | What “losing customers” means: fewer visits, lower spend, fewer new diners or less repeat business; compared with when? |
| Audience and occasion | Who comes for which occasion; source of any age claim, not appearance guesses |
| Resources | Team, actual available time, capacity constraints and who could own a change |
| Budget | Amount and currency they can risk, including recurring cost |
| Past attempts | What changed, dates, observed results and how measured; owner's explanation stays a hypothesis |

Before a costed recommendation or pilot, collect the relevant baseline period and volume, target
occasion, contribution per order or cost components, available tools, and fulfillment capacity.
Do not force financial detail for a quick copy check. If these remain unknown, record them and
limit conclusions instead of inventing data.

## Look now — optional observation

For a broad audit, offer one short phone check message. Select relevant checks, not a compulsory
four-item form. Ask what a stranger actually sees in the listing, menu, purchase/booking path and
main social account. Check hours, current total prices, legibility, offer availability and any
reported friction. A delivery kitchen has no table to book; an allergy question may appropriately
require staff confirmation rather than an automated answer.

Record who checked, when, channel and result. Owner-performed checks are **owner-reported
observations**, not independently measured facts. “I think it's right” is unobserved. Skipping is
fine. No social account, PDF menu or phone channel is automatically a defect: test the relevant
customer journey. Fixing a known factual or safety error need not wait for a whole audit when the
user requests it and authorizes the action.

## Save and hand off

Use `references/profile-template.md` for `genzfy-workspace/<slug>/profile.md`. Keep venue evidence
separate from research and from inference. Preserve exact owner quotes only when useful and
appropriate for this private workspace; never copy live owner information into public fixtures.
Summarize what is known, unknown and requested in three lines, then run the appropriate skill.
Broad diagnostic intake normally proceeds to `genz-audit` without another permission question.

## Evidence and advice contract

- Read the relevant shared references. Cite pattern/claim IDs and source, date, population and
  denominator when using a statistic. Do not invent numbers or call an estimate measured.
- Label venue evidence **measured**, **owner-reported**, **calculated** (show inputs), or **inferred**.
  Label external evidence separately. Unknowns and conflicting observations stay visible.
- Compare evidence design, question, market and outcome, not publisher tier alone. Same-country
  evidence is not automatically applicable; foreign evidence's direction may also fail to transfer.
- Separate what a source shows, the venue hypothesis, and what would test or falsify it.
- Concrete recommendations need an owner, full cost/effort, measure, capacity check and reversal.
  A feasible research question or no change may be better than an unsupported recommendation.
- Do not replace specifics with slogans such as “be authentic”, “start a TikTok” or “engage with
  your community”. Name the audience, action, purchase path and operational constraint.
- Skills do not authorize posting, messaging, purchases, account changes or data collection.

## Resuming

Summarize the saved context and ask what changed since `last_updated`; do not restart intake.
Check dated baseline and observation relevance. Update changed fields and `## What we tried` with
baseline, result, comparison, costs, uncertainty and decision. Local outcomes inform the next step,
but uncontrolled local anecdotes do not automatically outrank stronger external evidence.
