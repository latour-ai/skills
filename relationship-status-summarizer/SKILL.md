---
name: relationship-status-summarizer
description: >-
  Surface where a professional relationship stands by pulling from Gmail —
  last touchpoint, what was discussed, open threads, commitments, and a
  suggested next move. Use whenever a user wants to re-engage someone, prep
  for outreach, or get a quick status check before reaching out. Trigger on
  "where do I stand with [Name]", "catch me up on my history with [Name]",
  "what's my relationship with [Name]", "when did I last talk to [Person]",
  "what was the last thing discussed with [Name]", "should I reach out to
  [Person]", "help me re-engage [Name]", "what do I owe [Person]", "any open
  threads with [Company]", "what's my history with [Name]", or any variation
  of wanting to understand a relationship's current state before making a move.
  Also trigger when the user mentions a person's name and asks about follow-ups,
  last contact, or relationship warmth. Designed for BD, fundraising, and IR
  professionals managing large networks who need a fast, honest read on where
  things stand.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Relationship Status Summarizer

Pull from Gmail to give the user an honest, fast read on where a specific relationship stands — and what to do next.

## Why This Skill Exists

Managing a large professional network in BD, fundraising, or IR means dozens of relationships in various states of warmth, dormancy, or momentum. Before re-engaging someone — a prospective LP, a potential partner, an intro target — you want to know: When did we last talk? What was discussed? Did I leave anything open? Is it weird to reach out now? This skill answers those questions from the email record so the user can move quickly and confidently.

## What This Skill Does Not Do

- It only reads Gmail. It cannot check CRM records, calendar history, LinkedIn messages, or other communication channels unless those integrations are explicitly available.
- It does not fabricate relationship history. If there are no emails with this person, say so clearly.
- It does not ghost-write the outreach message — that is the intro-email-generator skill's job. This skill ends with a suggested next move, not a drafted email.
- It cannot assess relationship quality beyond what the email record shows. A warm email thread does not guarantee a warm relationship — use judgment.

## Inputs

The user provides at minimum:

- A person's name, email address, or company name

Optionally helpful:

- Context on why they're asking (re-engagement, LP meeting prep, warm intro, deal follow-up)
- Approximate timeframe to search ("last year", "last 6 months")
- The user's goal in re-engaging this person

If no timeframe is specified, default to searching the last 18 months.

## Workflow

### Step 1 — Search Gmail for relevant threads

Run targeted searches to surface all meaningful email history with this person. Use the Gmail connector tools for all email operations.

Primary search — by name or email:
- Query: `from:[name or email] OR to:[name or email]`
- maxResults: 50
- newer_than: 18 months (or user-specified range)

Secondary search — by company (if name alone is ambiguous):
- Query: `[company name] -category:promotions -category:social`
- maxResults: 20
- newer_than: 18 months

Deduplicate by thread ID. If the name is common and returns many unrelated threads, use company name or any additional context the user provided to filter.

### Step 2 — Filter to signal threads

Discard threads that are clearly noise: newsletters, automated notifications, marketing emails, calendar accept/decline responses with no personal content, automated receipts, confirmations, DocuSign completions, and CC-only threads where neither party initiated anything meaningful.

Keep threads where either party wrote something substantive, there was a clear ask, commitment, or follow-through, the relationship was being actively developed (intros, meetings, deals, pitches), or there is an unanswered message from either side.

### Step 3 — Read the surviving threads

For each surviving thread, read enough to understand what the conversation was about, what was asked or offered, whether it was resolved or left open, and the tone and warmth of the exchange.

### Step 4 — Produce the relationship brief

Use this exact output structure:

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

Be honest, not flattering. If the relationship is cold, say it's cold. If the user left something open and didn't follow through, flag it — that's the most useful thing you can surface.

Recency matters most. A warm thread from 3 years ago and nothing since is a cold relationship.

Direction signals intent. If the user has been doing all the reaching out, note that pattern explicitly.

Open threads are critical. An unanswered email is the single most important thing to surface — it shapes both the temperature and the next move.

No email history is a clear answer. Say so directly: "No meaningful email history found." Don't pad with speculation.

CC-only threads are weak signal. Only count direct, substantive exchange.

## When the Person Is Ambiguous

If the name is common and returns multiple people, ask the user to clarify with an email address, company, or more context. Do not guess which person is meant.

## Quality Checks

Before delivering, verify:

- Threads cited are actually with the target person (not a different person with a similar name)
- No invented history — every data point traces to an actual email
- Relationship Temperature is calibrated to recency, not volume
- Open threads are surfaced even if uncomfortable (especially if the user dropped the ball)
- Suggested Next Move is specific to this relationship, not generic advice

## Important Reminder

This brief is only as good as the email record. Relationships that live primarily in phone calls, LinkedIn, or in-person meetings will appear colder than they actually are. Flag this caveat when the email record is sparse but the user's context suggests the relationship may be richer than what's visible in Gmail.
