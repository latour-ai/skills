---
name: ic-question-anticipator
description: >-
  Read a draft IC memo and model summary the way the toughest committee member
  will, and generate the twenty hardest questions the committee is likely to
  ask — sourced from the memo's weakest evidentiary points, standard IC
  pressure areas like customer concentration, management depth, and multiple
  justification, and the firm's own past IC minutes where provided. Each
  question comes with a suggested answer citing the specific memo section or
  diligence source that supports it, an honesty rating (solid, partial, cannot
  answer yet), and a ranked list of the questions the team genuinely cannot
  answer with the work that would close each gap before the meeting. For
  private equity and growth deal teams preparing for investment committee.
  Trigger on phrases like "prep me for IC," "what will the committee ask,"
  "red-team this memo before IC," "hardest questions on this deal,"
  "pre-mortem the IC meeting," "anticipate IC pushback," or when a user
  uploads a draft IC memo and asks how it will hold up. Do NOT use for
  drafting the memo itself — use the ic-memo-drafter skill. Do NOT use for
  attacking the investment thesis from first principles — use the
  thesis-red-team skill. Do NOT use for recording what the committee actually
  said — use the ic-minutes-generator skill. Deal materials are confidential;
  assume a firm-approved AI environment.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# IC Question Anticipator

You know roughly what the committee will push on, and "roughly" is how deals get sent back for two more weeks of work. This reads your draft memo and model the way your most skeptical committee member does — hunting for the assertion with the thinnest support, the number that appears twice with different values, the risk mentioned once and never priced — and hands you the twenty hardest questions with sourced answers before the meeting instead of the morning after. The most valuable output is the shortest: the list of questions you cannot yet answer, ranked by damage, with the work that would close each gap.

## Why this skill exists

IC prep is rehearsal without an opponent. The team that wrote the memo reads it back to themselves, and the memo's blind spots are by construction the team's blind spots — the customer-concentration risk got a paragraph because a paragraph is what the team believes it deserves, and no amount of re-reading changes that belief. What changes it is a hostile reader, and hostile readers are exactly what committees supply, one meeting too late.

The failure has a specific shape. Committees rarely reject deals outright; they send them back. And they send them back not because the answer to their question was bad, but because the team visibly did not have one — the scramble in the room converts a manageable issue into evidence the diligence was thin. Most of those questions were predictable: any experienced partner can name the standard pressure areas, and the firm's own IC minutes are a literal transcript of what this committee asks. Nobody mines either systematically, because the week before IC is the week nobody has.

There is also a quieter benefit. Forcing every anticipated question through an honesty rating — solid, partial, cannot answer yet — before the meeting is the discipline that gets the memo fixed while it can still be fixed. A "cannot answer yet" discovered on Tuesday becomes a data request; the same gap discovered in the meeting becomes a resubmission.

## Inputs

**Required:**
- The draft IC memo (uploaded or pasted)
- A model summary or key model outputs — returns by case, leverage, entry and exit assumptions, sensitivities. The full model works; a summary page is enough.

**Optional but high-value:**
- **Minutes, question lists, or recollections from the firm's past IC meetings** — this is the highest-value optional input, because every committee has house obsessions that generic pressure-testing will miss
- Which committee members will attend, and any known priors (the one who always asks about management, the one burned by a rollup)
- The diligence file or key workstream outputs (QoE, commercial, legal), so suggested answers can cite evidence beyond the memo
- Prior memos for deals this committee approved or killed, for pattern-matching
- The IC date, so the close-the-gap work can be sequenced realistically
- The deal team's own list of feared questions — their fears are usually well-founded and worth pressure-testing first

**Missing-input behavior:** Memo plus model summary is enough to run. Without past IC minutes, draw questions only from the memo's evidentiary weaknesses and standard pressure areas, and say the firm-specific layer was skipped. Without diligence materials, suggested answers cite only the memo and model — and where the memo itself lacks support for a claim, the honest answer is "cannot answer yet," not a plausible-sounding response invented for rehearsal. Never fabricate a diligence finding, a data point, or a committee member's view to make an answer sound complete.

## How it works

1. **Read the memo as evidence, not narrative.** For each material claim — market growth, competitive position, management quality, addback validity, exit multiple — note what actually supports it: a diligence source, a management assertion, a single expert call, or nothing but the sentence itself. The gap between claim strength and evidence strength is where questions come from.
2. **Check the memo against the model.** Numbers cited in prose that differ from model outputs, base-case assumptions more aggressive than the memo's tone implies, and downside cases that still clear the return hurdle are all committee catnip. A downside case that never loses money will be the first question asked.
3. **Mine past IC materials** where provided: recurring question types, the topics that generated the longest discussions, the reasons deals were sent back, and any prior deal that resembles this one — committees reason by scar tissue, and a deal that rhymes with a past loss inherits its questions.
4. **Apply the standard pressure areas** — the archetype list below — but only where the memo is actually exposed. A generic question the memo already answers well is noise; the skill's job is the questions it answers badly.
5. **Draft each question in committee voice:** short, pointed, and phrased as a member would ask it, not as an analyst would title a section. "Walk me through why churn is 8% here when the CIM said 5%" beats "discuss retention assumptions."
6. **Draft the suggested answer** for each, citing the specific memo section, model output, or diligence source that supports it. The answer must be honest to the evidence — where support is partial, the suggested answer concedes the limit rather than papering over it, because a committee member who smells papering asks three follow-ups.
7. **Rate every answer honestly:** solid (evidence-backed and citable), partial (an answer exists but has a real hole a follow-up would find), or cannot answer yet. Grade harshly — the rating exists to direct work, and a generous "solid" defeats the purpose.
8. **Rank the cannot-answer-yet list by damage:** which unanswerable question most threatens the deal or the team's credibility, and what specific work — a data request, an expert call, a model rebuild, a management session — would close each gap before the IC date.
9. **Sequence the top questions into a rehearsal order** — lead with the kill-question class, since a strong answer there buys goodwill for everything after — and flag any question whose honest answer implies the memo itself should change before submission.

## Output format

Adapt the skeleton to the deal; the sections are the contract, the layout is not.

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# IC Question Anticipation — [deal name]
IC date: [ ] | Memo version: [ ] | Past IC materials: [used / not provided]

## Read on the memo (one paragraph)
Where the memo is strong, where it is exposed, and the two or three question
lines most likely to dominate the meeting.

## The twenty questions
### Q[#] — [pressure area] — [archetype]
**As the committee will ask it:** "[question in committee voice]"
**Suggested answer:** [ ] — cites [memo §, model output, or diligence source]
**Honesty rating:** [solid / partial / cannot answer yet]
**If partial — the hole a follow-up finds:** [ ]

## Question summary
| # | Question (short) | Pressure area | Rating | Source of answer |
|---|---|---|---|---|

## Cannot answer yet — ranked by damage
| Rank | Question | Why damaging | Work that closes it | Feasible by [IC date]? |
|---|---|---|---|---|

## Fix the memo first
[Questions whose honest answer means the memo should change before
submission — the cheapest possible outcome of this exercise.]

## Rehearsal order
[Suggested sequence for the prep session, kill-questions first.]
```

## The question archetypes committees actually use

Committee questions cluster into recognizable types, and knowing the type tells you what a good answer must contain:

- **The kill question** — the one issue that, unanswered, ends the deal: concentration, a broken unit economic, a regulatory overhang. There is usually exactly one per deal, the team usually knows what it is, and the memo usually under-addresses it precisely because it is frightening. A good answer quantifies the exposure and shows the mitigation priced into the bid.
- **The "why does this exist" question** — why is this business available, at this price, to us? If the answer is "proprietary relationship," expect the follow-up asking why better-informed insiders passed. A good answer names the seller's actual motivation and why the auction dynamics were what they were.
- **The sizing question** — why this check, this leverage, this entry multiple? Committees test whether conviction and sizing match: a memo that reads nervous but proposes full leverage will be asked to reconcile the two.
- **The prior-deal-scar-tissue question** — "this looks like [the deal that went wrong]." Inherited from the firm's history, invisible without the minutes or an old hand. A good answer names the resemblance first and then the specific difference, in that order.
- **The downside-credibility question** — what actually breaks this, and does the downside case model that or a mild version of it? A downside constructed by shaving growth 200bps convinces no one who has seen a real one.
- **The management question** — who runs this in year two, what does the org lack, and what did references actually say verbatim rather than in summary.
- **The exit question** — who buys this from us, at what multiple, and why is that multiple defensible if entry multiples were "elevated" when we bought?
- **The "what did diligence not cover" question** — asked to test candor more than content. The only good answer is a real list, delivered without flinching.

## Guardrails

- **Never invent an answer to make rehearsal comfortable.** If the evidence for a claim is not in the memo, model, or provided diligence, the rating is "cannot answer yet" — a flattering fabricated answer is worse than the gap, because it gets rehearsed and then repeated in the room.
- **Every suggested answer cites its source** — memo section, model output, or diligence document. An answer the presenter cannot trace under pressure is an answer they do not have.
- **Grade honesty harshly.** "Partial" with the hole named beats "solid" that fails on the first follow-up. The ratings exist to allocate the remaining prep time, and inflation defeats them.
- **Questions must be exposure-driven, not template-driven.** Twenty generic questions the memo already answers is a checklist, not a pre-mortem. Every question should point at a real soft spot.
- **This is preparation, not prediction.** The committee will ask things no one anticipated; the output claims to cover the probable, not the possible, and says so.
- **Not investment advice.** The skill pressure-tests the presentation of a decision; it does not recommend making or rejecting the investment.
- **Confidentiality:** IC memos, models, diligence files, and IC minutes are among the most sensitive documents a firm produces, and underlying deal materials are typically NDA-covered. Assume a firm-approved AI environment, and do not carry one deal's confidential facts into another deal's answers.

## Example prompts

> "Draft IC memo and model summary page for [deal name] attached, IC is [date]. We also attached minutes from our last four IC meetings — this committee has a thing about customer concentration and about deals sourced from one banker. Give me the twenty hardest questions, sourced answers, honest ratings, and the cannot-answer list ranked by damage."

> "Second time at IC with this deal — we got sent back for the downside case and management depth. Memo v2 attached. Pressure-test whether the fixes actually hold up, and tell me what the committee asks next if they accept them."

> "No past minutes to give you — new firm, first IC. Memo and model attached for a [sector] carve-out. Run the standard pressure areas hard, especially why the parent is selling and what the standalone cost structure really looks like."

## Works well with

Run this after **ic-memo-drafter** produces the draft and before submission — the "fix the memo first" list feeds directly back into the next draft. Pair with **thesis-red-team** earlier in the process, when the question is whether the thesis survives attack rather than how the memo survives the meeting, and use **ic-minutes-generator** afterward so next quarter's run of this skill has the firm-specific layer it wants most.
