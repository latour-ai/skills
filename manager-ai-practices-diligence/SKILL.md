---
name: manager-ai-practices-diligence
description: >-
  Add an AI-practices module to the diligence file on an external manager —
  hedge fund, private markets, or long-only — built from the manager's DDQ
  responses, ODD questionnaire, vendor and service-provider list, policies,
  and call notes. It maps where AI sits in the manager's investment and
  operating process: which workflows are model-assisted, what data goes to
  which outside vendors and under what stated terms, whether outputs that
  reach an investment decision or an investor document are reviewed by a
  person before they are relied on, who owns changes to models, prompts, and
  tools, and what the record of errors and incidents looks like. Each
  finding is labeled as stated by the manager or evidenced by a document,
  missing and evasive answers are flagged, and the output is a one-page
  summary for the diligence file plus the follow-up question set for the
  manager call. Run on every name in the pipeline and at re-underwriting.
  For ODD analysts, research analysts, and compliance staff at
  fund-of-funds, OCIOs, endowments, foundations, pensions, and family
  offices. Trigger on phrases like "diligence their AI use," "how is this
  manager using AI," "AI-enabled strategy diligence," "add the AI module to
  the ODD file," "what are they sending to model vendors," "build the AI
  questions for the manager call," or when a user attaches a manager's DDQ
  and asks about AI, machine learning, or model governance. Do NOT use for
  the full first look at a new manager — use the hedge-fund-diligence
  skill. Do NOT use as the complete operational review and findings memo —
  this module is one section that feeds it. Do NOT use
  for a red-flag read of the whole DDQ — use the ddq-red-flag-scanner
  skill. Do NOT use to review your own firm's AI workflows — use the
  ai-workflow-audit skill. Do NOT use to diligence a vendor your own firm
  is onboarding; this module covers external managers only. Findings describe the
  manager's practices as stated and evidenced; questions of data licensing
  or rights are routed to counsel, and nothing here is a legal conclusion
  or investment advice.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Manager AI Practices Diligence

Allocators are now expected to answer a question that most diligence files were not built to hold: how does this manager use AI, and does that use introduce risk the rest of the review would miss? The answers are scattered. A sentence in the DDQ's technology section, a new vendor on the service-provider list, a pitch-deck slide about "proprietary machine learning," a compliance manual that predates any of it. This skill pulls those pieces into one module per manager, separates what the manager told you from what a document actually shows, flags the questions that went unanswered or were answered around, and produces the follow-up set for the manager call. It is designed to be run on every name in the pipeline, the same way each time, so managers can be compared.

## Why this skill exists

AI use at a manager is not a single fact. It ranges from analysts using a chat assistant to summarize filings, to models that generate signals feeding position sizing, to automated drafting of investor letters and DDQ answers. Each of these carries different risks: research data leaving the firm, a signal nobody can explain, an investor communication containing a figure nobody checked. A diligence process that asks "do you use AI?" and records yes or no captures none of that. The useful picture is workflow by workflow: what the tool does, what data it sees, who reviews its output, and what happens when it is wrong.

Standard ODD questionnaires mostly predate the question. Technology and cyber sections ask about infrastructure, access controls, and business continuity, and many managers answer AI questions inside those sections in general language, if at all. The result is that the most relevant information sits in places an ODD checklist does not look: the vendor list, the data-use language in research policies, the description of the investment process in the pitch deck, and remarks made on calls. Reading those together is what this module adds.

Marketing and practice also diverge in both directions. Some managers describe ordinary tools in ambitious terms because "AI-enabled" helps fundraising; others use models materially in the investment process and describe it modestly because they do not want the scrutiny. Either gap is a finding. The allocator needs to know what is actually happening, which means distinguishing the manager's claims from the evidence behind them and treating a confident, unevidenced answer differently from a documented one.

Finally, the module has to be repeatable. An AI-practices view built differently for each manager cannot be compared across the pipeline or tracked over time at the same manager. The same categories, the same evidence labels, and the same question set every time are what make it usable at re-underwriting.

## Inputs

**Required:**
- The manager's DDQ responses, current version, including technology, research, compliance, and service-provider sections
- The name of the manager and the strategy under review

**Optional but high-value:**
- **The ODD questionnaire and supporting documents** — compliance manual, information security policy, research and data-use policy, any AI or acceptable-use policy the manager has written
- **The vendor and service-provider list**, ideally with what each vendor does and what data it receives
- **Pitch deck and investor letters**, where AI claims tend to appear in marketing language
- **Notes from manager calls or on-site visits**
- **Prior DDQ versions or a prior AI module on the same manager**, so changes can be shown
- **The allocator's own AI questions or policy expectations**, which take precedence over the default categories below
- **Strategy context** — for a systematic or quantitative manager, model use is the strategy, and the module should go deeper on model governance; for a discretionary manager, the focus is usually research and operations workflows

**Missing-input behavior:** The module runs on whatever is provided and states which categories it could and could not assess. If the DDQ does not address AI at all, that absence is the first finding, and the follow-up set does the work the DDQ did not. If no vendor list is supplied, data-flow findings are marked as based on the manager's description only. Gaps are never filled with assumptions about what a manager of this type typically does.

## How it works

1. **Collect every reference to AI, models, and automation across the file.** Search beyond the obvious section: technology, research process, risk, compliance, vendor list, marketing materials, and call notes. Record each reference with its source document and location.
2. **Build the workflow inventory.** For each workflow where the manager uses a model or AI tool, record what it does, where it sits (research, signal generation, portfolio construction, trading, risk, operations, investor reporting, compliance), and whether its output can reach an investment decision or an investor-facing document. Workflows the manager mentions but does not describe are listed as incomplete.
3. **Trace the data flows.** For each workflow, what data goes in — proprietary research, position data, investor information, licensed third-party data, material non-public information risk — and where it goes: an in-house model, a vendor's hosted service, or a general-purpose tool. Record what the manager says about vendor terms, data retention, and use of inputs for model training. Note where licensed third-party data appears to be sent to an outside model, and route that question to counsel rather than assessing it.
4. **Assess human review at the points that matter.** For each workflow whose output reaches a decision or an investor document, who reviews it, at what stage, and whether the review is described in a written procedure or only asserted. A model-generated figure in an investor letter with no named reviewer is a different finding from one checked against the books by operations.
5. **Establish ownership and change control.** Who can add a tool, change a prompt, retrain or replace a model, or grant a vendor access to new data. Whether changes are logged, tested, or approved, and by whom. For systematic strategies, how model changes are validated before they trade.
6. **Ask for the failure record.** Errors, incidents, near-misses, or vendor outages involving AI tools, and what changed afterward. A manager with material AI use and no reported incidents has either an unusually clean record or no process for noticing; the follow-up asks which.
7. **Label every finding.** Each finding is marked *stated* (the manager asserted it in the DDQ, a call, or marketing), *evidenced* (a policy, procedure, log, contract excerpt, or other document supports it), *missing* (the question was not answered), or *evasive* (the answer did not address the question asked). Claims in marketing material that are not supported elsewhere are noted as such.
8. **Compare against the prior module, where one exists.** New workflows, new vendors, changed answers, and questions that were evasive last time and remain so.
9. **Write the follow-up question set.** Specific to this manager's answers, ordered so the questions that matter most for the allocation come first, each tied to the gap it closes. Generic questions that the file already answers are left out.

## Output format

A skeleton to adapt — the summary and the follow-up questions are what the analyst takes into the manager call; the inventory and evidence labels are what make the module comparable across managers and over time.

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# AI practices module — [manager], [strategy]
Prepared: [date] | Sources: [documents reviewed, with versions/dates]
Prior module: [date or none] | Allocator AI expectations applied: [yes / default categories]

## Summary
[Three to five sentences: how material AI is to this manager's process, the most significant
risks or gaps, and what the call needs to resolve]
Answer quality: [N stated / N evidenced / N missing / N evasive]

## Workflow inventory
| Workflow | Area | Tool type (in-house / vendor / general-purpose) | Reaches decision or investor doc? | Human review | Label |
|---|---|---|---|---|---|

## Data flows
| Workflow | Data sent | Destination | Stated terms (retention, training use) | Label | Counsel question? |
|---|---|---|---|---|---|

## Ownership and change control
[Who adds tools, changes prompts or models, approves vendor access; how changes are logged
and tested] — [label per point]

## Failure record
[Incidents, errors, outages as reported, and what changed] — [label]

## Missing and evasive answers
| Question or topic | Where asked | What was said (quoted) | Why it matters |
|---|---|---|---|

## Changes since prior module
[New workflows, new vendors, changed answers, still-unresolved items]

## Follow-up questions for the manager call
1. [Question] — closes: [gap]

## For counsel
[Data licensing or rights questions identified, described factually, no conclusion]

## Not assessed
[Categories skipped and the input that would have been needed]
```

## Where AI practices diligence goes wrong

- **Treating the DDQ answer as the finding.** A well-written paragraph describing review controls is a statement, not evidence. Without a procedure, log, or document behind it, it stays labeled *stated*, however confident it sounds.
- **Looking only in the technology section.** The most useful information is often in the vendor list, the research policy, or the pitch deck. A model vendor on the service-provider list that the DDQ never mentions is a finding.
- **Recording "uses AI: yes."** Material risk depends on the workflow. An analyst summarizing public filings and a model setting position sizes are not the same answer and should not share a row.
- **Filling silence with assumptions.** A missing answer is flagged as missing. It is not completed with what a manager of this size or strategy would probably do.
- **Missing the investor-document path.** Attention goes to investment decisions, but AI-drafted letters, DDQ answers, and performance commentary go straight to allocators. Who checks those figures matters.
- **Assessing licensing instead of describing it.** Whether a manager may send a licensed dataset to an outside model depends on contracts the module has not seen. Describe what is being sent and route the question.
- **Taking a clean failure record at face value.** No incidents from a manager with heavy AI use usually means no reporting process. Ask how errors would be noticed.
- **Over-weighting the marketing.** "Proprietary AI" in a deck may describe a spreadsheet macro or a core signal. Match each claim to a workflow or mark it unsupported.

## Guardrails

- **Stated and evidenced are always separated.** Every finding carries its label, and the summary counts them. What the manager said and what a document shows are never merged into one assertion.
- **Missing and evasive answers are flagged, not filled.** The module never supplies a likely answer on the manager's behalf. Evasive answers are quoted so the reader can judge.
- **No legal conclusions on data licensing or rights.** Where data appears to flow to an outside vendor under terms that may matter, the module describes the flow factually and lists it for counsel. It does not conclude that a use is permitted or prohibited.
- **The file is the evidence base.** Every finding traces to a document, note, or quoted answer. General knowledge of the manager, its vendors, or industry practice does not substitute for what is on file.
- **No vendor endorsements or assessments.** Vendors are recorded as the manager describes them. The module does not rate AI products or repeat their marketing claims.
- **Confidentiality.** DDQs, policies, and call notes are confidential manager materials. Assume a firm-approved AI environment and reproduce nothing beyond what the module requires.
- **Not investment advice.** This is one input to the allocator's diligence. It does not recommend hiring, retaining, or redeeming any manager.

## Example prompts

> "Attached are [manager]'s DDQ, their ODD questionnaire, the service-provider list, and the deck from last week's meeting. It's a discretionary long/short equity fund. Build the AI practices module and the follow-up questions for Thursday's call — I especially want to know whether any of our position-level or investor data could end up with an outside model vendor."

> "This one is a systematic macro manager, so model use is the strategy. Go deep on change control and validation: who can change a model, how changes are tested before they trade, and what their incident history looks like. Flag every answer that describes a control without showing it."

> "Re-underwriting. Here's this year's DDQ, last year's DDQ, and the AI module we wrote last cycle. Show me what changed — new tools, new vendors, answers that moved — and which of last year's evasive answers are still evasive."

## Works well with

The module is one section of the full operational due diligence file, and its missing and evasive answers sit naturally alongside the whole-document read from **ddq-red-flag-scanner**. On a new manager, **hedge-fund-diligence** frames the investment case the AI findings inform, and its reference-check questions are the place to carry the sharpest follow-ups to former employees and service providers. At re-underwriting, rerun the module and carry the changes into the annual manager review, where a material new AI dependency belongs in the what-changed register.
