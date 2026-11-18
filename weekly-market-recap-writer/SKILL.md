---
name: weekly-market-recap-writer
description: >-
  Turn a set of links, notes, and data points the user provides into a
  client-ready weekly market recap — what happened, why it matters, neutral
  tone, every claim sourced, no predictions, no advice. The note's audience,
  length, standing sections, house voice and required disclaimer are
  recorded once in a short first-run setup, so every week's note comes out
  in the same shape. For IR teams, client advisors, wealth managers, and
  anyone who sends a weekly note. Trigger on phrases like "write the weekly
  recap," "market recap from these links," "weekly commentary," "client
  market update," "turn these notes into the Friday note," "weekly wrap,"
  "set up weekly-market-recap-writer," "change my weekly-market-recap-writer
  settings," or when the user provides a batch of market links/data and
  wants a polished recap. Do NOT use for quarterly LP letters — use the
  lp-update-generator skill. Do NOT use for a redline of a central bank
  statement — use the fomc-statement-diff skill. Do NOT use for a curated
  roundup of links for a newsletter, or when the user wants market analysis
  researched from scratch — this skill writes from what the user supplies.
license: MIT
metadata:
  author: latourai
  version: '2.0'
---

# Weekly Market Recap Writer

Turn the week's raw material — links, jotted notes, data points — into a clean weekly market recap: what happened, why it matters, neutral tone, zero predictions, zero advice. Every claim is traceable to a source the user supplied (or is flagged as unsourced), because in a client-facing document, "where did this number come from?" must always have an answer.

## Why this skill exists

The weekly note is the most reliably recurring writing task in client-facing finance, and it eats Friday afternoons. The inputs already exist — a folder of links, a few terminal screenshots described in notes, three things the PM mentioned — but assembling them into something a client can read takes two hours and carries real compliance risk if a stray prediction or unsourced number slips in. This skill does the assembly under strict rules: it writes only from what the user provided, it attributes everything, and it refuses the two things that get weekly notes pulled by compliance — forecasts and advice.

## Inputs

**Required:**
- The week's raw material: links, pasted articles, notes, data points, bullet fragments. Anything goes in; only sourced material comes out as fact. Material can be pasted, attached, or pulled from connected file storage (SharePoint / OneDrive, Google Drive, Box, Dropbox, a local folder) if the user or the settings name the folder where the week's links and notes are collected; if that storage can't be reached, say so and ask for the material.

**Optional, per run (the saved settings or the defaults apply if absent):**
- **Audience:** client-facing or internal (default: client-facing — the stricter standard)
- **Length:** short (~300 words), standard (~600), long (~1,000) (default: standard)
- **As-of date** for the week being covered (default: infer from the materials and label it)
- If web access is available and the user provides bare links, fetch them to read the content; if fetching fails, say so rather than summarizing from the URL text.

**Set once in setup (step 0):** usual audience and length, standing sections, the voice to match, the asset classes readers care about, the required disclaimer and review rule, and where the week's material and finished notes live.

**Missing-input behavior:** Don't block on missing preferences — apply the saved settings, or the defaults above, and state any assumption at the top of the draft. The one thing never assumed is a market fact: if the user's materials don't establish it, it doesn't appear as fact.

## How it works

**0. First-run setup (once, then only when asked).** Run setup the first time the skill is used, or when the user says "set up weekly-market-recap-writer" or "change my weekly-market-recap-writer settings". Look first for a saved `weekly-market-recap-writer-settings.md` in the project's files or the notes folder. If one exists, read it and skip setup.

Setup is one short round of questions, each with a default the user can accept; "none" is a valid answer.

- **Detect before asking.** Check whether file storage and web access are available, and pre-fill what an attached prior recap already settles (sections, length, sign-off, disclaimer). Show what was pre-filled for confirmation.
- **Ask, in one message:**
  - **Audience and length:** client-facing (default) or internal; short, standard (default) or long.
  - **Standing sections:** sections the note carries every week, for example "Rates", "Equities", "The week ahead: scheduled events only", or none (default; the week's materials drive the themes).
  - **Voice:** a prior recap to match, or the default neutral register.
  - **Reader focus:** the strategies or asset classes the readers care about, so emphasis lands right.
  - **Required disclaimer and review rule:** the firm's standard disclosure for market commentary, which is added below the compliance reminder word for word, and who reviews the note before it goes out.
  - **Where things live:** the folder where the week's links and notes are collected and where finished notes are saved, or "I'll paste everything and take the draft in chat" (default).
- **Save the settings** to `weekly-market-recap-writer-settings.md` in plain language the user can edit. If nothing persistent can be written, show the settings as a short block and tell the user to paste it into their project instructions.
- **Continue straight into the recap** if the user gave the week's material with the setup request.

On later runs, read the settings and don't re-ask; the user can override any of them for one note. Setup never blocks a first run: if the user says "skip setup", write with the defaults and label them. Setup records the note's shape only. The skill produces a draft for review and does not send or publish it.

1. **Inventory the materials.** List what was provided, what each source is (publication, data point, user note), and the date of each. Flag anything stale relative to the week being covered.
2. **Sort claims into three bins:**
   - **Sourced fact** — established by a provided link/document: usable, with attribution
   - **User assertion** — stated in the user's notes without a source: usable only as flagged ("per your notes — no source provided")
   - **Neither** — gaps the user might expect covered (e.g., no rates material in a week the Fed met): listed at the end as gaps, never filled from memory
3. **Structure the week.** Group into 3–5 themes that organize the materials (e.g., central banks, earnings, a sector story, a notable data release). The materials drive the themes — don't impose a template the inputs can't support.
4. **Write "what happened" tight and attributed.** Each factual statement traces to a provided source. Market levels and moves appear only if the user's materials contain them, always with the as-of date.
5. **Write "why it matters" without crossing the line.** Context and mechanism are fine ("higher rates raise discount rates on long-duration assets"); forecasts are not ("we expect rates to fall"). Attribute third-party views as views ("Strategists at [firm] argue..."), never adopt them as the note's own.
6. **Assemble the note** with the source list, the unsourced-items box, the gaps list and the compliance reminder.

## Output format

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

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

- **No predictions.** Nothing about what markets, rates, or prices *will* do — including hedged versions ("could continue to," "may face pressure"). Mechanism and history are allowed; forecasts are not. Third-party forecasts appear only as attributed views. Words like "will," "expect," "likely," "should," "forecast," and "poised to" usually signal a forecast.
- **No advice.** No "investors should," no "we favor," no positioning suggestions, no "opportunities." If the user's notes contain advice-flavored lines, move them to the unsourced/flagged box with a note. "We recommend" and "attractive" fall in the same category.
- **Every claim attributed.** Facts trace to a provided source with date; user assertions are flagged as unsourced in the dedicated box, never silently woven in as fact.
- **Never fill gaps from memory.** No market levels, moves, or events from the AI's own knowledge — if it wasn't in the materials, it goes in "Gaps." A plausible-but-wrong S&P level in a client note is the worst failure mode this skill has.
- **Neutral tone.** No cheerleading, no doom. "Equities fell" not "markets were crushed."
- **As-of dates on all data.** Weekly notes get forwarded weeks later; undated numbers become wrong numbers.
- **The compliance reminder appears on every client-facing draft.** The skill does not remove it, because client-facing market commentary typically needs compliance review before distribution.

## Example prompts

> "Set up weekly-market-recap-writer. Client-facing, standard length, always a Rates section and an Equities section, readers are mostly fixed income clients, match the voice of the attached note, and add our standard market commentary disclosure at the bottom."

> "Friday note time. Here are six links from this week (Fed minutes coverage, two earnings stories, an oil piece), plus my notes: 'S&P roughly flat on the week, 10yr backed up ~15bps — check exact numbers.' Client-facing, standard length, neutral. Flag anything I gave you without a source."
