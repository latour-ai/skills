---
name: inbox-triage
description: >-
  Pre-market inbox triage for hedge fund and investment management
  executives. Scans the user's unread email in Microsoft 365 (Outlook) or
  Google Workspace (Gmail), or a pasted or exported message list when no
  mailbox is connected, and surfaces only the messages that matter before the
  trading day starts, sorted into high, medium and low priority with a
  suggested action for each. The VIP sender list, market-open time and any
  extra senders to ignore are set once in a short first-run setup. For
  executives who receive hundreds of emails a day and need a strictly
  filtered view. Trigger on "pre-market inbox", "morning email scan", "what's
  urgent before the open", "check my email", "inbox triage", "morning
  briefing", "email priorities", "what needs my attention", "any urgent
  emails", "what did I miss overnight", "catch me up on email", "trading day
  prep", "anything from investors", "LP emails", "compliance emails", "risk
  alerts", "set up inbox-triage", or "change my inbox-triage settings". Do
  NOT use to review the history of one relationship; use the
  relationship-status-summarizer skill. Do NOT use to work through sell-side
  research; use the sellside-research-triage skill. The skill reads mail
  only: it never sends, replies, archives, deletes or marks anything as read.
license: MIT
metadata:
  author: latourai
  version: '2.0'
---

# Inbox Triage

Filter a hedge fund executive's inbox down to what matters before markets open. This person gets hundreds of emails a day, so the bar for surfacing something is high.

## Why this exists

A hedge fund executive's morning is not like a normal morning. Before the open, they need to know: is there anything in my inbox that could affect my positions, my investors, my compliance posture, or my team? Everything else is noise. This skill applies that lens strictly.

## Inputs

- **The mailbox.** Read from the user's connected mail system: Microsoft 365 (Outlook) or Google Workspace (Gmail). If no mailbox is connected, or the connection fails, say so and ask the user to paste or export the unread messages (sender, To or CC, subject, time, and the first lines of each); the triage then runs on that list.
- **Optional scope from the request:** a time window, a sender, or a topic ("anything from our prime broker?", "LP emails this week").
- **Set once in setup (step 0):** mail system, VIP sender list, market-open time and time zone, default look-back window, and extra senders to ignore.

## Step 0 — First-run setup (once, then only when asked)

Run setup the first time the skill is used, or when the user says "set up inbox-triage" or "change my inbox-triage settings". Look first for a saved `inbox-triage-settings.md` in the project's files or the skill's working folder. If it exists, read it and skip setup.

Setup is one short round of questions, each with a default the user can accept:

1. **Detect before asking.** Check which mail system is connected and pre-fill it.
2. **Ask, in one message:**
   - **Mail system:** Microsoft 365 (Outlook), Google Workspace (Gmail), or neither (the user will paste messages).
   - **VIP senders:** names, email addresses or domains whose messages are always high priority. Offer the groups below as a prompt; "none" is valid, and the list can be filled in over time.
     - People the user reports to: CIO, managing partner, fund principal or founder
     - Portfolio managers
     - Investors and LPs: key LP contacts, placement agents
     - Risk and compliance: chief risk officer, chief compliance officer, risk committee members, outside regulatory counsel
     - Prime brokerage and key counterparties
     - Others: board members, fund administrator, auditor, legal
   - **Market open and time zone:** default 9:30 AM Eastern.
   - **Default look-back window:** default the last 12 hours.
   - **Extra senders to ignore:** newsletters, digests or internal lists specific to this inbox. Default none.
3. **Save the settings** to `inbox-triage-settings.md` in plain language the user can edit by hand. If nothing persistent can be written, show the settings as a short block and tell the user to paste it into their project instructions.
4. **Continue straight into the triage** if the user asked for one.

On later runs, read the settings and do not re-ask. Setup never blocks a run: if the user says "skip setup", triage with the defaults and an empty VIP list, and say so in the briefing.

---

## Priority Tiers

### 🔴 HIGH — Action required before market open

These are emails that could affect positions, capital, compliance, or key relationships. The executive should see them before anything else.

**Automatically high, whatever the content:**

- The sender is on the VIP list from setup
- Someone is following up on something the user owes them ("circling back", "any update", "following up", "checking in")

**High based on content:**

- Trade-related communications: execution issues, settlement fails, margin calls, position inquiries, NAV discrepancies
- Investor/LP communications: capital calls, redemption notices, reporting requests, due diligence questions, investor meeting follow-ups
- Regulatory and compliance: SEC notices, compliance alerts, regulatory filing deadlines, audit requests, suspicious activity flags
- Risk alerts: limit breaches, drawdown notifications, counterparty credit issues, liquidity concerns
- Urgent operational: fund administrator issues, prime brokerage communications, wire transfer confirmations or issues, legal matters with deadlines
- Client escalations: unhappy investors, service complaints, performance questions with urgent tone
- Time-sensitive language: "before the open", "EOD", "ASAP", "urgent", "immediately", "deadline today", "time-sensitive", "waiting on you", "need this by"

### 🟡 MEDIUM — Important but can wait until mid-day

These matter, but nothing breaks if they wait a few hours.

- Meeting prep for today's calendar (board meetings, investor calls, PM reviews), especially if there are materials to review
- Non-urgent colleague requests: research asks, process questions, team coordination
- Counterparty communications without urgency: documentation requests, standard confirms, relationship check-ins
- Operational items with deadlines this week but not today
- New business and fundraising threads that aren't time-critical
- Warm introductions and referrals: valuable for the relationship, but they can wait
- Legal documents for review (no imminent deadline)
- HR and compensation matters

### 🟢 LOW — Worth knowing, no action needed today

- Industry news that is relevant to the fund's strategy (not generic market commentary)
- Conference and event invitations
- Completed document signatures (confirmation only)
- Internal announcements that are informational
- Professional network updates with real substance
- Building and office logistics (visitor passes, facility notices)

---

## What to ignore entirely

These do not appear in the output except as counts in the footer.

**Newsletters and digests:**

- Any sender containing "substack", "newsletter", "digest", "noreply", "no-reply", "mailer", "notify", "updates@", "news@"
- Mail sent through newsletter and marketing platforms (for example beehiiv.com, substack.com, mailchimp.com, hubspot.com, intercom.io)
- Market commentary blasts, research distribution lists, morning notes from the sell side
- Topic newsletters and daily digests of any kind
- Any sender on the ignore list from setup

**Research and market blasts:**

- Sell-side research distribution (Goldman, JPM, Morgan Stanley morning notes and the like)
- Market data service alerts (automated emails from Bloomberg, Refinitiv, FactSet)
- Generic market commentary and "daily wrap" emails from brokers
- Bulk research reports, unless a PM or analyst on the VIP list forwarded something specific

**Promotional and transactional:**

- SaaS product emails, billing receipts, welcome emails
- Vendor pitches, demo requests, cold sales outreach
- Product-update and admin notifications from the mail or office suite
- Subscription confirmations, order receipts

**Calendar noise:**

- "Accepted:", "Declined:", "Tentative:" auto-responses, unless they contain a personal note
- Automated calendar notification senders

**Low-signal social:**

- LinkedIn and X notifications, social media digests
- Group threads that are clearly social banter (short messages, jokes, emojis)
- Short acknowledgments such as "Thanks!", "Got it", "Sounds good!" that show a conversation is resolved

**Automated system alerts:**

- CI/CD notifications, deployment alerts
- IT system monitoring, unless it reports a trading system outage (use judgement)
- Password reset emails and one-time codes

---

## Workflow

### Step 1 — Fetch recent unread messages

Search the connected mailbox twice. The default window is the look-back window from setup (12 hours unless changed). Adjust to the request: "what did I miss this week" means 7 days; "anything urgent" means the last 6 hours.

- **Search 1, direct mail:** unread messages in the window, leaving out anything the mail system has already sorted as promotional, social, junk or low-priority (Gmail's Promotions and Social categories; Outlook's Junk folder and "Other" tab). Up to 75 results.
- **Search 2, CC'd mail:** unread messages in the window where the user is on the CC line, with the same exclusions. Up to 30 results.

Use the mail system's own search syntax. Deduplicate by thread or conversation across both searches. Track whether the user was in the To field or only CC'd.

If the user pasted or exported a message list, treat that list as the search result and continue.

### Step 2 — First-pass filtering (metadata only)

Using only sender, subject line and preview text, discard anything matching the ignore patterns above. There is no need to open obvious noise. This pass should cut 75 or more messages down to the 10 to 20 that deserve a closer look.

### Step 3 — Read and classify surviving emails

Open each surviving thread and read the full content. Apply the tier rules in this order:

1. **VIP list first.** A sender on the VIP list is 🔴 HIGH.
2. **"Waiting on me" signals.** Follow-ups, unanswered questions, and threads where the user was last asked something are 🔴 HIGH whoever sent them.
3. **Content-based classification** using the tier definitions above. Read before classifying: an email from compliance that says "annual training reminder" is noise, and one that says "urgent: position limit breach" is 🔴.
4. **To versus CC.** If an email is borderline between two tiers and the user is only CC'd, put it in the lower tier. CC-only emails need a strong signal (VIP sender, urgent language, trade-related content) to reach 🔴.

If an email still looks like noise after reading it, drop it. When unsure between surfacing and dropping, keep the item as 🟢: missing a real issue is worse than showing one extra low-priority line.

### Step 4 — Present the briefing

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

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

## Behaviors

- **Read only.** The skill reads mail. It does not send, reply, forward, archive, delete, label or mark anything as read. The actions in the briefing are suggestions for the user to take.
- **Overnight versus intraday.** If the user runs this before the market open set in setup, weight anything that arrived overnight or early morning more heavily, since they haven't seen it yet. If they run it mid-day, adjust accordingly.
- **A quiet inbox is a valid result.** If nothing is urgent, say so: "Your inbox is clean. Nothing requires attention before the open." Don't manufacture urgency.
- **Adapt to specificity.** If the user asks about a specific sender, topic or timeframe, narrow the search instead of running the full triage.
- **Keep it scannable.** The user has a few minutes before the open; one line of summary per email is enough.
- **Confidential content.** Assume a firm-approved AI environment. Summarize what an email needs from the user; do not copy position details, investor names or account numbers into the briefing beyond what is needed to identify the item.

## Example prompts

> "Pre-market inbox. What needs me before the open?"

> "Set up inbox-triage. We're on Outlook. VIPs are our CIO, the two PMs, our CCO, anyone at our prime broker's domain and our three anchor LPs. Market open is 9:30 Eastern, look back 14 hours, and ignore the internal ops-digest list."

> "Anything from investors or the fund administrator this week?"
