---
name: sellside-research-triage
description: >-
  Triage a batch of sell-side research — a morning's notes pasted or
  attached, a folder of PDFs, or a forwarded-email export — against a
  coverage list and the desk's current key debates: rating and estimate
  changes on covered names flagged first with the analyst's stated reason,
  notes carrying a genuinely new argument or data point summarized in two
  sentences with a "why you care" line, and everything else dismissed in one
  line as maintenance, duplicative, or off-coverage. Ends with a verdict on
  the two or three notes actually worth opening today, in priority order.
  For research analysts and PMs at any fund drowning in broker flow. Trigger
  on phrases like "triage this morning's research," "what's in the broker
  notes," "anything worth reading in this pile," "any estimate changes on
  our names," "sort my research inbox," "which of these notes matter," or
  when a user drops a stack of sell-side notes with a coverage list. Do NOT
  use for triaging a general email inbox for action items — use the
  inbox-triage skill. Do NOT use for a mixed reading pile of newsletters,
  memos, and alerts; this skill is built for broker research. Do NOT use for
  the earnings call or results themselves — use the
  earnings-call-extractor skill. A triage verdict is a reading decision,
  not a view on any security.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Sell-Side Research Triage

You receive far more sell-side research than any human can read, and the honest default — skimming subject lines and hoping — occasionally misses the estimate cut that moves your name at the open. This applies a consistent filter to the morning pile: your names first, changes before reiterations, new arguments before rehashed ones, and a two-line verdict on each survivor so you decide what to open in seconds. The first 45 minutes of the morning come back, without the anxiety that the one note that mattered went unread.

## Why this skill exists

The economics of sell-side research guarantee the pile. Analysts are paid to publish, so most notes exist to maintain coverage rather than to say something — the earnings recap that restates the press release, the reiteration that moves a target price 4% for model-housekeeping reasons, the thematic piece recycling last month's thematic piece. Buried in that flow, at unpredictable intervals, are the notes that actually matter: a real estimate cut with a stated reason, a rating change that will move the tape, a data point from a survey or channel check that nobody else has. The ratio is maybe one in twenty, and nothing about a subject line reliably tells you which one.

Human triage under that ratio degrades in a known way. Attention goes to the brokers you like and the names you're anxious about; the note that mattered came from a broker you deprioritized on a name you felt fine about. And the skim reads titles, which are written by marketing convention — "Adjusting Estimates" can mean a rounding pass or a 20% cut, and the only way to know is the thing you don't have time to do.

The debates dimension is what elevates triage from filtering to research. A note is worth reading when it says something *you have not already incorporated* — which means the filter needs to know what the desk currently believes and argues about. The same note is maintenance noise on one desk and a must-read on another, purely because of what each desk's live debates are. A triage that ignores this reduces to keyword matching; one that uses it is doing the first pass of actual research work.

## Inputs

**Required:**
- The batch of research: pasted notes, attached PDFs, a folder of files, or a forwarded-email export. Baseline mode works entirely from this material — no inbox connection required.
- The coverage list: the tickers the desk owns or actively follows

**Optional but high-value:**
- **The desk's current key debates on its most important names** — a sentence or two per name on what is contested; this is what separates "new argument" from "rehash," and without it that judgment falls back to a weaker novelty heuristic
- A watchlist distinct from the coverage list, triaged at lower priority
- Broker or analyst notes-to-self ("this analyst's channel work is good, ignore their target prices"), which sharpen the differentiated-work call
- Yesterday's triage or recent notes on the same names, so repetition across days gets caught
- A live research inbox or shared drive connection, where available, as an upgrade path — the skill then pulls the morning's flow itself instead of receiving it; the triage logic is identical

**Missing-input behavior:** Notes plus a coverage list are enough to run. Without stated debates, run the triage on changes-and-novelty alone and say prominently that the "new argument" filter is operating without knowledge of what the desk already believes — expect some false positives. Without a coverage list at all, ask once; triaging flow against no names is not triage. Never fabricate the content of a note that was listed but not provided (an email export with subject lines only): such items are triaged by metadata and explicitly marked "not read — subject line only."

## How it works

1. **Inventory the batch before judging it:** count the notes, identify broker, analyst, ticker(s), and note type for each, and flag any items that are metadata-only (subject line without body). The verdict at the end should account for every item — a triage that silently drops notes reproduces the original problem.
2. **Separate covered names from everything else immediately.** Coverage-list items get full treatment; watchlist items get a lighter pass; off-coverage items get one line unless they carry read-across to a covered name — and read-across is the one reason an off-coverage note ever survives triage.
3. **Pull every rating and estimate change on covered names to the top,** with the direction, the magnitude, and the analyst's *stated reason* — not just "cut estimates" but why, in the analyst's own framing. The reason is what the PM needs at the open; the change itself will be in the tape anyway.
4. **Distinguish real changes from housekeeping.** A target price nudged for a roll-forward of the valuation year, or estimates trimmed to mark to FX, is maintenance wearing a change's clothes. Magnitude and stated reason make the call; when in doubt, say which it looks like and why.
5. **Test each remaining covered-name note for a genuinely new argument or data point** — new against the desk's stated debates where provided, new against the rest of the batch otherwise. A proprietary survey, a channel check with specifics, a differentiated read on unit economics passes; a well-written restatement of consensus does not, however well-written.
6. **Summarize each survivor in two sentences plus a "why you care" line** tied to the specific name, debate, or position it touches. The two sentences carry the argument, not the note's structure — "analyst argues X because Y" beats "the note discusses X."
7. **Dismiss the rest in grouped one-liners:** maintenance, duplicative (of what), off-coverage (with any read-across noted). Dismissals are visible and auditable — the reader should be able to spot-check that nothing was buried.
8. **Check the batch for convergence.** Three brokers publishing the same direction on the same name in one morning is itself information — either something moved, or a company or conference just guided them all. Flag it as a pattern above any single note.
9. **Deliver the verdict: the two or three notes actually worth opening today, in priority order,** each with one line on what reading it will change. If nothing in the batch clears the bar, say so plainly — "nothing worth opening" is a legitimate and valuable verdict.

## Output format

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# Research Triage — [date]
Batch: [N] notes, [N] brokers | Coverage list: [N] names | Debates provided: [yes / no]
Metadata-only items: [N, listed]

## Changes on our names — read first
| Ticker | Broker/analyst | Change | Magnitude | Analyst's stated reason | Real or housekeeping? |
|---|---|---|---|---|---|

## Worth reading — new argument or data point
### [Ticker] — [broker, analyst]
[Two sentences: the argument and its basis.]
**Why you care:** [tied to a position, debate, or number the desk owns]

## Patterns across the batch
[Convergence, unusual volume of publishing on a name, read-across clusters.]

## Dismissed
**Maintenance ([N]):** [ticker — broker — one line each]
**Duplicative ([N]):** [note — duplicative of what]
**Off-coverage ([N]):** [one line; read-across flagged where present]

## Verdict — open these today
1. [Note] — [what reading it will change]
2. [ ]
[or: Nothing in today's batch clears the bar. The closest call was [ ].]
```

Adapt the skeleton to the batch — a single-note "is this worth reading" query needs only the survivor treatment and a verdict.

## What's worth reading in sell-side flow

The filter, made explicit — where the value hides and what the noise looks like:

- **Estimate changes with stated reasons** are the highest-value items in the flow, and the reason matters more than the number. "Cutting on channel checks showing slower sell-through" is research; "trimming to reflect the quarter" is bookkeeping.
- **Rating changes move the tape regardless of merit** — read them for positioning even when the argument is weak, because the flow they trigger is real either way.
- **The analyst's actual edge is narrow and specific.** Most analysts are excellent at one thing — access to management, a proprietary survey, genuine channel work, a real model on a complicated segment — and average elsewhere. A note is worth reading when it draws on the edge, not when the analyst is merely publishing. Broker notes-to-self, where provided, encode exactly this.
- **Initiations are surveys, not calls.** A new analyst's initiation is usually the best single summary of consensus on a name — read it for the map, ignore the rating.
- **Maintenance tells:** target moved under ~5% with estimates roughly unchanged; "adjusting model" language; valuation-year roll-forwards; recaps published within hours of a release that add no number to the release. Each is dismissible on sight.
- **Thematic and sector pieces** earn a read only when they contain proprietary data (survey, pricing tracker, channel work). A theme piece built from public data is a well-formatted opinion.
- **Contrarian ratings deserve one honest look** — the lone underperform on a loved name is occasionally the analyst spending career capital on something real, and the flow-weighted reader systematically misses it.
- **Read-across is the sleeper category.** A supplier's guidance cut, a competitor's pricing note, a customer's inventory comment — off-coverage by ticker, on-coverage by implication. The triage that catches these earns its keep on them.
- **Silence is occasionally the signal.** An analyst who publishes on every quarter and says nothing after this one, or a broker conspicuously absent from a controversy their peers all covered, is worth a line in the patterns section — the flow's gaps carry information the flow itself does not.

## Guardrails

- **Every item in the batch is accounted for.** Flagged, summarized, or dismissed with a line — never silently dropped. The dismissals section exists so the filter can be audited.
- **Notes are triaged from their content, never fabricated.** Metadata-only items are marked as such and judged only on metadata. The skill never summarizes a note it was not given.
- **The analyst's reason is reported in the analyst's framing,** attributed to broker and analyst, and kept distinct from any editorial judgment the triage adds. "Real or housekeeping" is the triage's call and is labeled as such.
- **Dismissal is a reading decision, not a verdict on the name.** A note dismissed as maintenance says nothing about the stock. The triage never converts reading priority into a view on any security.
- **Novelty judgments are only as good as the debates provided.** When debates are absent, the output says its "new argument" filter is running blind and calibrates its confidence accordingly.
- **Sell-side research is licensed content.** Summaries stay at triage depth — two sentences and a reason to read — and do not reproduce notes or substitute for them. Redistribution of broker research outside its license is the user's compliance problem to avoid, and the output is built not to create it.
- **Not investment advice.** The output prioritizes reading, and nothing else. Estimate changes are reported as what an analyst said, not endorsed.
- **Confidentiality:** the coverage list, the desk's debates, and its positions are sensitive. Assume a firm-approved AI environment.

## Example prompts

> "This morning's broker flow attached — [N] PDFs. Coverage list: [tickers]. Our live debates: [name]: [one line]; [name]: [one line]. Triage it. I have twenty minutes before the open and I want changes first, then anything genuinely new, then the verdict."

> "Here's an export of the research inbox from the past week — some full notes, some subject-line-only. Same coverage list as usual: [tickers]. No debates doc this time, just tell me what I actually missed while I was traveling, and mark anything you're judging from subject lines alone."

> "Single note attached — [broker]'s 60-page initiation on [ticker], which we own. Worth my time? Two sentences on what's actually new versus our debate on [topic], and whether anything in it draws on this analyst's real edge or it's a consensus map."

## Works well with

Feed each morning's "worth reading" survivors into **key-debates-ledger** so new arguments update the debates that tomorrow's triage filters against — the two skills compound. Use **earnings-call-extractor** on the call itself in earnings season and let this skill handle the recap wave that follows.
