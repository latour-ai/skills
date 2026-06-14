---
name: conference-prep-planner
description: Turn a conference attendee or speaker list plus the user's goals into a working conference plan — a tiered, prioritized target list with why-them one-liners, pre-conference outreach drafts, per-day scheduling logic, talking points per target, and a post-conference follow-up tracker. Built for BD, IR, and fundraising professionals attending industry events (SuperReturn, Milken, SALT, iConnections, sector conferences). Trigger on "prep me for [conference]", "here's the attendee list for [event]", "who should I meet at [conference]", "build my conference target list", "conference game plan", "outreach for [event]", "I'm going to [conference] next month", or when a user shares a speaker/attendee/exhibitor list and a goal. Do NOT use for deep prep on one specific person — use the professional-profile-brief skill. Do NOT use for institution-level LP research — use the lp-prospect-brief skill.
---

# Conference Prep Planner

Convert a conference attendee list, speaker roster, or app export plus the user's goals into an executable plan: who to pursue (tiered, with a one-line reason each), what to send them before the event, how to sequence the days, what to say in each conversation, and a tracker that makes the follow-up actually happen. The plan is built around a truth every BD person knows: conferences are won in the two weeks before and the week after, not at the booth.

## Why this skill exists

A fundraiser lands at SuperReturn with 3,000 attendees, 48 hours, and a vague intention to "see who's around." The attendee list was available three weeks earlier; nobody triaged it. The result is serendipity-dependent BD: coffee with people they already know, two random hallway meetings, and a stack of badge-scan contacts nobody follows up with. Triaging 800 names against a goal, drafting 25 outreach notes, and building a follow-up tracker is a solid two days of work — which is why it doesn't happen. This skill compresses it to an afternoon.

## Inputs

**Required:**
- The attendee, speaker, sponsor, or exhibitor list (pasted, file, or export from the event app) — names with firms at minimum
- The user's goal, concretely: raising Fund III from US insurance LPs; sourcing co-invest partners; selling a SaaS platform to fund CFOs; meeting acquirers for a portfolio company

**Optional but high-value:**
- Conference name and dates, session agenda, the user's existing commitments (panels, dinners)
- The user's existing relationships on the list ("know well / met once / cold")
- Firm/fund one-liner for outreach drafts
- Number of days attending and realistic meeting capacity per day

**Missing-input behavior:** If the list or the goal is missing, ask once for whichever is absent — without a goal, prioritization is fake. Otherwise proceed with labeled assumptions (default: 2 conference days, 8 meeting slots/day, standard 25-minute coffee meetings).

## How it works

1. **Score the list against the goal.** Every name gets a relevance read based on what's actually known (title, firm, firm type). Where the list gives only name + firm, use your AI's web search to enrich the top candidates — role, focus area, recent news — rather than enriching all 800.
2. **Tier the targets:**
   - **Tier 1 (5–10):** direct goal fit; pursue with pre-booked meetings; walk away disappointed if missed
   - **Tier 2 (10–25):** strong fit; pre-conference outreach, opportunistic scheduling
   - **Tier 3 (open-ended):** worth a hello if encountered; no outreach investment
   - Each target gets a **why-them one-liner** grounded in evidence ("CIO of $4B insurance pool, spoke last year on private credit allocations") — not "could be interesting."
3. **Draft pre-conference outreach** for Tiers 1–2: short, specific, sendable. Each note references something true about the target, states the ask plainly (20 minutes, specific day), and avoids the "would love to connect" void. Cold and warm variants where relationship status is known. Output as text to copy-paste — or into your email tool if one is connected.
4. **Build the per-day schedule logic** (not a fantasy calendar): which targets to anchor each day around, when to be at which sessions (a Tier 1 target's panel is a scheduling anchor and a conversation opener), where the user's own commitments create adjacency opportunities, and explicit white space — back-to-back-packed conference schedules collapse by 2pm Day 1.
5. **Write talking points per Tier 1 target:** an opener tied to them, two substantive threads, the soft ask, and the thing *not* to lead with (don't pitch the fund in sentence one to an LP who gets pitched forty times a day).
6. **Produce the follow-up tracker** — a table the user fills during/after the event, with pre-drafted follow-up note skeletons keyed to meeting outcome (met / missed-but-targeted / new contact).

## Output format

```
# Conference Plan — [Event], [Dates]
Goal: [user's goal] | List size: [n] | Tiered: [n1]/[n2]/[n3]
Assumptions: [days attending, slots/day, anything defaulted]

## Tier 1 Targets
| Name | Firm / Role | Why Them (one line) | Status | Pre-Book? |
|---|---|---|---|---|

## Tier 2 Targets
Same table, compressed.

## Pre-Conference Outreach (send ~2 weeks out)
### [Target name] — [cold/warm]
Subject: …
[3–5 sentence note with a specific ask and day]
(repeat for each Tier 1–2 target)

## Day-by-Day Logic
### Day 1
Anchor meetings, session positioning, adjacency plays, protected white space.
(repeat per day)

## Talking Points — Tier 1
### [Target name]
Opener: … | Threads: 1)… 2)… | Soft ask: … | Don't lead with: …

## Follow-Up Tracker (fill in as you go)
| Name | Tier | Met? | Key Notes | Promised | Follow-Up Owed | Sent? |
|---|---|---|---|---|---|---|

## Follow-Up Note Skeletons
Met / Missed / New-contact variants, ready to personalize within 48h post-event.
```

## Outreach drafting notes

What makes a pre-conference note get answered (and what kills it):

- **Subject lines name the event and the ask:** "iConnections — 20 min Tuesday?" beats "Connecting at the conference"
- **First sentence is about them**, and specifically them — their panel, their recent commitment, their firm's stated focus. If the only available opener is generic, say something honest and short instead of faking specificity.
- **One ask, one timeframe:** "20 minutes Tuesday morning near the main stage" — concrete asks get calendar responses; "grab time" gets silence.
- **Two sentences of who-you-are maximum.** The meeting is the pitch; the email is not.
- **No attachments on first contact.** Deck requests come after a yes — and sending a fund deck cold can itself be a compliance event; route materials through the firm's approved process.
- **The bump:** plan one short follow-up 3–4 days later for non-responders ("Floating this back up — Wednesday also works"). Draft it with the original.
- Send ~2 weeks out: calendars are forming but not full. Day-before outreach only works for Tier 3 hellos.

## Guardrails

- **Why-them lines must be evidenced.** From the list, from enrichment search (with the source implicit in the claim), or from the user's input. Never invent a target's title, mandate, or interests — if enrichment found nothing, the line says what's actually known ("Partner at [firm]; firm invests in [space] per their site").
- **Never fabricate a relationship or prior interaction** in outreach drafts. Cold notes are honestly cold.
- **No invented event details:** don't make up session times, party invites, or venue logistics not in the provided agenda.
- **Outreach drafts contain no performance claims** unless the user supplied the exact language — fundraising outreach is marketing material and compliance rules apply; flag any draft where the user's one-liner includes returns.
- People research stays public and professional.
- Be honest about capacity: if Tier 1+2 exceeds realistic meeting slots, say so and force-rank rather than pretending 40 meetings fit in two days.

## Quality checks

- Every Tier 1–2 target has an evidence-based why-them line?
- Outreach notes specific enough that the target can say yes to a time and place?
- Schedule includes anchors, adjacencies, and protected white space?
- Talking points reference something true per target, not generic openers?
- Tracker usable on a phone between meetings (simple columns, no essay fields)?
- Capacity math honest?

## Example prompts

> "Attached is the attendee list export from iConnections Global Alts — I'm there Tuesday and Wednesday. Goal: first meetings with US family offices and RIAs for our $150M opportunistic credit fund (Fund II, I can share the one-liner). I know maybe ten people on this list well. Build me the plan — tiers, outreach I can send Thursday, and the follow-up tracker."

> "SuperReturn Berlin speaker list pasted below. I'm BD for a fund-admin platform; goal is meetings with COOs and CFOs of mid-market PE firms. Three days, I'm also on a Wednesday panel — build the plan around that."

> "Smaller event: 80-person sector dinner-and-day conference, attendee list attached. Goal is two specific co-invest relationships. Skip the tiers, give me outreach and talking points for the eight names that matter."

## Works well with

Deep-prep individual Tier 1 targets with **professional-profile-brief** (people) or **lp-prospect-brief** (institutions); after the event, **call-transcript-followup** and **relationship-status-summarizer** keep the tracker honest.
