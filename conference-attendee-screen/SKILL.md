---
name: conference-attendee-screen
description: >-
  Screen a deal conference's attendee or delegate list — sector summits,
  sponsor-lender events, industry trade shows — against a firm's live
  investment themes and CRM. Enriches each attendee company from public
  sources (what it actually does, revenue or headcount signals, ownership
  status, recent transaction news), scores it against the themes as strong
  fit, adjacent, or no fit with a one-line reason, and cross-references CRM
  history so the team knows who it already covers, who owns each
  relationship, and who is genuinely new. Output is a tiered meeting target
  list capped at a workable number, a draft outreach note per tier-1 name
  that references something specific about the business, and an explicit
  no-fit list with reasons so the same names never get re-screened. For PE
  and private credit origination teams, business development, and deal
  professionals working a conference for deal flow. Trigger on phrases like
  "screen this attendee list," "who should we meet at [conference]," "run
  the delegate list against our themes," "conference target list," "who's
  worth meeting here," "sort this exhibitor list," or when a user uploads an
  attendee list alongside investment themes. Do NOT use for preparing an LP
  or fundraising conference schedule — use the conference-prep-planner
  skill. Do NOT use for a deep brief on one individual before a meeting —
  use the professional-profile-brief skill. Attendee lists and CRM exports
  are confidential; assume a firm-approved AI environment.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Conference Attendee Screen

A 600-person delegate list is theoretically the highest-density sourcing opportunity of the quarter, and practically it gets skimmed on the flight over — because screening it properly means 600 lookups nobody has time for, so the conference gets spent with the people you already know. This does the 600 lookups: every attendee company enriched from public sources, scored against your live themes with a one-line reason, cross-referenced against the CRM so nobody courts a colleague's relationship, and reduced to a tiered target list with a specific outreach note per must-meet name — before you book flights, not after.

## Why this skill exists

Conference sourcing fails by defaulting. The delegate list arrives three weeks out, the screening job is real but unglamorous, and it loses the priority fight every day until the flight — at which point the schedule fills with the path of least resistance: existing relationships, inbound requests, and booth adjacency. The firm pays for a sourcing trip and gets a maintenance trip. The attendees who would have justified the whole conference — the founder-owned distributor squarely inside a live theme, attending precisely because they are starting to think about a process — walk the same floor unmet, because meeting them required knowing they mattered, and knowing they mattered required the lookup nobody did.

The screening itself has a quality problem too, when it happens at all. Skimming a list pattern-matches on names and industry labels, and both mislead: "logistics" on a badge spans freight brokerage, warehouse robotics, and last-mile software, which are three different theses; meanwhile the dull-sounding company name that fits perfectly gets skipped because nothing about the name says so. Genuine screening is per-company work — what it does, what it might earn, who owns it — and that work is exactly what compresses out under time pressure.

The CRM cross-reference is the third leg, and it prevents two embarrassments that recur at every large firm: two colleagues independently courting the same company, and an enthusiastic cold approach to a founder a partner already knows — where the cold note reads as the firm not talking to itself. And the no-fit list, the least glamorous output, is what stops the same 400 names from being re-screened from scratch at the same conference next year.

## Inputs

**Required:**
- The attendee, delegate, or exhibitor list, in whatever form the organizer provides — export, PDF, or pasted
- The firm's live investment themes, described concretely enough to screen against: sector, size range, ownership preference, and what makes a company interesting within the theme

**Optional but high-value:**
- **A CRM export of companies and contacts the firm tracks** — this enables the coverage cross-reference, which is the difference between a target list and a collision map; a spreadsheet of names and owners is enough
- The number of meeting slots realistically available, which sets the tier-1 cap
- Prior screens of the same conference, so returning no-fits carry forward instead of being re-worked
- The conference agenda, since a target speaking on a panel is easier to meet than one to find on a floor
- Who from the firm is attending, so targets can be matched to the right person
- Live connected sources (CRM, email) as an upgrade path — the baseline runs entirely from the exported and pasted materials

**Missing-input behavior:** List plus themes runs the screen; without a CRM export, skip the coverage cross-reference and say so — never guess at who owns a relationship. Where public information on a company is thin or ambiguous, say "could not reliably determine" and park the name on an unresolved list rather than scoring a guess; a wrong enrichment silently propagates into a wasted meeting or a skipped gem. Individuals who attend without a company affiliation are listed separately, not force-matched to same-named companies.

## How it works

1. **Parse and de-duplicate the list.** Multiple attendees from one company collapse into one company entry with its people attached — the unit of screening is the company; the unit of outreach is the person, and seniority among the attendees changes who to approach.
2. **Enrich each company from public sources:** what it actually does in one concrete sentence (not its tagline), size signals (disclosed revenue, headcount, locations, fleet — whatever the sector's honest proxy is), ownership status (founder or family, sponsor-backed and which vintage, subsidiary, public), and recent news — financings, acquisitions, leadership changes. Distinguish found facts from inference, and mark every company where reliable information could not be found rather than papering over it.
3. **Score against the themes** — strong fit, adjacent, or no fit — with a one-line reason naming the specific theme and the specific evidence. "Strong fit: route-based commercial services theme — 400-tech HVAC servicer, family-owned, ~$12M EBITDA by headcount proxy" earns its tier; "fits logistics" does not. The scoring discipline lives in the fit-versus-noise section below.
4. **Cross-reference the CRM:** already covered and by whom, contacted before and what happened (a passed deal, a dormant thread, a banker relationship), or genuinely new. Prior contact is not disqualifying — a company passed on two years ago at a silly price may be the best meeting at the show — but it changes who reaches out and what the note says.
5. **Flag conflicts between public information and the CRM** — the CRM says founder-owned, the news says a sponsor bought it last spring — explicitly, because a stale CRM record walking into a meeting is worse than no record.
6. **Tier the targets:** tier 1 must-meet, capped at what the calendar can actually hold and ordered by fit; tier 2 opportunistic, worth a floor conversation if paths cross. Resist tier inflation — a 40-name tier 1 for a two-day conference is a skimmed list wearing a ranking.
7. **Draft the tier-1 outreach notes** — short, specific, and referencing something real about their business (per the note anatomy below), written for the named firm attendee to send in their own voice. Adjust where a relationship owner exists: the note routes through them or references them, never around them.
8. **Assemble the no-fit list with reasons,** one line each, so next year's screen of the same conference starts from a decision log instead of a blank sheet — and so a colleague can audit whether a no-fit call was right.
9. **Package for the trip:** the tiered list ordered by fit, people to approach per company, agenda intersections where the agenda was provided, and the unresolved list as its own short section — names worth a hallway question precisely because the public record was thin.

## Output format

A skeleton to adapt to list size and firm conventions.

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# Conference Attendee Screen — [conference, dates]
List: [N attendees, M unique companies] | Themes: [short labels]
CRM cross-reference: [run / not provided] | Tier-1 cap: [N]

## Read on the list (one paragraph)
Density of genuine fits, which theme this conference actually serves, and
whether the trip's meeting capacity matches the opportunity.

## Tier 1 — must meet ([N], ordered by fit)
### [Company]
**What it does:** [one concrete sentence]
**Signals:** [size proxy | ownership | recent news]
**Theme fit:** [theme] — [one-line reason]
**CRM:** [new / covered by (owner) / prior contact + outcome / CONFLICT]
**Who attends for them:** [names, titles] | **Approach via:** [firm attendee]
**Draft note:** "[2–4 sentences, specific to their business]"

## Tier 2 — opportunistic
| Company | What it does | Fit reason | CRM status | Attendees |
|---|---|---|---|---|

## CRM conflicts and coverage flags
| Company | CRM says | Public record says | Action |
|---|---|---|---|

## Could not reliably determine
| Company | What's known | What's missing | Worth a hallway question? |
|---|---|---|---|

## No fit ([N] — kept for reuse)
| Company | Reason |
|---|---|
```

## Fit versus name-matching noise

The screen's value is the gap between what a company is and what its name and badge category suggest. The discipline:

- **Score the business, not the label.** Conference categories are marketing taxonomy. A theme is a thesis about economics — recurrence, fragmentation, ownership, size — and the test is whether *this company's actual operations* express those economics, which the one-sentence description either demonstrates or doesn't.
- **Adjacent is a real category, not a soft yes.** Adjacent means one identifiable attribute short of the theme — right sector but likely above the size band, right model but sponsor-owned in year two. Name the missing attribute; "sort of fits" is noise wearing a tier.
- **Ownership status is the sharpest single filter for deal relevance** — a founder-owned company in-theme is a different object from the same company eighteen months into sponsor ownership — and it is also the fact most often stale in both public sources and CRMs. Check it last-known-date, not just last-known-value.
- **Beware the well-known name.** Recognizable companies drift into tier 1 on familiarity. Familiarity is not fit; a famous no-fit is still a no-fit, and it costs a scarce meeting slot.
- **Absence of information is information to flag, not to fill.** A thin public record is common precisely in the founder-owned, never-raised, never-pressed companies the themes want most — which is why the unresolved list is a feature, not a failure state.
- **A good pre-meeting note** — and the target note the screen drafts — has four properties: it names something specific and recent about their business (proof of homework, one sentence); it states plainly why the firm is relevant to them (a theme, an owned company they would know, a pattern — not "we invest in great businesses"); it makes one small ask (fifteen minutes at the event, not a process); and it omits everything else. Two to four sentences. Anything longer reads as a mail merge, and founders can smell a mail merge from the subject line.

## Guardrails

- **Enrichment is public-source only, about companies.** Business facts, ownership, transactions, and professional roles — no personal-life details about attendees, no compiling of personal information beyond name, title, and employer as the list itself states them.
- **Never guess an enrichment.** Ambiguous name matches (three companies called "[Summit] [Sector]"), thin records, and conflicting sources land on the unresolved list, stated as unresolved. One confidently wrong "what it does" poisons trust in the whole screen.
- **Facts versus inference stay labeled.** A headcount from a filing is a fact; "~$12M EBITDA by headcount proxy" is an inference and says so.
- **CRM ownership is respected in every output.** No draft note routes around an existing relationship owner; conflicts between CRM and public record are flagged for a human, never silently resolved in either direction.
- **Tier caps are honored.** The cap exists because meetings are the scarce resource; if more strong fits exist than slots, say so and rank — do not widen the tier.
- **No-fit reasons are recorded, never discarded** — the reuse value of the screen lives there.
- **Not investment advice.** Fit scores rank meeting priority against stated themes; they are not a view on any company's merits as an investment.
- **Confidentiality:** attendee lists usually carry organizer terms restricting use, and CRM exports and live theme descriptions are competitively sensitive — a firm's themes are its pipeline strategy. Assume a firm-approved AI environment and keep the screen internal.

## Example prompts

> "Attendee list for [conference, dates] attached — about 550 names. Our themes: route-based commercial services, specialty distribution with fragmented supply, and healthcare compliance software, all $3–20M EBITDA, founder or family owned. CRM export attached too. Tier-1 cap of 12; [partner] and I are attending. Full screen, notes for tier 1, and flag anything where the CRM looks stale."

> "Same trade show as last year — last year's screen attached, this year's exhibitor list attached. Carry forward the no-fits, screen only what's new or changed, and tell me which of last year's tier-1 companies are back."

> "No CRM export for this one — just the delegate list and our themes: [describe]. Screen and tier, skip the coverage check, and give me the unresolved list separately; thin public record is a good sign for what we hunt."

## Works well with

Run **professional-profile-brief** on the individuals behind each tier-1 meeting once the schedule is set — the screen picks the companies; the brief preps the conversations. Use **intro-email-generator** where an outreach note needs a warm-path version through a shared connection, and keep **conference-prep-planner** for the LP-fundraising conferences this skill deliberately does not cover.
