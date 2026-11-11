# Genzfy as a Custom GPT

The seven skill sources are packaged as flat knowledge files with rewritten references.

## Build

```bash
python3 scripts/build.py chatgpt
python3 -m unittest discover -s tests -v
```

Use generated `dist/chatgpt/instructions.md` for the GPT Instructions field and every file in
`dist/chatgpt/knowledge/` for Knowledge. The build checks its configured 8,000-character and
20-file limits. Edit source instructions here, not generated files. Current product limits and
UI labels can change, so verify them in the destination when installing.

## Configure and try privately

Name: Genzfy. Suggested description: “Evidence-informed customer and staffing advice for food and
beverage owners, with costed tests and honest uncertainty.” Example starters:
- “I run a café and afternoon visits have fallen.”
- “Is this Instagram caption cringe?”
- “My new staff keep leaving in the first month.”
- “How can we test a new pickup offer?”

A browsing tool is not required. If enabled, new sources still need provenance and claim records;
search results do not override the evidence standard. File-generation capability is optional.
Keep the GPT private while evaluating it, and follow platform requirements before sharing.

## Differences from a local skill installation

Do not assume persistence between chats. Save completed profiles, audits and plans and provide them
again to resume. Knowledge retrieval can miss a file or section; the assistant should say what it
could not retrieve rather than pretend it read a source. A brief caption question needs no file.

## Behavioral checks before sharing

Use the regression scenarios under `fixtures/` in fresh chats with the built GPT. Save actual
responses, model/configuration, date and pass/fail observations separately. Check at least:

1. A broad new F&B customer problem gets a short relevant intake; saved profiles resume.
2. Caption and staffing questions route directly without customer intake.
3. An unrelated industry is outside this evidence base.
4. Age bands, denominators and source limits remain correct in the final advice, not only footnotes.
5. A low-volume zero-baseline test does not promise incremental sales or a detectable effect.
6. Negative contribution and missing follow-up can produce stop or inconclusive outcomes.
7. Deliberate humor is not automatically banned; factual, consent and disclosure risks still matter.

Build/unit tests are packaging checks, not evidence that these behavioral tests passed.

## Other assistants

Assistants that accept instructions plus reference files may use the same generated bundle.
Check their current limits, retrieval behavior and permissions, and repeat the behavioral tests;
compatibility with one host is not validation of another.
