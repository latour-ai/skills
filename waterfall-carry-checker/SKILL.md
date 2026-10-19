---
name: waterfall-carry-checker
description: >-
  Independently recompute a fund's distribution waterfall and carried
  interest from raw cash flows and the LPA terms, then reconcile the result
  against the administrator's or internal model's calculation line by line —
  preferred return accrual, GP catch-up, tiered splits, European vs.
  deal-by-deal, and the current clawback position. For fund CFOs,
  controllers, fund accountants, and finance teams at private equity, private
  credit, real assets, and venture funds. Trigger on phrases like "check the
  waterfall," "recompute the carry," "does the admin's distribution
  calculation tie," "verify the preferred return," "what's our clawback
  position," "model the waterfall from the LPA," "review this distribution
  before it goes out," or when a user uploads fund cash flows, an LPA
  distribution section, or an administrator's waterfall schedule. Do NOT use
  for drafting the LP-facing distribution notice — that is an IR deliverable.
  Do NOT use for extracting side letter economics — use the
  side-letter-term-extractor skill. This is an independent check, not the
  fund's official calculation, and not tax or legal advice.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Waterfall Carry Checker

Recompute the waterfall from the raw cash flows and the LPA's own words, then compare against the calculation you were handed — and when the two disagree, trace exactly where they diverge: which investor, which tier, which assumption, and how many dollars. The point is two genuinely independent calculations that agree, rather than one calculation reviewed twice.

## Why this skill exists

The waterfall is the highest-stakes arithmetic in a fund. It determines what every LP receives and what the GP earns, it is governed by a document written by lawyers rather than modelers, and it typically lives in a single spreadsheet maintained by one person — checked against an administrator running their own version of the same spreadsheet, built from the same summary of terms. Two models built from the same abstract are not independent. When they disagree, the reconciliation is a week of archaeology conducted after someone has already asked when the wire is going out. This rebuilds the calculation from the primary sources and localizes any difference to a line, before the wire, not after.

## Inputs

**Required:**
- The complete cash flow history: capital calls and distributions by date and by investor (or at minimum by class, if LP-level detail is unavailable)
- The LPA's distribution and carried interest provisions, plus the relevant defined terms — verbatim, not a summary
- The calculation being checked: the administrator's waterfall schedule, or the internal model's output, for the distribution in question

**Optional but high-value:**
- Side letters affecting economics — fee discounts, reduced carry, most-favored-nation elections, special allocations
- The fund's investor register with commitment amounts and admission dates (essential if there were subsequent closings)
- Prior distribution waterfalls, so the running pref and catch-up balances can be verified rather than assumed
- Current portfolio carrying values, for the clawback assessment
- Whether the fund uses a subscription line, and how call dates relate to it

**Missing-input behavior:** All three required inputs are genuinely required — a waterfall cannot be recomputed from a summary of terms, and comparing against nothing is not a check. Ask once, specifically, for whichever is missing. If LP-level cash flows are unavailable but aggregate flows are, run the check at the aggregate level and label the output clearly as an aggregate check that cannot detect investor-level allocation errors. If the LPA text is paraphrased rather than quoted, say that the check is only as good as the paraphrase and ask for the actual sections.

## How it works

1. **Restate the waterfall in mechanical terms before computing anything.** Read the LPA provisions and write out the tier structure as an explicit sequence of steps: return of capital (of what — contributions for the investment only, or all contributions including fees and expenses?), preferred return, GP catch-up, residual split. Get the user's confirmation on any ambiguity **before** running numbers. Most waterfall disputes are definitional, not arithmetic.
2. **Fix the convention questions explicitly.** Compounding frequency, simple vs. compounded pref, day count, whether pref accrues on unreturned capital or on all contributions, whether fees and expenses earn pref, catch-up percentage and what it catches up on, European (whole-fund) vs. deal-by-deal, and the treatment of recycled capital. List each convention and cite the LPA section that establishes it. Where the LPA is silent, say so and state the convention you applied.
3. **Build the pref accrual schedule** from the cash flow history, by investor, period by period, from first close to the distribution date. Show the running balance.
4. **Run the distribution through the tiers,** allocating the distributed amount step by step and showing the balance remaining after each tier.
5. **Compute the GP catch-up and carried interest,** noting whether the catch-up is full (100/0) or partial (e.g. 80/20 or 50/50) and what base it is measured against.
6. **Reconcile line by line against the provided calculation.** For every line that differs, isolate the cause: a different pref convention, a different treatment of a specific cash flow, an investor admitted at a subsequent closing, a side letter term, a date or day-count difference, or an arithmetic error. Quantify the dollar impact of each cause.
7. **Compute the clawback position** — carry received to date versus carry that would be due if the fund were liquidated at current carrying value today, net of the LPA's tax-distribution and escrow provisions. Flag if the position is negative.
8. **Write the memo** for the distribution approval file.

## Output format

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# [Fund] — Waterfall Check, [Distribution Date] Distribution of $[amount]
Sources: [cash flow file] | [LPA §§] | [calculation being checked, version/date]
Level of check: [investor-level / aggregate] | Structure: [European / deal-by-deal]

## Bottom line
Agree / Disagree. If disagree: the number of differences, the largest one in
dollars, and whether it changes any investor's distribution or the GP's carry.

## Waterfall as restated from the LPA
Tier 1: [description] [§]
Tier 2: [description] [§]
Tier 3: [description] [§]
Tier 4: [description] [§]

## Conventions applied
| Convention | Applied | LPA basis | Note |
|---|---|---|---|
| Pref rate | | [§] | |
| Compounding | | [§] | |
| Pref base | | [§] | |
| Day count | | [§] | |
| Catch-up % / base | | [§] | |
| Recycling treatment | | [§] | |
[Mark any convention where the LPA is silent or ambiguous.]

## Independent recomputation
### Preferred return accrual
| Investor | Contributions | Unreturned capital | Pref accrued | Pref paid | Pref balance |
|---|---|---|---|---|---|

### Tier allocation of this distribution
| Tier | Amount allocated | Cumulative | Remaining |
|---|---|---|---|

### Carried interest
GP catch-up: $[ ] | Carry this distribution: $[ ] | Cumulative carry: $[ ]

## Reconciliation to [administrator / internal model]
| Line | Our figure | Their figure | Difference | Cause |
|---|---|---|---|---|
[One row per differing line. Cause must be specific — a mechanism, not "rounding"
unless the difference is genuinely sub-dollar.]

Total difference: $[ ] | Investors affected: [list or count]

## Clawback position (as of [date], at carrying value)
Carry received to date: $[ ]
Carry due on hypothetical liquidation: $[ ]
Clawback exposure: $[ ] | Escrow held: $[ ] | Net: $[ ]
Sensitivity: exposure at [-10%] / [-25%] carrying value: $[ ] / $[ ]

## Items requiring a human decision
Numbered. Ambiguous LPA language, side letter interactions, or conventions
the document does not settle.
```

## Where waterfalls actually break

The differences are almost never arithmetic. In order of how often they cause a reconciliation break:

- **Pref base** — accrued on unreturned capital only, or on all contributions including management fees and fund expenses? These diverge substantially over a fund's life.
- **Compounding convention** — annual vs. quarterly, simple vs. compounded, and whether compounding starts at contribution date or period end. A 8% pref compounded quarterly is not an 8% pref.
- **Day count** — 30/360 vs. actual/365, and whether the accrual runs to the distribution date or the period end.
- **Subsequent closings** — true-up interest paid by later investors, and whether equalization amounts are treated as contributions (earning pref) or as income.
- **Catch-up base** — does the GP catch up on the preferred return only, or on the pref *and* the returned capital? The second is far more GP-favorable and both appear in market documents.
- **Recycled capital** — recallable distributions that reduce unreturned capital, increase it again on recall, and may or may not restart pref.
- **Subscription line effects** — capital called late because the line funded the investment. Pref usually accrues from the call date, which means line usage suppresses the pref clock; confirm whether the LPA has a deemed-contribution provision.
- **Deal-by-deal loss carryforwards** — in American waterfalls, whether prior realized losses and write-downs must be recovered before carry is paid on the next exit.
- **Side letters** — reduced carry, fee offsets, or bespoke pref rates for specific LPs that the standard model does not carry.
- **Tax distributions** — treated as advances against future carry or as a separate tier, and whether they count toward the clawback calculation.
- **Excused and defaulting investors** — excluded from specific investments, which breaks the assumption that every LP shares pro rata.
- **Management fee offsets** — transaction and monitoring fee credits reducing the fee, changing contributions, and therefore changing pref.

## Guardrails

- **Recompute from primary sources.** The check is only independent if it is built from the raw cash flows and the LPA's own language, never from the administrator's summary of terms or a prior model's assumptions. If you find yourself adopting an input from the calculation being checked, say so explicitly — that line is no longer independently verified.
- **Every convention cites an LPA section.** Where the LPA is silent or ambiguous, do not pick a convention silently: state the ambiguity, state which reading you applied, and quantify what the other reading would produce.
- **Never fabricate a cash flow.** If the history has gaps, the recomputation stops there. A waterfall built on inferred cash flows is worse than no check.
- **Differences get a mechanism, not a shrug.** "Rounding" is only acceptable for genuinely sub-dollar differences. Every material difference is traced to a specific cause or explicitly labeled unexplained.
- **This is a check, not the fund's calculation.** The LPA governs, the administrator's books are the record, and this output is a review workpaper — not a distribution instruction, not an accounting opinion, and not a basis for a wire.
- **Not tax or legal advice.** Clawback, tax distribution, and allocation questions have tax and legal consequences that belong with the fund's counsel and tax advisors.
- **Confidentiality:** LP-level cash flow data is highly sensitive. Assume a firm-approved AI environment; do not reproduce investor names or amounts beyond what the check requires.

## Example prompts

> "Attached: the fund's full call and distribution history by LP, the LPA distribution sections, and the administrator's waterfall for the $42M distribution scheduled for the 15th. Recompute it independently and tell me whether it ties. We're European, 8% pref, 100% catch-up."

> "Our controller and the admin are $310k apart on the carry for this quarter's distribution and nobody can find it. Here are both schedules, the cash flows, and the LPA. Where do they diverge?"

> "Year-end clawback assessment. Cash flows and carrying values attached, LPA sections pasted below. What's our exposure if the portfolio marks are right, and if they're 25% too high?"

## Works well with

Use **side-letter-term-extractor** first if the fund has LP-specific economics that need to be reflected in the waterfall. Pair with **lp-update-generator** once the distribution is approved and the LP-facing communication is being written.
