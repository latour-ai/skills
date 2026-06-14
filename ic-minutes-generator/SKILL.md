---
name: ic-minutes-generator
description: Turn an investment committee meeting transcript or detailed notes into formal IC minutes — attendees, agenda items, balanced per-item discussion summaries including dissent and risks raised, decisions with vote outcomes, action items with owners, and documents referenced. Built for fund operations, compliance, and CCO teams that need a defensible written record. Trigger on "draft IC minutes", "turn this transcript into minutes", "minutes for the investment committee meeting", "formalize these IC notes", "document the committee's decision", "write up Tuesday's IC", or when a user provides an IC/valuation committee/credit committee transcript and needs the formal record. Accuracy over polish — flags inaudible or ambiguous passages rather than guessing. Do NOT use for client/prospect call recaps and follow-up emails — use the call-transcript-followup skill. Do NOT use for portfolio company board packs — use the board-pack-kpi-digest skill.
---

# IC Minutes Generator

Convert an investment committee transcript or detailed meeting notes into formal minutes: who attended, what was discussed item by item (including the disagreements and the risks raised, not just the conclusion), what was decided and by what vote, who owns which action, and which documents the committee relied on. Written for the audience minutes actually have: future-you, your auditors, and — for registered advisers — potentially SEC examiners.

## Why this skill exists

IC minutes are one of the most consequential documents a fund produces and one of the most carelessly made. They get drafted from memory three days later, sanitized into "the committee discussed and approved," and stripped of exactly the content that protects the firm — the dissent, the risk discussion, the conditions attached to approval. When an examiner or a litigant asks "show me the committee considered valuation risk," minutes that say "approved 4–0" are worth nothing. A transcript contains everything needed; turning it into a faithful, balanced record is exacting work that this skill does properly — with the discipline that ambiguity gets flagged, never smoothed over.

## Inputs

**Required:**
- The meeting transcript (preferred) or detailed contemporaneous notes
- Meeting identity: committee name, date, fund/vehicle if applicable

**Optional but high-value:**
- Attendee list with roles (transcripts mangle names; a roster fixes attribution)
- The agenda (gives the minutes their structure; otherwise structure is inferred and labeled)
- The firm's prior minutes format (match it — consistency matters to auditors)
- Voting rules (quorum, who votes vs. advises, whether abstentions are recorded)
- Documents distributed before/at the meeting

**Missing-input behavior:** If the transcript/notes are missing, ask once. If attendee roles or voting rules are missing, draft with **[CONFIRM: …]** placeholders rather than guessing — a wrong vote count in minutes is worse than a placeholder. If no agenda exists, infer item boundaries from the discussion and note "agenda structure inferred from transcript."

## How it works

1. **Establish the frame:** committee, date, time, location/medium, attendees (present/absent/guests, with roles), quorum status if rules were provided, and who chaired.
2. **Segment the transcript by agenda item.** Mark where each item starts and ends; discussion that wanders gets attributed to the item it substantively belongs to.
3. **Summarize discussion per item — balanced by construction.** For each item capture: the proposal or matter presented and by whom; the material points raised in support; **the concerns, risks, and dissenting views raised, attributed appropriately**; questions asked and whether they were answered or deferred; any conditions or modifications introduced during discussion. Minutes are a summary, not a transcript — but a summary that omits the pushback is a misrepresentation.
4. **Record decisions with precision.** For each decision: the exact matter decided (including amendments adopted along the way — the thing voted on is often not the thing originally proposed), the vote outcome (for/against/abstain/recused, by name where the transcript supports it), and conditions attached to approval. Recusals and their stated reasons always get recorded.
5. **Extract action items:** task, owner, deadline if stated. Only what was actually assigned — don't invent owners for orphaned tasks; flag them as **[unassigned in meeting]**.
6. **List documents referenced:** memos, models, valuation reports, third-party reports the committee discussed or relied on, with dates/versions if mentioned.
7. **Flag, don't guess.** Every inaudible passage, ambiguous attribution, unclear vote, or contradictory moment gets an explicit marker: **[INAUDIBLE — transcript 00:42:15]**, **[AMBIGUOUS: unclear whether the motion included the fee waiver — confirm with chair]**. These flags are for the human finalizer and should be resolved before the minutes are adopted.
8. **Close with the formalities:** next meeting if stated, adjournment time, and a signature/approval block per the firm's convention.

## Output format

```
# Minutes of the [Committee Name]
**[Firm name]** | Meeting of [date], [start–end time], [location/medium]
STATUS: DRAFT — for review and adoption by the committee

## Attendance
Present (voting): … | Present (non-voting/guests): … | Absent: …
Chair: … | Quorum: [met / [CONFIRM]]

## Documents Distributed / Referenced
1. [Title, date/version]

## Item 1 — [Agenda item title]
**Presented by:** …
**Summary of discussion:** [Balanced narrative: proposal, support, concerns and
dissent with attribution, questions and answers, conditions raised.]
**Decision:** [Exact matter as voted, including amendments.]
**Vote:** [For: names/count | Against: … | Abstain: … | Recused: … (reason)]
**Action items:** [task — owner — due date]

(repeat per item)

## Consolidated Action Items
| # | Action | Owner | Due | Source Item |
|---|---|---|---|---|

## Open Flags for Finalization
Every [INAUDIBLE], [AMBIGUOUS], [CONFIRM] item listed with location.

## Adjournment & Approval
Adjourned [time]. Next meeting: [date or "not stated"].
Minutes prepared by: ____ | Approved by the Committee on: ____
```

## Level-of-detail calibration

The recurring judgment call in minutes is granularity. Working rules:

- **Decisions: maximum precision.** Exact matter, exact vote, exact conditions. This is the part regulators read first.
- **Discussion: summary with substance.** Capture each materially distinct point once, attributed; don't capture every restatement of it. "Ms. Chen raised concentration risk in the top customer; the deal team responded that the contract renews through 2028" — not three paragraphs of back-and-forth.
- **Dissent: more detail, not less.** A lone objection gets its reasoning recorded, even briefly. Sanitizing dissent is the most damaging common edit.
- **Numbers discussed: only as discussed.** If the committee discussed "a roughly 12x entry multiple," the minutes say that — they don't substitute the precise figure from the memo unless it was stated.
- **Humor, tangents, personnel chatter: omit** unless it bears on the decision (a joke about a target's accounting is, awkwardly, discussion of accounting risk — capture the substance, not the joke).
- **Recurring items (valuation marks, watch lists):** consistent structure period over period beats prose variety; auditors compare across meetings.

## Guardrails

- **Accuracy over polish — these minutes may be read by regulators, auditors, or opposing counsel.** Never invent statements, votes, attendees, or attributions. Never paraphrase into quotation marks.
- **Never resolve ambiguity by choosing the plausible reading.** Unclear vote? Flag it. Two people possibly named "Mike"? Flag it. The flag list exists so a human resolves every one before adoption.
- **Dissent and risk discussion are mandatory content**, not optional color. If an item genuinely had no pushback, the minutes may say so — but check the transcript before concluding that.
- **No editorializing.** Minutes record what occurred; they do not assess whether the decision was good, characterize tone beyond what was said, or add context the meeting didn't contain.
- **The DRAFT banner stays** until a human finalizes; this skill never produces "final" minutes.
- **Confidentiality:** IC discussions routinely contain MNPI and deal-confidential information — firm-approved AI environment assumed; distribution of the draft should follow the firm's existing minutes-handling practice.

## Quality checks

- Every decision states the exact matter voted on, post-amendment?
- Vote counts add up against the voting-member attendance?
- Each substantive item's summary includes concerns/dissent, or an explicit "no objections raised"?
- All flags consolidated in the finalization list — none buried?
- No quoted language that isn't verbatim from the transcript?
- DRAFT status and approval block present?

## Example prompts

> "Here's the transcript of yesterday's investment committee — we considered the Project Atlas add-on acquisition and the Q2 valuation marks. Five voting members, Sarah recused on Atlas (her brother works at the target). Draft the minutes in our usual format (attaching last month's as a template). Flag anything where the vote or wording is unclear — our CCO reviews these and we're a registered adviser."

> "Valuation committee call, transcript attached, four marks reviewed and one written down. No formal agenda existed — infer the structure and say so. Attendee roster pasted below."

> "These are my typed notes from Tuesday's credit committee (no recording — counsel's preference). Turn them into draft minutes and be aggressive with [CONFIRM] flags wherever my notes are thin."

## Works well with

The diligence materials behind an IC decision often come from **cim-first-pass** or **hedge-fund-diligence** outputs; the assigned action items can flow into your task tool of choice via **call-transcript-followup** conventions.
