---
name: credit-agreement-covenant-extractor
description: >-
  Extract the complete covenant package from a credit agreement, indenture,
  or term sheet into a page-cited structured abstract — financial covenants
  and step-downs, negative covenant baskets, the full EBITDA definition with
  every add-back, and change-of-control and prepayment terms — then flag
  off-market or borrower-friendly provisions against standard formulations.
  For private credit and direct lending teams, leveraged finance analysts,
  distressed and special situations investors, and CLO managers. Trigger on
  phrases like "extract the covenants," "what are the covenants in this
  credit agreement," "read this indenture," "abstract this loan agreement,"
  "what's the EBITDA definition," "how much RP capacity do they have," "is
  this doc off-market," "build a key terms sheet," or when the user uploads a
  credit agreement, indenture, note purchase agreement, unitranche facility,
  or term sheet. Do NOT use for checking a quarterly compliance certificate
  against terms already extracted — that is ongoing monitoring. Do NOT use
  for screening an M&A target's CIM — use the cim-first-pass skill. Do NOT
  use for a hedge fund side letter — use the side-letter-term-extractor
  skill. This is a document abstract, not legal advice.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Credit Agreement Covenant Extractor

Turn a 200-page credit agreement into a covenant abstract a credit analyst can work from: every financial covenant with its definition and step-downs, every negative covenant basket with its size and conditions, the full EBITDA definition with each add-back itemized, and a flag on every provision that is looser than market. Every extracted term carries a page or section citation, so the output is checkable rather than trustable.

## Why this skill exists

The terms that hurt a lender show up years later, and they are almost never in the covenant section. They are in the defined terms: an uncapped run-rate synergy add-back that makes the leverage test meaningless, an unrestricted-subsidiary provision that lets the sponsor move the crown-jewel IP outside the credit group, a builder basket that grows off the same inflated EBITDA. Reading for those requires chasing cross-references through a document written to make them hard to find, and it takes days. This does the extraction pass systematically so the human spends their time on the three provisions that actually matter, and so the abstract the monitoring team relies on for the life of the loan is built from the document rather than from someone's recollection of the deal.

## Inputs

**Required:**
- The credit agreement, indenture, note purchase agreement, or term sheet (uploaded file or pasted text). Amendments and the first-lien/second-lien intercreditor should be included if they exist.

**Optional but high-value:**
- Deal type and market context: broadly syndicated, middle-market unitranche, club deal, high-yield indenture — this determines what "market" means for the off-market flags
- The lender presentation or model, to compare covenant headroom against the projected case
- Your firm's house positions or prior precedent docs from the same sponsor
- Which specific provisions the user already cares about

**Missing-input behavior:** Without a document there is nothing to extract — ask once. If deal type is not stated, infer it from the document's own features (agent bank vs. direct lender, presence of a maintenance covenant, tranche structure) and **state the inference explicitly** at the top of the output, since every off-market judgment depends on it. If the document is clearly partial — exhibits or schedules missing, defined terms referenced but not included — say which sections are absent and mark the affected extractions incomplete rather than guessing.

## How it works

1. **Identify the document and the parties.** Borrower, holdco/opco structure, agent, facility types and sizes, maturity dates, pricing grid, and whether this is amended-and-restated (if so, note which amendment you are reading).
2. **Chase the defined terms first.** Before extracting any covenant, pull the definitions it depends on: EBITDA/Consolidated EBITDA, Indebtedness, Consolidated Total Debt (and whether cash netting is capped), Restricted Subsidiary, Unrestricted Subsidiary, Permitted Investments, Available Amount/Builder Basket, Material Subsidiary. A covenant is only as strong as the terms it is written in.
3. **Extract financial covenants.** For each: the ratio, its full formula, testing frequency, first test date, step-down schedule with dates, equity cure rights (how many, how often, whether cure proceeds count as EBITDA or debt reduction, whether over-cure is permitted), and whether the covenant is maintenance or incurrence. For revolver-only springing covenants, note the utilization trigger.
4. **Itemize the EBITDA definition in full.** Every add-back, separately listed, with: whether it is capped (and the cap's basis — % of EBITDA, dollar, or uncapped), whether there is a look-forward period for synergies and cost savings, whether "run-rate" or "annualized" appears, and whether add-backs are subject to a single overall cap. This section is usually the single most important output.
5. **Extract negative covenants and size every basket.** Restricted payments, debt incurrence (including free-and-clear/incremental capacity, ratio-based incurrence, and MFN protection with any sunset), investments, liens, asset sales and reinvestment rights, affiliate transactions, restricted/unrestricted subsidiary designation rights. For each basket, give the fixed dollar amount, the grower component if any (usually % of total assets or EBITDA), and the conditions to use it.
6. **Extract prepayment and control terms.** Mandatory prepayments (excess cash flow sweep and its step-downs, asset sale and debt issuance sweeps, reinvestment periods), call protection and soft-call, change of control definition and whether the deal is portable, and any anti-net-short or disqualified-lender provisions.
7. **Run the off-market flag pass** using the checklist below, judged against the stated or inferred deal type.
8. **Compute headroom where the inputs allow it,** labeling every derived figure and showing the arithmetic. If current financials were not provided, say so rather than estimating.
9. **Write the one-page key terms abstract** the monitoring team will use going forward.

## Output format

```
# [Borrower] — Credit Agreement Abstract
Document: [title, date, amendment no.] | Facility: [type, size, maturity]
Deal type assumed: [BSL / MM unitranche / club / HY indenture] — [stated by user / inferred from X]
Sections not provided: [list, or "none"]

## Headline read (one paragraph)
Cov-lite or maintenance? How much real protection does this document give a lender,
and the 2–3 provisions that drive that answer.

## Financial Covenants
| Covenant | Formula | Frequency | Opening level | Step-downs | First test | § |
|---|---|---|---|---|---|---|
Equity cure: [count / frequency / mechanics / over-cure] [§]
Springing trigger (if revolver-only): [utilization %] [§]

## EBITDA Definition — Add-Back Inventory
| # | Add-back | Capped? | Cap basis | Look-forward | § |
|---|---|---|---|---|---|
Overall cap on add-backs: [yes/no, size] [§]
Assessment: [how much reported EBITDA could plausibly be adjusted, and on what]

## Negative Covenants & Basket Capacity
| Covenant | Fixed basket | Grower | Conditions to use | § |
|---|---|---|---|---|
Restricted payments | | | |
Debt incurrence (free-and-clear) | | | |
Ratio debt | | | |
Investments | | | |
Liens | | | |
Asset sales / reinvestment | | | |
Unrestricted subsidiary designation | | | |
Available amount / builder basket: [starting balance, build formula, conditions] [§]
MFN: [spread, scope, sunset] [§]

## Prepayment, Call Protection & Change of Control
ECF sweep: [%, step-downs, deductions] [§]
Asset sale sweep / reinvestment period: [§]
Call protection: [§]
Change of control: [definition, portability] [§]

## Off-Market / Borrower-Friendly Flags
Ranked. Each: the provision, quoted or cited [§], the standard formulation it
departs from, and one sentence on the exposure it creates.

## Headroom (only if financials provided)
| Test | Covenant level | Current | Headroom | EBITDA decline to breach |
|---|---|---|---|---|
[All figures derived — inputs shown]

## One-Page Key Terms Abstract
[The standing reference for the monitoring team: facility, pricing, maturity,
covenants and levels, reporting obligations and due dates, key baskets,
change of control, and the three provisions to watch.]

## Open questions for counsel / the agent
Numbered, ordered by how much they'd change the credit view.
```

## Off-market provision checklist

Apply as hypotheses to test against the stated deal type, not as automatic findings. Each is standard in some markets and aggressive in others.

- **Uncapped run-rate synergies** with no look-forward limit, or a look-forward beyond 24 months → the leverage test can be satisfied with cost savings that never arrive
- **No overall cap on add-backs** → the individual caps are decorative
- **Uncapped cash netting** in Consolidated Total Debt → leverage can be managed with drawn revolver proceeds sitting on the balance sheet
- **Unrestricted subsidiary designation with a permissive investment basket** → the trapdoor; assets can leave the credit group (the J.Crew pattern)
- **Permissive lien subordination or non-pro-rata debt exchange rights** → your position can be primed by a majority group (the Serta pattern); check the sacred rights and voting provisions
- **MFN with a sunset** (6 or 12 months) or narrow scope (term loans only, excluding incremental equivalent debt) → pricing protection expires
- **Grower baskets** on the greater of a dollar amount and a % of EBITDA or total assets → capacity expands with the same EBITDA the add-backs inflate
- **Builder/available-amount basket starting above zero** or building off CNI with generous inclusions
- **Unlimited restricted payments subject only to a pro forma leverage test** set close to opening leverage
- **Portable change of control** → the sponsor can sell without repaying you
- **Equity cure with no frequency limit,** cure proceeds added to EBITDA rather than applied to debt, or over-cure permitted
- **ECF sweep starting at 50% with early step-downs** to 25%/0%, plus deductions for voluntary prepayments and permitted investments
- **Springing revolver covenant** with a high utilization trigger (35%+) and a level set well outside the projected case → nominal protection only
- **Long reinvestment periods** (12–18 months plus extension) on asset sale proceeds
- **Reporting: no lender calls, no borrower-provided compliance certificate detail,** or financial delivery deadlines beyond 120 days for annuals

## Guardrails

- **Every extracted term carries a section or page citation.** No term without a locator. If the citation is uncertain because of PDF extraction quality, say so and flag it for manual verification.
- **Quote defined-term language verbatim** where the exact words matter — especially EBITDA add-backs, the unrestricted subsidiary definition, and any sacred-rights provision. No paraphrase inside quotation marks.
- **Never reconstruct a provision from what is typical.** If a section was not provided or is illegible, mark it "not provided" — an assumed covenant is worse than an acknowledged gap.
- **Derived figures are labeled and shown.** Headroom, implied leverage, and basket capacity in dollars are computed, not extracted; show the inputs and arithmetic every time.
- **"Off-market" is a benchmark comparison, not a legal conclusion.** State the standard formulation you are comparing against, and note that market conventions vary by vintage, size, and sponsor.
- **This is not legal advice** and does not replace counsel's review, a formal covenant analysis, or the credit agreement itself, which governs. Complex intercreditor, lien subordination, and structural subordination questions belong with a lawyer.
- **Confidentiality:** private credit documents are confidential and often NDA-covered. This skill assumes a firm-approved AI environment. Do not reproduce large verbatim sections of the agreement in the output.

## Quality checks

- [ ] Deal type stated or inferred, with the inference labeled
- [ ] Every covenant, basket, and add-back has a section citation
- [ ] EBITDA add-backs itemized individually — not summarized as "customary add-backs"
- [ ] Cap status recorded for every add-back, including "uncapped"
- [ ] Unrestricted subsidiary and lien subordination provisions addressed explicitly, even if standard
- [ ] Every basket shows fixed amount *and* grower component
- [ ] Off-market flags each name the standard formulation being compared against
- [ ] Derived figures labeled and arithmetic shown
- [ ] Missing sections listed rather than silently skipped
- [ ] The one-page abstract is usable standalone by someone who never sees the full output

## Example prompts

> "Attached is the credit agreement for a middle-market unitranche we're being shown — $180M facility, sponsor-backed healthcare services. Extract the full covenant package. I mainly want to know how much of the EBITDA definition is real and whether there's a trapdoor."

> "Here's an amended-and-restated credit agreement plus Amendment No. 3. Build the key terms abstract for our monitoring file, and tell me what Amendment No. 3 actually loosened."

> "Broadly syndicated TLB, sponsor is [X]. Read the doc and flag anything off-market versus what we'd expect for a 2024-vintage BSL. Skip the pricing grid, I have it."

## Works well with

Run **cim-first-pass** on the sponsor's marketing materials to compare the business narrative against what the document actually permits. Use **thesis-red-team** on the resulting credit view once the abstract is built.
