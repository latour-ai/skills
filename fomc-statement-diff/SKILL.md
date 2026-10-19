---
name: fomc-statement-diff
description: >-
  Produce a word-level redline of a central bank policy statement against the
  prior meeting's, classify every substantive change as hawkish, dovish, or
  neutral with one line of reasoning each, summarize dot-plot and projection
  shifts when a SEP is released, and test whether the market's first move is
  trading the text or something else. Works for the FOMC and equally for ECB,
  BoE, BoJ, BoC, and RBA statements. For macro and rates portfolio managers,
  traders, multi-asset investors, economists, and market strategists. Trigger
  on phrases like "diff the FOMC statement," "what changed from last meeting,"
  "redline the Fed statement," "is this hawkish or dovish," "read the ECB
  statement against the last one," "Fed day," "what did they take out," "dot
  plot changes," or when a user pastes two central bank statements. Requires
  both statements to be provided — it never reconstructs a statement from
  memory. Do NOT use for summarizing a speech or testimony from a single
  official. Do NOT use for a company earnings call — use the
  earnings-call-extractor skill. Not investment advice.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# FOMC Statement Diff

Everyone reads the statement. The edge is in knowing precisely what changed, what each change signals, and whether the first market move is responding to the text or to a headline. This produces the redline, a change-by-change hawkish/dovish classification, the SEP shifts when there is a SEP, and a read on whether the tape and the text agree — fast enough to be useful before the press conference starts.

## Why this skill exists

FOMC statements are written to be compared. The Committee reuses language deliberately, and the signal is carried almost entirely by what was added, removed, or reworded — a dropped adjective, a reordered risk sentence, a shift from "additional policy firming" to "the extent of any additional policy firming." Reading the new statement alone tells you the stance; reading it against the prior tells you the *change* in stance, which is what prices move on.

Doing that comparison by hand under time pressure is exactly the kind of task where humans are slow and error-prone: the diffs are small, the language is repetitive, and the first ninety seconds are noisy. The mechanical part — find every difference, miss nothing — is what this automates, so the human spends the time on the judgment part.

## Inputs

**Required:**
- The new statement, in full, pasted or attached
- The prior meeting's statement, in full, pasted or attached

Both are genuinely required. See the guardrails — this skill does not reconstruct statements from memory.

**Optional but high-value:**
- The Summary of Economic Projections (new and prior), for the dot-plot section
- The market reaction so far: 2-year and 10-year yields, fed funds futures or OIS-implied path, DXY, equity index moves, and the timestamps
- What was priced going in — the market-implied probability of the decision and the expected path
- The prior meeting's minutes, or recent speeches from the Chair, for context on whether a change was telegraphed
- The user's positioning or the specific question they care about

**Missing-input behavior:** If only one statement is provided, ask for the other — do not proceed. If the SEP is not provided, skip that section explicitly rather than describing dot movements. If no market data is provided, run everything except the text-versus-tape section and say it was skipped; the language analysis stands on its own.

## How it works

1. **Produce the word-level redline first, mechanically, before interpreting anything.** Paragraph by paragraph, showing additions, deletions, and rewordings in place. Completeness matters more than elegance here — a missed deletion is the failure mode. Paragraphs with no changes are still listed, marked unchanged.
2. **Separate substantive changes from housekeeping.** Date updates, rotating voter names, and routine reference changes are noted and set aside so they do not dilute the signal.
3. **Classify each substantive change** as hawkish, dovish, or neutral/ambiguous, with one line of reasoning. Ambiguous is a legitimate and frequently correct classification — a change that cuts both ways should be labeled as such rather than forced.
4. **Read the structural signals** that live above the word level: the order of the risk sentence, whether inflation or employment is discussed first, the balance-of-risks language, the conditionality of the forward guidance, and any change in the description of the policy stance itself.
5. **Note the vote and any dissents,** including who dissented and in which direction, and whether the dissent composition changed from the prior meeting.
6. **Summarize the SEP if released:** median path changes for the current and following years, the movement of the distribution (not just the median — a median that holds while the tails shift is itself the story), and changes to the longer-run rate, growth, unemployment, and inflation projections.
7. **Deliver the verdict:** net hawkish, net dovish, or on-hold relative to the prior meeting, and the single most significant change. Commit to a call.
8. **Compare text against tape.** Given the market reaction, assess whether the move is consistent with what the text actually says, and name the plausible alternative explanations if it is not — a SEP surprise, a leak-to-consensus repricing, positioning unwind, or the market front-running the press conference.

## Output format

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# [FOMC / ECB / BoE / BoJ] Statement Diff — [meeting date] vs. [prior meeting date]
Decision: [action] | Vote: [count, dissents] | SEP: [released / not released]

## Verdict
Net [hawkish / dovish / neutral] versus the prior statement.
The single most significant change: [one sentence].
[2–3 sentences of support.]

## Redline
[Paragraph-by-paragraph, showing every difference in place.
Additions and deletions marked clearly. Housekeeping changes separated out.]

## Change-by-change classification
| # | Change | Type | Reasoning |
|---|---|---|---|
| 1 | "[old]" → "[new]" | Hawkish / Dovish / Ambiguous | [one line] |

Housekeeping (no signal): [list]

## Structural signals
- Risk balance sentence: [what changed, or "unchanged"]
- Order of inflation vs. employment discussion: [ ]
- Forward guidance conditionality: [ ]
- Description of the policy stance: [ ]

## Vote and dissents
[Who, which direction, and whether the composition changed.]

## SEP shifts (if released)
| Projection | Prior median | New median | Change | Distribution note |
|---|---|---|---|---|
| Fed funds, end [yr] | | | | |
| Fed funds, end [yr+1] | | | | |
| Longer run | | | | |
| Core PCE, [yr] | | | | |
| Unemployment, [yr] | | | | |
| Real GDP, [yr] | | | | |
Dot distribution: [where the mass moved, beyond the median]

## Text vs. tape (if market data provided)
| Instrument | Move | Consistent with the text? |
|---|---|---|
Assessment: [is the market trading the statement, the SEP, or something else —
and what the alternative explanations are]

## What to listen for in the press conference
3–5 specific questions the redline raises that only the Chair can resolve.
```

Keep the whole brief to roughly one page excluding the redline.

## Reading central bank language

Recurring patterns worth checking on every statement. These are conventions, not rules — verify against the actual text each time.

- **Conditionality shifts carry the guidance.** "Additional policy firming may be appropriate" → "the extent of any additional policy firming" moves from *whether* to *how much*, which is a directional signal even though no rate changed.
- **Adjective removal is a signal.** Dropping "elevated," "strong," or "solid" from a description of inflation or the labor market is usually deliberate and usually the point.
- **The risk balance sentence is the most reliable single indicator.** Watch for movement between "risks are weighted to the upside," "risks are moving into better balance," and "risks to both sides of the mandate."
- **Order matters.** Which mandate leg gets discussed first, and which is described with more qualification.
- **"Attentive to" vs. "highly attentive to"** — intensity modifiers on risk language are load-bearing.
- **"Gained greater confidence" / "has not gained greater confidence"** — explicit statements about the Committee's own conviction level are among the strongest tells.
- **Data-dependence language** that becomes more or less specific about which data.
- **Balance sheet paragraphs** change rarely; when they do, it is rarely incidental.
- **Dissents** are information about the distribution of views, and a new dissenter or a dissent flipping direction can matter more than the statement text.
- **Median-holding, tails-moving** dot plots: the median is the headline, but a widening or shifting distribution tells you about conviction.

## Guardrails

- **Never reconstruct a statement from memory.** Both texts must be provided by the user. Central bank statement language is reproduced with near-identical wording meeting to meeting, which makes a plausible-sounding fabrication both easy to generate and very hard to spot — and a fabricated diff is worse than no diff. If a statement is not provided, stop and ask.
- **The redline is mechanical; the classification is interpretation.** Keep them visually separate. The reader must be able to check the redline against the source without wading through commentary.
- **Quote exactly.** Old and new language reproduced verbatim, in quotation marks, with no paraphrase presented as a quote.
- **"Ambiguous" is a valid classification.** Do not force a hawkish/dovish call on a change that genuinely cuts both ways — a manufactured signal is worse than an acknowledged wash.
- **Distinguish the statement from the press conference.** The statement is the Committee's collective language; the Chair's remarks are not, and are frequently where the market's real move comes from. Never attribute press conference content to the statement.
- **Market data is as-provided, timestamped, and never assumed.** Do not describe a market reaction that was not given to you, and do not extrapolate from partial data.
- **Not investment advice.** This produces a reading of a document and a comparison to observed prices. It does not recommend trades, positioning, or a rates view, and it does not forecast the next meeting.
- **Confirm the date and meeting** you are analyzing from the documents themselves rather than assuming the current one.

## Example prompts

> "Both statements pasted below — today's and the March meeting. SEP is out too, medians attached. Diff them, classify the changes, and tell me if this is hawkish. Front end is +7bp, DXY +0.4%, S&P -0.6% in the first ten minutes."

> "ECB statement from today and the prior one, attached. What changed, and does the language support the market pricing an earlier cut?"

> "Statement diff only, no market data needed — I want to see exactly what they took out of the inflation paragraph and what the risk sentence looks like now versus the last three meetings. Prior two statements also attached."

## Works well with

Pair with **weekly-market-recap-writer** when the Fed day read needs to become client-facing commentary, and with **thesis-red-team** when a policy call is driving positioning and needs to be attacked before it is sized.
