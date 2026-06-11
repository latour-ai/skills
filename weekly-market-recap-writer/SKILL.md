---
name: weekly-market-recap-writer
description: >-
  Turn a set of links, notes, and data points the user provides into a
  client-ready weekly market recap — what happened, why it matters, neutral
  tone, every claim sourced, no predictions, no advice. For IR teams, client
  advisors, wealth managers, and anyone who sends a weekly note. Trigger on
  phrases like "write the weekly recap," "market recap from these links,"
  "weekly commentary," "client market update," "turn these notes into the
  Friday note," "weekly wrap," or when the user provides a batch of market
  links/data and wants a polished recap. Do NOT use for quarterly LP letters
  — use the lp-update-generator skill. Do NOT use for curated newsletter
  link roundups — use the roundup-newsletter skill. Do NOT use when the user
  wants market analysis researched from scratch — this skill writes from
  what the user supplies.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Weekly Market Recap Writer

Turn the week's raw material — links, jotted notes, data points — into a clean weekly market recap: what happened, why it matters, neutral tone, zero predictions, zero advice. Every claim is traceable to a source the user supplied (or is flagged as unsourced), because in a client-facing document, "where did this number come from?" must always have an answer.

## Why this skill exists

The weekly note is the most reliably recurring writing task in client-facing finance, and it eats Friday afternoons. The inputs already exist — a folder of links, a few Bloomberg screenshots described in notes, three things the PM mentioned — but assembling them into something a client can read takes two hours and carries real compliance risk if a stray prediction or unsourced number slips in. This skill does the assembly under strict rules: it writes only from what the user provided, it attributes everything, and it refuses the two things that get weekly notes pulled by compliance — forecasts and advice.

## Inputs

**Required:**
- The week's raw material: links, pasted articles, notes, data points, bullet fragments. Anything goes in; only sourced material comes out as fact.

**Optional (defaults applied and labeled if absent):**
- **Audience:** client-facing or internal (default: client-facing — the stricter standard)
- **Length:** short (~300 words), standard (~600), long (~1,000) (default: standard)
- **Sections/format preferences,** prior recaps to match voice
- **Firm context:** strategies or asset classes the readers care about, so emphasis lands right
- **As-of date** for the week being covered (default: infer from the materials and label it)
- If your AI has web access and the user provides bare links, fetch them to read the content; if fetching fails, say so rather than summarizing from the URL text.

**Missing-input behavior:** Never block on missing preferences — apply the defaults above and state them at the top of the draft. The one thing never assumed is a market fact: if the user's materials don't establish it, it doesn't appear as fact.

## How it works

1. **Inventory the materials.** List what was provided, what each source is (publication, data point, user note), and the date of each. Flag anything stale relative to the week being covered.
2. **Sort claims into three bins:**
   - **Sourced fact** — established by a provided link/document: usable, with attribution
   - **User assertion** — stated in the user's notes without a source: usable only as flagged ("per your notes — no source provided")
   - **Neither** — gaps the user might expect covered (e.g., no rates material in a week the Fed met): listed at the end as gaps, never filled from memory
3. **Structure the week.** Group into 3–5 themes that organize the materials (e.g., central banks, earnings, a sector story, a notable data release). The materials drive the themes — don't impose a template the inputs can't support.
4. **Write "what happened" tight and attributed.** Each factual statement traces to a provided source. Market levels and moves appear only if the user's materials contain them, always with the as-of date.
5. **Write "why it matters" without crossing the line.** Context and mechanism are fine ("higher rates raise discount rates on long-duration assets"); forecasts are not ("we expect rates to fall"). Attribute third-party views as views ("Strategists at [firm] argue..."), never adopt them as the note's own.
6. **Run the compliance self-scrub** (see Guardrails), then assemble with the source list and the unsourced-claims flag box.

## Output format

```
# Weekly Market Recap — Week of [date range]
Audience: [client-facing / internal] | Length: [setting] 
[If defaults were assumed: "Assumed: client-facing, standard length."]

## [Theme 1 — e.g., "Central banks: the week's main event"]
[What happened — attributed. Why it matters — mechanism and context, no
forecasts.]

## [Theme 2]
...

## [Theme 3]
...

## The week in brief
[3–6 one-line items that didn't merit a section, each attributed.]

---
**Sources:** [numbered list: every provided source used, with date accessed/published]

**⚠ Unsourced items (from your notes — verify before sending):**
- "[claim]" — no source provided

**Gaps:** [topics a reader might expect this week that the materials didn't cover]

**Compliance reminder:** This draft is for internal review. Client-facing
market commentary typically requires compliance review before distribution —
route this through your firm's process. This note contains no investment
advice or recommendations and should stay that way through editing.
```

For internal audience, the compliance reminder shortens to one line and tone may be more direct, but sourcing discipline is identical.

## Guardrails

- **No predictions, period.** Nothing about what markets, rates, or prices *will* do — including hedged versions ("could continue to," "may face pressure"). Mechanism and history are allowed; forecasts are not. Third-party forecasts appear only as attributed views.
- **No advice.** No "investors should," no "we favor," no positioning suggestions, no "opportunities." If the user's notes contain advice-flavored lines, move them to the unsourced/flagged box with a note.
- **Every claim attributed.** Facts trace to a provided source with date; user assertions are flagged as unsourced in the dedicated box, never silently woven in as fact.
- **Never fill gaps from memory.** No market levels, moves, or events from the AI's own knowledge — if it wasn't in the materials, it goes in "Gaps." This is absolute: a plausible-but-wrong S&P level in a client note is the worst failure mode this skill has.
- **Neutral tone.** No cheerleading, no doom. "Equities fell" not "markets were crushed."
- **As-of dates on all data.** Weekly notes get forwarded weeks later; undated numbers become wrong numbers.
- **Compliance reminder is mandatory** on every client-facing draft and may not be removed by the skill.

## Quality checks

- [ ] Zero forward-looking statements (scan for: will, expect, likely, should, forecast, "poised to")
- [ ] Zero advice language (scan for: investors should, we recommend, opportunity, attractive, favor)
- [ ] Every factual claim maps to a numbered source
- [ ] Unsourced box lists every user assertion used
- [ ] Every data point carries an as-of date
- [ ] Gaps section honest about what the materials didn't cover
- [ ] Compliance reminder present

## Example prompt

> "Friday note time. Here are six links from this week (Fed minutes coverage, two earnings stories, an oil piece), plus my notes: 'S&P roughly flat on the week, 10yr backed up ~15bps — check exact numbers.' Client-facing, standard length, neutral. Flag anything I gave you without a source."
