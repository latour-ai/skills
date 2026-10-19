---
name: performance-attribution-narrator
description: >-
  Turn raw attribution output into the performance narrative a PM, CIO, or
  investor actually needs — return decomposed into alpha versus factor beta,
  the largest contributors and detractors assessed against the thesis that
  justified each position, "right for the wrong reasons" winners flagged, and
  a drafted performance commentary section for the investor letter in the
  firm's voice. For portfolio managers, CIOs, risk and quant teams, and IR
  professionals at hedge funds, long-only managers, and multi-strategy firms.
  Trigger on phrases like "write up the attribution," "explain the month,"
  "why were we up," "what drove performance," "draft the performance
  commentary," "turn this attribution into a narrative," "month-end write-up,"
  "was this alpha or beta," or when a user uploads attribution output, a P&L
  by position or sector, or a risk model decomposition. Do NOT use for
  drafting a full quarterly LP letter — use the lp-update-generator skill. Do
  NOT use for synthesizing other managers' letters — use the
  quarterly-letter-synthesizer skill. Performance commentary drafted here
  requires compliance review before it goes to investors.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Performance Attribution Narrator

Attribution reports tell you what happened. They do not tell you whether your process worked. This does the translation: which P&L was skill and which was factor weather, which winners you should be suspicious of, which losers were actually fine — and then drafts the investor-letter commentary from the same numbers, so what you tell LPs and what the attribution says never drift apart.

## Why this skill exists

Two things eat a day at every month-end, and they are the same underlying work done twice. First, someone stares at an attribution report and tries to convert a table of contributions into an explanation of the period. Second, someone writes the performance commentary for investors, usually from a slightly different set of numbers and a slightly different narrative, which is how the letter and the risk report come to disagree.

The analytically interesting part is the one that gets skipped under time pressure: separating outcome from process. A position that made money because the whole sector rallied is not evidence your thesis was right, and treating it as such corrupts the feedback loop that is supposed to make you better. Same in reverse — a loser that behaved exactly as underwritten is not a mistake. Attribution data contains the answer to that question; almost nobody has time to extract it before the letter is due.

## Inputs

**Required:**
- Attribution output for the period: P&L or return contribution by position, and ideally by sector, factor, and strategy. Whatever form your risk system or admin produces.

**Optional but high-value — the "optional" ones are what make this more than a summary:**
- Your active theses: a sentence or two per major position on why you own it and what you expected. This is the input that turns the output from a description into an assessment.
- Factor decomposition from a risk model (beta, size, value, momentum, quality, volatility, sector factors) — without it, alpha-vs-beta separation is inference rather than measurement, and will be labeled as such
- Positioning: gross and net exposure, top positions and weights, sector tilts, and how these changed during the period
- Benchmark or hurdle, if performance is measured against one
- Prior period letters or commentary, for voice matching
- Fees, financing, borrow costs, and FX, if they are material and not already in the attribution
- What the user already believes drove the period — worth capturing, and worth testing against the data

**Missing-input behavior:** Attribution data alone is enough to run, but say plainly what the absence of theses costs: without them, the skill can describe contribution but cannot judge thesis-consistency, which is the section with the most value. Ask once for even rough thesis notes on the top five positions. Without a factor decomposition, do not silently estimate alpha — state that the alpha-vs-beta split is directional inference from sector and market behavior, not a measured decomposition.

## How it works

1. **Reconcile the total before decomposing it.** Confirm the contributions sum to the reported period return, and flag any residual. An unexplained residual is a data problem that invalidates everything downstream — surface it rather than distributing it.
2. **Decompose the return** into market/beta, factor contributions, and residual/idiosyncratic. Where a risk model was provided, use its numbers and name the model. Where one was not, separate what can be attributed to obvious sector and market moves from what cannot, and label the whole section as inference.
3. **Rank contributors and detractors** — typically the top five each — with contribution in basis points, average weight, and return.
4. **Assess each against its thesis.** For each major contributor and detractor, ask: did this work for the reason we underwrote? Sort into four buckets — right for the right reasons, right for the wrong reasons, wrong for the right reasons, wrong for the wrong reasons. The two middle buckets are where the learning is, and they are the ones a normal write-up erases. Where no thesis was supplied for a position, its thesis-consistent column reads "no thesis provided."
5. **Test the user's own explanation against the data** if they offered one. If the numbers do not support it, say so directly and show which figures contradict it. This is the highest-value thing the skill does and it should not be softened.
6. **Note what did not happen.** Positions that contributed nothing despite a thesis that predicted movement, hedges that failed to hedge, and sizing that was too small to matter given conviction — absence of contribution is information.
7. **Check consistency with the prior period's narrative** if prior commentary was provided. A story that changes every month to fit the outcome is itself a finding.
8. **Draft the investor commentary** — three to four paragraphs, factual, in the firm's voice, derived strictly from the same numbers, with no forward-looking claims and no spin.

## Output format

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# [Fund / Strategy] — Performance Narrative, [period]
Return: [gross] / [net] | Benchmark: [ ] | Attribution source: [system, date]
Factor model: [named model / none provided — alpha-vs-beta is inferred]

## Reconciliation
Sum of contributions: [ ] vs. reported return: [ ] | Residual: [ ]
[If the residual is material, stop and flag it before anything else.]

## The period in three sentences
[What drove the return, in plain language, no jargon.]

## Return decomposition
| Source | Contribution | % of total |
|---|---|---|
| Market / beta | | |
| Factor: [ ] | | |
| Factor: [ ] | | |
| Idiosyncratic / alpha | | |
| Fees, financing, borrow, FX | | |
[Method note: measured from [model] / inferred, and what that means.]

## Top contributors
| Position | Contribution (bps) | Avg weight | Return | Thesis-consistent? |
|---|---|---|---|---|

## Top detractors
| Position | Contribution (bps) | Avg weight | Return | Thesis-consistent? |
|---|---|---|---|---|

## Process assessment
**Right for the right reasons:** [positions, one line each]
**Right for the wrong reasons:** [positions — what actually drove the P&L, and
why counting this as a win would be a mistake]
**Wrong for the right reasons:** [positions — thesis intact, timing or noise]
**Wrong for the wrong reasons:** [positions — the thesis was incorrect; say so]

## What didn't happen
[Non-contributors with live theses, hedges that didn't work, undersized
conviction positions.]

## Where the data disagrees with the stated view
[Only if the user offered an explanation. Be direct and show the figures.]

## Draft investor commentary — REQUIRES COMPLIANCE REVIEW
[3–4 paragraphs. Factual, matches the provided voice, gross/net labeled
explicitly, no forward-looking statements, no cherry-picked positions.]

## Open questions for the investment team
Numbered — what this period's data suggests should be examined.
```

## Reading attribution honestly

- **Contribution is not skill.** A 60bps contribution from a 6% position that rose with its sector is beta you paid attention to, not alpha you generated. The test is relative behavior, not absolute P&L.
- **Allocation vs. selection vs. interaction** (Brinson): being in the right sector is a different decision from picking the right name in it, made by different processes, and worth crediting separately.
- **Factor exposure is usually unintentional.** Most managers are more exposed to momentum, size, or a sector factor than they believe. When the factor contribution is large, the useful question is whether that exposure was a decision.
- **Short book attribution needs its own treatment.** Contribution, borrow cost, and the effect of position drift as shorts move against you are separate lines. A short that "worked" while borrow ate the return did not work.
- **Hedges are supposed to lose money in up periods.** Judge them against what they were meant to protect, not against zero.
- **Concentration in the attribution** — if two positions drove the whole period, say so plainly. A diversified narrative over a concentrated outcome is misleading.
- **Gross vs. net matters everywhere,** but especially in anything investor-facing. Label every figure.
- **A single period is a small sample.** Resist narrating one month as if it validates or invalidates a process; note where the same pattern has or has not appeared before.

## Guardrails

- **Reconcile first.** Never publish a decomposition that does not tie to the reported return. Residuals are surfaced, never allocated away.
- **Do not compute alpha you cannot measure.** Without a factor model, the split is inference — label it as such everywhere it appears, including in the drafted commentary.
- **Never soften a contradiction.** If the data does not support the PM's explanation of the month, say it directly. That is the reason to run this.
- **The investor commentary is a draft requiring compliance review, and it must say so.** Performance communications to investors are regulated. The draft must: label gross and net explicitly, avoid cherry-picking positions, avoid forward-looking or promissory language, avoid unsubstantiated superlatives, and never present hypothetical or backtested figures alongside actuals without clear labeling.
- **Use only provided numbers.** Never estimate a position's weight, a benchmark return, or a factor contribution that was not supplied. A missing input is stated as missing.
- **Attribution methodology varies.** Note the source system and, where it matters, that different methodologies (arithmetic vs. geometric linking, transaction-based vs. holdings-based) produce different numbers.
- **Not investment advice, and not a recommendation to change positioning.** The open questions section raises questions; it does not answer them.
- **Confidentiality:** position-level P&L is among the most sensitive data a fund holds. Assume a firm-approved AI environment.

## Example prompts

> "Attribution for October attached — P&L by position and Barra factor decomposition. Theses for the top ten positions are in the second file. We were up 2.1% gross. Write the narrative and draft the commentary paragraph for the monthly letter; here's last month's letter for voice."

> "We were down 40bps and I think it was entirely the energy short. Attribution attached — is that actually what happened?"

> "Q3 attribution, long-only, benchmark is the Russell 2000. No factor model. Decompose what you can, tell me which of my winners were just small-cap beta, and be blunt about it."

## Works well with

Feed the drafted commentary into **marketing-compliance-prescreen** before it reaches investors. Use **lp-update-generator** when the commentary needs to become a full quarterly letter, and **thesis-red-team** on any position that lands in "right for the wrong reasons."
