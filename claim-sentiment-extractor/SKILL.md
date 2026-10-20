---
name: claim-sentiment-extractor
description: >-
  Turn any research document — an annual, semi-annual, or quarterly report, an
  earnings-call transcript, a broker note, an expert-network transcript, an
  investor-day deck — into a claim-level table. Each row is one claim with
  the verbatim quote and its location, a fact-or-sentiment label, a polarity
  (positive, negative, neutral), a theme, and a score against the named
  thesis factors for the position, such as expected buybacks, margin
  expansion, or deleveraging. The labelling is calibrated to the analyst's
  own judgment: the analyst keeps a plain file of labelled example claims
  and corrections, the skill reads it on every run, and every run reports
  how far its labels agree with the analyst's. For research analysts and
  portfolio managers on long/short, long-only, activist, and credit teams.
  Trigger on phrases like "pull the claims out of this transcript," "fact
  versus sentiment on this note," "score this report against our thesis
  factors," "tag every claim in the semi-annual," "how bullish is this broker
  really, claim by claim," "run the claims table and show agreement with my
  labels," or when a user attaches a document plus a list of thesis factors.
  Do NOT use to track how management's language shifts across quarters. Do
  NOT use to file whole items in the incoming flow as bull or bear evidence
  on a position's debates — use the key-debates-ledger skill. Do NOT use
  for a structured note on a single expert call with a credibility
  assessment. Do NOT use to decide which sell-side notes deserve reading —
  use the sellside-research-triage skill. Do NOT use for what the market
  has priced in ahead of a print. Quotes are verbatim, facts and sentiment
  are never blended in one label, and the table carries no trade
  recommendation.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Claim Sentiment Extractor

A forty-page transcript or a semi-annual report contains perhaps sixty claims that matter, and they arrive mixed together: a reported number, a management assertion about next year, a broker's adjective, an expert's guess. Analysts read for the gist and come away with an impression — "management sounded confident on capital return" — that cannot be checked, compared across documents, or argued with. This skill breaks the document into individual claims, quotes each one exactly with its location, labels it fact or sentiment, gives it a polarity and a theme, and scores it against the thesis factors the position actually depends on. The labels are tuned to the analyst's own calls through a file of labelled examples the analyst keeps, and each run says how closely it matched them.

## Why this skill exists

The unit of evidence in a research document is the claim, not the document. A broker note rated "buy" may contain three factual sentences and twenty sentences of sentiment, and the useful information is in knowing which is which. A reported gross margin is a fact; "we see margins expanding meaningfully into next year" is management sentiment about a fact that has not happened; "the stock looks cheap" is the broker's sentiment about the stock. Reading them as one stream lets the confident ones carry the weight of the factual ones. Separating them, row by row, is what lets an analyst say precisely what a document established and what it merely asserted.

Generic sentiment scoring does not help much, because "positive" means nothing until it is attached to the question the position turns on. A paragraph can be upbeat overall and negative for the buyback thesis if it mentions a new acquisition pipeline. Scoring each claim against the named thesis factors — the three to six things the investment case needs to go right — turns a pile of tagged sentences into something the analyst can use: for each factor, what the document said, how hard, and whether it was a fact or an opinion.

The last reason is trust. Two analysts reading the same sentence will often disagree on whether it is positive, and a model will disagree with both unless it is shown how this analyst reads. What an analyst needs is simple: let me correct the labels, keep my corrections, and tell me each time how often the tool agrees with me. Without that number nobody knows whether to rely on the table or re-read the document, and without the kept corrections the tool repeats its mistakes. The calibration file is what turns a one-off extraction into something that improves with use.

## Inputs

**Required:**
- The document or documents, each with type (report, transcript, broker note, expert call, deck), issuer or author, and date
- The thesis factors for the position: each a short name and a sentence on what "positive" means for it, with the position direction (long, short, or credit exposure)

**Optional but high-value:**
- **The calibration file** — a plain file the analyst keeps (a spreadsheet, CSV, or markdown table) with one row per labelled claim: the quote, its source, and the analyst's fact/sentiment label, polarity, theme, and factor scores, plus an optional note on why. Rows the analyst marks `test` are held back for measuring agreement; the rest are guidance. The skill reads it every run and never edits it.
- **The analyst's corrections to the previous run**, in the same format, so the skill can propose rows to append to the calibration file
- **A theme list** the team already uses, so themes are consistent across documents rather than invented each time
- **Prior claim tables** for the same company, so recurring claims and changed claims can be noted
- **The speaker roster** for a transcript, so each claim is attributed to a role (CEO, CFO, analyst, expert, operator)

**Missing-input behavior:** If no thesis factors are given, extract and label claims without factor scores, propose three to five factors from the document under `[proposed factors — confirm]`, and do not score against them until confirmed. If there is no calibration file, run on the default rules below, say the run is uncalibrated, and offer a starter file built from twenty claims in this document for the analyst to label. If the calibration file has no `test` rows, report agreement as not measured rather than scoring against guidance rows the skill has already read. If a document is truncated or a page is unreadable, list the gap; never reconstruct missing text.

## How it works

1. **Read the calibration file first.** Load the guidance rows and note the analyst's patterns: where they draw the fact/sentiment line, how they treat hedged forward statements, which themes they use, how strict they are on "neutral." Set the `test` rows aside unread until step 7.
2. **Segment the document into claims.** A claim is the smallest statement that could be true or false, or that expresses a view. Split compound sentences when the parts would get different labels; keep a sentence whole when splitting would lose the qualifier. Skip pleasantries, safe-harbour language, and operator instructions, and count what was skipped.
3. **Quote each claim verbatim with its location.** Page and paragraph for reports and notes; speaker, section (prepared remarks or Q&A), and timestamp or line for transcripts. Mark any ellipsis. A paraphrase is never placed in the quote column.
4. **Label fact or sentiment.** Fact: a reported figure, a completed event, or a verifiable statement about the past or present. Sentiment: a forecast, an intention, a characterization, an opinion, or a rating. Forward-looking statements are sentiment even when they contain a number ("we expect 200 basis points of expansion"). Where a sentence contains both, it is split; if it cannot be split, it is labelled sentiment and the factual element is noted.
5. **Assign polarity, theme, and factor scores.** Polarity is the claim's direction on its own terms. Factor scores are separate: for each named factor the claim bears on, a score from -2 to +2 relative to the position's view, so a claim positive for the company can score negative on a short's factor. Most claims bear on one factor or none; a claim with no factor relevance is left unscored rather than forced.
6. **Attribute and weight the speaker.** Record who made the claim and in what capacity. A CFO's statement on capital allocation, an expert describing their own purchasing, and a broker's view of the multiple are different kinds of evidence; the table shows the role so the reader can weigh it.
7. **Measure agreement against the test rows.** Label each `test` quote as if new, then compare with the analyst's labels: percent agreement on fact/sentiment, on polarity, and on factor scores (exact and within one point). List every disagreement with both labels side by side.
8. **Summarize by factor.** For each thesis factor: the count of claims, the split between fact and sentiment, the net score, and the two or three claims that carry the most weight, quoted. Facts and sentiment are summed separately and never combined into one score.
9. **Propose calibration rows.** From the analyst's corrections to the previous run and this run's disagreements, draft new rows in the file's format for the analyst to accept or reject. The skill never appends to the file itself.

## Output format

A skeleton to adapt — the claim table and the agreement line are the fixed parts; the factor summary scales with the number of factors.

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# Claim table — [company], [document type], [date]
Position: [long / short / credit] | Factors: [list] | Claims: [n] | Skipped: [n boilerplate]
Calibration: [file, n guidance rows, n test rows / uncalibrated]
Agreement with analyst labels: fact/sentiment [x]% | polarity [x]% | factor score exact [x]%, within one [x]% (n = [test rows])

## Factor summary
| Factor | Claims | Facts | Sentiment | Net score (facts) | Net score (sentiment) | Key claim |
|---|---|---|---|---|---|---|

## Claims
| # | Quote (verbatim) | Location | Speaker / role | Fact or sentiment | Polarity | Theme | Factor scores |
|---|---|---|---|---|---|---|---|

## Disagreements with test labels
| Quote | Analyst label | This run | Note |
|---|---|---|---|

## Proposed calibration rows
[Rows in the file's format — proposed, not appended]

## Gaps
[Truncated pages, unreadable sections, claims split or merged on a judgment call]
```

## Where claim extraction goes wrong

- **Forward statements labelled as facts.** "We will return all free cash flow" is an intention, not a fact, however firmly it is said. Numbers inside a forecast do not make it factual.
- **Blending fact and sentiment in one score.** A net factor score that adds a reported buyback to a broker's enthusiasm about future buybacks hides exactly the distinction the table exists to show. Keep the columns apart.
- **Polarity read against the company instead of the factor.** A strong acquisition pipeline is positive for growth and negative for a buyback thesis. Score factors relative to the position's view, and say so in the header.
- **Paraphrase drifting into the quote column.** A tidied quote can flip a hedge into a commitment. Quote exactly, mark ellipses, and give the location so the analyst can check in seconds.
- **Over-splitting.** Breaking "margins should expand, subject to input costs" into two claims drops the qualifier from the first. Split only where the parts genuinely differ.
- **Scoring every claim.** Most sentences in a document do not bear on any thesis factor. Forcing a score onto them inflates the factor totals.
- **Agreement measured on rows the skill has already learned from.** Scoring against guidance examples gives a flattering number. Agreement is reported on `test` rows only, and the sample size is always shown.
- **The calibration file going stale.** An analyst whose thesis changed last quarter may now read the same sentence differently. Old rows that conflict with recent corrections are flagged for the analyst to retire.

## Guardrails

- **Quotes are verbatim, with location.** Every row carries the exact text and where it sits in the source. Nothing is paraphrased in the quote column, and no claim appears without its source location.
- **Fact and sentiment are labelled, never blended.** Each claim gets one label, compound sentences are split, and factor summaries total facts and sentiment separately.
- **Only supplied documents are read.** The skill does not fill gaps from recall, infer what a missing page said, or attribute a claim to a speaker the document does not name. Figures are quoted as extracted, never adjusted.
- **The analyst owns the labels.** The calibration file is read, never edited; proposed rows are offered for the analyst to accept. Agreement is reported every run, including when it is low.
- **Licensed content stays within its terms.** Broker research and expert-network transcripts are quoted at the length each claim needs, and the table does not reproduce whole documents.
- **Confidentiality.** Thesis factors and calibration labels reveal what the firm believes and why. Assume a firm-approved AI environment and reproduce nothing beyond what the table requires.
- **No trade recommendations.** The output is a labelled record of what a document said. It is not a view on the stock, a rating, or a recommendation to buy, sell, size, or hold anything.

## Example prompts

> "Semi-annual report for [company] attached. We're long on three factors: buybacks resume next year, operating margin expands at least 150 basis points, net debt below two times by year end. Pull every claim, label fact or sentiment, score against the three factors, and use my calibration file — report agreement on the test rows and show me every disagreement."

> "Here's a broker initiation on [company] and the Q&A section of last week's call. I want to know how much of the broker's bull case is fact and how much is adjective. Claims table for both, factor summary with facts and sentiment kept separate, and attribute every transcript claim to the speaker's role."

> "My corrections to last week's table are in the attached sheet. Turn them into proposed rows for the calibration file, flag any older rows they contradict, then run the same factors against this expert-network transcript from a former procurement head at a key customer."

## Works well with

The factor summary feeds **key-debates-ledger** when the thesis factors map to the team's open debates, and the ledger carries the same questions forward across the weekly flow rather than one document at a time. For expert calls, **expert-call-synthesis** is the next step when several calls bear on one factor. **sellside-research-triage** decides which broker notes are worth a claims pass in the first place.
