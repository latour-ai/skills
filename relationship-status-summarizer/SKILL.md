---
name: relationship-status-summarizer
description: >-
  Surface where a professional relationship stands from the user's email
  record: last touchpoint, what was discussed, open threads, commitments, and
  a suggested next move. Reads Microsoft 365 (Outlook) or Google Workspace
  (Gmail), adds meeting dates from the calendar and logged activity from a
  CRM where those are connected, and works from pasted or exported threads
  when nothing is connected. Use whenever a user wants to re-engage someone,
  prep for outreach, or get a quick status check before reaching out. Trigger
  on "where do I stand with [Name]", "catch me up on my history with [Name]",
  "what's my relationship with [Name]", "when did I last talk to [Person]",
  "what was the last thing discussed with [Name]", "should I reach out to
  [Person]", "help me re-engage [Name]", "what do I owe [Person]", "any open
  threads with [Company]", "what's my history with [Name]", or when the user
  names a person and asks about follow-ups, last contact, or relationship
  warmth. For BD, fundraising, and IR professionals managing large networks
  who need a fast, honest read on where things stand. Do NOT use to find who
  at the firm knows a target; use the network-referral-path-mapper skill. Do
  NOT use for a background brief on a person; use the
  professional-profile-brief skill. Do NOT use to prepare a full LP meeting;
  use the lp-meeting-prep-brief skill.
license: MIT
metadata:
  author: latourai
  version: '2.0'
---

# Relationship Status Summarizer

Pull from the user's email record to give an honest, fast read on where a specific relationship stands, and what to do next.

## Why This Skill Exists

Managing a large professional network in BD, fundraising, or IR means dozens of relationships in various states of warmth, dormancy, or momentum. Before re-engaging someone (a prospective LP, a potential partner, an intro target) you want to know: When did we last talk? What was discussed? Did I leave anything open? Is it weird to reach out now? This skill answers those questions from the email record so the user can move quickly and confidently.

## What This Skill Does Not Do

- It reads the user's own email, and the calendar and CRM only where they are connected. It cannot see phone calls, LinkedIn messages, chat, or in-person meetings that left no record.
- It does not fabricate relationship history. If there are no emails with this person, say so clearly.
- It does not draft the outreach message. It ends with a suggested next move, not a drafted email.
- It cannot assess relationship quality beyond what the record shows. A warm email thread does not guarantee a warm relationship.
- It only reads. It does not send, label, or change anything in the mailbox, calendar or CRM.

## Inputs

The user provides at minimum:

- A person's name, email address, or company name

Optionally helpful:

- Context on why they're asking (re-engagement, LP meeting prep, warm intro, deal follow-up)
- Approximate timeframe to search ("last year", "last 6 months")
- The user's goal in re-engaging this person

If no timeframe is specified, default to searching the last 18 months.

**Where the record comes from:** the user's connected mail system, Microsoft 365 (Outlook) or Google Workspace (Gmail). If a calendar is connected, use it for the dates of past meetings with this person. If a CRM is connected (Salesforce, HubSpot, Dynamics 365, DealCloud, Affinity), read the logged activity for the contact. If no mail system is connected, or the connection fails, say so and ask the user to paste or export the threads with this person; the brief then covers only what was provided and says that.

## Workflow

### Step 1 — Search for relevant threads

Run targeted searches in the connected mail system, using its own search syntax, to surface all meaningful email history with this person.

Primary search, by name or email:
- Messages from or to the person's name or email address
- Up to 50 results
- Within the last 18 months (or the user-specified range)

Secondary search, by company (if the name alone is ambiguous):
- Messages mentioning the company name, leaving out anything the mail system has sorted as promotional or social
- Up to 20 results
- Within the last 18 months

Deduplicate by thread or conversation. If the name is common and returns many unrelated threads, use the company name or any additional context the user provided to filter.

### Step 2 — Filter to signal threads

Discard threads that are clearly noise: newsletters, automated notifications, marketing emails, calendar accept/decline responses with no personal content, automated receipts, confirmations, e-signature completions, and CC-only threads where neither party initiated anything meaningful.

Keep threads where either party wrote something substantive, there was a clear ask, commitment, or follow-through, the relationship was being actively developed (intros, meetings, deals, pitches), or there is an unanswered message from either side.

### Step 3 — Read the surviving threads

For each surviving thread, read enough to understand what the conversation was about, what was asked or offered, whether it was resolved or left open, and the tone and warmth of the exchange.

### Step 4 — Produce the relationship brief

Use this output structure. Where a line comes from the calendar or the CRM and not from email, say so on that line.

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
## Relationship Brief: [Name] — [Title / Company if known]

### Last Contact
Date: [Most recent email date]
Direction: [You reached out / They reached out / Mutual]
Subject: [Subject line of most recent thread]
Summary: [1-2 sentences on what was discussed or exchanged]

### Relationship History
[3-6 bullet chronological summary of meaningful touchpoints]
- [Date] — [What happened and outcome]

### Open Threads
[List any unanswered emails, pending commitments, or explicitly flagged follow-ups.
If none: "No open threads identified."]

### Relationship Temperature
One-line honest read:
- **Warm** — Recent, engaged, mutual exchange
- **Cooling** — Last contact 6-12 months ago, ended well
- **Cold** — Last contact 12+ months ago, or ended without resolution
- **Never started** — No meaningful email history found

### Suggested Next Move
One specific, actionable recommendation. Not a drafted message — just the right move.

### Email Record Summary
[X threads found | Most recent: [date] | Oldest: [date] | Time since last contact: X months]
```

## Tone and Judgment Principles

Be honest, not flattering. If the relationship is cold, say it's cold. If the user left something open and didn't follow through, flag it, even when it is uncomfortable. That is the most useful thing the brief can surface.

Recency matters most. A warm thread from 3 years ago and nothing since is a cold relationship. Calibrate temperature to recency, not to the volume of email.

Direction signals intent. If the user has been doing all the reaching out, note that pattern explicitly.

Open threads are critical. An unanswered email is the single most important thing to surface. It shapes both the temperature and the next move.

No email history is a clear answer. Say so directly: "No meaningful email history found." Don't pad with speculation.

CC-only threads are weak signal. Only count direct, substantive exchange.

Every data point traces to an actual email, calendar entry or CRM record. The suggested next move is specific to this relationship, not generic networking advice.

The brief is only as good as the record. Relationships that live mainly in phone calls, LinkedIn, or in-person meetings will look colder than they are. When the email record is sparse but the user's context suggests a richer relationship, say that the brief may understate it.

## When the Person Is Ambiguous

If the name is common and returns multiple people, ask the user to clarify with an email address, company, or more context. Do not guess which person is meant, and do not mix threads from a different person with a similar name into the brief.

## Example prompts

> "Where do I stand with Dana Reyes at Harbor Analytics? I want to reach out about our next fund."

> "Any open threads with Northbridge Capital Partners in the last six months? What do I owe them?"
