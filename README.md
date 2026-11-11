# Genzfy

An evidence-informed skill pack for food and beverage owners: understand a customer or staffing
problem, choose a feasible change, and measure what the result actually shows.

Gen Z is an audience lens, not a diagnosis. The pack considers occasion, locality, budget, service
format and individual needs. It can conclude that the problem is not generational, more evidence
is needed, or no change is justified.

**Food and beverage only:** restaurants, cafés, bars, bakeries, food trucks and delivery kitchens.
The references do not support sector-specific advice for unrelated businesses.

## Install

**Claude Code plugin** from this repository:

```text
/plugin marketplace add Kaseban/genzfy-public
/plugin install genzfy@genzfy
```

**Claude Code loose skills**, from a checkout:

```bash
ln -s "$PWD/skills"/* ~/.claude/skills/
```

Install all seven together: shared references use sibling paths.

**Claude.ai:** run `python3 scripts/build.py claude-ai`, then upload each zip in
`dist/claude-ai/` under Settings → Capabilities → Skills. Each bundle includes its referenced
resources. Save the private profile and audit and reattach them when resuming in a new chat.

**ChatGPT and other assistants:** see [the adapter guide](platforms/chatgpt/README.md).
Build outputs are generated locally and are not tracked source files.

## Skills

| Skill | Purpose |
|---|---|
| `genzfy` | Short diagnostic intake, reusable profile and task-specific routing |
| `genz-audit` | Seven dimension-level findings with evidence, alternatives and unknowns; no overall score |
| `genz-playbook` | Feasible actions, full costs, contribution, capacity, responsibilities and reversals |
| `genz-pilot` | Feasibility versus causal testing, baselines, comparisons and inconclusive decisions |
| `genz-voice` | Audience-led channel choices and content that fits real production capacity |
| `genz-cringe-check` | Fast creative review that separates taste, accuracy, respect and privacy |
| `genz-workforce` | Hiring, vacancies and retention with correct follow-up denominators |

Start with the problem, for example: “I run a café and afternoon visits have fallen.” The intake
clarifies what changed and how it was measured before diagnosing a cause. A caption check or
staffing question goes directly to its specialist skill; it does not require a customer interview.

Private working state lives in `genzfy-workspace/<venue>/`, which is ignored by Git. Do not add
real customer or employee information to public examples.

## Evidence standard

- [Patterns](skills/genzfy/references/patterns.md) are hypotheses to test, not universal traits.
- The [claim ledger](skills/genzfy/references/claim-ledger.md) records source, dates, market,
  population, denominator, research design and missing information. Unsupported precision is
  quarantined, not silently repaired or treated as false.
- [Workforce evidence](skills/genz-workforce/references/workforce-patterns.md) is separate from
  customer research. Early exits alone do not diagnose poor onboarding.
- Venue evidence is labelled measured, owner-reported, calculated or inferred. Local observations
  and external research have different limitations; neither automatically outranks the other.
- Uptake is not incrementality, revenue is not contribution, and voluntary customer posts are not
  a guaranteed free marketing plan. Costs include setup and recurring labor.
- Marketing checks accuracy, capacity, consent, rights, disclosure, accessibility and age safeguards.

## Validate and evaluate

Python 3.9+; standard library only:

```bash
python3 scripts/build.py all
python3 -m unittest discover -s tests -v
```

The build validates frontmatter/reference paths and creates Claude.ai and ChatGPT bundles. Unit
tests inspect real generated bundles and source/reference integrity. **These checks do not prove
that generated advice is correct.** Use the scenarios and review instructions under `fixtures/`
for separate behavioral evaluation, recording actual outputs and failures. A worked example or
expected-outcome checklist is not an executed model test.

Before publishing new advice, review factual claims, arithmetic, unknowns, routing and real
outputs. Keep evidence review dates current and recheck applicability before quoting old research.

## Attribution and licensing

No license file has been supplied. Public visibility alone does not grant an open-source reuse
license; obtain permission before assuming redistribution or modification rights.

All examples under `fixtures/` are newly authored fictional scenarios. They contain no real venue
interviews, employee records or customer information. The source and Git commit metadata use
nonpersonal maintainer identification; no live working state is included.
