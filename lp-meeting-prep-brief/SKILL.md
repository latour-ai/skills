---
name: lp-meeting-prep-brief
description: >-
  Compile a one-page briefing before any LP meeting: the relationship
  timeline and who-knows-whom from CRM and email history, the LP's current
  holdings across the firm's funds with performance framed in the metrics
  they use, open items promised or requested in prior conversations, recent
  news about their organization worth acknowledging, and the five questions
  they are most likely to ask — each with a suggested answer — plus anything
  sensitive the partner should raise proactively. For IR, fundraising, and
  BD teams at private equity, private credit, hedge fund, real assets, and
  venture managers, and the partners they send into the room. Trigger on
  phrases like "prep me for the [LP] meeting," "briefing for [pension] on
  Thursday," "what do I need to know before I see [LP]," "meeting prep for
  [investor]," "build the one-pager for tomorrow's LP call," or when a user
  names a scheduled LP meeting and attaches relationship materials. Do NOT
  use for capturing what happened after the meeting — use the
  call-transcript-followup skill. Do NOT use for a multi-meeting conference
  schedule — use the conference-prep-planner skill. Do NOT use for a deep
  profile of one individual — use the professional-profile-brief skill. LP
  data is confidential; assume a firm-approved AI environment.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# LP Meeting Prep Brief

The partner is in the car reconstructing the relationship from memory — when the last meeting was, what was promised, whether the LP is in Fund II or Fund III, and what that markdown looks like in their numbers. The LP, who has exactly one meeting with your firm this quarter, notices the reconstruction immediately. This produces the briefing that currently only the biggest relationships get: one page, same structure every time, covering the history, the holdings in their terms, the open items, the news, and the five questions they will most likely ask — ready the morning of the meeting.

## Why this skill exists

LP meeting prep is a solved problem for maybe the top ten relationships, where an IR lead assembles a briefing by hand. Everyone else gets whatever the partner remembers, and what the partner remembers is the last conversation, not the commitment made two meetings ago. The asymmetry is brutal: to the firm, this is one of forty meetings this month; to the LP, it may be their only read this year on whether the firm has its act together. A partner who doesn't know the LP entered Fund III but skipped Fund IV has told the LP something, and it wasn't about Fund V.

The raw material almost always exists — CRM entries, email threads, holdings reports, prior meeting notes. What fails is assembly under time pressure. Pulling five sources into one page takes an hour nobody has the morning of a meeting, so it doesn't happen, and the meeting runs on improvisation. The open items are the costliest casualty: the co-invest data the LP asked for in March resurfaces awkwardly in September, raised by the LP, and the answer "we're pulling that together" is heard as "we forgot."

There is also a translation failure. The firm thinks in its own metrics; the pension board thinks in net IRR against a benchmark, the family office in cash back versus cash in, the consultant in whatever their reporting template says. Performance presented in the wrong dialect forces the LP to do the conversion themselves — and they may do it less charitably than you would.

## Inputs

**Required:**
- Who the meeting is with — the LP organization, the attendees on their side if known, the date, and the meeting's purpose if there is one (routine update, re-up conversation, first meeting on a new fund, damage control).
- **Whatever relationship record exists** — a CRM export, email threads, prior meeting notes, or at minimum a plain description of the history. The brief is assembled from this; it cannot be conjured.

**Optional but high-value:**
- **Current holdings and performance for this LP across the firm's funds** — commitments, NAV, called and distributed capital, net IRR/DPI/TVPI — because framing performance in their numbers is half the meeting
- The metrics and benchmarks this LP actually uses, from their reporting requests or prior questions
- Open-items list or task history for the relationship, if tracked separately from the CRM
- The current fund's status if the meeting touches a raise: progress, timing, terms headlines
- Attendee names and titles on their side, for the who-knows-whom mapping
- Known sensitivities: a markdown, a team departure, a delayed exit, a prior complaint

**Missing-input behavior:** Build the best brief the supplied record supports and label every gap in place — "no contact history provided before 2024," "holdings data not supplied; performance section omitted" — rather than smoothing over the holes. Recent organizational news may be drawn from public sources and cited as such; everything about the relationship itself comes only from the supplied record. Never invent a touchpoint, a promise, a holding, or a performance figure. If the record is so thin the meeting is effectively cold, say so plainly — "treat this as a first meeting" is a useful briefing conclusion, and the brief then leans on public information about the organization and its program.

## How it works

1. **Establish the frame.** Who is this meeting with, what kind of LP are they, what is the meeting for, and what does the firm want out of it? A routine update, a re-up ask, and a nervous-LP repair call need different briefs — the same facts, differently weighted. If the purpose isn't stated, infer it from the timeline and say what you inferred.
2. **Build the relationship timeline** from the CRM and email record: first contact, meetings, commitments made and declined, and the trajectory — warming, stable, cooling. Note who on each side knows whom, and flag if the firm-side relationship is concentrated in one person. The single most useful line is often "last meeting ended with X."
3. **Assemble holdings and performance in their dialect.** State what they hold across the firm's funds, then frame performance in the metrics this LP uses — and at the level they experience it, their commitments, not the flagship fund's headline. If their vintage or fee terms make their numbers differ from the marketing figures, the brief says so before the LP does.
4. **Hunt the open items.** Read the record specifically for promises and requests still outstanding — materials promised, questions taken away, intros offered, follow-ups committed. Date each one and name who owns it. An open item the partner raises first is diligence; the same item raised by the LP is a lapse.
5. **Scan recent news about their organization** — leadership changes, published returns, allocation announcements, strategy shifts, headlines. Two purposes: things worth acknowledging in the room, and things that change what they'll ask. A new CIO reviewing all external managers turns a routine update into an audition, and the brief should say that.
6. **Predict the five most likely questions.** Ground each in evidence — their prior questions, their investor type's standard concerns, current performance, and anything newsworthy about the firm — not in a generic list. Then draft a suggested answer per question, in the register the partner would use, flagging any answer that needs a number verified or a compliance-sensitive phrasing.
7. **Surface the sensitive items for proactive handling.** The markdown, the departure, the delayed distribution — whatever the LP likely knows or will learn. State each plainly, with the recommended one-line framing, so the partner raises it before the LP has to.
8. **Compress to one page.** The brief's value is that it gets read in the ten minutes before the meeting. Cut to what changes behavior in the room; move anything else to a short appendix. Same structure every time, so a partner can find the open items without hunting.

## Output format

One page is the contract; the skeleton adapts to what the record supports.

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# LP Meeting Brief — [LP name]
Meeting: [date] | Their side: [names, titles] | Our side: [names]
Purpose: [stated or inferred] | Relationship trajectory: [warming / stable / cooling]

## The one thing
[A single sentence: the most important thing to know or do in this meeting.]

## Relationship timeline
| Date | Touchpoint | Outcome / note |
|---|---|---|
Who knows whom: [ ] | Last meeting ended with: [ ]

## Their holdings & performance (in their terms)
| Fund | Commitment | Called | Distributed | NAV | [Their metrics, e.g. net IRR / DPI] |
|---|---|---|---|---|---|
Framing note: [how their numbers differ from headline figures, if they do]

## Open items — raise these before they do
| Item | Promised/asked | When | Owner | Status |
|---|---|---|---|---|

## Their recent news
- [item — why it matters for this meeting]

## Five likely questions — with suggested answers
1. **[Question]** — [why they'll ask] → [suggested answer; flag if a figure
   needs verification or compliance wording]
...

## Handle proactively
- [Sensitive item] — [recommended framing, one line]

## Gaps in this brief
[What wasn't in the record: e.g., no holdings data supplied.]
```

## What LPs ask, by investor type

The likely-questions section should be seeded by who is across the table. Patterns that hold widely:

- **Public pensions** — process, consistency, and defensibility: fees and transparency, benchmark-relative performance, team stability, anything a board or beneficiary could read about. They ask what they will have to justify upward. Expect questions traceable to their consultant's checklist.
- **Consultants** — the checklist plus the delta: what changed since the last review — personnel, process, terms, AUM. They are pattern-matching across every manager they cover, and inconsistency with what you told them last time costs more than a soft number honestly explained.
- **Endowments and foundations** — the thinking, not just the results: sourcing edge, why this strategy now, portfolio construction, what you're seeing in the market. More willing to tolerate short-term underperformance if the reasoning is sound; least tolerant of a partner who can't go off-script.
- **Family offices** — alignment and access: GP commitment, fee terms, co-invest availability, who they actually get on the phone. Decisions can be fast and personal; a relationship lapse (a forgotten open item) does disproportionate damage here.
- **Insurance companies** — cash-flow shape and treatment: pacing, duration, distributions, and regulatory capital treatment of the exposure. Performance questions come denominated in yield and loss rates more than multiples.
- **Sovereigns and large platforms** — capacity, scalability, and governance: how much they could deploy, side-letter and reporting accommodation, key-person terms. The meeting may be one gate in a long institutional process; the question behind their questions is whether the firm can service them at their size.

Across all types: whatever is worst in the current numbers will be asked about. The brief should assume the LP has read their statement.

## Guardrails

- **Nothing about the relationship is invented.** Every touchpoint, promise, holding, and figure traces to the supplied record. Gaps are labeled, never smoothed. A brief that misremembers on the partner's behalf is worse than no brief.
- **Performance figures are carried, not computed or estimated.** If the LP-level numbers aren't supplied, the section is omitted and marked — a partner quoting an inferred IRR in an LP meeting is the exact failure this skill must never cause.
- **Suggested answers are drafts for a human, not a script.** Answers touching performance, track record, terms, or regulatory matters are flagged for the same review they would need in writing; a verbal answer to an LP is still a representation.
- **Sensitive items are stated plainly inside the brief.** The document's job is to arm the partner, not to protect them from the file. Softening the markdown in the brief guarantees it lands worse in the room.
- **News is cited and dated.** Public information about the LP's organization carries its source; rumor and secondhand color are labeled as such or left out.
- **This is preparation, not personal-data compilation.** Attendee background stays at the professional level relevant to the meeting — roles, tenure, prior interactions with the firm — not personal detail scraped for leverage.
- **Confidentiality:** the CRM record, email history, holdings, and performance data are confidential, and LP-specific terms may be NDA-bound. Assume a firm-approved AI environment, and never carry one LP's terms or holdings into a brief about another.

## Example prompts

> "I'm seeing [pension fund] Thursday — their side is [CIO name] and [PE program lead]. Attached: CRM export for the relationship, the email history, and their holdings summary across Funds II and III. Build the one-pager. They care about net IRR versus [benchmark], and I want the open items front and center — I think we owe them co-invest data from the spring."

> "First meeting with a family office that got introduced through [mutual contact] — no history with us at all. Here's the fund one-pager and what we know about them. Build the brief around who they are, what a family office will push on, and the five questions I should expect on a first meeting about Fund I."

> "Damage-control prep: [LP] is unhappy about the Q2 markdown in Fund III and asked for this meeting. Attached are the relationship record and their numbers. I want the sensitive-items section to lead — give me the honest framing for the markdown and predict the hard questions, not the easy ones."

## Works well with

Run **professional-profile-brief** when a specific attendee — a new CIO, an unfamiliar consultant lead — deserves a deeper individual read than the one-pager allows. Afterward, **call-transcript-followup** closes the loop on the meeting notes, and its action-item capture is what makes the next brief's open-items section accurate.
