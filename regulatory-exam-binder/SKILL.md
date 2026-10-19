---
name: regulatory-exam-binder
description: >-
  Turn an SEC examination document request list into an organized, indexed
  production — mapping each request item to responsive firm records, surfacing
  the gaps where a policy exists but testing evidence does not, drafting
  narrative responses to examiner interview questions from the firm's actual
  policies, and producing a prioritized remediation list. Also runs as a mock
  exam against current exam priorities before any letter arrives. For chief
  compliance officers, compliance analysts, and COOs at registered investment
  advisers, private fund managers, and broker-dealers. Trigger on phrases like
  "we got an exam letter," "SEC document request," "prep for the exam," "run a
  mock exam," "map this request list," "what are we missing for the exam,"
  "deficiency letter prep," "examiner interview questions," or when a user
  uploads an examination request list, compliance manual, or annual review
  document. Do NOT use for screening marketing material against the Marketing
  Rule — use the marketing-compliance-prescreen skill. Do NOT use for
  evaluating an external manager's compliance program — use the
  ddq-red-flag-scanner skill. Not legal advice; involve counsel.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Regulatory Exam Binder

Turn a document request list into an indexed production and an honest gap list. Every request item mapped to the records that answer it, every gap ranked by how much trouble it is, narrative responses drafted from the firm's real policies, and a remediation list you can work. Run it against a live request list, or against current exam priorities as a mock exam while there is still time to fix what it finds.

## Why this skill exists

The two weeks after an exam letter arrives are the worst two weeks in a CCO's year, and the quality of the initial production sets the tone for everything that follows. A production that arrives organized, indexed, and internally consistent reads as a firm with a functioning compliance program. One assembled in a scramble — inconsistent date ranges, documents that contradict each other, a policy produced with no evidence it was ever tested — invites the examiner to look harder.

The gap that causes real problems is specific and predictable: a written policy with no record of testing. Firms rarely lack policies. They lack the log, the minutes, the attestation file, or the review memo showing the policy was actually operated. That gap is findable months in advance, and it is almost never found, because nobody sits down and maps records to requirements until the letter forces it.

## Inputs

**Required (one of):**
- The examination document request list, **or**
- A request that the skill build a mock request list from current SEC examination priorities for the firm's registration type and business model

**Required in either case:**
- The firm's compliance manual and code of ethics
- An inventory of compliance records the firm holds — what exists, where, and for what date range. A rough list is fine; precision comes later.

**Optional but high-value:**
- The most recent annual compliance review (Rule 206(4)-7) and any prior deficiency letters
- Form ADV Parts 1, 2A, and 2B as most recently filed
- The specific interview questions the examiners have flagged, or the topics the exam letter emphasizes
- Firm profile: AUM, strategies, client types, custody arrangements, affiliates, number of employees, whether the firm has been examined before

**Missing-input behavior:** The record inventory is the input people most often skip, and the output is nearly worthless without it — a mapping table with no records to map to is just the request list retyped. Ask once for the inventory, and accept an approximate one. If the compliance manual is unavailable, the narrative responses cannot be drafted from firm policy; produce the mapping and gap analysis, and say clearly that the narrative section was skipped rather than writing generic answers that misdescribe the firm.

## How it works

1. **Parse the request list into discrete items.** Exam requests bundle several asks into one numbered paragraph. Split them — each distinct document type and date range becomes its own row, retaining the original item number for the response index.
2. **Map each item to responsive records** from the inventory: document name, custodian, format, and the date range actually available versus the date range requested. A partial date range is a finding, not a match.
3. **Classify every item** as fully responsive, partially responsive, no responsive record, or not applicable to the firm — and for "not applicable," draft the one-sentence explanation the response letter will need, because an unexplained blank reads as a refusal.
4. **Run the policy-versus-evidence test on every mapped item.** For each area, ask separately: is there a written policy? Is there evidence the policy was operated during the review period? These are different questions and the second one fails far more often. Flag every case of policy-without-testing-evidence as a distinct gap type.
5. **Check internal consistency across the production.** Records produced together must agree with each other and with the Form ADV: AUM figures, employee counts, service provider names, fee descriptions, strategy descriptions, custody arrangements. Contradictions between produced documents are among the most damaging findings, and they are entirely preventable.
6. **Draft narrative responses to interview-style questions,** grounded strictly in the firm's actual policies and quoting the manual where relevant. Where the firm's practice differs from the manual, say so in the internal output — never paper over it in a response.
7. **Rank the gaps** by severity: likelihood of becoming a deficiency, and how bad that deficiency would be.
8. **Build the remediation list,** separating what can be genuinely fixed before production from what must be disclosed and remediated going forward — and be explicit about that distinction.

## Output format

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# [Firm] — Examination Preparation Binder
Mode: [live request list / mock exam vs. current priorities]
Request list: [source, date] | Review period: [dates] | Prepared: [date]
Records inventory as of: [date]

## Readiness summary
[4–6 sentences: how much of the request the firm can satisfy today, the number
of gaps by severity, and the 2–3 items that need attention first.]

Items: [N] fully responsive / [N] partial / [N] no record / [N] N/A
Gaps: [N] HIGH / [N] MEDIUM / [N] LOW

## Request mapping
| Item # | Request (short) | Responsive record(s) | Custodian | Period held vs. requested | Status |
|---|---|---|---|---|---|

## Policy-vs-evidence gaps
The findings that matter most. For each:
### G1. [Area]
- **Policy:** [exists / absent] — [manual §, quoted if useful]
- **Evidence of operation:** [what exists, or what is missing]
- **Request items affected:** [#s]
- **Why an examiner would care:** [1–2 sentences, tied to the rule]
- **Severity:** HIGH / MEDIUM / LOW
- **Remediable before production?** [yes — how / no — why]

## Internal consistency check
| Fact | Source A (doc, §) | Source B (doc, §) | Consistent? |
|---|---|---|---|
[AUM, headcount, service providers, fee terms, custody, strategy descriptions,
each cross-checked against Form ADV.]

## Drafted narrative responses
### [Interview question]
[Response drafted from firm policy, with manual citations. Any place the draft
relies on a practice not documented in the manual is marked
**[UNSUPPORTED BY MANUAL — confirm before use]**.]

## Production index
| Bates / file | Document | Item # responded to | Date range | Pages |
|---|---|---|---|---|
[Complete enough that someone who did not build the binder can locate each document from it.]

## Remediation list
| # | Gap | Action | Owner | Fix before production? | Priority |
|---|---|---|---|---|---|

## For counsel
Items where privilege, disclosure obligations, or the scope of the response
need a lawyer's judgment before anything goes out.
```

## Standard request categories for an adviser exam

Use as the checklist when building a mock request list, and as a completeness test against a live one. Scope to the firm's actual business — a manager with no custody should not be producing custody records, but should be able to explain why not.

- Organizational documents, ownership, affiliates, and org chart
- Compliance manual, policies and procedures, and the Rule 206(4)-7 annual review — **including the testing that supports it**
- Code of ethics, access person list, personal trading pre-clearance and reporting records
- MNPI and insider trading controls, restricted list, information barriers, expert network policies
- Trading records, allocation policy and allocation testing, best execution reviews, soft dollar and commission arrangements, trade errors log
- Valuation policy, valuation committee minutes, pricing sources, and the treatment of hard-to-value assets
- Custody arrangements, surprise examination or audited financial statement delivery, qualified custodian confirmations
- Marketing and advertising materials, performance calculations, and Marketing Rule substantiation files
- Fee calculations, expense allocation policy, and evidence of fee accuracy testing
- Client and investor agreements, side letters, and MFN elections
- Books and records: emails and electronic communications, retention, off-channel communications policy and enforcement
- Cybersecurity program, incident log, vendor due diligence, and business continuity plan with test records
- Conflicts inventory, related-party transactions, principal and cross trades
- Political contributions and pay-to-play records
- Complaints log and litigation
- Filings and evidence of timely submission: Form ADV, Form PF, 13F, 13H, 13D/G
- Service provider oversight: administrator, auditor, prime brokers, and evidence of due diligence

## Guardrails

- **Never draft a record to fill a gap.** If evidence of testing does not exist for the review period, the answer is that it does not exist. Creating a document now and presenting it as contemporaneous is a far more serious problem than the original gap. Every remediation item is explicitly labeled as prospective or as a genuine pre-production fix (e.g. locating a record that exists but was not inventoried).
- **Never backdate, and never describe a remediation as if it predates the request.**
- **Ground narrative responses in the manual, not in best practice.** If the firm's policy is weaker than what an examiner would like, the draft says what the policy is. Aspirational descriptions of a program the firm does not run are the fastest route to a misrepresentation finding.
- **Flag every place practice diverges from the written policy** in the internal output. That divergence is a real finding and it belongs in remediation, not in a smoothed-over response.
- **This is not legal advice.** Exam responses have legal consequences, involve privilege questions, and can create disclosure obligations. Counsel reviews before anything is produced — say so in the output.
- **Do not assert regulatory requirements without grounding.** Where a rule is cited, cite it accurately; where a practice is convention rather than requirement, label it convention. Rules and exam priorities change — verify current requirements rather than relying on recall.
- **Confidentiality and privilege:** exam materials, the compliance manual, and the gap analysis are sensitive and potentially privileged. Assume a firm-approved AI environment. The gap analysis in particular should be handled with counsel's guidance on privilege before it circulates.

## Example prompts

> "We received an SEC exam letter Friday — request list attached, review period is the last 24 months. Our compliance manual, code of ethics, and a rough inventory of what we've got are also attached. Map it, tell me where we're exposed, and draft responses to the interview questions in items 14–18."

> "No exam pending. Build a mock request list for a $900M private fund adviser with no custody, three funds, and 14 employees, run our manual and records inventory against it, and tell me what we'd fail on today."

> "Prior deficiency letter attached along with our remediation memo. Build the binder for this exam and specifically show me whether we can evidence that each prior deficiency was actually fixed."

## Works well with

Run **marketing-compliance-prescreen** over the marketing materials being produced, since Marketing Rule substantiation is a standard request category and a common deficiency. Use **ic-minutes-generator** to build the defensible committee records this skill will look for.
