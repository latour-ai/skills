---
name: ddq-response-drafter
description: >-
  Draft responses to an incoming LP due diligence questionnaire or consultant
  RFP by matching each question to the firm's approved answer library,
  adapting approved language to the asker's wording and format without
  changing any facts, carrying the source and approval date beside every
  answer, and flagging questions with no acceptable match as NEEDS DRAFTING
  rather than improvising. Separately routes every performance, regulatory,
  and policy answer for compliance review. For IR, fundraising, COO, and
  compliance teams at private equity, private credit, hedge fund, real
  assets, and venture managers. Trigger on phrases like "draft the DDQ,"
  "answer this questionnaire," "RFP from [consultant]," "fill out this DDQ,"
  "we got an ILPA DDQ," "respond to these LP questions," "match this to our
  answer library," or when a user uploads a due diligence questionnaire, RFP,
  or investor question list. Do NOT use for scanning someone else's completed
  DDQ for red flags — use the ddq-red-flag-scanner skill. Do NOT use for
  drafting a fund one-pager — use the fund-marketing-one-pager skill. Never
  invents facts; drafted answers require human and compliance review.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# DDQ Response Drafter

Get a DDQ from blank to substantially drafted in an hour, with every answer traceable to an approved source and every genuinely new question clearly flagged for a human. The goal is not to answer faster than you can think — it is to stop your best IR people from spending three weeks retyping answers they have already written, so their judgment goes to the twenty percent that actually needs it.

## Why this skill exists

A fund in market handles a lot of DDQs, and they ask the same things in different words. The work is overwhelmingly matching and adaptation, not thinking: the LP wants your valuation policy described in their template's section 4.2 rather than yours, with their terminology and their character limit. That work is real, it takes forty to sixty hours per questionnaire, and it is done by the people you least want doing data entry.

It is also where the mistakes happen. The failure mode is not a wrong answer thought up from scratch — it is a right answer that went stale: an AUM figure from two quarters ago, a headcount that changed, a policy description that no longer matches the manual, a performance figure carried forward without its as-of date. Fatigue at week three is exactly when those slip through, and an LP who catches an inconsistency between your DDQ and your ADV will ask about it in the ODD call.

So the discipline this skill enforces is narrow and strict: adapt approved language, never generate facts, always carry the source and the as-of date, and be loud about what has no approved answer.

## Inputs

**Required:**
- The incoming DDQ, RFP, or investor question list (uploaded or pasted)
- **The firm's approved answer library** — ideally an export with, per entry: the question or topic, the approved answer, the source document, and the approval or as-of date. A prior completed DDQ works as a substitute library, with the caveats noted below.

**Optional but high-value:**
- The most recent Form ADV, PPM, LPA, and compliance manual, for cross-checking that library answers still match the governing documents
- Current firm facts with as-of dates: AUM, fund sizes, headcount by function, portfolio company count, office locations
- The most recent performance figures, with the required net/gross labeling and as-of date
- Who the asker is — an ILPA-standard DDQ, a consultant's proprietary RFP, and a sovereign wealth fund's bespoke list get different treatment
- Character or word limits per question, and the required output format
- Prior DDQs completed for this same LP or consultant, so answers stay consistent with what they were told before
- The firm's tone conventions and any language compliance has previously rejected

**Missing-input behavior:** Without an answer library there is nothing to draft *from*, and generating answers about a firm's policies would be fabrication of exactly the kind this skill exists to prevent. Say that plainly and ask once. If the user offers a prior completed DDQ instead of a formal library, use it — but flag that its answers carry no approval dates, so every extracted fact needs re-verification before use, and mark them accordingly throughout. If firm facts with as-of dates are not provided, never carry a figure forward from the library without marking it `[VERIFY AS-OF DATE]`.

## How it works

1. **Parse the questionnaire into discrete questions,** preserving the asker's numbering and section structure — the response has to go back in their format. Split multi-part questions into their parts; a partially answered compound question reads as evasion.
2. **Classify each question** by type: firm and organization, strategy and process, track record and performance, team, operations and service providers, valuation, risk, compliance and regulatory, ESG, terms, references. The classification drives routing in step 6.
3. **Match each question to the library** by meaning rather than wording. Record the match confidence honestly — a close match, a partial match that covers some of what was asked, or no match.
4. **Adapt the approved language** to the asker's terminology, format, and length limit. Adapting means rephrasing and reordering; it does not mean adding a fact, sharpening a claim, or filling a gap in the approved answer with something reasonable-sounding.
5. **Flag every no-match and partial-match as NEEDS DRAFTING** with a note on what specifically is being asked that the library does not cover. Never improvise the answer. A blank flagged for a human takes five minutes to fill; an invented answer that reaches an LP is a different category of problem.
6. **Route for review.** Every answer containing a performance figure, a regulatory statement, a policy description, an AUM or headcount figure, or a forward-looking statement goes to compliance review — see the routing list below.
7. **Run the consistency checks:** answers against each other within this DDQ, against the Form ADV and governing documents where provided, and against any prior DDQ for the same asker.
8. **Flag every stale-dated fact** — anything where the library's as-of date is old enough that the figure has probably moved.
9. **Assemble the deliverable** in the asker's structure, with the internal tracking table alongside it.

## Output format

```
# DDQ Response Draft — [asker] [questionnaire name/version]
Received: [date] | Due: [date] | Questions: [N]
Library: [source, export date] | Format required: [ ]

## Status summary
Ready for review: [N] | Needs drafting: [N] | Needs compliance review: [N]
Stale-dated facts flagged: [N] | Consistency issues: [N]

## Response tracker
| Q# | Question (short) | Drafted response | Library source | Approved | Match | Status |
|---|---|---|---|---|---|---|
[Status: READY / NEEDS DRAFTING / NEEDS COMPLIANCE / VERIFY AS-OF DATE]

## Needs drafting — no acceptable library match
### Q[#]: [full question]
**What's being asked that the library doesn't cover:** [specific]
**Closest library entry:** [entry, and why it falls short]
**Who should draft this:** [IR / compliance / CFO / CIO]

## Needs compliance review
| Q# | Response excerpt | Why routed |
|---|---|---|

## Stale-dated facts
| Q# | Fact | Value in library | As of | Needs refresh? |
|---|---|---|---|---|

## Consistency check
| Fact | This DDQ (Q#) | Other source (doc, §) | Consistent? |
|---|---|---|---|
[Internal, vs. Form ADV / PPM / LPA, and vs. prior DDQ for this asker.]

## Assembled response document
[The full draft in the asker's structure and numbering, ready for review.
Every NEEDS DRAFTING item appears in place as a clearly marked placeholder —
never silently omitted, never filled with plausible text.]
```

## Always route to compliance

These answer types go to compliance review without exception, regardless of how well the library matches:

- Any performance figure — returns, IRR, MOIC, DPI, TVPI, benchmark comparisons, attribution — including whether gross and net are labeled as required
- Track record presentation: which funds and deals are included, how realized and unrealized are treated, and whether the selection could read as cherry-picking
- AUM, fund sizes, and dry powder
- Regulatory history: examinations, deficiency letters, enforcement, litigation, and any "has the firm ever…" question
- Valuation policy and process, especially for hard-to-value assets
- Conflicts of interest, related-party transactions, and allocation policy
- Side letters, MFN, and preferential terms
- Key person, succession, and team departures
- Fees and expenses charged to the fund
- Cybersecurity, BCP, and insurance coverage claims
- ESG claims and any policy the firm states it follows
- Anything forward-looking: target returns, pipeline, fundraising plans, capacity

## Guardrails

- **Never invent a fact about the firm.** Not an AUM figure, not a headcount, not a policy, not a date, not a service provider, not a process description. If the library does not contain it, the answer is NEEDS DRAFTING. This is the single rule the skill exists to enforce, and it holds even when the answer seems obvious from context or appears in an adjacent library entry.
- **Adapt language; do not upgrade claims.** Rephrasing an approved answer to fit an LP's wording is the job. Making it sound more impressive, more definitive, or more complete is not — even removing an approved hedge changes the claim.
- **Every drafted answer carries its library source and approval date.** An answer without provenance cannot be reviewed efficiently, which defeats the point.
- **Stale facts are flagged, never refreshed by inference.** If AUM was $2.1B as of two quarters ago, the draft says so and flags it. It does not estimate the current figure.
- **Performance answers are the highest-risk output in the document.** Marketing Rule requirements around net presentation, time periods, hypothetical and extracted performance, and substantiation apply to DDQ responses that will be used in an investment decision. Route them all, and never generate a performance figure that was not supplied.
- **Do not answer questions about individuals' backgrounds, regulatory history, or personal circumstances** from anything other than approved firm records.
- **Never omit a question.** An unanswered question left out of the response document is worse than one flagged as needing drafting.
- **This is a draft, not a submission.** Every response requires human review by someone accountable for its accuracy, and compliance review for the routed items, before it goes to the LP.
- **Confidentiality:** DDQs, answer libraries, and fund documents are confidential. Assume a firm-approved AI environment.

## Quality checks

- [ ] Every question in the source questionnaire appears in the output, in the asker's numbering
- [ ] Compound questions split and each part addressed
- [ ] Every drafted answer carries a library source and approval date
- [ ] No fact appears that is not in the library or the provided firm facts
- [ ] Every no-match flagged NEEDS DRAFTING with a note on the specific gap and who should draft it
- [ ] All performance, regulatory, and policy answers routed to compliance
- [ ] Gross and net labeled wherever performance appears
- [ ] Stale-dated facts flagged with their as-of dates
- [ ] Consistency checked internally and against Form ADV / governing documents where provided
- [ ] Assembled document is in the asker's required format and respects length limits

## Example prompts

> "ILPA DDQ from [consultant] attached, due in ten days. Our approved answer library export is the second file — it has question, answer, source doc, and approval date. Draft what you can, flag what needs real drafting, and route anything compliance has to see. AUM as of quarter end was $3.4B, headcount 41."

> "This LP sent a bespoke 90-question list, no standard format. We don't have a formal library but here's our last completed DDQ from March. Draft from it, but flag everything that needs re-verification since we don't have approval dates."

> "Short-form DDQ, 200-character limit per answer. Library attached. Adapt our standard answers to fit the limit without dropping anything compliance requires."

## Works well with

Run **ddq-red-flag-scanner** over the finished response before it goes out — reading your own DDQ the way a skeptical ODD analyst would is the cheapest quality check available. Route performance sections through **marketing-compliance-prescreen**, and use **fund-marketing-one-pager** for the materials that accompany the response.
