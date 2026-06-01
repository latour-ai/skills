---
name: inbox-triage
description: Pre-market inbox triage for hedge fund executives. Scans Gmail and surfaces only the emails that matter before the trading day starts. Use this skill whenever the user asks to triage their inbox for trading day prep, says "pre-market inbox", "morning email scan", "what's urgent before the open", "check my email", "inbox triage", "morning briefing", "email priorities", "what needs my attention", "any urgent emails", "what did I miss overnight", "catch me up on email", "what's waiting for me", "pre-market check", "morning triage", or any variation of wanting to see what emails need attention before markets open. Also trigger when the user says "trading day prep", "what came in overnight", "anything from investors", "LP emails", "compliance emails", "risk alerts", or mentions needing to scan email before the bell. This skill is purpose-built for hedge fund and investment management executives who receive hundreds of emails daily and need a ruthlessly filtered view of what actually matters.
---

# Inbox Triage

Ruthlessly filter a hedge fund executive's inbox down to what matters before markets open. This person gets hundreds of emails a day — the bar for surfacing something is HIGH.

## Why this exists

A hedge fund executive's morning is not like a normal morning. Before 9:30 AM ET, they need to know: Is there anything in my inbox that could affect my positions, my investors, my compliance posture, or my team? Everything else is noise. This skill applies that lens mercilessly.

## VIP Stakeholders (customize this list)

Messages from anyone on this list are automatically flagged 🔴 HIGH regardless of content. Update these names and emails to match the actual people in your orbit.

### Direct Reports To

- [Your CIO / Managing Partner name]
- [Fund principal / founder]

### Portfolio Managers

- [PM 1 name]
- [PM 2 name]

### Investors / LPs

- [Key LP contact 1]
- [Key LP contact 2]
- [Placement agent contacts]

### Risk & Compliance

- [Chief Risk Officer]
- [Chief Compliance Officer]
- [Risk committee members]
- [Outside counsel — regulatory matters]

### Prime Brokerage & Counterparties

- [Prime broker contact]
- [Key counterparty contacts]

### Other VIPs

- [Board members]
- [Fund administrators]
- [Key service providers — auditor, legal]

---

## Priority Tiers

### 🔴 HIGH — Action required before market open

These are emails that could affect positions, capital, compliance, or key relationships. If it's 🔴, the executive should see it before they look at anything else.

**Auto-HIGH triggers (regardless of content):**

- Sender is on the VIP Stakeholders list above
- Someone is following up on something you owe them ("circling back", "any update", "following up", "checking in")

**Content-based HIGH triggers:**

- Trade-related communications: execution issues, settlement fails, margin calls, position inquiries, NAV discrepancies
- Investor/LP communications: capital calls, redemption notices, reporting requests, due diligence questions, investor meeting follow-ups
- Regulatory and compliance: SEC notices, compliance alerts, regulatory filings deadlines, audit requests, suspicious activity flags
- Risk alerts: limit breaches, drawdown notifications, counterparty credit issues, liquidity concerns
- Urgent operational: fund administrator issues, prime brokerage communications, wire transfer confirmations/issues, legal matters with deadlines
- Client escalations: unhappy investors, service complaints, performance questions with urgent tone
- Time-sensitive language: "before the open", "EOD", "ASAP", "urgent", "immediately", "deadline today", "time-sensitive", "waiting on you", "need this by"

### 🟡 MEDIUM — Important but can wait until mid-day

These matter, but the fund won't blow up if they wait a few hours.

**Content-based MEDIUM triggers:**

- Meeting prep for today's calendar (board meetings, investor calls, PM reviews) — especially if there are materials to review
- Non-urgent colleague requests: research asks, process questions, team coordination
- Counterparty communications without urgency: documentation requests, standard confirms, relationship check-ins
- Operational items with deadlines this week but not today
- New business / fundraising threads that aren't time-critical
- Warm introductions and referrals — these are relationship-valuable but can wait
- Legal documents for review (not deadline-imminent)
- HR and compensation matters

### 🟢 LOW — Worth knowing, no action needed today

Good to be aware of, but zero urgency.

**Content-based LOW triggers:**

- Industry news that's genuinely relevant to the fund's strategy (not generic market commentary)
- Conference and event invitations
- Completed document signatures (DocuSign, etc.) — confirmation only
- Internal announcements that are informational
- Professional network updates that are actually substantive
- Building/office logistics (visitor passes, facility notices)

---

## What to IGNORE entirely

These never appear in the output. Don't even count them in the filtered total — they're invisible.

**Newsletters & digests:**

- Any sender containing "substack", "newsletter", "digest", "noreply", "no-reply", "mailer", "notify", "updates@", "news@"
- Domains: beehiiv.com, substack.com, mailchimp.com, hubspot.com, intercom.io
- Market commentary blasts, research distribution lists, morning notes from sell-side
- AI newsletters (The Rundown, Ben's Bites, TLDR, etc.)
- Pebblr daily digests ([noreply@pebblr.io](mailto:noreply@pebblr.io))
- Substack notification emails and own-post delivery copies

**Research & market blasts:**

- Sell-side research distribution (Goldman, JPM, Morgan Stanley morning notes, etc.)
- Market data service alerts (Bloomberg, Refinitiv, FactSet automated emails)
- Generic market commentary and "daily wrap" emails from brokers
- Bulk research reports — unless from a PM or analyst on the VIP list forwarding something specific

**Promotional & transactional:**

- SaaS product emails, billing receipts, welcome emails
- Vendor pitches, demo requests, cold sales outreach
- Google Workspace notifications, product updates
- Subscription confirmations, order receipts

**Calendar noise:**

- "Accepted:", "Declined:", "Tentative:" auto-responses (unless they contain a personal note)
- Google Calendar notification sender ([calendar-notification@google.com](mailto:calendar-notification@google.com))

**Low-signal social:**

- LinkedIn notifications, Twitter/X notifications
- Social media digests
- Group threads that are clearly social banter (short messages, jokes, emojis)
- "Thread closed" replies — short acknowledgments like "Thanks!", "Got it", "Sounds good!" that signal a conversation is resolved

**Automated system alerts:**

- CI/CD notifications, deployment alerts
- IT system monitoring (unless it's a trading system outage — use judgment)
- Password reset emails, 2FA codes (these are ephemeral)

---

## Workflow

### Step 1 — Fetch recent inbox messages

Run two targeted Gmail searches. Default time window: overnight (last 12 hours). Adjust based on what the user asks — "what did I miss this week" = 7 days, "anything urgent" = last 6 hours.

**Search 1 — Direct emails:**

```
Query: "is:unread -category:promotions -category:social newer_than:1d"
maxResults: 75
```

**Search 2 — CC'd emails (shorter leash):**

```
Query: "is:unread cc:me -category:promotions -category:social newer_than:1d"
maxResults: 30
```

Use the Gmail MCP tools (prefixed `mcp__6c627729-09a2-40da-97c1-850fb310e12e__`) for all email operations:

- `search_threads` to run the queries above
- `get_thread` to read full message content for emails that survive first-pass filtering

Deduplicate results by thread ID across both searches. Track which emails had the user in the To field vs. CC — To-field emails get priority over CC in borderline cases.

### Step 2 — First-pass filtering (metadata only)

Using only sender, subject line, and snippet from search results, immediately discard anything matching the IGNORE patterns above. No need to read full messages for obvious noise.

Be aggressive here. The goal is to cut the list from potentially 75+ emails down to the 10-20 that deserve a closer look.

### Step 3 — Read and classify surviving emails

For each email that survived the first pass, use `get_thread` to read the full content. Apply the priority tier rules:

1. **Check VIP list first.** If the sender matches anyone in the VIP Stakeholders section, it's automatically 🔴 HIGH.
2. **Check for "waiting on me" signals.** Follow-ups, unanswered questions, threads where the user was last asked something — these are 🔴 HIGH regardless of sender.
3. **Apply content-based classification** using the tier definitions above.
4. **CC vs. To tiebreaker.** If an email is borderline between two tiers and the user is only CC'd (not in the To field), drop it to the lower tier.

If an email still looks like noise after reading the full content, drop it silently.

### Step 4 — Present the briefing

**Header line with counts:**

```
📬 X emails scanned, Y surfaced (Z high / W medium / V low), N filtered out
```

**Then organize by priority tier:**

#### 🔴 HIGH — Before the open

```
**[Sender Name]** — [Subject line]
[One-line summary: what happened / what they need]
⏩ Action: [Reply / Forward to [person] / Review and decide / Schedule call / Escalate]
🕐 Received: [time, e.g., "6:42 AM" or "Yesterday 11:15 PM"]
```

#### 🟡 MEDIUM — Mid-day

```
**[Sender Name]** — [Subject line]
[One-line summary]
⏩ Action: [Reply / Review / Schedule / FYI only]
🕐 Received: [time]
```

#### 🟢 LOW — When you have a moment

```
**[Sender Name]** — [Subject line]
[One-line summary]
⏩ Action: [FYI only / Review later / No action needed]
🕐 Received: [time]
```

**Footer:**

```
Filtered out: ~N newsletters, ~N research blasts, ~N promotional, ~N calendar/system noise
```

---

## Important Behaviors

- **The bar is HIGH.** This is not a general inbox summary. If you're unsure whether something deserves to surface, lean toward filtering it out for 🔴 and 🟡, but keep borderline items as 🟢 rather than dropping them entirely. It's worse to miss a genuine issue than to include one extra low-priority item.
- **Direct-to beats CC.** If the user is in the To field, the email is more important than if they're CC'd. CC-only emails need strong signals (VIP sender, urgent language, trade-related content) to reach 🔴.
- **Context matters for compliance and risk.** An email from "compliance@" that says "annual training reminder" is noise. An email from compliance that says "urgent — position limit breach" is 🔴. Read before classifying.
- **Overnight vs. intraday.** If the user runs this before market open, weight anything that arrived overnight or early morning more heavily — those are things they haven't seen yet. If they run it mid-day, adjust accordingly.
- **Empty inbox is a good sign.** If there's nothing urgent, say so: "Your inbox is clean — nothing requiring attention before the open." Don't manufacture urgency.
- **Adapt to specificity.** If the user asks about a specific sender, topic, or timeframe ("anything from our prime broker?", "LP emails this week"), narrow the search instead of running the full triage.
- **Respect the clock.** Keep the output tight and scannable. This person has 15 minutes before the open, not 15 minutes to read your email summary.

