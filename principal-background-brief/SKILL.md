---
name: principal-background-brief
description: >-
  Compile a sourced background brief on a fund's key principals from the
  public record — Form ADV disclosures, FINRA BrokerCheck and IAPD items,
  litigation and press coverage, a reconstructed employment timeline
  compared line by line against the official bio, and departure
  circumstances from prior firms where the record supports them. Separates
  verified facts (with sources) from unresolved questions, and feeds the
  follow-ups into reference calls. For allocators, fund-of-funds and OCIO
  diligence teams, endowments, foundations, and family offices building
  the ODD file at initial diligence or on a key-person change. Trigger on
  phrases like "background check on [principal]," "run the principals,"
  "check the bios against the record," "any regulatory history on this
  manager," "BrokerCheck and ADV review," or when a user attaches official
  bios or a DDQ personnel section. Do NOT use for a general pre-meeting
  brief on a person — use the professional-profile-brief skill. Do NOT use
  for scanning a full DDQ for red flags — use the ddq-red-flag-scanner
  skill. Never speculates about non-public conduct; anything unconfirmable
  is marked as such.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Principal Background Brief

The disqualifying facts in manager diligence are rarely in the deck — they are in the public record, waiting for someone to cross-reference it against the manager's own narrative. The regulatory event the bio omits, the departure that was not voluntary, the two-year gap nobody mentions, the outside affiliation that never made it into the DDQ. This skill compiles the background review on a fund's key principals into a sourced brief the ODD file can stand behind: verified facts with citations, discrepancies between bio and record, unresolved questions, and the follow-ups those questions generate for the reference calls.

## Why this skill exists

Principal background work fails in one of two directions. Done shallowly — a quick web search and a skim of the bio — it becomes a checkbox that would not have caught any of the cases that later became famous. Done properly, it means pulling Form ADV Item 11 and the brochure supplements, running BrokerCheck and IAPD on every registered principal, searching litigation dockets and press, rebuilding the employment timeline from independent sources, and then comparing all of it against what the manager chose to tell you. That is hours of tedious cross-referencing per principal, so it gets outsourced expensively, or deferred, or done once at initial diligence and never refreshed when a key person changes.

The subtler failure is epistemic. Background work generates a mix of hard facts, absences, and inferences — and briefs routinely launder one into another. "No BrokerCheck disclosures" quietly becomes "clean record" (it is not; most fund principals were never FINRA-registered). A bio gap becomes "probably left under a cloud" (it is a gap, nothing more, until a source says otherwise). A lawsuit naming the firm becomes a lawsuit naming the person. Once an inference is written down as a finding, it propagates through the diligence file with unearned authority — in either direction.

The brief this skill produces is organized around that distinction. Every line is either a verified fact with a source, an identified discrepancy stated neutrally, or an open question routed to the step that can actually answer it — usually a reference call or a direct question to the manager. Nothing in between.

## Inputs

**Required:**
- The principals in scope: names, titles, and the firm
- **The manager's own account** — official bios, the DDQ personnel section, or the marketing deck's team page. The comparison against this narrative is the core of the brief; without it, the output is a record summary, not a background check.

**Optional but high-value:**
- **Pulled records, attached** — Form ADV Parts 1 and 2 with brochure supplements, BrokerCheck or IAPD reports, docket search results, news clippings. Attached records are the strongest basis; the brief cites them directly
- Live web access, where available, to search regulatory databases, dockets, and press directly
- LinkedIn profiles or other self-published histories, as a second version of the narrative to triangulate
- Prior background briefs on the same principals, for a what-changed comparison
- The open questions already in the diligence file, so discrepancies can be connected to them

**Missing-input behavior:** With bios but no pulled records and no web access, the skill inverts into planning mode: it produces the record-pull checklist — which databases to query for each principal and what to look for, based on what the bio claims — plus the internal-consistency review of the bios themselves, which regularly surfaces gaps and oddities on its own. It says plainly that no record checking was performed. It never simulates a database result, never asserts that a search "found nothing" unless that search was actually run and provided, and never fills a timeline gap with a guess.

## How it works

1. **Fix each principal's identity first.** Full name, common variants, approximate age or graduation years, CRD number if registered. Background work on a common name without disambiguators produces false positives, and a false-positive regulatory hit attributed to the wrong person is the worst error this work can make. Flag identity uncertainty explicitly wherever it exists.
2. **Extract the official narrative into a claims table** — every firm, title, date range, credential, and accomplishment the bio asserts, per principal. This is the thing the record will be checked against; vague bio language ("spent over a decade at leading firms") gets flagged as unverifiable by construction.
3. **Work the regulatory record.** Form ADV Item 11 disciplinary disclosures and the brochure supplements for the individuals; BrokerCheck and IAPD for anyone ever registered, with each disclosure item's date, allegation, and disposition. Note the coverage limits honestly — an unregistered principal has no BrokerCheck file to be clean.
4. **Work litigation and press,** distinguishing three things that briefs habitually blur: the principal as named party, the principal's firm as party with the principal merely employed there, and the principal merely mentioned or quoted. Only the first is a personal litigation history. Note dispositions where the record shows them; a dismissed case is reported as dismissed.
5. **Reconstruct the employment timeline from the record** — filings, registrations, press, self-published histories — independently of the bio, with a source per entry.
6. **Run the line-by-line comparison:** reconstructed timeline against official narrative. Flag every gap of more than a few months, every omitted employer or role, every title or date mismatch, and every affiliation in the record that the manager's materials do not mention — outside business activities, board seats, other funds. State each discrepancy neutrally: what the bio says, what the record shows, no motive attached.
7. **Assess departure circumstances only where the record supports them** — a filing, a press account, a regulatory document. Where the circumstances are not determinable from public sources, say exactly that, and route the question to the reference calls.
8. **Sort everything into the three buckets** — verified facts with sources, discrepancies and open questions, and items checked with nothing found (scoped: which sources, what dates) — and resist the pull to editorialize. The reader is a professional; the facts arranged clearly are the analysis.
9. **Write the follow-ups:** the specific questions for the manager and the specific probes for each reference call that the open questions generate, each traceable to the discrepancy that motivated it.

## Output format

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# Principal Background Brief — [firm]
Principals: [names, titles] | Prepared: [date]
Basis: [attached records / live search / bios only — record pull pending]
Sources checked: [list, with dates] | Not checked: [list, with why]

## Summary
[Per principal, 2–3 sentences: the material verified facts, the most
significant open question, and whether anything found is potentially
disqualifying or merely needs an answer.]

## [Principal name] — [title]
### Verified facts
| Fact | Source | Date |
|---|---|---|

### Regulatory record
[ADV / BrokerCheck / IAPD items with date, allegation, disposition —
or "no items in sources checked," scoped, with registration status noted.]

### Litigation and press
| Matter | Principal's role (party / firm party / mentioned) | Status | Source |
|---|---|---|---|

### Timeline: record vs. official bio
| Period | Record shows (source) | Bio says | Discrepancy |
|---|---|---|---|

### Open questions
[Each stated neutrally, with what would resolve it.]

## Follow-ups
| # | Question | Ask whom (manager / reference type) | Motivated by |
|---|---|---|---|
```

## The public-record checklist

What to pull, per principal, and what each source can and cannot tell you:

- **Form ADV Part 1, Item 11** — the firm's disclosed disciplinary events: criminal, regulatory, and civil judicial. Firm-level; a clean Item 11 does not clear any individual.
- **Form ADV Part 2B brochure supplements** — the individual-level disclosure document: disciplinary history, other business activities, additional compensation. The most commonly skipped source, and the one where individual disclosures actually live.
- **FINRA BrokerCheck / SEC IAPD** — disclosure events, employment history as registered, exam history. Only covers registered persons and registered periods; many hedge fund and PE principals have thin or no files, which is an absence of coverage, not a clean bill.
- **Litigation dockets** — federal (PACER) and relevant state courts. Search the person and their prior firms; read the caption carefully before attributing anything to the individual.
- **SEC enforcement releases and administrative proceedings** — searchable independently of the ADV, and occasionally ahead of it.
- **Press archive** — the departure coverage from prior firms is where "left to pursue other opportunities" meets contemporaneous reporting.
- **Prior firm history** — registration records and old filings often show employers and date ranges the current bio compresses or omits. Gaps between the record and the bio are the single highest-yield finding in this work.
- **Affiliations** — board seats, other advisory entities, related vehicles, outside business activities. Undisclosed current affiliations are a conflicts question; undisclosed past ones are a candor question.

## Guardrails

- **Never speculate about non-public conduct.** No inference about why someone left, what a settlement implies, or what a bio gap conceals. The brief reports what the record shows and marks everything else as an open question. This is the skill's defining rule, and it protects the firm as much as the principal — an unfounded inference in a diligence file is a liability in both directions.
- **Never present inference as finding.** Every line is sourced fact, neutrally stated discrepancy, or open question — and the reader can always tell which.
- **Absence of a record is not a clean record.** Every "nothing found" is scoped to the sources actually checked and their coverage limits, with registration status noted.
- **Identity discipline.** No hit is attributed to a principal without the identity being established; uncertain matches are flagged as uncertain, prominently.
- **Party versus mentioned, always distinguished** in litigation and press. Firm-level events are never silently attributed to individuals.
- **Dispositions travel with allegations.** A dismissed case, a withdrawn complaint, or an expunged item is reported with its disposition, not as a bare accusation.
- **Public record only.** The skill does not use, request, or infer from non-public personal information, and it is not a consumer report or an FCRA-governed background check — employment-screening use is out of scope.
- **Not investment advice.** The brief informs the diligence file; it does not conclude on the manager.
- **Confidentiality:** the manager's DDQ and bios are confidential diligence materials, and the brief itself is sensitive — it concerns named individuals. Assume a firm-approved AI environment and restrict circulation to the diligence and compliance team.

## Example prompts

> "Attached: official bios and the DDQ personnel section for the three founding partners of [fund], plus their BrokerCheck reports and the firm's ADV. Compile the background brief — timeline versus bio line by line, every regulatory item with disposition, and the follow-ups for our reference calls next week."

> "Key-person change at [fund] — a new CIO joining from [prior firm]. Here's the announcement bio and his LinkedIn. We haven't pulled records yet: give me the record-pull checklist specific to his claimed history, plus anything the bio itself doesn't add up on."

> "Re-running backgrounds on [fund]'s principals ahead of a re-up; our 2023 brief is attached along with fresh ADV and docket pulls. What's changed since last time, and does anything new need to go to the ODD committee?"

## Works well with

Chain with **hedge-fund-diligence** — the first-pass note identifies which principals are key, and this brief deepens them for the ODD file. The open questions feed directly into the reference calls, where they become probes for the people who actually know. Use **professional-profile-brief** instead when the need is a general pre-meeting brief on a person, not an adverse-record review.
