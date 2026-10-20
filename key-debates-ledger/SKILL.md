---
name: key-debates-ledger
description: >-
  Maintain an explicit bull/bear debate ledger for each significant
  position: the two to four decidable questions that will actually
  determine the outcome, the current evidence on each side with source and
  date cited, and the pre-registered upcoming data point most likely to
  resolve each debate. As new filings, earnings transcripts, sell-side
  notes, and internal call notes arrive, it files each data point against
  the ledger — bull side, bear side, or neither — flags when the balance
  of evidence has meaningfully shifted, screens for genuinely new debates,
  and retires settled ones with the evidence that settled them. For
  research analysts and PMs running fundamental equity and credit books.
  Trigger on phrases like "update the debates ledger," "what are the key
  debates on [ticker]," "does this change the debate," "build a debates
  ledger from this thesis memo," "where does this data point land," "what
  would change our mind on this name," or when a user pastes new material
  against an existing ledger. Do NOT use to extract a single earnings call
  into a memo — use the earnings-call-extractor skill. Do NOT use to
  stress-test the whole thesis adversarially — use the thesis-red-team
  skill. Do NOT use to synthesize a stack of expert transcripts — use the
  expert-call-synthesis skill. Not investment advice.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Key Debates Ledger

Most position debates go in circles because nobody has written down what the open questions actually are, what evidence exists on each side, and what would settle them — so every new data point restarts the argument from zero, and the loudest recent voice sets the frame. This maintains the ledger that stops the circling: the two to four questions that decide the outcome, the evidence on each side with citations, and the pre-registered data point that would resolve each. New material lands somewhere specific — it moves a debate or it doesn't — and the team argues about what's genuinely unresolved instead of re-litigating what's settled.

## Why this skill exists

An investment thesis is really a small set of contested questions wearing a narrative. The narrative is what gets written down; the questions stay implicit — and implicit questions can't be updated, only re-argued. So the same disagreement about pricing power resurfaces at every IC touchpoint, framed slightly differently each time, with whoever read the most recent sell-side note holding the floor. Nobody can say whether the evidence has moved since last quarter, because nobody wrote down where it stood last quarter.

The failure compounds through how new information gets processed. Without a ledger, every data point is evaluated against the mood of the position: bulls file confirming points and explain away the rest, and a drip of individually minor confirmations hardens conviction without any single piece of evidence being examined. With a ledger, each data point has to land against a specific named question — and "this is relevant to none of our debates" becomes a legitimate, common, and clarifying answer that kills the noise trade of reacting to every headline.

The discipline that makes it work is deciding *in advance* what would move each debate. A resolver chosen before the data arrives is a commitment; one chosen after is a rationalization. Written down when the debate is opened, the resolver forces the honest question at every update — did the thing we said would change our mind happen? — and its absence is why "what would change your mind?" so often gets answered, in effect, with "nothing that has occurred so far."

## Inputs

**Required:**
- Either an existing debates ledger for the position, or the material to build the first version from — a thesis memo, an IC memo, or a written description of the position and why it's held

**Optional but high-value:**
- **The new material to file** — a filing excerpt, earnings transcript, sell-side note, expert call summary, channel work, or internal debate notes; this is what drives every update run
- The position's direction and rough sizing — a debate that decides a 6% position deserves a different resolution bar than one behind a 50bp starter
- Prior versions of the ledger, so shifts can be described against a baseline rather than asserted
- The catalyst calendar — upcoming prints, investor days, regulatory decisions — for grounding resolvers in real, dated events
- Who holds which side internally, if the team wants the ledger to track the human disagreement as well as the evidentiary one

**Missing-input behavior:** Building a first ledger from a thesis memo alone is a legitimate mode — extract the contested questions the memo glosses over, and mark each side's evidence as thin where the memo asserts rather than supports. Without new material, an update run has nothing to file; say so rather than re-summarizing the existing ledger as if it were news. Without prior ledger versions, describe current evidence but flag that shift detection has no baseline. Never fabricate a citation, a data point, or an evidence entry — a side of a debate with no real evidence is written as "no direct evidence currently; held on [reasoning]," which is itself information the team should see.

## How it works

1. **Establish or load the ledger.** From an existing ledger, load it as the baseline. From a thesis memo, extract the questions that would genuinely change the outcome if answered against you — not the ten things the memo discusses, but the two to four it actually turns on. A thesis that yields six or more "key" debates hasn't been distilled yet; force-rank by outcome impact and keep the top few.
2. **Test every debate for decidability.** Each one must be a question evidence can move — falsifiable, with observable resolution criteria. Rewrite vague worries into decidable form using the standard below; a debate that can't be rewritten is a sentiment, and it gets logged as background risk rather than occupying a ledger slot.
3. **State the current evidence on each side, cited.** Every entry carries its source, date, and the specific data point — "Q2 transcript, 8/5: management guided gross adds down 3% sequentially," not "management sounded cautious." Distinguish evidence from opinion: a sell-side analyst's conclusion is not evidence, though a datum inside their note may be. Price action is not evidence for either side of a fundamental debate.
4. **Pre-register the resolver for each debate:** the specific upcoming data point or event most likely to move or settle it, with its expected date and — where possible — what reading would count for which side. This is the line that keeps future updates honest, and it is written before the data arrives, not after.
5. **File new material against the ledger, debate by debate.** For each debate: does this material add evidence to the bull side, the bear side, or neither? Cite the specific data point that lands, not the document. "Neither" is a common and valuable verdict — record it once and move on.
6. **Flag meaningful shifts, and only meaningful ones.** A shift means the balance of evidence has moved — a pre-registered resolver resolved, a load-bearing data point reversed, an assumption broke — not that one more confirming item joined a pile. When flagging a shift, say what it implies for the debate and, at the position level, what question that raises. Distinguish "evidence accumulated on the existing lean" from "the lean should change."
7. **Screen for genuinely new debates.** Most candidate new debates are an existing debate in new clothing — a fresh anecdote about the same competitive question. Admit a new debate only if it could independently change the outcome and isn't reducible to one already on the ledger; if admitting it takes the count past four, something must merge or demote.
8. **Retire settled debates explicitly.** When a resolver has resolved, record the verdict and the evidence that settled it, and move the debate to the resolved log — still visible, so it cannot be quietly re-litigated in three months by someone who missed the settlement. If a settled debate re-opens, that requires new evidence, named.
9. **Restate the ledger clean.** End every run with the current two to four live debates, each with its lean, its confidence, and its next resolver dated — the one-page version a PM can read before the IC discussion.

## Output format

A skeleton to adapt — the per-debate block is the invariant part.

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# Key Debates Ledger — [ticker / issuer]
Position: [direction, rough size] | Thesis in one line: [ ]
Ledger updated: [date] | New material filed: [source, date / none]

## Live debates ([2–4])

### Debate 1: [decidable question, phrased so evidence can move it]
Why it decides the outcome: [one line — what breaks if answered against you]
| Side | Evidence | Source | Date |
|---|---|---|---|
| Bull | [specific data point] | [doc] | [ ] |
| Bear | [specific data point] | [doc] | [ ] |
Current lean: [bull / bear / genuinely open] — confidence: [low / med / high]
Resolver: [specific upcoming data point or event, expected date, and what
reading counts for which side]

### Debate 2: ...

## This update — where the new material landed
| Debate | Verdict | The data point that landed | Shift? |
|---|---|---|---|
[Verdict: BULL / BEAR / NEITHER. Shift flagged only when the balance moved.]

## Shifts flagged
[Each: which debate, what moved it, what it implies — or "none this update."]

## New debate screen
[Candidate raised by the material, and whether it was admitted, merged into
an existing debate, or declined — with reasoning. Or "none raised."]

## Resolved log
| Debate | Verdict | Settled by | Date |
|---|---|---|---|
```

## Decidable questions versus vague worries

A ledger slot is expensive — there are only four — and a vague worry occupying one produces circular meetings forever, because no evidence can ever move it. The test for every debate:

- **It's falsifiable.** Some observable outcome would count against each side. "Competition is a risk" fails — nothing that could happen next quarter settles it. "Will [entrant]'s launch take more than 200bps of share in [segment] by FY26?" passes: share data will arrive and land on one side.
- **Evidence can update it.** Named sources — filings, KPIs, transcripts, channel data — bear on it directly. "Is management good?" fails; "will management hit the [metric] target they guided without cutting [the investment line]?" updates every quarter.
- **It has a horizon.** A debate no evidence can touch for five years is a premise, not a debate; note it as one and spend the slots on questions the next four quarters can move.
- **Rewriting is the move, not deletion.** Behind most vague worries sits a real decidable question. "Margin sustainability" becomes "is the FY gross-margin bridge driven by mix (durable) or by the input-cost tailwind (reverting)?" The worry names a topic; the debate names the mechanism in dispute.

And the update discipline that keeps a good ledger honest: file the data point, not the document — one 10-Q may feed three debates and touch none. Never average the sides into a mushy midpoint; the lean can be "genuinely open," but each side's evidence stays intact and attributed. Weight resolution of a pre-registered resolver far above an unanticipated confirming anecdote — the first was a commitment, the second may be selection. And watch for confirmation drip: five minor data points on the same side, none individually flagged as a shift, deserve an explicit look at whether the pile is independent evidence or one narrative echoed five times.

## Guardrails

- **Every evidence entry is cited with source and date.** An uncited entry is an opinion wearing a table row, and it corrupts the ledger's whole claim to being an evidence record.
- **Never merge the sides.** Bull and bear evidence stay separately stated even when the lean is strong. Averaging a disagreement destroys exactly the information the ledger exists to preserve.
- **Resolvers are pre-registered, not retrofitted.** A resolver added after the data arrived is labeled as such. The skill never rewrites an old resolver to fit what happened.
- **"Neither" is a verdict, not a failure.** Material relevant to no debate is filed as such, once, without manufacturing relevance — the ledger is not a news log, and letting every headline in is how it dies.
- **Shifts are flagged conservatively and stated plainly.** Under-flagging hides drift; over-flagging trains the team to ignore flags. When a shift is real, say it directly — including when it runs against the position — and never soften "the balance has moved bear" into "worth monitoring."
- **Settled means settled in writing.** Re-opening a resolved debate requires new evidence, named. Re-litigation by amnesia is the specific disease this ledger treats.
- **No fabricated evidence, ever.** A thin side is reported thin. The gap between "we believe" and "we can cite" is the most useful thing the first version of a ledger reveals.
- **Not investment advice.** The ledger organizes what is known, contested, and pending on each question. Position decisions — size, direction, exit — belong to the PM and the IC, not to the ledger.
- **Confidentiality:** ledgers encode live positions, internal debate, and unpublished research. Assume a firm-approved AI environment, and flag rather than file anything in the source material that appears to be MNPI.

## Example prompts

> "Here's our debates ledger for [ticker] and the Q2 10-Q excerpt plus last night's earnings transcript: [attach]. File the new material — where does each data point land, did any balance actually shift, and did the resolver we pre-registered on the churn debate resolve?"

> "Build a first debates ledger from this thesis memo on [issuer]: [attach]. The memo is confident everywhere — extract the two to four questions it's actually betting on, be honest about which sides currently have real cited evidence versus assertion, and pre-register a resolver for each."

> "IC revisits [ticker] Thursday. Restate the ledger clean from these three prior versions: [attach] — what's settled since we opened the position, what's still genuinely open, what shifted over the period, and which resolver dates fall before our next scheduled review."

## Works well with

Run **thesis-red-team** when a ledger review shows the bear columns thinning suspiciously — an adversarial pass generates the disconfirming evidence the ledger then tracks. Chain **earnings-call-extractor** each quarter so the print arrives as structured data points ready to file, and use **expert-call-synthesis** when a debate needs channel evidence — its disagreements section maps almost one-to-one onto ledger debates.
