---
name: thesis-evidence-monitor
description: >-
  Proactive, thesis-based monitoring for each live position. Take the two to
  four key debates that decide a position, from the team's debate ledger or
  the written thesis, and read the incoming flow against them: expert-network
  transcripts, podcasts, industry forums and employee-review sites, news,
  filings, sell-side notes, and internal notes. Classify each item against a
  specific debate as confirming, disconfirming, or neutral, with a strength
  rating and the exact passage cited; build a per-position feed organized by
  debate rather than keyword; flag an alert only when a debate moves or new
  primary data lands; and produce a weekly digest per position that leads
  with the disconfirming evidence. Reads from whatever is connected (a
  transcript library, a research mailbox in Outlook or Gmail, file storage,
  a market data source) or from attached material, with the ledger location,
  sources and alert preferences saved once in a short first-run setup. For
  research analysts and portfolio managers on fundamental long/short and
  long-only equity teams. Trigger on "monitor the thesis on this position",
  "read the flow against our debates", "what came in this week that moves
  the thesis", "set up a thesis feed for the book", "did anything disconfirm
  the short", "classify these transcripts against the key debates", "set up
  thesis-evidence-monitor", "change my thesis-evidence-monitor settings", or
  when a user attaches a debate ledger and a batch of new sources. Do NOT use
  for maintaining the debate ledger itself; use the key-debates-ledger skill,
  which this skill feeds. Do NOT use for an allocator's watchlist of hedge
  funds; use the fund-news-alert skill. Do NOT use for triaging sell-side
  notes as a category; use the sellside-research-triage skill. Do NOT use
  for synthesizing a batch of expert calls on one question; use the
  expert-call-synthesis skill. The skill proposes ledger updates and never
  rewrites the thesis on its own.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Thesis Evidence Monitor

Every live position rests on two or three questions, and the answers arrive scattered across sources nobody has time for: a forty-page transcript from a second-tier expert network, an operator's podcast, a thread on an industry forum, an employee review that mentions the product roadmap in passing. Keyword alerts fire on the company name and miss the sentence that matters because it never names the company. This reads the whole flow against the position's actual debates, tags each item as confirming, disconfirming, or neutral with the passage quoted, and speaks up only when a debate moves — leading every digest with the evidence against the position, because that is the evidence the analyst is least likely to go looking for.

## Why this skill exists

A thesis is a small set of debates with a view on each, and the value of monitoring is entirely in whether the incoming information changes one of those views. Keyword feeds cannot do that: they match names, not arguments, so they fire on every mention and stay silent when a supplier's expert call describes a pricing change that decides the margin debate without ever naming the customer. The analyst ends up with two bad options — read everything, which does not scale past a handful of positions, or read the sources that are cheap to process and skip the rest. What gets skipped is usually the primary material: long transcripts, niche podcasts, forum threads, employee reviews. Those are low-ROI only because of the processing cost, and removing that cost changes what they are worth.

The second problem is direction. Analysts who own a position read for confirmation without meaning to; the disconfirming sentence gets rationalized before it is written down. A monitor that classifies each item against a specific debate and puts the disconfirming pile first does not fix the bias, but it makes the analyst confront the counter-evidence in a form that is hard to wave away — a quoted passage with a source and a date, attached to the debate it bears on. Over a quarter, the ratio of disconfirming to confirming items per debate becomes a signal in itself, one the analyst would never assemble by hand.

The third problem is discipline about what counts. Not every item is evidence. A sell-side note restating the company's guidance is not new information about the debate; a transcript in which an operator describes their own purchasing decision is. New primary data — a fresh transcript, a dataset release, a filing — deserves an alert even before it is classified, because the analyst may want to read it whole. Everything else deserves an alert only if it moves a debate. The monitor's job is to draw that line consistently so the analyst trusts the pings, and to hand the results to the debate ledger as proposals rather than edits, because the decision to update a view belongs to the person who holds it.

## Inputs

**Required:**
- The position's key debates — two to four, each stated as a question with the team's current view — from the debate ledger, the IC memo, or a written thesis
- The incoming flow to be read: any mix of expert-network transcripts, podcast transcripts, forum and employee-review excerpts, news, filings, sell-side notes, and internal notes, each with source and date

**Where the material comes from:** The ledger and the flow can be attached or pasted, or read from the places saved in setup: a folder in connected file storage (SharePoint / OneDrive, Google Drive, Box, Dropbox), a connected transcript library (for example Tegus, AlphaSense, GLG or Third Bridge), a research mailbox in Microsoft 365 (Outlook) or Google Workspace (Gmail), and a connected market data source or public filings for a named filing. If a source isn't connected or fails on a given run, say which one, read what is attached, and list it under Coverage as not read this cycle.

**Set once in setup (step 0):** where the debate ledger and prior digests live, which sources to read, alert preferences and digest cadence, and where digests are saved.

**Optional but high-value:**
- **The prior digests** for the position, so the new one can report what changed and track the evidence ratio per debate over time
- **The thesis's own expectations** — what the analyst expects the next data point, the next transcript, or the next filing to show — so items can be scored against a stated expectation rather than a general direction
- **Named entities that bear on each debate** — suppliers, customers, competitors, regulators, products — so items that never name the company can still be routed to the right debate

**Missing-input behavior:** If the debates are not written down, draft them from the thesis document, label them `[proposed debates — confirm]`, and classify against the draft while flagging that the frame itself is unconfirmed. If only some sources are supplied, read what is there and list the source categories that were not covered rather than implying a full sweep. If an item cannot be assigned to a specific debate, file it as neutral with a note on why, and do not force it into the nearest debate. Summarize only sources that were actually read; a title is not a reading, and a strength rating needs a quoted passage to justify it.

## How it works

### 0. First-run setup (once, then only when asked)

Run setup the first time the skill is used, or when the user says "set up thesis-evidence-monitor" or "change my thesis-evidence-monitor settings". Look for a saved settings file first (`thesis-evidence-monitor-settings.md`, in the project's files or the folder where digests are saved). If one exists, read it and skip setup. If a `key-debates-ledger-settings.md` exists, pre-fill the ledger location from it.

Setup is one short round of questions, each with a default the user can accept:

1. **Detect before asking.** Check which file storage, mail, transcript and market data tools are connected, and pre-fill what that settles.
2. **Ask only what detection could not settle, in one message:**
   - **Debate ledger and prior digests:** where they live. Default: the user attaches them each run.
   - **Sources to read:** which folders, which mailbox or mail folder, which transcript library, and any public sources to check for each position. Default: only what is attached each run.
   - **Alerts:** every disconfirming item, moderate-or-stronger disconfirming items plus anything strong and new primary data (default), or new primary data only.
   - **Digest cadence and where digests are saved:** weekly (default); a folder in connected storage, or "just send it to me" (default).
   - **Firm rules (optional):** for example limits on quoting expert-network or licensed content, or positions that must not be named in a saved file.
3. **Save the settings** to `thesis-evidence-monitor-settings.md` in plain language the user can edit. If nothing persistent can be written, show the settings as a short block and tell the user to paste it into their project instructions.
4. **Continue straight into the run** if the user gave debates and material with the setup request.

On every later run: read the settings and never re-ask. Setup never blocks a first run: if the user says "skip setup", work from what was attached with the defaults above and say what was assumed.

### Steps for each run

1. **Load the debates and state each one as a testable question.** For each debate, write down the current view, what would confirm it, and what would disconfirm it — in the terms the flow will actually use. A margin debate becomes a list of the price, cost, and mix observations that would bear on it. This frame is what every item is classified against, and it appears at the top of the digest so a reader can check the classification logic.
2. **Route each item to a debate, or to none.** Read the item whole. Decide which debate it bears on, if any, based on content rather than keywords — a supplier transcript about lead times may bear on the demand debate without naming the company. Items that touch nothing go to neutral with a one-line reason; that pile is reported in aggregate so the analyst can see it was read.
3. **Classify direction against the debate, not the stock.** Confirming means the item supports the team's current view on that debate; disconfirming means it cuts against it. A bullish item on a short position is disconfirming. State the direction relative to the view held, and say so in the header so nobody misreads the labels.
4. **Rate strength by source quality and specificity.** Strong: first-hand, specific, recent, and from someone positioned to know — an operator describing their own decision, a filing, a dataset. Moderate: second-hand but specific, or first-hand but general. Weak: sentiment, speculation, or restated public information. A sell-side note repeating guidance is weak regardless of how confident it sounds; a single employee review describing a product delay is moderate at best until corroborated.
5. **Quote the exact passage.** Every classification carries the sentence or two that supports it, with source, date, and the speaker's role where known. The analyst should be able to verify the call in ten seconds without opening the source. A paraphrase can't be checked, so quote; if the passage is long, quote the load-bearing part and mark the ellipsis.
6. **Distinguish new primary data from commentary.** A fresh transcript, a dataset release, a filing, or a management appearance is primary and gets flagged as such whether or not it moves a debate, because the analyst may want to read it in full. Commentary on primary data is not primary. The digest lists primary items in their own block.
7. **Decide what warrants an alert.** Using the alert preference from setup (default: an item that is disconfirming at moderate strength or above, any item that is strong in either direction, or new primary data), put those items in an Alerts block at the top of the run's output so the analyst sees them before the digest. Everything else waits for the digest. The skill does not message anyone; the alert is part of what it returns. When several weak items point the same way on one debate, note the accumulation in the digest without alerting — it is a pattern to watch, not a call to action.
8. **Assemble the weekly digest per position, disconfirming evidence first.** For each debate: disconfirming items, then confirming, then the count of neutral. Follow with the primary-data block, then a coverage section listing which sources were read and which produced nothing. Where prior digests exist, show the running ratio of disconfirming to confirming items per debate and note any shift.
9. **Write proposed ledger updates, not edits.** For each item that moves a debate, draft the update in the form the debate ledger expects — debate, direction, strength, passage, source — and mark it as proposed. Do not change the wording of a debate, the team's view, or the thesis. If the evidence suggests a debate is resolved or a new debate has opened, say so as a recommendation for the analyst to take to the ledger.
10. **Report what the monitor could not do.** Sources that were not supplied, items that could not be routed, transcripts that were truncated, and any place where a classification was a judgment call between two debates. This section keeps the analyst's trust in the pings, which is the whole product.

## Output format

A skeleton to adapt — the per-debate evidence blocks and the proposed ledger updates are the fixed parts; the rest scales with the week's flow.

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# Thesis evidence digest — [position] — week of [date]
Direction: [long / short] | Debates: [n] | Items read: [n] | Alerts this week: [n]
Labels are relative to the team's current view on each debate.

## Debate 1 — [question] — current view: [view]
Disconfirming:
- [Strength] — "[exact passage]" — [source, date, speaker role]
Confirming:
- [Strength] — "[exact passage]" — [source, date, speaker role]
Neutral: [n items] | Running ratio (disconfirming : confirming, last [n] weeks): [x : y]

## Debate 2 — ...

## New primary data this week
[Transcripts, filings, dataset releases — with a one-line note on whether each moved a debate]

## Proposed ledger updates
| Debate | Direction | Strength | Passage | Source / date | Status |
|---|---|---|---|---|---|
[Proposed — not applied]

## Coverage
Read: [sources by vendor / type] | Produced nothing: [list] | Not supplied or not reachable this cycle: [list]

## Judgment calls and gaps
[Items routed with low confidence, truncated sources, anything the analyst should re-read]
```

## Where thesis monitoring goes wrong

- **Classifying against the stock instead of the debate.** "Good for the company" is not a classification. An item confirms or disconfirms a specific view on a specific question; an item that is bullish overall can still disconfirm the margin debate. Route first, then classify.
- **Treating restated information as evidence.** A note that repeats guidance, a podcast that summarizes the earnings call, a forum post quoting a news article — none of these is new. Trace each item to its origin and rate the origin, not the echo.
- **Strength inflation from confident tone.** Sell-side conviction, an expert's fluency, and a forum poster's certainty are not evidence quality. Strength follows position to know, specificity, and recency.
- **Single-source escalation.** One employee review, one expert, one thread is a data point. Alert on it if it is strong and disconfirming, but say it is uncorroborated, and let the digest show whether a second source appears.
- **Letting the confirming pile grow quietly.** The failure mode is not a missed alert; it is a quarter of "confirms thesis" items that lull the analyst. The running ratio per debate exists to make a lopsided pile visible.
- **Forcing every item into a debate.** Neutral is a legitimate and common classification. A monitor that finds thesis relevance in everything is producing noise, and the analyst will stop reading it.
- **Silently narrowing the sweep.** If a vendor's feed was down or a source was not supplied, the digest says so. A clean-looking digest that covered half the sources is worse than one that reports the gap.
- **Editing the thesis by accretion.** Each classification is a proposal. If the monitor starts rewording debates or restating the view to match the evidence, the ledger loses its audit trail and the analyst loses ownership of the call.

## Guardrails

- **The thesis is not rewritten here.** The monitor classifies evidence and proposes ledger updates. Changing a debate's wording, the team's view, or the thesis itself is the analyst's decision, made in the ledger.
- **Every classification carries a quoted passage.** No direction or strength rating stands without the exact text that supports it, with source and date. Paraphrase does not qualify.
- **Direction is relative to the view held.** The header states the position direction and that labels are relative to the team's view, so a disconfirming item on a short is never misread as bearish on the stock.
- **Only sources actually read are reported.** The monitor reads what was attached and what setup pointed it to, and nothing else. It does not summarize a source it could not open, infer content from a title, or fill a coverage gap with recall. What was not read is listed.
- **Read-only everywhere.** Mailboxes, transcript libraries, shared folders and the debate ledger are read and never changed: no moving, marking, forwarding, replying or editing. The only thing the skill writes is its own digest, to the location saved in setup.
- **Figures come from a named source, not recall.** Where an item contains a number that matters — a price, a volume, a margin — it is quoted from the source with attribution, labeled extracted, and never adjusted or reconstructed. Any derived figure is labeled estimated with its basis.
- **Expert-network and licensed content stays within its terms.** Transcripts and licensed feeds are used as their vendor agreements allow; passages are quoted at the length the classification needs and no further, and the digest does not reproduce whole sources.
- **Confidentiality.** Debate ledgers, internal notes, and the book's positions are among the most sensitive information the firm holds. Assume a firm-approved AI environment and reproduce nothing beyond what the digest requires.
- **Not investment advice.** This is internal evidence classification against a stated thesis. It is not a recommendation to buy, sell, size, or hold anything, and an accumulation of disconfirming items is a prompt to re-examine, not a signal to trade.

## Example prompts

> "Debate ledger for [position] attached — three debates, we're long. This week's flow: [four] expert transcripts across [two vendors], [six] sell-side notes, two podcast transcripts, and a scrape of the employee-review site. Classify everything against the debates, disconfirming first, quote the passages, and give me the proposed ledger updates in our table format. Also tell me which of the transcripts I should actually read in full."

> "Short position, thesis document attached but no formal debate list — draft the debates from the memo and flag them as proposed. Then read the [10-Q] filed [date] and the [three] transcripts attached against them. I care most about whether anything confirms the bull case I'm short against; put that at the top even though it's 'confirming' for the company."

> "Set up thesis-evidence-monitor. The debate ledgers are in the 'Debates' folder on SharePoint, one file per position, and prior digests are saved next to them. Read the expert transcripts in our transcript library, the 'Research' folder in Outlook, and anything I attach. Alert me only on strong items either way, moderate-or-stronger disconfirming items, and new primary data. Weekly digest, saved to the same folder."

> "This week's items for [position] are attached; run the digest and show me the running ratio per debate against the prior weeks."

## Works well with

This skill is the intake for **key-debates-ledger**: the ledger holds the debates and the team's views, and this monitor reads the flow against them and hands back proposed updates, so run them as a pair. When a debate accumulates enough disconfirming evidence to warrant a structured challenge, **thesis-red-team** is the next step. For the sources themselves, **expert-call-synthesis** is the right tool when a single debate needs a batch of calls synthesized rather than monitored, **sellside-research-triage** handles the sell-side inbox as a category before the surviving notes are read here, and **earnings-call-extractor** turns a call transcript into a memo worth classifying. For claim-level tagging of a single long document, use **claim-sentiment-extractor**.
