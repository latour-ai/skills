---
name: no-recording
description: >-
  Turn a spoken or typed post-meeting brain dump into a complete record of a
  meeting nobody recorded: meeting notes (Markdown plus a Word copy), a
  follow-up email draft that is never sent, tasks for what the user owes and
  waiting-on items for what the other side owes, and an optional CRM activity
  note. Attendees, titles, firms and the meeting's purpose are pulled from the
  calendar and email, so the user never types them. Works with Microsoft 365
  (Outlook mail and calendar) or Google Workspace (Gmail and Google Calendar),
  any task tool (Microsoft To Do, Planner, Asana, Jira, Todoist, Monday,
  ClickUp, Notion, or none), and any CRM (Salesforce, HubSpot, Dynamics 365,
  DealCloud, Affinity, or none), chosen once in a short first-run setup. For
  corporate and investment professionals who take meetings without a
  notetaker: in-person visits, client dinners, calls where recording was not
  appropriate. Trigger on "/no-recording", "just got out of a meeting
  with...", "debrief my call with...", "write up this meeting", "I just met
  [name]", "log my meeting with [name]", "set up no-recording", "change my
  no-recording settings", or a dictated or pasted brain dump that names a
  person or firm from a meeting that just happened. Do NOT use when a
  transcript or recording exists; use the call-transcript-followup skill. Do
  NOT use for investment committee meetings; use the ic-minutes-generator
  skill. Do NOT use to prepare for a meeting that has not happened yet.
license: MIT
metadata:
  author: latourai
  version: '2.0'
---

# No-Recording Meeting Debrief

The meeting wasn't recorded. Right afterwards the user talks or types for about a minute, usually by voice dictation, so the input is already clean prose. This skill turns that brain dump into a finished post-meeting package: notes, a follow-up email draft, tasks, and, if the firm uses one, a CRM activity note. The brain dump supplies what was said. The calendar and email supply the tedious details: who attended, their titles, their firm, and why the meeting was booked.

It works with whatever systems the user's firm runs. A one-time setup records which email and calendar, task tool, CRM and notes location to use, and every later run goes straight to work.

## Why this skill exists

Many of the most important conversations in a working week happen with no notetaker running: a coffee with a prospect, an in-person client visit, a call where asking to record would have changed the tone. Those are exactly the meetings whose details are gone by the end of the day, and the cost shows up later, when someone needs to know what was promised, to whom, and by when.

The bottleneck is not the thinking; the user knows what happened. It is the typing: looking up attendee titles, writing the notes, drafting the recap email, creating the tasks, logging the activity in the CRM. Each step takes a few minutes, so together they get postponed, and postponed write-ups get written from fading memory or not at all.

The notes matter for a second reason. With no transcript, they are the only lasting record of the meeting, and later AI sessions will read them to prepare the next meeting, draft a proposal, answer "where do we stand with this firm?" or write a follow-up. So the notes are written for a future reader with no other context, not only for a person skimming today:

- Name every person, firm, product, tool and number in full. Write "Northbridge Capital Partners" and "Dana Reyes (Harbor Analytics)", not "they" or "Dana".
- Use absolute dates, never relative ones.
- Keep specifics and the user's own phrasing over polished generalities. A detail that seems minor now (a system they use, a team they mentioned, a hesitation) is often what a later question needs.
- Record conflicts with earlier sources (for example, a title in the brain dump that differs from the email signature) instead of silently resolving them.

## Inputs

**Required:**
- The brain dump: spoken or typed, in any order. Who was there, what was discussed, what was agreed, what the user owes, what the other side owes.

**Read from connected systems (never asked of the user):**
- The calendar event: title, time, location or video link, description, attendee list and RSVP status
- Email: each external attendee's most recent message (for the signature block) and the latest thread with that person or firm
- The CRM record for the firm and contacts, if a CRM is connected (to match the right account and avoid creating duplicates)

**Set once in setup (see step 0):** email and calendar system, task tool, CRM and how to use it, where notes are saved, internal email domains, and any firm rules.

**Missing-input behavior:** Gaps never block a run. If the calendar event can't be found, use what the brain dump says and note it. If no source has an attendee's title, write "title unknown"; never guess one. Leave a due date empty when none was given. If a connected system is missing or fails, finish everything else and give that output as copy-paste text, saying which system failed.

## How it works

### 0. First-run setup (once, then only when asked)

Run setup the first time the skill is used, or when the user says "set up no-recording" or "change my no-recording settings". Look for a saved settings file first (`no-recording-settings.md`, in the notes location or the project's files). If one exists, read it and skip setup.

Setup is a single round of questions, not an interview:

1. **Detect before asking.** Check which tools are connected in this environment: Microsoft 365 or Outlook, Gmail and Google Calendar, task tools, CRMs, file storage. Pre-fill every answer that detection settles and show it for confirmation instead of asking. Pre-fill internal domains from the user's own email address.
2. **Ask only what detection could not settle**, in one batch, with sensible defaults marked:
   - **Email and calendar:** Microsoft 365 (Outlook) / Google Workspace (Gmail and Google Calendar) / neither (the user will paste meeting details).
   - **Task tool:** which one, and which list or project follow-ups go in. How the tool should show waiting-on items: a label or tag (default `waiting-on`), a separate list, or a prefix in the task title, whichever the tool supports. "None" is a valid answer; tasks then appear as a checklist in the notes.
   - **CRM:** which one, or none. And how to use it: **copy-paste note** (default; the skill writes the note and the user logs it), or **log as an activity** on the matched account and contacts, only if the CRM is connected and the firm allows it. The skill never creates or edits accounts, contacts, opportunities or deal stages.
   - **Notes location:** a OneDrive or SharePoint folder, a Google Drive folder, a local folder, a Notion or Confluence space, or "just send me the files". Default file formats: Markdown plus Word.
   - **Internal domains:** confirm the pre-filled list and add any affiliates, so internal attendees are recognized.
   - **Firm rules (optional):** for example "never put client names in task titles", "follow-ups to clients need a compliance review before sending", "don't log anything to the CRM about deals under NDA", a required email disclaimer, or a preferred sign-off.
3. **Save the settings.** Write `no-recording-settings.md` to the notes location (or the project's files) in plain language the user can edit by hand. If nothing persistent can be written, show the settings as a short block and tell the user to paste it into their project instructions, so the next run can read it.
4. **Continue straight into the debrief** if the user gave a brain dump with the setup request.

On every later run: read the settings and never re-ask. If a configured system isn't reachable today, fall back for that output only (copy-paste text) and say so in the report.

### 1. Get the brain dump

If the user hasn't given one, ask for it in one line: "Talk me through it: who, what you agreed, what you owe, what they owe." Don't interview them; one pass is enough.

### 2. Pick outputs without asking

Produce every output the settings enable. Never ask a separate question about outputs. Read the brain dump and the request for scoping words instead: "just notes", "notes only", "no email", "skip the tasks", "don't log it", "just the CRM note" and the like narrow the set. Then do only the work that selection needs. Steps 3 and 4 always run, because every output uses the meeting details and the parsed brain dump.

### 3. Find the meeting on the calendar

Search the calendar from 6 hours ago until now. Match on the names, firms or topics in the brain dump. If nothing matches, use the most recently ended event that has external attendees. Pull the title, date, start and end time, location or video link, the purpose (the event description or agenda, plus the subject of the invite thread if there is one), and the attendee list with RSVP status.

If two events fit equally well, ask which one. If none fits, say so and continue with what the brain dump provides.

### 4. Enrich each attendee and parse the brain dump

Split attendees into **external** and **internal** using the internal domains. For each external attendee:
- **Firm:** from the email signature, otherwise the email domain.
- **Title:** in this order: (a) the signature block in their most recent email, (b) the calendar invite or invite thread, (c) the CRM contact record, if a CRM is connected. Record which source each title came from. **Never guess a title.** If no source has one, write "title unknown".
- **Recent context:** the last email thread with this person or firm, in one line, including anything already promised there.
- **CRM match** (if a CRM is connected): the account and contact records this meeting belongs to. If the match is ambiguous (two accounts with similar names, or no record at all), note it; never create a record.

From the brain dump, extract:
- A summary of 2 to 4 sentences, in the user's framing
- Decisions or agreements
- **My action items:** each with a due date
- **Their action items:** waiting-on items, each with the owner and any date
- Intros to make: both names plus the reason
- Open questions, or anything left unresolved

Resolve relative dates ("Thursday", "next week", "after the quarter closes") against today and show the actual date. "Next week" with no day becomes that Monday.

### 5. Pause only when a wrong guess is costly

Notes files, an email draft and tasks are all easy to edit or delete, so create them in one pass without showing a preview first. Pause and ask a single question only when:
- two calendar events fit the brain dump equally well;
- the email draft would go to an address not found in the calendar, email or CRM (in that case, skip the draft and give the email as copy-paste text instead of asking);
- the settings say to log CRM activity. The CRM is a shared record that colleagues rely on, so show the activity note and the matched account and contacts, and write it only after the user says yes. Everything else is created first, so this question never holds up the rest.

Missing due dates, unknown titles and unresolved points are not reasons to pause. Leave them empty or marked, and list them under Open questions.

### 6. Produce the selected outputs

**Meeting notes.** Write the Markdown file first; it is the main record. Then build the Word copy from the same content (using a Word document skill or tool if one is available): a title, a bold details block, a real table for attendees, headings matching the Markdown, no decorative styling. Name both `YYYY-MM-DD_[Firm]_meeting-notes`. Save them to the notes location if one is set and reachable; either way, send both files to the user.

**Raw notes: use judgement.** The brain dump is usually clean dictation and often the richest context available. Add it word for word under `## Raw notes` when it holds nuance the structured sections lose: tone, reasoning, hesitations, side comments, how something was said. Leave it out when the structured sections already capture everything. Fix only obvious transcription errors in names. When in doubt, include it: for a future reader, extra context costs little and a missing detail can't be recovered.

**Follow-up email.** Create a **draft** in the user's own mail system (Outlook or Gmail), addressed to the external attendees, confirming what was agreed and the next steps in 3 to 6 lines. Apply any sign-off, disclaimer or review rule from the settings. Never send it, and don't attach the notes unless the user asks. If the firm rule says client emails need compliance review, say so in the report.

**Tasks.** Create the user's action items in the configured task tool and list, in one batch. Create the other side's items as waiting-on items, using the waiting-on convention from setup, with the owner's name in the title. Each task description names the meeting and its date, so the task makes sense on its own. If no task tool is set, the action items appear as a checklist in the notes and the report.

**CRM note.** Write a short activity note: meeting type and date, attendees, 3 to 5 sentences on what was discussed and agreed, next step with date. In copy-paste mode, show it in the report. In log mode, write it as an activity on the confirmed account and contacts after the user's yes (step 5). Never change any other CRM field.

### 7. Report

Send the files, then show the report below with each output marked done: file names and where they were saved, the email draft, the task tool and number of tasks, and the CRM note's status. Flag any title still unknown and any open questions so the user can fill them in. End with: "Reply with any edits." Apply edits to the files, draft, tasks and note already created; don't create new ones.

## Output format

The report is the product: keep it to one screen and show only the blocks for outputs produced.

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
MEETING
  [Title]: [date, time]
  Purpose: [from the calendar or invite]
  Attendees:
    • [Name], [Title] ([source]), [Firm], [email]
    • [Name], title unknown, [Firm]
    • Internal: [names]

NOTES → [YYYY-MM-DD]_[Firm]_meeting-notes (.md + .docx), saved to [location]
  Summary: [2–4 sentences]
  Decisions: [bullets]

EMAIL DRAFT → [to], in [Outlook / Gmail] drafts
  Subject: [subject]
  [3–6 line follow-up confirming agreements and next steps]

TASKS → [task tool]: [list or project]
  ☐ [task], due [date]
  ⏳ waiting on [owner]: [their item], [date]

CRM → [copy-paste note / logged to Account: Contact(s)]
  [3–5 sentence activity note]

QUESTIONS (if any)
```

The notes files share one structure:

```
# [Meeting title]
**Date:** [date], [start–end, time zone]   **Location:** [place or video link]
**Purpose:** [from the calendar or invite]

## Attendees
| Name | Title | Firm | Email |
(one row per person, external first; "title unknown" where no source has one)

## Summary
## Decisions
## My action items        (task, due date)
## Their action items     (owner, item, date)
## Intros to make
## Open questions
## Context from prior emails   (one line per relevant thread)
## Raw notes                  (optional, see step 6)

_Source: post-meeting debrief; attendee details from calendar, email and CRM._
```

## Guardrails

- **Drafts only, never sent.** The skill never sends an email, posts a message or shares the notes with anyone. The user sends.
- **The CRM is a shared record.** Default to a copy-paste note. Log an activity only when setup enabled it and the user confirms this specific note and account. Never create, merge or edit accounts, contacts, opportunities or deal stages.
- **Titles and firms come from sources, never inference.** Keep the source label in the report; "title unknown" beats a plausible guess.
- **Nothing the user didn't say.** Don't put anything in the notes, email, tasks or CRM note that isn't in the brain dump or already in the calendar, email or CRM.
- **Never delete or edit existing tasks, drafts or CRM entries** other than the ones this run created.
- **Confidential and sensitive content.** Assume a firm-approved AI environment. If the brain dump mentions something that looks like material non-public information, deal terms under NDA, or personal details about an attendee (health, family, compensation), keep it in the notes only if it is business-relevant, keep it out of task titles, the email draft and the CRM note, and flag it in the report so the user can decide. Follow any firm rules saved in setup.
- **One pass.** Gather, then create everything selected without waiting for approval, except in the pause cases in step 5.
- **When a system fails, say which one**, finish the other outputs, and give the missing part as copy-paste text.

## Example prompts

> "Just got out of coffee with the CFO and treasurer at Northbridge Capital Partners. They're unhappy with their current reporting provider, mainly the turnaround time on month-end packs. I said I'd send our sample pack and two references by Friday. They'll send their current pack and the RFP timeline next week. Their treasurer wants an intro to our head of operations."

> "Set up no-recording. We're on Outlook, tasks go in Microsoft Planner under 'Client follow-ups', we use Salesforce but I'll log notes myself, and save the notes to my OneDrive 'Meeting notes' folder. Never put client names in task titles."

> "Debrief my 2pm, notes only, no email: the board member walked us through their concerns on the integration timeline and asked for a revised plan before the March meeting."

## Works well with

**call-transcript-followup** handles the same job when a recording or transcript does exist. **relationship-status-summarizer** gives the email side of a relationship; the notes this skill saves add what was said in meetings that email never captured. **professional-profile-brief** and **lp-meeting-prep-brief** prepare the next meeting; hand them these notes as the meeting history.
