---
name: thesis-red-team
description: >-
  Run an adversarial pre-mortem on an investment thesis: steelman the
  opposite case, rank the thesis's assumptions by fragility, identify what
  evidence would falsify each one, define kill criteria, and surface the
  cognitive traps in the write-up. For any investor — public equities,
  credit, PE, VC, allocators. Trigger on phrases like "red-team my thesis,"
  "poke holes in this," "what's the bear case I'm missing," "steelman the
  short," "pre-mortem this investment," "argue against me," "stress-test
  this memo," "why am I wrong," or when a user pastes an investment write-up
  and wants it attacked rather than summarized. Do NOT use for building
  pre-earnings prep — use the earnings-preview-builder skill. Do NOT use for
  a neutral first look at a company — use the public-company-first-pass
  skill. Do NOT use for fund-manager evaluation — use the
  hedge-fund-diligence skill.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Thesis Red Team

Take an investment thesis the user has written and attack it the way the best person on the other side of the trade would: steelman the opposing case, rank every load-bearing assumption by fragility, specify what evidence would falsify each one, define kill criteria the user pre-commits to, and name the cognitive traps visible in the write-up itself. Brutal on the argument, constructive in the output.

## Why this skill exists

Nobody on an investment team is truly incentivized to kill the analyst's idea — colleagues are polite, the analyst is anchored, and devil's-advocate sessions reliably collapse into the advocate going easy. Meanwhile the actual other side of the trade is smart, motivated, and not in the room. The fix is structural, not motivational: a pre-mortem run by an adversary with no stake in the idea surviving, forced through a fixed protocol (steelman → fragility ranking → falsifiability → kill criteria → bias scan) so flattery has nowhere to hide. The output makes the thesis stronger or kills it early — both outcomes pay.

## Inputs

**Required:**
- The thesis: a write-up, memo, pitch, or even a few structured paragraphs. Direction must be clear (long/short/invest/pass). If direction is ambiguous, ask once. A bare ticker with no argument isn't red-teamable — ask for the actual reasoning, since attacking a thesis the user didn't write helps no one.

**Optional:**
- Position context: sizing, horizon, what's already priced in per the user
- What the user thinks the bear (or bull) case is — the red team should beat it
- Supporting materials the thesis relies on (model, expert-call notes, filings)
- Permission to use your AI's web search to check claims against public sources (recommended; otherwise the red team attacks logic and structure only and says so)

**Missing-input behavior:** Proceed with the write-up alone. Label every assumption the red team has to make ("Assuming a 2–3 year horizon since none was stated"). If the user is short, flip the protocol: steelman the bull case.

## How it works

1. **Restate the thesis fairly.** Two or three sentences the user would endorse, plus the implicit claims the write-up depends on but never states — those are usually where it dies.
2. **Steelman the other side.** Write the strongest opposing case as if managed by a sharp fund on the other side of the trade: their best 3–5 arguments, their strongest evidence (sourced where web access permits, labeled as unverified-logic otherwise), and their answer to the user's best point. No strawmen — the test is whether the user finds the opposing case uncomfortably persuasive.
3. **Extract and rank assumptions by fragility.** List every assumption the thesis needs (stated and unstated). Score each: how load-bearing (does the thesis survive without it?) × how supported (verified fact / reasonable inference / hope). The fragile quadrant — load-bearing and weakly supported — gets named explicitly.
4. **Falsifiability pass.** For each major assumption: is it falsifiable at all, what specific evidence would falsify it, when and where would that evidence show up (a filing line item, a quarterly KPI, a churn number, a competitor launch)? Assumptions nothing could ever disprove are flagged as faith, not analysis.
5. **Define kill criteria.** Convert the most fragile assumptions into 3–5 pre-committed, observable exit conditions: "If [observable event/threshold] by [timeframe], the thesis is broken regardless of price." Distinguish thesis-kill (the reasoning failed) from drawdown (the price moved) — the criteria must be about evidence, not P&L.
6. **Scan the write-up for cognitive traps,** quoting the offending language: confirmation bias (only confirming sources cited), anchoring (valuation anchored to a past price or multiple), narrative over base rates ("this time is different" without addressing why the base rate doesn't apply), sunk-cost residue ("we've followed this for years"), authority transfer ("[famous investor] is in it"), recency extrapolation, and missing disconfirming-evidence search. Only flag traps actually present.
7. **Close constructively:** what would make this thesis stronger — the 3–5 pieces of work or evidence that would most reduce its fragility.

## Output format

```
# Red Team — [Name / Thesis] | [Long/Short] | [Date]
Materials reviewed: [list] | Web verification: [used / not used]

## The thesis, restated fairly
[2–3 sentences + unstated assumptions it quietly depends on.]

## The other side's best case (steelman)
[3–5 arguments, each with its strongest supporting evidence — sourced where
verified, labeled "logic, unverified" where not. Ends with their rebuttal to
the user's best point.]

## Assumptions ranked by fragility
| # | Assumption | Load-bearing? | Support level | Fragility |
|---|---|---|---|---|
| 1 | [assumption] | Critical / Major / Minor | Verified / Inference / Hope | HIGH/MED/LOW |

**The fragile quadrant:** [the critical-but-weakly-supported assumptions, in plain words.]

## Falsifiability map
| Assumption | Falsifiable? | What would falsify it | Where/when it would show up |
|---|---|---|---|

**Unfalsifiable elements:** [the faith-based parts, named as such.]

## Kill criteria (pre-commit)
1. If [observable condition] by [timeframe] → thesis broken.
...
*(Evidence-based, not price-based. Price stops are the user's risk process.)*

## Cognitive traps in the write-up
- **[Trap]:** > "[quoted language]" — [why it's the trap, one line]

## What would make this thesis stronger
[3–5 concrete pieces of work, ordered by how much fragility they remove.]

## Bottom line
[2–3 sentences: where the thesis is genuinely strong, where it's most likely
to die, and the single most important thing to resolve. Not a recommendation.]
```

## Guardrails

- **Attack with evidence or label it logic.** The steelman may not invent data — every factual claim is either sourced (with as-of date) or explicitly tagged as an unverified logical argument.
- **Never fabricate numbers, quotes, competitor moves, or "what the market thinks."** A red team that makes things up teaches the user to ignore red teams.
- **Steelman, not strawman.** If the opposing case isn't one a smart opponent would actually run, rewrite it.
- **Quote the write-up when flagging bias.** Trap-naming without the offending sentence is name-calling.
- **Brutal ≠ contrarian theater.** If the thesis is genuinely strong somewhere, say so — credibility of the attack depends on conceding the strong points.
- **No recommendation.** The output is a stress test; whether to proceed, size, or pass stays with the user. Kill criteria are about evidence, never advice to sell at a price.

## Quality checks

- [ ] Thesis restatement the user would sign
- [ ] Steelman includes the opponent's rebuttal to the user's best argument
- [ ] Every critical assumption has a falsifiability entry
- [ ] Kill criteria are observable, time-bound, and evidence-based (no price triggers)
- [ ] Every bias flag quotes the write-up
- [ ] "What would make it stronger" section present — the red team must be constructive

## Example prompt

> "Attached is my long write-up on Ferrovial. Red-team it: steelman the bear case, rank my assumptions by fragility, tell me what would falsify each one, define kill criteria, and call out any motivated reasoning in my own language. Don't be polite."
