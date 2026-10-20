---
name: expert-call-question-guide
description: >-
  Prepare a prioritized question guide for an upcoming expert network call —
  Tegus, AlphaSense, GLG, Third Bridge, or direct — from the analyst's
  thesis, model assumptions, and prior transcripts on the name. Sequences
  questions deliberately (rapport, landscape, the money questions, sensitive
  topics last), phrases them to elicit specifics rather than generalities,
  tailors every block to what this expert's vantage point can actually
  answer, pre-writes follow-up probes for the likely evasions, and marks the
  one question the call cannot end without answering. For public equity
  analysts and PMs, private equity and growth deal teams, and credit
  analysts running channel work. Trigger on phrases like "prep my expert
  call," "question guide for tomorrow's call," "what should I ask this
  expert," "call with a former [role] at [company]," "help me prep for this
  Tegus call," or when a user describes an upcoming expert call and their
  open questions. Do NOT use for synthesizing completed transcripts after
  the calls — use the expert-call-synthesis skill; this one runs before the
  call, that one runs after the stack. Do NOT use for prepping a management
  meeting at a conference — use the conference-prep-planner skill. Observes
  expert network compliance limits.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Expert Call Question Guide

The most expensive hour in the research process is routinely the least prepared: five questions scribbled ten minutes before, twenty minutes burned on background the last three experts already covered, and the realization afterward that the one question the thesis turns on was never asked. This designs the interrogation in advance — a sequenced guide built from your thesis, your model's live assumptions, and what your existing transcripts already answer, with every question matched to what this particular expert was in a position to know and a pre-written probe for each likely evasion.

## Why this skill exists

A $1,000-per-hour call has a strange economics: the cost is fixed, the yield is set almost entirely by preparation, and preparation is the step that gets squeezed. The failure is rarely asking bad questions — it is asking questions the expert cannot answer well. A former regional sales VP gets asked about gross margin structure; a supply chain consultant gets asked about win rates. The expert answers anyway, because experts are paid to answer, and the analyst walks away with confident testimony from someone who was never positioned to know. Matching questions to vantage point is the single highest-yield move in call prep, and it requires deliberately deciding what *not* to ask.

The second failure is redundancy. Firms sit on transcript libraries and still spend the first third of every call re-purchasing landscape context they already own. The prior transcripts define the frontier — what is settled, what is contested, what nobody has answered — and the new call should start at the frontier, not at the beginning.

The third is phrasing and sequence. Leading questions collect echoes of the analyst's own thesis at $1,000 an hour. Sensitive questions asked early shut experts down; the same questions in the last fifteen minutes, after rapport and momentum, get answered. And vague answers stand unless a specific follow-up is ready in the moment — which it never is, unless it was written in advance. None of this craft is exotic; it is journalism and litigation practice applied to research. It just doesn't happen ten minutes before the call.

## Inputs

**Required:**
- The expert's vantage point: role, employer, seniority, function, and how recently they held the position
- The subject — company or industry — and what you are trying to figure out, even roughly

**Optional but high-value:**
- **Your thesis and your model's live assumptions** — this is what turns a generic topic list into an interrogation aimed at the numbers that move your outcome; two or three sentences of thesis and three to five assumptions are enough
- Prior transcripts and call notes on the name, so the guide skips what you already own and probes where past experts disagreed
- The call length and format (30 vs. 60 minutes changes how ruthless the prioritization must be)
- The screening questionnaire or the expert's network profile, which often reveals what they are eager to talk about — and what they dodged
- Whether this is public equity or a live private deal, which changes both the questions and the compliance envelope

**Missing-input behavior:** Vantage point plus subject is enough to produce a useful guide built on the standard uncertainty map for that kind of business. Without a thesis, say the guide is untargeted and build it around what this vantage point is uniquely positioned to know — do not invent a thesis to aim at. Without prior transcripts, skip the redundancy screen and say so; never guess at what earlier calls covered. If the expert's vantage point is unknown, stop and say the guide cannot be tailored — a question guide not matched to the expert is the failure mode this skill exists to prevent.

## How it works

1. **Map what this expert can actually know.** From the vantage point, list the topics where they are authoritative, the topics where they have a view but no privileged position, and the topics where their testimony would be noise. The guide draws only from the first column; the third column is written down precisely so it does not get asked.
2. **Build the uncertainty ledger.** From the thesis and model assumptions, list the live questions — the assumptions that move the outcome and are genuinely unresolved. Then screen against the prior transcripts: mark each as settled (skip it), contested (probe the disagreement), or unasked. The call attacks contested and unasked items only.
3. **Cross the two maps.** The core of the guide is the intersection: live uncertainties this expert is positioned to resolve. Where a major uncertainty falls outside this expert's knowledge, note it for a future call rather than forcing it into this one.
4. **Write calibration questions first** — two or three questions whose answers you already know from filings, transcripts, or the screen. They open the call as warm-up, matched to the expert's background, and they measure the witness: an expert who is vague or wrong on what you can verify gets discounted on what you cannot. Do not reveal which questions are calibration.
5. **Sequence the body:** landscape questions the expert finds easy and flattering, then the money questions in priority order while attention and time are abundant, then sensitive topics — competition, departures, failures, anything that could embarrass a former employer — in the final third, phrased softly. Never open with what you most need; open with what gets them talking.
6. **Phrase for specifics, against leading.** Every question open-ended and neutral: "walk me through how a renewal negotiation actually goes" beats "would you say customers have strong switching costs?" — the second buys an echo. Prefer questions about *mechanisms and events the expert lived through* over requests for opinion; ask for numbers wrapped in experience ("in deals you worked on, what discount did it take to displace the incumbent?").
7. **Pre-write the probes.** For each core question, script the follow-up for the two likely bad outcomes: the vague answer (force an example: "when did you last see that happen — what were the specifics?") and the surprising answer (test it before believing it: "is that your experience directly, or the industry read?"). Probes are the difference between a guide and a script that collapses at first contact.
8. **Mark the must-answer question.** One question, flagged unmistakably, that the call cannot end without addressing — with a note on when to force it in if the clock is running out (usually by minute forty of sixty).
9. **Add the closing pair:** "what should I have asked that I didn't?" and "who else should I talk to about this?" — the two cheapest questions in the guide and reliably among the highest-yield.
10. **Cut to fit the clock.** A 60-minute call carries eight to twelve core questions with probes; a 30-minute call carries five. Rank everything, draw the line, and park the remainder as a bench list in case the call runs fast.

## Output format

A skeleton to adapt — the sequencing logic matters more than the exact headings.

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# Expert Call Guide — [company / subject]
Expert: [role, employer, tenure, left when] | Call: [date, length] | Network: [ ]
Thesis: [stated / none provided] | Prior transcripts screened: [N / none]

## What this expert can and cannot answer
Authoritative on: [ ]
Has a view, no privileged position: [ ]
Do not ask (noise from this vantage point): [ ]

## The must-answer question
> [The one question, phrased as it should be asked]
Why it's the one: [link to thesis/model] | Force by: [minute mark]

## Warm-up & calibration (minutes 0–8)
1. [Question matched to expert's background]
   — Known answer: [what you already know, for calibration scoring]

## Core blocks (minutes 8–40, in priority order)
### Block: [topic] — targets: [model assumption / open question]
Q: [open-ended, neutral phrasing]
   If vague → [specific probe]
   If surprising → [verification probe]

## Sensitive topics (final third)
Q: [softened phrasing]
   Rationale for placement: [ ]

## Closing pair
- What should I have asked that I didn't?
- Who else should I talk to about this?

## Bench (if time allows)
| Q | Target | Why it didn't make the cut |
|---|---|---|

## Parked for other calls
| Question | Vantage point that could answer it |
|---|---|
```

## Sequencing craft — why the order is the method

The guide's structure encodes interviewing practice that analysts rarely get taught:

- **Calibration before reliance.** Two or three questions with verifiable answers, asked innocently at the top, tell you how much to trust everything after. An expert crisp on the checkable is worth probing hard; one who bluffs the checkable is a 30-minute call no matter what was booked.
- **Easy and flattering first.** Experts talk more freely once they've demonstrated expertise. The landscape opener isn't wasted time if it is chosen from the frontier — one question, not twenty minutes.
- **Money questions in the second quarter.** Attention, rapport, and clock are all still abundant. The common error is saving the best for last and losing it to overtime.
- **Sensitive topics late, phrased as observations.** "Some people we've talked to see turnover on that team — what's your read?" gets an answer where "why did everyone quit?" gets a wall. Late placement means a shutdown costs minutes, not the call.
- **Never telegraph the thesis.** Experts are agreeable by profession; an expert who can infer what you want to hear will drift toward it. Neutral phrasing isn't politeness — it is contamination control.
- **Mechanism beats opinion.** "What happens operationally when a customer threatens to churn?" yields evidence; "is churn a problem?" yields a take. Ask for the lived sequence of events and let the conclusion be yours.
- **Silence is a probe.** Note in the guide where to simply wait after an answer — experts fill silences with the unrehearsed material, which is the material you came for.

## Guardrails

- **Never ask what the vantage point cannot support.** The do-not-ask list is a real output, not a formality — confident testimony from an unpositioned expert is worse than no testimony, because it arrives wearing authority.
- **No leading questions in the core blocks.** Every core question is screened for embedded conclusions before it ships; if the question contains the thesis, rewrite it.
- **Redundancy screen is evidence-based.** A question is only marked "settled — skip" when prior transcripts actually answer it well, cited; never assume coverage from memory.
- **The guide prepares questions, not answers.** It does not predict what the expert will say or pre-fill conclusions — the probes handle answer contingencies, which is different from expecting an answer.
- **MNPI and compliance.** The guide must not solicit material non-public information: no questions seeking undisclosed financials, unannounced customer wins or losses, pending transactions, or anything confidential to a current employer. Flag any user-requested question that crosses this line rather than rephrasing it into compliance. Current employees of the subject company and covered consultants get a visibly narrower guide, noted as such. This skill does not replace the firm's expert network policy, chaperone requirements, or pre-clearance process.
- **Not investment advice.** The guide structures inquiry; it does not recommend a position, and a well-run call is testimony to be weighed, not a decision.
- **Confidentiality:** theses, model assumptions, and prior transcripts are sensitive research property, and transcripts are licensed content under network terms. Assume a firm-approved AI environment.

## Example prompts

> "Expert call Thursday, 60 minutes, with a former VP of sales at [company] who left 18 months ago. Thesis: net retention holds above 115% because switching costs are underappreciated. Model assumptions: pricing holds through the renewal cycle, sales productivity recovers by Q3. Prior transcripts attached — build the guide, and skip anything the last four calls already nailed down."

> "First call on a new name — a supply chain consultant who works with [industry] manufacturers. No thesis yet, no prior transcripts; I'm two days into the file. Give me a guide built around what someone in that seat actually knows, and tell me explicitly what NOT to ask them."

> "Live private deal, 30 minutes with a former customer of the target who switched away last year. We're worried about churn and pricing pressure. Half an hour only — give me the five questions with probes, mark the must-answer, and keep the sensitive competitive stuff phrased so they don't clam up."

## Works well with

This skill and **expert-call-synthesis** are the two halves of one loop: this one designs the next call from the frontier, that one redraws the frontier from the completed stack — and its next-call list is this skill's best input. Run **thesis-red-team** before a call series to sharpen which assumptions deserve the expensive minutes, and **conference-prep-planner** when the meeting is with management rather than an expert.
