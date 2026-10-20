---
name: coinvest-triage-memo
description: >-
  Produce the rapid evaluation memo when a GP offers a co-investment on a
  short fuse: a plain-English deal summary from the GP's materials, the
  adverse-selection analysis of why the GP is syndicating this particular
  deal, fit against the program's co-invest criteria, concentration
  impact on the existing co-invest book, an expedited red-flag scan of
  the company and terms, and a participate/pass recommendation with the
  key questions for the GP call — every claim labeled verified,
  GP-asserted, or inferred, because a two-week process cannot verify much
  and should be honest about it. For allocators, fund-of-funds, OCIOs,
  endowments, foundations, and family offices running co-invest
  programs. Trigger on phrases like "co-invest triage," "GP just offered
  us a co-investment," "two weeks to decide on this deal," "should we
  take this co-invest," "triage this allocation," or when a user uploads
  GP co-investment materials with a decision deadline. Do NOT use for
  screening a CIM as a direct buyer — use the cim-first-pass skill. Do
  NOT use for diligence on the GP's fund itself — use the
  hedge-fund-diligence skill. This is triage under time pressure, not
  full diligence, and it is not investment advice.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Coinvest Triage Memo

A co-investment offer arrives with a deck, a model output, and a deadline chosen by someone else — and the deadline is the point. Two weeks is enough time to feel diligent and not enough to be diligent, so the realistic choice is between a rushed yes, a reflexive no, and a disciplined triage that spends the available days on the two or three questions that actually decide it. This skill produces that triage in hours: what the deal is, why the GP is showing it to you, whether it fits your program, what it does to your book, what the expedited scan turns up, and a participate/pass with the GP-call questions — every claim labeled by whether it was verified, asserted by the GP, or inferred.

## Why this skill exists

The central analytical problem in co-investment is adverse selection, and it hides in plain sight because the offer is flattering. The GP has capital; they chose to share this deal. The benign reasons are real — equity check exceeds concentration limits, LP relationship building, a fund between vintages — but so are the malignant ones: the deal is bigger than conviction, the GP wants risk off their fund's book, or better-informed co-investors already passed and you are further down the list than you think. Which explanation is true is knowable, roughly, from observable facts — check size versus fund size, where the fund is in its life, how broadly the deal is being shown, whether the GP's own money is increasing or being diluted — but only if someone assembles those facts and asks. Under deadline pressure, nobody asks; the deck gets read instead.

The second problem is that time pressure inverts the natural order of work. Instincts say start with the business — read the deck, understand the company — because that is how normal diligence begins. But the deck is the GP's argument, and days spent absorbing it are days spent inside the seller's frame. Triage runs the other way: disqualifiers first. Program fit, concentration, structural terms, and the adverse-selection read can each kill the deal in an afternoon from materials on hand; the business itself is evaluated only if the deal survives them. A pass on day three is a good outcome — it returns the calendar.

The third problem is epistemic laundering. A two-week memo is built almost entirely from the GP's own materials, and by page four, "the company's revenue grew 40%" has quietly stopped being "the deck asserts 40% growth." When everything is written in the voice of fact, the IC cannot tell what was checked from what was copied — so this memo labels every material claim, and treats the labeling as the honesty mechanism that makes speed defensible at all.

## Inputs

**Required:**
- The GP's co-investment materials — deck, deal summary, model output, whatever was provided
- The GP, the company, and the decision deadline
- **The program's co-invest criteria** — check size range, relationship requirements, sector and deal-type exclusions, concentration limits. Fit is the fastest kill test and it cannot run without them.

**Optional but high-value:**
- **The current co-invest book** — positions, sectors, vintages, GP exposure — without it the concentration section is skipped, and concentration is a common silent killer
- The fund relationship context: which of the GP's funds you hold, its vintage, remaining dry powder, and how this deal sits in it
- The proposed structure and terms: fees and carry on the co-invest, governance rights, information rights, transfer restrictions, follow-on obligations
- How the opportunity arrived and who else is being shown it
- Prior co-invest history with this GP, including how the last one was allocated and how it performed
- Any independent material on the company — news, filings, prior research in your own archive

**Missing-input behavior:** Triage runs on whatever exists — that is its nature — but every skipped section is named as skipped, not silently absent. No criteria: the fit section becomes the questions to resolve about fit, labeled accordingly. No book data: concentration is flagged as unassessed and listed as a pre-decision requirement. And the skill never fills gaps from the deck's own framing: if the GP's materials are the only source on a point, the point is labeled GP-asserted no matter how plausible it reads.

## How it works

1. **Fix the clock first.** Deadline, days remaining, and what can realistically be verified in them — which determines what the memo can honestly claim and what must be labeled as unverified regardless of how important it is. State this in the header; it frames every judgment after it.
2. **Summarize the deal in plain English, sourced:** business, deal structure, entry valuation and multiple, leverage, the GP's stated thesis, and proposed co-invest terms. Every number tagged to its source — this pass builds the verified/GP-asserted/inferred discipline into the memo's foundation before any analysis begins.
3. **Run the kill tests before the business.** Program fit line by line against each criterion; structural terms (economics, governance, transfer, follow-on obligations); concentration against the book. A clean kill here ends the triage honestly — recommend pass, note what would have come next, stop.
4. **Work the adverse-selection question with observable facts,** not vibes: equity check versus fund size and typical hold, fund vintage and dry powder, the GP's own commitment to this deal relative to pattern, breadth of syndication, and how the opportunity reached you. Conclude with the most plausible reason this deal is being shared — and say directly whether that reason concerns you.
5. **Check GP-LP alignment on this specific deal:** co-invest economics versus fund economics, whether the GP earns fees on your co-invest capital, cross-fund issues, and who controls exit timing. A no-fee co-invest and a fee-bearing SMA-style allocation are different propositions wearing the same deck.
6. **Run the expedited red-flag scan of the company** — now, having survived the kills: customer concentration, revenue quality and adjustments, unit economics direction, leverage versus cyclicality, management turnover, pending litigation or regulatory exposure visible in the materials or public record. Depth is bounded by the clock; the scan says what it could not reach.
7. **Pressure-test the GP's case at its load-bearing points.** Identify the two or three assumptions the returns actually depend on — the multiple at exit, the growth bridge, the synergy or margin claim — and assess each for plausibility against whatever independent reference exists. Do not re-underwrite the deal; name what would have to be true.
8. **Size the decision:** proposed check against program limits, portfolio impact if the deal goes to zero, and what participation does to remaining capacity for this GP and this sector.
9. **Write the participate/pass recommendation with its confidence honestly stated** — including, where right, "participate subject to" specific verifications or "pass on process, not on the asset" when the timeline itself is the disqualifier. A recommendation that hides its uncertainty defeats the labeling discipline everywhere else.
10. **Draft the GP call questions,** ordered by decision-weight: the questions whose answers would change the recommendation, then the verifications, then the housekeeping. Note beside each what a concerning answer sounds like.

## Output format

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# Co-invest Triage — [company], offered by [GP]
Deadline: [date] ([N] days) | Check: [proposed] | Decision: [PARTICIPATE / PASS / PARTICIPATE SUBJECT TO]
Basis: [what was verified vs. taken from GP materials — one line]

## Deal summary
[Business, structure, entry valuation, leverage, GP thesis, co-invest
terms — each material figure tagged: (V) verified / (G) GP-asserted / (I) inferred]

## Kill tests
| Criterion | Program requirement | This deal | Pass/Fail/Unknown |
|---|---|---|---|
Structural terms: [economics, governance, transfer, follow-ons — issues flagged]
Concentration: [impact on book / UNASSESSED — book not provided]

## Why is the GP showing us this?
Observable facts: [check vs. fund size, vintage, GP commitment, syndication breadth, path to us]
Most plausible explanation: [ ] | Concerning? [ ]

## Alignment on this deal
[Fees/carry on co-invest capital, cross-fund issues, exit control]

## Expedited red-flag scan
| Area | Finding | Source | Label |
|---|---|---|---|
Not reached in available time: [ ]

## Load-bearing assumptions
| Assumption | GP's case | Independent reference | Plausibility |
|---|---|---|---|

## Recommendation
[Participate / pass / participate subject to — with confidence stated and
the two or three considerations that actually drove it.]

## GP call questions
| # | Question | Why it matters | A concerning answer sounds like |
|---|---|---|---|
```

## The adverse-selection decoder

The question is never whether the GP has a reason to syndicate — they always do. The question is which reason, and the observable facts usually say:

- **Check size vs. fund size** — an equity check above the fund's concentration limit is the benign explanation and it is checkable arithmetic. A deal the fund could comfortably hold alone, syndicated anyway, needs a different explanation.
- **Fund vintage and dry powder** — late-vintage deals from a nearly deployed fund raise reserve questions; a deal shown while fundraising is partly a marketing artifact, which does not make it bad, but prices the flattery at zero.
- **The GP's own money** — is the GP's commitment to this deal, through the fund and any GP commitment, at or above their pattern? A GP reducing their own relative exposure while inviting yours is the single loudest observable.
- **Syndication breadth and your place in line** — a deal shown narrowly to top relationships differs from one shopped widely, and a deal that reaches you late may have been passed on by co-investors with better information. Ask how long the process has run and who saw it first; the answer is usually obtainable and rarely volunteered.
- **Fee structure as signal** — no-fee/no-carry co-invest is relationship currency; fee-bearing co-invest is a product. Products are sold; currency is spent on people the GP wants more from. Both are fine, but they answer the "why us" question differently.
- **The deadline itself** — real deadlines come from deal timelines and are explainable; manufactured urgency is a process-control tactic. A GP who cannot explain what drives the date is compressing your diligence on purpose, and that is information.

None of these is disqualifying alone. The pattern across them is the finding.

## Guardrails

- **Every material claim carries its label** — verified, GP-asserted, or inferred — and the memo never silently promotes a deck assertion into a fact. This is the rule that makes a fast memo honest rather than merely fast.
- **Triage is not diligence, and the memo says so.** The scan's depth is bounded by the clock; what was not reached is listed, not glossed. A participate recommendation names the verifications it is subject to.
- **Never soften the adverse-selection section.** It is the part most likely to be uncomfortable with a GP relationship at stake, and the part the memo exists for. Facts, most plausible explanation, stated concern.
- **A pass recommendation needs no apology.** "Pass on process" — the timeline does not permit responsible evaluation — is a complete and legitimate conclusion, and the memo will reach it rather than stretch verification claims to fit the calendar.
- **No fabricated market checks.** If no independent reference on valuation or growth exists within the time available, the load-bearing-assumptions table says so; it does not invent a comp.
- **Relationship pressure is named, not obeyed.** Where the real argument for participating is the GP relationship rather than the deal, the memo says that explicitly so the IC can weigh it as what it is.
- **Not investment advice.** The memo structures a triage for a professional investment team; the decision, and accountability for it, are the firm's.
- **Confidentiality:** co-investment materials are shared under NDA and often contain MNPI about a private transaction. Assume a firm-approved AI environment, restrict the memo to the deal team, and flag any content whose sensitivity outlives a pass decision.

## Example prompts

> "GP deck and model summary attached for [company] — [GP] offered us $8M, decision due [date], nine days out. Criteria: existing fund relationships only, $5–15M checks, max 3% of program NAV per deal, no turnarounds. Book summary attached. Full triage, and be blunt on why they're showing us this."

> "Second co-invest from [GP] this year, this time fee-bearing — deck attached, deadline in twelve days. We don't have the book file handy, so flag concentration as open. I mainly want the adverse-selection read and the alignment section: what changed that they're now charging?"

> "We have four days, not two weeks — materials attached. Run kill tests and the adverse-selection facts only, tell me if anything ends it today, and if not, give me the five questions for tomorrow's GP call ordered by what would change the answer."

## Works well with

Use **cim-first-pass** instead when you are screening the deal as a direct buyer rather than triaging a GP's allocation — the frame and the criteria differ. Chain with **hedge-fund-diligence** when the co-invest offer is the first contact with an unfamiliar GP, since the sponsor question precedes the deal question, and run **ic-question-anticipator** on the finished memo before it goes to committee.
