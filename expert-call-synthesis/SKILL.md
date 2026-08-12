---
name: expert-call-synthesis
description: >-
  Synthesize a stack of expert network call transcripts — Tegus, AlphaSense,
  GLG, Third Bridge, or internal — into one structured view of a company or
  industry: points of genuine consensus, real disagreements with each side
  attributed and credibility-weighted by vantage point, every quantitative
  data point in a sourced table, how expert views shifted over the date range,
  and the open questions nobody answered, framed as the next call list. For
  public equity analysts and PMs, private equity and growth deal teams, and
  credit analysts running channel work. Trigger on phrases like "synthesize
  these expert calls," "what did the experts say," "pull together these
  transcripts," "where do the experts disagree," "channel check summary,"
  "read these Tegus calls," "what am I still missing on this name," or when a
  user uploads multiple expert call transcripts on one company or sector. Do
  NOT use for a single earnings call — use the earnings-call-extractor skill.
  Do NOT use for a podcast episode — use the investment-podcast-analyzer
  skill. Do NOT use for building a sector map from public sources — use the
  market-map-builder skill. Observes expert network compliance limits.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Expert Call Synthesis

Fifteen transcripts, read weeks apart, become a vague impression plus the two quotes you happened to highlight. This reads them side by side and produces the thing you actually paid for: what the experts agree on, what they genuinely disagree about and whose vantage point makes them credible on that specific question, every number anyone cited, how the views moved over time, and what nobody has answered yet.

## Why this skill exists

Expert calls are expensive and the value decays in a specific way. Each call is useful when you take it, but the insight lives in the pile rather than in any single transcript — and the pile is never read as a pile. So the analyst carries an impression into the debate, and the impression is weighted toward whoever they spoke with most recently.

The disagreements are the worst casualty. When a former VP of sales and a current channel partner contradict each other on churn, that contradiction usually *is* the thesis question. But it only becomes visible when the transcripts are side by side, and it usually reads as noise when the calls are three weeks apart. The same goes for view drift: experts who were confident about a product cycle in January and hedged by May are telling you something, and nobody notices because nobody re-reads January.

The last output matters most for spend. Knowing which questions remain unanswered means the next call goes at the gap instead of re-covering ground you already bought.

## Inputs

**Required:**
- Two or more expert call transcripts on the same company or industry. Five to twenty is the intended range; below five the synthesis is thin, above twenty it still works but flag that coverage may be uneven.

**Optional but high-value:**
- **Your current thesis, in a sentence or two** — this enables the contradiction check, which is the section most likely to change your mind
- Each expert's vantage point if not clear from the transcript: role, employer, seniority, function, and how recently they left
- Call dates, if not in the transcripts — required for the view-drift analysis
- The specific questions you are trying to answer
- Your model's key assumptions, so expert data points can be tested against them
- Prior synthesis on the same name, for a what-changed comparison
- Whether this is public equity or a live private deal — it changes which questions matter and which compliance limits apply

**Missing-input behavior:** Transcripts alone are enough to run. Without a stated thesis, skip the contradiction section and say so — do not infer a thesis from the transcripts and then test it against them, which is circular. Without call dates, skip the view-drift section explicitly rather than guessing at chronology from content. If the transcripts are on materially different companies or subjects, say so and either scope to the largest coherent group or ask which subject to synthesize.

## How it works

1. **Build the expert roster first.** For each call: date, the expert's role and employer, function, seniority, how recently they held the role, and their relationship to the company (former employee, current or former customer, competitor, supplier, channel partner, industry consultant). Every claim downstream is attributed to a row in this table, because a claim without a vantage point cannot be weighted.
2. **Extract claims, not summaries.** Go through each transcript pulling discrete factual and judgmental claims with the supporting quote. Resist compressing at this stage — compression is where disagreements disappear.
3. **Cluster claims by topic** — demand, pricing, competition, churn and retention, product, management quality, unit economics, regulatory, whatever the calls actually cover. Let the topics come from the transcripts, not from a template.
4. **Identify consensus within each topic,** and distinguish real consensus from apparent consensus. Three former employees of the same company at the same time are one data point with three voices, not three independent confirmations. Say so when it happens.
5. **Identify genuine disagreements.** For each: state both positions, who holds each, quote both, and assess which vantage point is more credible *on that specific question* — a former CFO is authoritative on margin structure and no better than anyone else on competitive win rates.
6. **Table every quantitative data point** — market share, pricing, growth, churn, unit costs, cycle times, capacity — with the expert, their vantage point, the date, and the quote. Note where two experts give different numbers for the same metric.
7. **Trace view drift across the date range** where dates are available: which views strengthened, which softened, and whether the change tracks something observable in the business.
8. **Test against the stated thesis.** Flag every place the expert evidence directly contradicts it, and be direct — this is the section with the most value and the most temptation to soften.
9. **Assess coverage and bias in the sample.** Which vantage points are over-represented, which are absent, whether the calls were sourced in a way that could have selected for a view, and how much weight the whole body of evidence deserves.
10. **Write the next-call list** from the unanswered questions, specifying the vantage point that would answer each.

## Output format

```
# Expert Call Synthesis — [company / industry]
Calls: [N] | Date range: [earliest]–[latest] | Networks: [ ]
Thesis tested: [stated / none provided]

## What the calls establish (one paragraph)
The two or three things this body of evidence actually supports, and the
confidence they deserve.

## Expert roster
| # | Date | Role | Employer | Vantage point | Recency | Authoritative on |
|---|---|---|---|---|---|---|

## Consensus
### [Topic]
**View:** [ ]
**Held by:** [expert #s] | **Independent sources:** [count — not voice count]
> "[strongest supporting quote]" — Expert [#], [vantage point]
**Confidence:** [high / medium / low] — [why, referencing independence and vantage]

## Disagreements
### [Topic] — the question at issue: [ ]
**Position A:** [ ] — Expert [#s]
> "[quote]" — Expert [#], [vantage point]
**Position B:** [ ] — Expert [#s]
> "[quote]" — Expert [#], [vantage point]
**Whose vantage point is stronger here:** [assessment specific to this question]
**What would settle it:** [ ]

## Quantitative data points
| Metric | Value | Expert | Vantage point | Date | Quote |
|---|---|---|---|---|---|
Conflicting figures for the same metric: [flagged explicitly]

## How views shifted over the date range
[Only if dates available. What strengthened, what softened, and whether it
tracks anything observable.]

## Against the thesis
[Only if a thesis was provided. Every direct contradiction, quoted, with the
expert's vantage point. Be direct.]

## Coverage assessment
Vantage points represented: [ ] | Missing: [ ]
Over-representation or sourcing bias: [ ]
Overall weight this evidence deserves: [ ]

## Next call list
| # | Open question | Vantage point that would answer it | Why it matters |
|---|---|---|---|
```

## Weighting by vantage point

Credibility is question-specific, not person-specific. The useful test is always: was this person in a position to know *this particular thing*?

- **Former employees** — authoritative on internal process, cost structure, and culture; decay quickly on current performance. Note how long ago they left and at what level. A former SVP two years out knows the org, not this quarter.
- **Current and former customers** — the best source on why they buy, switching costs, and pricing pressure; representative only of their segment. One enterprise customer says nothing about SMB churn.
- **Competitors** — informative on market structure and competitive dynamics, systematically biased on the target's position and win rates.
- **Suppliers and channel partners** — good on volumes, lead times, and order patterns; often the best quantitative source; usually see only their slice.
- **Industry consultants** — broad view, frequently the least specific, and sometimes recycling what they heard on other calls including yours.
- **Seniority cuts both ways** — executives see strategy and are further from operational reality; individual contributors see the mechanism and not the aggregate.
- **Recency beats seniority** for anything about current conditions.
- **Independence matters more than count** — several experts from the same employer and era are one observation. Weight by independent vantage points, not by headcount.

## Guardrails

- **Every claim is attributed to a numbered expert with their vantage point.** An unattributed claim in a synthesis is worse than useless, because it inherits false authority from the aggregate.
- **Quote exactly.** Verbatim, with the expert number. No paraphrase presented as a quote, and no composite quotes assembled from multiple speakers.
- **Never merge disagreeing experts into a single view.** Averaging away a contradiction destroys the most valuable content in the pile. If two experts disagree, the output shows both.
- **Distinguish independent confirmation from repetition.** Say explicitly when apparent consensus comes from a single vantage point echoed by several voices.
- **Do not fill gaps with general industry knowledge.** If the experts did not address something, it belongs in the next call list, not in the synthesis dressed as a finding.
- **Expert opinion is opinion.** These are individuals' recollections and judgments, frequently about companies they no longer work for, sometimes wrong and sometimes stale. The synthesis reports what was said, weighted — it does not convert testimony into fact.
- **MNPI and compliance.** Expert network calls carry real regulatory risk. Flag any content that appears to be material non-public information — undisclosed financial results, specific unannounced customer wins or losses, pending transactions, or anything an expert describes as confidential to their current employer. Do not incorporate flagged content into the synthesis; surface it separately for the compliance team. Where an expert appears to be a current employee of the subject company or a covered supplier discussing confidential specifics, say so prominently. This skill does not replace the firm's expert network policy, chaperone requirements, or pre-clearance process.
- **Not investment advice.** The synthesis maps what is known, contested, and unasked. It does not recommend a position.
- **Confidentiality:** expert call transcripts are licensed content subject to the network's terms and are usually restricted to the subscribing firm. Assume a firm-approved AI environment, and do not reproduce transcripts beyond the quotes the synthesis requires.

## Quality checks

- [ ] Every expert on the roster with a vantage point and recency
- [ ] Every claim attributed to a numbered expert
- [ ] Every quote verbatim, no composites
- [ ] Consensus sections distinguish independent sources from voice count
- [ ] Disagreements preserved with both sides quoted, never averaged
- [ ] Credibility assessed per question, not per person
- [ ] Every quantitative data point sourced and dated; conflicts flagged
- [ ] View drift section run or explicitly skipped for missing dates
- [ ] Thesis contradictions stated directly, or the section marked skipped
- [ ] Coverage gaps and sourcing bias assessed honestly
- [ ] Possible MNPI surfaced separately and excluded from the synthesis body
- [ ] Next call list specifies the vantage point needed, not just the topic

## Example prompts

> "Twelve Tegus transcripts on [company] attached, calls run over the last five months. My thesis: pricing power is durable because switching costs are underappreciated. Synthesize them, and be blunt about anywhere the experts contradict me."

> "Nine expert calls from a live diligence process on a specialty distribution business. Synthesize by topic, table every number anyone gave us, and tell me what we still need to ask before IC in two weeks."

> "These six calls span eighteen months on the same industry. I mainly want the drift — what did people believe early that they don't believe now, and does anything explain it?"

## Works well with

Run **thesis-red-team** on your view after the synthesis, using the disagreements as ammunition. Pair with **earnings-call-extractor** to test whether management's commentary matches what the channel says, and **market-map-builder** when the calls are sector work rather than single-name work.
