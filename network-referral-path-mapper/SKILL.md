---
name: network-referral-path-mapper
description: >-
  Given a target — a company to source, an LP to raise from, an executive
  to reference, a name on next week's calendar — work the firm's whole
  relationship surface (email and calendar history, the CRM, board and
  portfolio rosters, public professional profiles) and return every
  connection path ranked by strength: who holds the relationship, how
  recently and how often they interact, what the shared context was, and
  whether the intermediary actually makes introductions. Surfaces the two
  or three second-degree routes worth trying when the direct path is cold,
  flags when two colleagues are about to reach out to the same person, and
  ends with the drafted ask for whoever is best placed to make the intro —
  or a plain "no known path" when the firm has none. For deal-origination
  and business-development teams, investor-relations teams, family-office
  and allocator staff, and research managers checking interaction history
  before meetings. Trigger on phrases like "who do we know at [firm],"
  "who can get us to [name]," "warm path to [target]," "does anyone here
  know [person]," "how are we connected to [company]," "best route into
  [LP]," "have we ever talked to these people," or when a user provides a
  target name plus a CRM export or contact list and asks about
  connections. Do NOT use for summarizing where one existing relationship
  stands before re-engaging — use the relationship-status-summarizer
  skill. Do NOT use for a briefing on one LP ahead of a meeting — use the
  lp-meeting-prep-brief skill. Do NOT use for a banker's deal-by-deal history
  before a coverage meeting; this skill maps paths, not deal records. Do
  NOT use for screening a conference delegate list — use the
  conference-attendee-screen skill. Email, calendar, and CRM data are
  internal and personal to the colleagues who generated them; the skill
  reports relationships, never message contents, and assumes the owner of
  a relationship is asked before it is used.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Network Referral Path Mapper

The question "does anyone here know them?" gets asked out loud, in a group chat, or not at all — and the answer depends on who happens to be in the room and what they happen to remember. Meanwhile the firm's actual network sits across a dozen inboxes, a CRM nobody fully trusts, portfolio-company boards, and the professional histories of everyone who has ever worked there. This traverses that surface from a target back to whoever can reach it: every path, ranked by how warm it really is, with the shared context that makes an introduction natural, the second-degree routes if the direct one has gone cold, and the intro request drafted for the colleague best placed to send it.

## Why this skill exists

A firm's collective network is much larger than any individual's map of it, and the gap is where sourcing and fundraising leak value. The partner who sat on a board with the target's former CFO does not know the associate is cold-emailing that company; the IR lead does not know that a portfolio CEO went to business school with the allocator's new head of privates. None of this is hidden — it is in calendars, in old deal logs, on public profiles — but nobody has stitched it together for the specific name in question, so the warm path goes unused and the cold one goes out. The cost is not just a lower hit rate; a cold approach to someone a colleague knows well actively damages the relationship the colleague built.

The second reason is that "connected" and "warm" are not the same thing, and every relationship tool conflates them. A CRM shows a contact exists; it does not show that the last real exchange was four years ago, that every message since has been one-directional, or that the person who owns the relationship has never once made an introduction for anyone. Path strength is a judgment about recency, reciprocity, seniority, and the intermediary's own habits, and it has to be made per path — a strong-looking direct connection is often worse than a slightly indirect one through someone who actually picks up the phone.

The third is etiquette. Relationships inside a firm belong to the people who built them, and using one without asking is how partnerships fray. A good referral-path answer is therefore not just "reach out to X"; it is "Y holds this relationship, here is what Y would need to know to make the ask comfortably, and here is who else is circling the same name so two people do not reach out in the same week." The skill exists to make the internal conversation happen before the external one.

## Inputs

**Required:**
- The target: a person (name, title, organization) or an organization with a note on the role you need to reach inside it
- The purpose of the approach — sourcing a deal, an LP allocation, an executive reference, a channel check, a pre-meeting history check — since the right path differs by purpose
- Some relationship material: a CRM export, a contact list, an exported email or calendar history, a board or portfolio roster, or a pasted list of "people we know" with context

**Optional but high-value:**
- **Email and calendar metadata across the team** — sender, recipient, date, and subject are enough; message bodies are not needed and should not be shared
- The CRM's interaction log with owner, last-touch date, and any notes on how the relationship was formed
- Board and advisory rosters for portfolio companies, plus the firm's own alumni and former colleagues
- Public professional profiles for the target and for the firm's senior people, which reveal shared employers, schools, and boards the CRM never recorded
- Any recent outreach to the target or their organization by anyone at the firm, to avoid a collision
- The firm's internal norms on relationship ownership — who must be asked before a partner's contact is used

**Missing-input behavior:** The baseline run works from whatever was pasted or exported: a CRM export alone yields direct paths with recency and owner; a contact list alone yields candidate paths with no strength score beyond "in the database." Say which level of evidence each path rests on. Never fabricate a relationship, a shared history, or an interaction that is not in the material — a plausible-sounding path ("they were likely at the same conference") is not a path. If the material shows no route to the target, the answer is "no known path," stated plainly, followed by the nearest adjacent route (someone at a peer organization, a former colleague of the target found on a public profile) labeled as a lead to develop rather than a connection the firm holds. Connected email and CRM systems make the traversal complete and current; they are an upgrade, not a precondition.

## How it works

1. **Resolve the target.** Confirm the person or organization, current role, and prior roles from public profiles, since the useful connection is often to who they were three employers ago. For an organization target, identify the two or three people inside it worth reaching for this purpose, and treat each as a target.
2. **Sweep the relationship surface for direct hits.** Search the CRM, email and calendar metadata, deal logs, and rosters for the target and their organization. For every colleague who appears, record the owner, the first and last dated interaction, frequency over the past two years, and how the relationship was formed if the record says.
3. **Expand to second degree through the target's history, not the firm's.** Take the target's prior employers, boards, schools, and co-investors from public profiles and search the firm's surface for those instead. This is where the real paths are: the portfolio CEO who worked under the target a decade ago, the LP whose board the target sits on. Cap the search at two degrees — a third-degree path is a rumor.
4. **Score each path on five signals**, stated separately rather than blended into one number. *Recency* — a dated interaction inside twelve months is warm, inside three years is tepid, older is a memory. *Frequency* — repeated exchanges over time outweigh a single meeting, however memorable. *Reciprocity* — two-way correspondence and accepted meetings beat one-directional outreach; a contact who has never replied is not a relationship. *Seniority fit* — the intermediary should be at a level the target would take a call from, and the ask should not require them to reach up. *Willingness* — whether the intermediary has made introductions before, from the CRM and from anything the team knows; some excellent relationships belong to people who never spend them, and that path should rank accordingly.
5. **Handle the same name in two colleagues' histories** by comparing, not merging. Two colleagues who each know the target hold two different relationships with different warmth and different context; report both, name the stronger one as the primary, and note whether the two colleagues know about each other's connection — often they do not, and telling them is itself useful.
6. **Run the collision check.** Look for any recent or planned outreach to the target or their organization from anyone at the firm, and for any live process — a deal in diligence, a fundraise in progress, a portfolio-company negotiation — that the approach could cut across. Two partners reaching out to the same allocator in the same month reads as disorganization; an associate cold-calling a company the firm is already talking to through a banker is worse. Flag it before the ask is drafted, not after.
7. **Rank the paths and say why.** Order by the composite of the five signals, but show the reasoning — a path that scores high on recency and low on willingness should be ranked below one that is a year older but held by someone who makes introductions freely. Separate paths into *warm* (a colleague can make the intro this week), *viable* (a colleague could re-open the relationship first), and *visible only* (the name is in the database and nothing more).
8. **Choose the ask and the asker.** Pick the best path's intermediary and match the ask to the shared context: a former colleague introduces differently from a co-investor, and a board member has obligations neither has. Decide whether the right request is a direct introduction, a mention that the firm will be reaching out, or simply intelligence on how the target prefers to be approached.
9. **Draft the internal ask first.** Write the note to the colleague who owns the relationship: what the firm wants from the target, why this colleague's connection is the right one, what the colleague is being asked to do, and an explicit out if they would rather not spend the relationship on this. The external introduction text is a draft the colleague can edit, offered alongside, never sent around them.
10. **Close with the honest summary:** the recommended path and its weakest signal, the fallback if the intermediary declines, who else at the firm should know before anyone reaches out, and — where the material supports nothing better than a cold approach — say that, and give the most credible cold angle instead of an inflated warm one.

## Output format

A skeleton to adapt — the ranked path table and the internal ask are the core; everything else scales with the number of paths found.

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# Referral paths — [target, title, organization]
Purpose: [sourcing / LP raise / reference / pre-meeting check]
Sources searched: [CRM export dated __, calendar metadata for __, rosters, public profiles]
Coverage: [whole firm / deal team only / one inbox] — paths outside this scope are not visible

## Recommended path
[Colleague] → [target], via [shared context]. Warmth: [warm / viable].
Weakest signal: [e.g., no two-way contact in 18 months].
Collision: [none found / note]

## All paths, ranked
| # | Holder | Route | Shared context | Last contact | Freq (2y) | Two-way? | Makes intros? | Tier |
|---|---|---|---|---|---|---|---|---|
[1 row per path; second-degree routes show both hops]

## Second-degree routes worth developing
- [Person the firm knows well] → [target's former employer / board / co-investor] — [why it plausibly reaches the target; evidence level]

## Collision check
[Recent or planned outreach to the target or organization by anyone at the firm;
live processes the approach could cut across; who should be told first]

## Internal ask — to [relationship holder]
[Draft note: what we want, why their connection, what we are asking them to do,
and the explicit out if they would rather not use the relationship for this.]

## Introduction draft — for [holder] to send or adapt
[Short, in the holder's voice, referencing the shared context; not to be sent by anyone else.]

## If no path holds
[Nearest adjacent lead, labeled as a lead; the most credible cold angle.]
```

## What makes a path strong — and what makes it merely visible

Relationship data flatters itself. A CRM with 40,000 contacts implies 40,000 relationships; the number of people at the firm who could get a reply from any given one is far smaller. The distinctions that matter:

- **A contact record is not a relationship.** Business cards scanned after a conference, mass-mailing list members, and inbound cold pitches all populate a CRM. A path built on one of these is "visible only" and should say so; ranking it alongside a genuine relationship misleads whoever acts on the list.
- **Recency decays faster than people think.** A warm relationship that has gone eighteen months without two-way contact needs to be re-opened before it can be spent on an introduction. The right first step on such a path is often the colleague re-engaging the intermediary directly, with the ask coming a conversation later.
- **Reciprocity is the strongest single signal.** Accepted meetings, replies, and introductions received in the past are evidence the other party values the relationship. One-directional outreach — however frequent — is evidence of the opposite, and a colleague who has sent nine unanswered notes does not hold a path.
- **Shared context sets the tone of the ask.** Former colleagues can ask for a favor; co-investors can ask for a courtesy; a shared board seat carries fiduciary overtones and the ask must be appropriate to it; a mutual school or hometown is a conversation opener, not a route. Match the ask to the strongest context on the path, and name the context in the draft.
- **The intermediary's own habits decide more than the relationship's strength.** Some people make introductions constantly and cheaply; some never do, and treat every request as a withdrawal from a small account. A firm's history of asks tells you which is which — a path through a generous connector at the second degree often beats a direct connection held by someone who will not spend it.
- **Seniority runs both ways.** A junior colleague with a genuine relationship to a senior target is a real path, but the introduction may need a senior name on it to be taken seriously; a senior partner asking a junior contact to introduce them upward puts the contact in an awkward position. Note when the path needs a seniority bridge.
- **Public profiles find paths the CRM never recorded.** Shared prior employers and boards between the target and the firm's people are the highest-yield source of overlooked routes — and the lowest-confidence, since a shared employer in overlapping years is a lead, not proof they knew each other. Label these as such and let the colleague confirm.
- **The organization is not the person.** Knowing three people at the target's firm does not mean knowing the target, and paths to an organization should name who inside it the path actually reaches. Internal introductions across a large organization are their own second hop.

## Guardrails

- **Never invent a connection.** Every path rests on a dated interaction, a record, or a public fact, and each is cited. Plausible overlaps — same city, same conference circuit, same sector — are not paths and are not presented as leads unless the material supports them.
- **The owner of a relationship is asked before it is used.** The internal ask to the colleague comes first and includes an explicit out; no introduction text is sent, forwarded, or adapted by anyone other than the person whose relationship it is. Where the firm has norms on partner contacts, follow them.
- **Report relationships, not correspondence.** Email and calendar data are used for sender, recipient, date, and subject; message contents are not quoted, summarized, or characterized. Interaction history is described at the level of "met twice in 2025 about a co-investment," never the substance of what was said.
- **Confidentiality of the source data.** CRM, email, and calendar exports are internal, and often personal to the colleague who generated them. Assume a firm-approved AI environment; reproduce nothing beyond what the path table requires; do not retain or restate contact details outside the output.
- **No speculation about personal matters.** Family, health, finances, personal relationships, and private circumstances of the target or any intermediary are out of scope even where the material hints at them. Shared context means professional context.
- **A cold answer is a valid answer.** "No known path" with the nearest lead is more useful than a manufactured warm route that embarrasses a colleague. Do not upgrade a visible-only contact to viable to make the list look better.
- **Collision findings are surfaced, not suppressed.** If the approach cuts across a live process or someone else's outreach, that is the lead finding of the output even when it makes the recommended path unusable.
- **Not advice.** Path rankings are relationship intelligence to support a colleague's own judgment about whom to ask and how; they are not a recommendation to transact, to raise from, or to hire anyone, and the target's fitness for any purpose is outside the skill.

## Example prompts

> "We want a look at [company] before it goes to a banked process. Here is our CRM export and the deal team's calendar history for the past two years. Who do we know who can get us to the founder or the CFO, how warm is each path really, and draft the note to whichever partner owns the best one — I don't want three of us emailing them the same week."

> "Family office, small team. I'm pasting our contact list with a column for how each person knows us, plus board rosters for the operating companies. Target is the new head of private markets at [allocator]. Map every route, tell me which ones are actually warm versus just names we have, and tell me plainly if we have nothing."

> "I have a meeting Thursday with [name] at [firm] and I'd like to know if anyone here has ever dealt with them or their organization before I walk in. Attached is our interaction log and a calendar export for the research team. Don't summarize what was discussed — just who, when, how often, and whether it was two-way."

## Works well with

Once a path is chosen and the target is an allocator, **lp-meeting-prep-brief** prepares the eventual meeting. For executive references, the paths this skill finds become the reference call list, and a delegate list from **conference-attendee-screen** is a natural batch of targets to run through here before the event.
