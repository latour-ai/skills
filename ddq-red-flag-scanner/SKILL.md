---
name: ddq-red-flag-scanner
description: >-
  Scan a completed DDQ or RFP response for red flags — vague or evasive
  answers, internal inconsistencies, missing standard disclosures, and
  answers that contradict the manager's deck or letters. For allocators,
  fund-of-funds analysts, OCIOs, and ODD teams. Trigger on phrases like
  "scan this DDQ," "red flags in this DDQ," "review these RFP responses,"
  "anything off in this questionnaire," "check this DDQ against the deck,"
  "what's missing from this DDQ," or when the user uploads a completed due
  diligence questionnaire or RFP response. Do NOT use for a general first
  pass on a manager — use the hedge-fund-diligence skill. Do NOT use for
  ongoing quarterly review of an existing manager — use the
  manager-monitoring-note skill. Do NOT use for NDAs or contracts — use the
  pe-nda-review skill.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# DDQ Red-Flag Scanner

Scan a completed DDQ or RFP response the way a skeptical ODD analyst reads it: not for what it says, but for what it avoids saying. Output a severity-ranked findings list where every finding quotes the exact language (or names the exact missing disclosure), explains why it matters, and gives the follow-up question to ask.

## Why this skill exists

DDQs are written by the manager's IR team and counsel, and they are very good at producing answers that are technically responsive and substantively empty. The tells are systematic: passive voice around compliance history, "from time to time" hedges, valuation policies that never mention level-3 assets, key-person questions answered with org charts. A human reviewer skimming 80 pages misses these; a systematic scan against a checklist of standard disclosures doesn't. This skill is the systematic scan — it ranks what it finds so the human spends time on what matters.

## Inputs

**Required:**
- A completed DDQ or RFP response (PDF, document, or pasted text)

**Optional (enables the cross-document consistency check — the highest-value finding type):**
- The manager's pitch deck, investor letters, tear sheet, or website copy
- Form ADV (or tell the skill to pull the public ADV via your AI's web search)
- A prior version of the same DDQ — enables a "what changed" diff
- The user's own DDQ standard or pet questions

**Missing-input behavior:** The DDQ alone is enough to run. If no comparison materials are provided, run the scan and note that the cross-document consistency section was skipped. Don't ask for anything unless the DDQ itself is unreadable or clearly partial — in that case ask once which sections exist.

## How it works

1. **Map the document.** List the sections present and immediately note standard sections that are absent (see the disclosure checklist in step 4).
2. **Evasiveness pass.** Flag answers that are vague, deflecting, or non-responsive. Tells: passive voice where an actor matters ("errors are addressed promptly" — by whom?), answers that restate the question, "please refer to" loops that never land, qualifiers like "generally," "typically," "from time to time," "we are not aware of," answers conspicuously shorter than neighboring ones, and boilerplate where specifics were asked.
3. **Internal consistency pass.** Cross-check the DDQ against itself: headcount vs. team bios, AUM in one section vs. another, stated strategy vs. described risk limits, service providers named inconsistently, dates that don't line up.
4. **Missing-disclosure checklist.** Verify the document substantively addresses, at minimum: regulatory exams/actions and material litigation; personal trading and code-of-ethics policy; valuation policy *including who values level-3/hard-to-value assets and who can override*; key-person provisions and succession; conflicts of interest and related-party arrangements; side letters / preferential terms (MFN); fund expenses charged to the fund vs. the manager; counterparty and prime broker arrangements; business continuity and cybersecurity; compliance staffing and whether the CCO is dedicated; auditor identity and any auditor changes; errors-and-omissions history and material NAV restatements. Each item is answered / partially answered / absent.
5. **Cross-document consistency pass (if materials provided).** Compare DDQ claims against the deck, letters, and ADV: performance characterizations, AUM, team size and tenure, capacity statements, strategy descriptions. Quote both documents wherever they disagree.
6. **Severity-rank everything** and write the findings report.

## Output format

```
# DDQ Red-Flag Scan — [Manager / Fund]
Document: [title, date/version] | Comparison materials: [list or "none"]
Sections covered: [list] | Standard sections absent: [list]

## Summary
[3–5 sentences: overall responsiveness, the 2–3 findings that matter most,
and whether the pattern suggests sloppiness or deliberate opacity.]

Findings: [N] HIGH / [N] MEDIUM / [N] LOW

## HIGH severity
### H1. [Short title]
- **Location:** [section / question number / page]
- **Exact language:** > "[verbatim quote]"  — or — **Missing:** [the disclosure that should be here]
- **Why it matters:** [1–3 sentences]
- **Possible benign explanation:** [1 sentence — there often is one]
- **Follow-up to ask:** "[specific question]"

[Repeat per finding; same structure for MEDIUM and LOW.]

## Cross-document inconsistencies
| Claim | DDQ says ([loc]) | Other doc says ([doc, loc]) |
|---|---|---|

## Disclosure checklist
| Standard disclosure | Status | Note |
|---|---|---|
[answered / partial / absent for each checklist item]

## Follow-up question list (consolidated)
[All follow-ups in one copy-paste-ready block, ordered by severity.]
```

Severity scale — **HIGH:** missing or evasive on compliance history, valuation of level-3 assets, conflicts, key-person, or a direct contradiction with other documents. **MEDIUM:** vague on material operational items, internal inconsistencies, boilerplate where specifics were asked. **LOW:** sloppiness, stale dates, minor gaps.

## Guardrails

- **Quote exactly.** Every finding about language must reproduce the language verbatim with its location. No paraphrased accusations.
- **An absence is a finding, not an allegation.** "The DDQ does not disclose X" is correct; "the manager is hiding X" is not. Always offer the benign explanation where one plausibly exists.
- **Never fabricate document content,** question numbers, or quotes. If text extraction from a PDF is uncertain, say so and flag the section for manual reading.
- **Fact vs. inference:** the quote is fact; the interpretation is inference — keep them visually separate in every finding.
- **This is a document scan, not operational due diligence.** It does not replace background checks, service-provider verification, or on-site ODD, and it is not an investment or redemption recommendation.
- **Confidentiality:** DDQs are confidential. Remind the user to handle the scan output under the same restrictions as the source document.

## Quality checks

- [ ] Every language-based finding has a verbatim quote and location
- [ ] Every absence-based finding names the specific standard disclosure
- [ ] Each HIGH finding includes a possible benign explanation
- [ ] Every checklist item has a status
- [ ] Every finding has a concrete follow-up question
- [ ] No claim about other documents without a quote from that document

## Example prompt

> "Attached: Crestline Partners' completed DDQ and their pitch deck. Scan the DDQ for red flags — especially valuation policy and compliance history — and check whether anything in it contradicts the deck. Rank findings by severity and give me the follow-up questions for the ODD call."
