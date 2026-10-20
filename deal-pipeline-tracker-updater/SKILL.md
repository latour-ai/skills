---
name: deal-pipeline-tracker-updater
description: >-
  Keep the deal pipeline tracker current from the communication exhaust
  instead of from someone remembering to update it — on a schedule, read
  the shared deal inbox and deal-team chat (or an exported batch of emails
  and messages), work out which messages concern which live opportunity,
  and propose the updates: stage changes, new intermediary contacts, moved
  bid dates and process deadlines, diligence items requested, and pass
  decisions, each cited to its source message, with a separate list of the
  changes it was not confident enough to apply and the pre-meeting delta of
  what moved, what has gone quiet, and what has no next step. For
  operations leads and deal teams at private equity and private credit
  firms whose pipeline meeting runs on a shared tracker. Trigger on phrases
  like "update the pipeline tracker," "what moved this week," "sync the
  tracker from the inbox," "pipeline delta before Tuesday," "which deals
  went quiet," "pull the bid dates out of the deal inbox," "reconcile the
  tracker against email," or when a user provides exported deal emails
  alongside a pipeline spreadsheet. Do NOT use for the LP fundraising
  pipeline. Do NOT use for screening brand-new inbound teasers or CIMs —
  use the cim-first-pass skill. Do NOT use for a personal inbox's action
  items — use the inbox-triage skill. Do NOT use for sourcing sweeps for
  add-on targets. The tracker is the system of record; this skill proposes
  changes to it and never overwrites a human entry without a citation.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Deal Pipeline Tracker Updater

Every deal team has a pipeline tracker and every pipeline tracker is a week stale, because the people who know what moved are the ones with the least time to type it in. The information is not missing — it is sitting in the deal inbox and the team chat, in the banker's note that the bid date slipped, the associate's message that management meetings are set, the partner's one-line "let's pass." This reads that traffic on a schedule, matches each message to the opportunity it concerns, and turns the tracker into a current record: stage changes, contacts, dates, diligence asks, and passes, each cited to the message that supports it, with a separate list of what it was not sure enough to apply. The pipeline meeting then starts from the record rather than from reconstructing it.

## Why this skill exists

Pipeline trackers rot for a structural reason, not a discipline one. The tracker is a shared artifact, but the events that should update it happen in private channels — a reply to a banker, a chat thread, a call summarized in one line to a colleague — and the person who witnessed the event is the one with a bid due Friday. Updating the record is a task with no natural owner and no natural moment, so it gets batched into the twenty minutes before the meeting, when memory is already lossy. The result is a tracker that is accurate about the deals people care about and fiction about the rest, which is exactly backwards: the meeting exists to catch the deals nobody is watching.

The raw material for a current tracker already exists in full. A process letter states its own deadlines; an intermediary's introduction email carries the contact's name, firm, and role; a chat message saying "IOI went in at 2pm" is a stage change with a timestamp. Nothing has to be remembered — it has to be read, attributed to the right opportunity, and carried across. The hard part is the attribution: deal traffic refers to the same opportunity by a project code name, the company's real name, the banker's name, and "that distribution deal," often in the same week, and a message that mentions two deals in one sentence has to be split, not guessed at.

A fully automatic write to the tracker is the wrong goal. The tracker is the system of record and the deal team has to trust it more after the run than before, which means every change must carry the sentence that justified it, and every uncertain reading must land in a review list rather than in the record. A cited change log is worth more than a silently perfect one: the associate scanning it Tuesday morning can confirm ten changes in two minutes, catch the one misread, and correct the alias that caused it — and the run gets better the next week. A tracker that updates itself without showing its work gets reconciled by hand anyway, which is the problem it was meant to solve.

## Inputs

**Required:**
- The message traffic for the window: a connected shared deal inbox and deal-team chat, or an exported batch of emails and messages with sender, timestamp, subject, and body
- The current pipeline tracker — spreadsheet, CRM export, or database view — with at least opportunity name, stage, owner, and key dates

**Optional but high-value:**
- **The alias list** — project code names, company names, intermediary firm names, and the shorthand the team actually uses, mapped to tracker entries; without it the first run builds one and the review list is longer
- The firm's stage definitions and the events that move a deal between them (what counts as "in process" versus "active diligence" is a house convention, not a standard)
- The intermediary roster: banker and broker contacts already known, so new contacts are detected rather than re-recorded
- The date of the last pipeline meeting, which sets the delta window
- A silence threshold per stage — how many days without traffic is normal for an early look versus a live process

**Missing-input behavior:** The baseline works from exported messages alone; a connected inbox and chat are the upgrade, not the requirement. Without a tracker, build a proposed one from the messages — opportunities, apparent stage, contacts, and dates as the traffic states them — and say plainly that it is a reconstruction for the team to correct, not a record. Without stage definitions, use the conventional ladder in the reference section below and label stage assignments as inferred. Never invent a stage change or a date: a deal is moved only when a message says it moved, and a date is entered only as a message states it. A mention that could concern one of two opportunities, a date without a clear referent, or an internal remark that could be a pass or a mood goes to the review list with the ambiguity spelled out, never into the tracker.

## How it works

1. **Build the opportunity index.** From the tracker and any alias list, assemble for each live opportunity every name it travels under: project code name, company name, sponsor or seller, the intermediary firm and individual, the sector shorthand the team uses, and the thread subjects that have carried it before. Treat closed and passed opportunities as part of the index too, so a banker reviving a dead process is matched rather than created as new.
2. **Classify every message** to one opportunity, several, or none, with a confidence and the evidence: a code name in the subject is near-certain, a banker's name plus a sector reference is probable, "the deal we discussed" is a guess. Internal newsletters, calendar noise, and general market chatter are "none" and are dropped without comment. A message that mentions two opportunities is split into two attributions, each with its own supporting sentence.
3. **Extract the update candidates** from each attributed message — stage change, new contact, moved or new date, diligence item requested, pass decision — and for each, quote the sentence that supports it. Dates are normalized to the tracker's format with the original phrasing kept ("end of next week" from a Thursday email is a date plus a note that it was relative).
4. **Reconcile across messages.** Where the window contains both the process letter's original bid date and a later note moving it, the later governs and the log shows the sequence. Where two messages disagree with no ordering to resolve them, neither is applied and the conflict is listed. Where a chat message and an email describe the same event, record it once with both citations.
5. **Reconcile against the tracker.** A candidate that matches the current record is noise, not a change. A candidate that moves a deal backward — a stage that regresses, a date that comes earlier — is applied only when the message is explicit, because backward moves are far more often a misattribution than a real event. A candidate that contradicts a human entry made after the message's timestamp is queued, since the human likely knew more.
6. **Apply only high-confidence changes** and queue the rest with the reason: ambiguous opportunity, relative date without an anchor, indirect pass language, a stage word the firm's definitions do not use, a contact whose firm cannot be identified. The review list is a product, not an apology; write each item so a reader can resolve it in one glance.
7. **Detect silence and staleness.** List every opportunity with no traffic in more than the threshold for its stage, and every tracker date that has passed without a message marking the event — a bid date that came and went in silence is either a missed submission or a missed update, and both belong in front of the meeting. Note opportunities with no owner or no recorded next step.
8. **Produce the change log and the pre-meeting summary:** applied changes with citations, the review list, silent and stale items, new contacts, and a stage-by-stage snapshot with the delta since the last meeting. The summary is written for the person running the meeting — what moved, what stalled, what needs a decision — in the order they would raise it.
9. **Keep the index current.** Every alias the run learned, every new intermediary contact, and every review-list resolution the team makes becomes part of the next run's inputs, so the same ambiguity is not surfaced twice.

## Output format

A skeleton to adapt — the citation column and the review list are the parts that must survive.

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# Pipeline update — [run date]
Window: [from] → [to] | Sources: [inbox / chat / export] | Messages: [N] read, [N] attributed, [N] dropped as unrelated
Tracker: [file / system, as of date] | Last meeting: [date]

## Applied changes
| Opportunity | Field | Old | New | Source message |
|---|---|---|---|---|
| [code name] | Stage | [ ] | [ ] | [sender, date, subject — quoted sentence] |
| [code name] | Bid date | [ ] | [ ] | [ ] |
| [code name] | Diligence requested | — | [item] | [ ] |
| [code name] | Status | Active | Passed | [internal statement quoted] |

## Needs review
| Opportunity (best guess) | Proposed change | Reason held | Source message |
|---|---|---|---|
| [ ] | [ ] | [ambiguous referent / relative date / indirect pass language / conflicts with later human entry] | [ ] |

## Silent and stale
- [opportunity] — no traffic since [date] ([N] days; threshold for [stage] is [N])
- [opportunity] — [date field] of [date] passed with no message marking it
- [opportunity] — no owner / no next step recorded

## New contacts
| Name | Firm | Role | Opportunity | Source message |
|---|---|---|---|---|

## Pipeline snapshot
| Stage | Count | Δ since [last meeting] | Moved in | Moved out |
|---|---|---|---|---|

## Before the meeting
[Three to six lines: what moved, what stalled, what needs a decision, in the order to raise them.]
```

## Reading deal traffic — what counts as a stage change

Deal correspondence rarely announces a stage change; it implies one, and the implication is only safe to record when it is grounded in a concrete event. The ladder below is a conventional default for a sponsor or private credit pipeline — replace it with the firm's own definitions whenever they exist.

- **Process letters set the calendar.** A first-round process letter states the IOI deadline, data room timing, and often the management meeting window; a second-round letter states the LOI or final bid date, markup timing, and exclusivity expectations. Every date in a process letter is a tracker date, and a later email from the same banker moving one of them supersedes it. "We are extending the timeline for select parties" is a moved date only if the firm is one of the parties.
- **The milestones that move a deal.** Teaser received and NDA signed are entry events. CIM received or data room opened marks a live process. IOI submitted is a stage in itself, and IOI accepted — usually phrased as "invited to the second round" or "management meetings" — is the next. LOI submitted, then LOI accepted or exclusivity granted, then confirmatory diligence, then signed. In private credit the analogues are term sheet issued, term sheet accepted, and commitment letter; the same logic applies.
- **Management meetings are a stage, not a courtesy.** An invitation to meet management means the firm advanced; a message scheduling the meeting is a stage change with a date attached. A meeting that was scheduled and then never mentioned again is a silence signal.
- **Exclusivity language is precise.** "We'd like to move forward with you" is warm but not exclusivity; "we are prepared to grant a [N]-day exclusivity period" is. Record exclusivity only from an explicit grant, with its expiry as a tracker date.
- **Passes are almost never explicit from the other side.** A banker rarely writes "you are out." The signals are a thank-you note with no next step, "we have decided to move forward with another party," a data room access that quietly ends, or the process simply going silent past its stated decision date. These go to the review list as probable losses, not to the tracker as passes. The firm's own pass is recorded only from an explicit internal statement — a partner's "we're passing" in chat or an email to the banker saying so — never inferred from an associate's skepticism or a thread that trailed off.
- **Diligence requests arrive as lists and as asides.** A formal request list from counsel or a QoE provider is easy to extract; "can you also send the customer cohort data by Wednesday" buried in a scheduling email is the kind that gets lost, and it carries a date.
- **Intermediary etiquette encodes information.** A banker who copies a managing director on a reply is escalating; one who moves from the deal-specific thread to a general "let's catch up" is often signaling the process has moved on. A new name in the cc line at an advisory firm is a new contact worth recording with its apparent role. None of this is a stage change; all of it belongs in the pre-meeting summary when it changes the read.

## Guardrails

- **Never write an update it cannot cite.** Every applied change carries the sender, date, and quoted sentence. A change without a message behind it does not exist.
- **Low-confidence changes are proposed, not applied.** The review list is where uncertainty lives; the tracker is where confirmed events live. Erring toward the review list costs the team a glance; erring toward the tracker costs them trust in the record.
- **Pass decisions are recorded only from an explicit internal statement.** A counterparty's silence, a lukewarm banker note, or an associate's doubt is a review-list item, never a recorded pass. Marking a live deal as passed on inference is the single most damaging error the skill can make.
- **The tracker is the system of record.** The skill proposes changes to it, applies the confident ones with citations, and never deletes an entry or overwrites a human edit made after the source message.
- **Deal traffic is confidential.** Process letters, CIM references, and counterparty names are covered by NDA; code names exist for a reason. Assume a firm-approved AI environment, keep code names as the primary identifier in the output, and reproduce nothing from the messages beyond the sentence that supports each change.
- **No external sending.** The skill reads correspondence and writes to the internal tracker. It does not reply to bankers, acknowledge process letters, or send anything outside the firm.
- **Not advice.** The output is an operational record of what the traffic says, not a view on which deals to pursue, what to bid, or whether a process is worth staying in.

## Example prompts

> "Friday export attached — about 140 emails from the deals@ inbox and the week's deal-channel chat, plus the tracker as of last Tuesday. Match everything to our live opportunities (code names are the [project-name] convention; the alias sheet is tab two), apply the changes you're sure of with citations, and give me the list of what you weren't sure about. Silence threshold is 10 days for anything past IOI, 21 for early looks."

> "You have the shared deal inbox and the deal-team channel connected. Run every Friday at 4pm against the pipeline database: apply confident stage, date, contact, and diligence-request changes; queue the rest; flag silent deals and passed dates. Post the change log and the Monday-meeting delta to the pipeline channel, and update the alias list with anything new you learned."

> "Our tracker has been unmaintained since the associate who owned it left in [month]. Here is the full quarter of deal inbox traffic and chat history, plus the last version of the tracker anyone trusted. Rebuild the record from the messages — every opportunity, its current stage as best the traffic supports, dates, contacts, and status — labeled as a reconstruction, with the ambiguous items separated out so we can resolve them in one sitting before Tuesday."

## Works well with

**cim-first-pass** sits at the front of the funnel — it screens what enters the pipeline, and this keeps the record current once it is there; a first-pass recommendation to pursue is the entry event this skill expects to find.
