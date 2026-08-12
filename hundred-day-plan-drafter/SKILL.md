---
name: hundred-day-plan-drafter
description: >-
  Convert diligence findings, the investment thesis, and the deal model into a
  working 100-day plan for a newly acquired portfolio company — structured as
  discovery-then-execute, with a KPI baseline and reporting cadence to install,
  quick wins tied to specific model assumptions, leadership decisions with
  decide-by dates, workstreams with named owners and week-by-week milestones,
  and a board-ready one-pager. Flags every value-creation assumption in the
  model that has no corresponding workstream. Also refreshes the plan against
  actuals at day 30, 60, and 90. For private equity operating partners, deal
  teams, portfolio operations groups, and newly installed portfolio company
  CEOs and CFOs. Trigger on phrases like "draft the 100-day plan," "we just
  closed," "post-close plan," "value creation plan," "first 100 days," "turn
  the diligence into workstreams," "day 30 refresh," or when a user provides
  post-close deal materials and asks what happens next. Do NOT use for
  pre-close deal evaluation — use the cim-first-pass or ic-memo-drafter skill.
  Do NOT use for the quarterly board pack — that is ongoing reporting.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Hundred Day Plan Drafter

Turn what you learned in diligence into what somebody owns on Monday. A 100-day plan built directly from the diligence record and the model — so every value-creation assumption you underwrote has a workstream, an owner, and a milestone — plus the board-ready one-pager and a refresh cycle that keeps it a working document rather than a folder nobody opens after week three.

## Why this skill exists

The 100-day plan usually gets written in the exhausted week after closing, from memory, by people who are already being pulled onto the next deal. The predictable result: the plan reflects what the author remembers rather than what diligence found, and half the value-creation assumptions that justified the price never become anybody's job. Nobody notices, because the assumptions live in a model tab and the plan lives in a deck, and no one ever puts the two side by side.

The second failure is timing. Plans written in week one commit to execution before the new owner knows anything from the inside — decisions made on a diligence-quality fact base, which is a fact base assembled from outside the company by people the company was managing. The plans that work treat the first month as fact-building and sequence execution behind it.

This drafts from the primary record, forces the model-to-workstream reconciliation, and builds in the refreshes.

## Inputs

**Required:**
- At least one of: the investment thesis or IC memo, the diligence readouts, or the deal model's value-creation summary. More is better; all three is the intended case.

**Optional, in rough order of value:**
- **The deal model's value-creation bridge** — how the underwriting gets from entry EBITDA to exit EBITDA, broken into its drivers. This is what makes the traceability check possible and it is the input most worth chasing down.
- Diligence readouts by workstream, including the issues that were noted but not resolved before close
- The QoE, particularly the add-backs that assumed a change the company had not yet made
- Management team assessment: who is staying, who is uncertain, what gaps were identified
- The company's current reporting — what management actually produces monthly today, and in what format
- Who is available to do the work: operating partners, the deal team's ongoing involvement, interim resources, budget for advisors
- Close date, first board meeting date, and fiscal calendar
- Any commitments made to management or lenders during the process
- The firm's own 100-day template or a prior plan

**Missing-input behavior:** Without the model's value-creation bridge, the traceability check — arguably the most valuable output — cannot run. Say so explicitly and ask once; a summary of the drivers is enough, the full model is not needed. Without a management assessment, draft the organizational workstream with owners marked `[OWNER TBD]` rather than assigning work to people whose roles you are inferring. Never invent a company metric, a headcount, or a financial figure.

## How it works

1. **Extract the value-creation bridge into a list of discrete assumptions.** Each one: what it assumes, how much EBITDA or multiple it contributes, and by when the underwriting expects it. This list is the spine of the plan.
2. **Extract the open items from diligence** — everything flagged as unresolved, conditional, or "confirm post-close." These become week-one workstreams, because they are the things that could change the plan.
3. **Design the fact base for weeks 1–4.** What the new owner needs to know from the inside that diligence could not establish: real customer-level profitability, actual pipeline quality, true capacity utilization, the state of the data, who actually makes decisions. Be specific to this company and this thesis, not generic.
4. **Specify the KPI baseline and reporting cadence to install,** which is the highest-leverage thing that happens in the first month. Which metrics, defined how, produced by whom, on what day of the month, in what format — and what has to change in the company's systems to produce them. A metric that cannot be produced monthly is not a KPI.
5. **Identify quick wins,** each tied to a specific model assumption or diligence finding. A quick win with no line in the model is a distraction; say so.
6. **Surface leadership and organization decisions** with a decide-by date. These are the decisions that get deferred and then cost a year.
7. **Build the workstreams** across the standard categories below, each with a named owner, a weekly milestone sequence, and the dependency that would block it.
8. **Run the traceability check.** Every model assumption mapped to a workstream; every workstream mapped back to an assumption or a diligence finding. Report both directions — unmapped assumptions are underwriting nobody owns, and unmapped workstreams are effort nobody underwrote.
9. **Sequence realistically against capacity.** Count the workstreams against the people actually available and flag over-commitment. Most 100-day plans fail on capacity, not on ideas.
10. **Write the board-ready one-pager,** and set up the day 30/60/90 refresh structure.

**Refresh mode:** when run at day 30, 60, or 90 with actuals, compare planned milestones to what happened, re-baseline what has slipped, retire what is done, surface what the inside fact base has changed about the thesis, and flag any model assumption that now looks unachievable — early, while there is still time to respond.

## Output format

```
# [Company] — 100-Day Plan
Closed: [date] | Plan date: [date] | First board meeting: [date]
Sources: [thesis/IC memo, DD readouts, model — list with dates]
Not provided: [list]

## Board one-pager
[The whole plan on one page: the three things that must be true at day 100,
the KPI baseline being installed, the top quick wins with their model impact,
the leadership decisions and their dates, and the biggest risk to the plan.]

## Value-creation assumptions from the underwriting
| # | Assumption | EBITDA / multiple impact | Underwritten by when | Workstream | Status |
|---|---|---|---|---|---|
**Assumptions with no workstream: [list — or "none"]** ← the critical output

## Weeks 1–4: build the fact base
| # | What we need to know | Why diligence couldn't establish it | Who | By |
|---|---|---|---|---|
Open diligence items carried into close: [list, each assigned]

## KPI baseline and reporting cadence
| KPI | Definition | Source system | Owner | Frequency | Available today? | Work to enable |
|---|---|---|---|---|---|---|
Monthly reporting package: [contents, due date, recipients]
Systems or data work required: [ ]

## Quick wins (achievable inside 100 days)
| # | Quick win | Model assumption / DD finding it serves | Owner | Target date | Est. impact |
|---|---|---|---|---|---|

## Leadership & organization decisions
| Decision | Options | Decide by | Decision owner | Consequence of delay |
|---|---|---|---|---|

## Workstreams
### [Workstream name] — Owner: [name] | Sponsor: [name]
Objective at day 100: [ ]
| Week | Milestone | Dependency |
|---|---|---|
[Repeat per workstream.]

## Capacity check
| Owner | Workstreams | Milestones in first 30 days | Over-committed? |
|---|---|---|---|

## Risks to the plan
| Risk | Impact on the plan | Early warning signal | Mitigation |
|---|---|---|---|

## Refresh schedule
Day 30 / 60 / 90 review dates, what gets re-baselined at each, and who attends.
```

## Workstream categories

Draft against these, drop the ones that do not apply to this company, and never include one just because it is on the list:

- **Finance & reporting** — KPI baseline, monthly close speed and reliability, chart of accounts, budget and forecast process, cash management and the 13-week if leverage is meaningful, lender reporting obligations
- **Commercial** — pricing, sales process and pipeline discipline, customer profitability, churn and retention mechanics, salesforce structure and comp
- **Operations** — capacity, throughput, procurement, supply chain, service delivery, the specific operational thesis if there is one
- **Organization & talent** — leadership assessment and gaps, org design, incentive and equity plan, key-person retention, the hires that must happen in year one
- **Technology & data** — systems that block the KPI baseline, ERP and CRM state, cybersecurity posture, technical debt that constrains the growth plan
- **M&A / add-ons** — pipeline, target criteria, integration capability, and whether the platform can absorb an acquisition yet
- **Governance** — board composition and cadence, reporting pack format, delegation of authority, management incentive alignment
- **Risk, compliance & insurance** — items flagged in legal, tax, environmental, or insurance diligence that need post-close resolution

## Guardrails

- **Every workstream has a named owner or an explicit `[OWNER TBD]`.** Work assigned to "the team" or "management" does not happen. If the user did not say who is available, mark it TBD rather than inventing an org.
- **Never invent company facts.** No revenue figures, headcounts, customer names, system names, or metrics that were not provided. A plan that misstates the company's baseline is worse than a plan with gaps.
- **The traceability check runs in both directions and is reported even when it is unflattering.** Unmapped model assumptions are the finding this skill exists to produce.
- **Distinguish what diligence established from what management said.** Carry the evidence quality forward from the diligence record — a workstream built on an unverified management claim should say so, because week one may disprove it.
- **Sequence discovery before execution.** Do not schedule irreversible decisions — reorganizations, pricing changes, system replacements — before the fact base that would inform them exists. Where the deal thesis genuinely demands an early irreversible move, flag it as a risk rather than burying it in a milestone.
- **Be honest about capacity.** If the plan requires more from an operating partner than one person can do, say it in the capacity check rather than distributing the milestones and hoping.
- **This is a draft plan, not a management directive.** The company's leadership owns execution, and a plan imposed without their input rarely survives contact. Note where management buy-in is required before a workstream can start.
- **Confidentiality:** post-close deal materials, management assessments, and organizational plans are highly sensitive, and the leadership section in particular concerns identifiable individuals. Assume a firm-approved AI environment and handle personnel content accordingly.

## Quality checks

- [ ] Every model value-creation assumption appears in the traceability table with a workstream or an explicit gap
- [ ] Unmapped assumptions listed prominently, not buried
- [ ] Weeks 1–4 are discovery, with irreversible decisions sequenced behind the fact base
- [ ] Every KPI has a definition, a source, an owner, and an honest "available today?" answer
- [ ] Each quick win names the model assumption or diligence finding it serves
- [ ] Every workstream has a named owner or `[OWNER TBD]`
- [ ] Leadership decisions carry decide-by dates and the cost of delay
- [ ] Capacity check completed and over-commitment flagged
- [ ] No invented company facts or figures
- [ ] The one-pager stands alone for a board member who reads nothing else

## Example prompts

> "We closed on [company] last Friday — a $40M EBITDA industrial services business. Attached: the IC memo, our final commercial and financial DD readouts, the QoE, and the model's value creation bridge. Draft the 100-day plan. Our operating partner is full-time on this, the deal team stays involved through the first board meeting, and the CFO is a question mark."

> "Day 30 refresh. Here's the original plan and where each milestone actually stands, plus the first monthly reporting package management produced. What's slipped, what needs re-baselining, and does anything we've learned inside change the underwriting?"

> "Add-on acquisition closing next month into an existing platform. Diligence readouts attached. Draft an integration-focused 100-day plan — the platform CFO will own most of it."

## Works well with

**ic-memo-drafter** produces the thesis and value-creation assumptions this plan traces against. Run **thesis-red-team** on the underwriting before drafting if the deal was competitive and the model is aggressive.
