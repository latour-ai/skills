---
name: ddq-answer-library-curator
description: >-
  Run the quarterly hygiene pass on a firm's DDQ answer library: reconcile
  every answer against the current golden-source documents (PPM, Form ADV,
  compliance manual, fund reports, team pages), flag every figure that no
  longer matches the source with both values side by side, flag answers
  referencing superseded policies, departed personnel, or prior-fund terms,
  flag answers past their re-approval window, and identify duplicate or
  near-duplicate answers to consolidate — outputting a fix-list grouped by
  answer owner and ranked by risk. For IR, fundraising, COO, and compliance
  teams at private equity, private credit, hedge fund, real assets, and
  venture managers. Trigger on phrases like "audit the answer library,"
  "scrub the DDQ library," "staleness check," "quarterly library review,"
  "are our DDQ answers current," "dedupe the answer library," or when a
  user uploads an answer library export alongside current fund documents.
  Do NOT use for drafting responses to an incoming DDQ or consultant RFP —
  use the ddq-response-drafter skill. Never rewrites an approved answer
  itself; it flags, recommends, and routes to owners for re-approval.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# DDQ Answer Library Curator

An answer library is only as good as its worst stale entry, and the stale entry surfaces at the worst possible moment — quoted confidently in a DDQ that an LP's operational due diligence team then checks against your Form ADV. This is the maintenance counterpart to DDQ drafting: a systematic sweep that reconciles every library answer against the current golden-source documents, flags what has drifted, retires what has been superseded, and hands each owner a ranked punch list — so that every questionnaire drafted downstream inherits accuracy instead of inheriting last fund's numbers.

## Why this skill exists

Nobody volunteers for the quarterly library scrub. It is unglamorous, it has no deadline until a DDQ arrives, and it requires reading the compliance manual against three hundred answers — so it slips, quarter after quarter, until an LP catches the discrepancy. And the discrepancy an LP catches is never the embarrassing-but-harmless kind: it is the AUM that doesn't match the ADV, the track record that still includes a fund the firm stopped marketing, the key-person answer naming someone who left in the spring. Every one of those becomes a question in the ODD call, and the real damage is not the correction — it is that the LP now re-verifies everything else you sent.

The library also rots in a second, quieter way: duplication. Every rushed DDQ adds a lightly-edited variant of an existing answer, and within two fundraises there are five descriptions of the valuation policy, four of them stale, and the drafter under deadline picks whichever one the search surfaced first. Deduplication is not tidiness — it is the mechanism that makes "update the answer" mean anything. One canonical answer per fact, or updates silently miss the copies.

The third failure is treating staleness as a calendar problem. A twelve-month re-approval cycle catches slow drift, but the answers that hurt go stale the day something happens — a fund closes, a partner departs, a policy is amended, an exam letter arrives. A curator worth having reads the current source documents for what changed, not just the timestamps for what is old.

## Inputs

**Required:**
- **The answer library export** — per entry, ideally: answer text, topic or question, source document, approval or as-of date, and owner. A prior completed DDQ can stand in as a rough library, with the caveat that it carries no approval metadata.
- At least one current golden-source document to reconcile against — the more, the better the audit.

**Optional but high-value:**
- **The full golden-source set:** latest PPM or LPA, Form ADV, compliance manual, most recent quarterly fund report, current team bios or org chart, current fund terms. Each document unlocks a category of check; the ADV and the latest fund report catch the most.
- Current firm facts with as-of dates: AUM, fund sizes, headcount by function, portfolio company count
- A list of known changes since the last scrub — departures, fund closes, policy amendments, new regulatory events — so the event-driven checks have a target list
- The firm's re-approval policy (e.g., 12 months, or per-category), so the aging flags match the actual standard
- The date and output of the last library audit, for a what-changed comparison
- Owner roster mapping answer categories to responsible people, for routing

**Missing-input behavior:** The library alone supports the internal checks — duplicates, aging against a stated or assumed re-approval window, internal contradictions between answers — and that pass is worth running on its own; label it as a partial audit. Each reconciliation check runs only against the source documents actually provided: no ADV means no ADV reconciliation, said explicitly in the output, not silently skipped. Never assert that an answer is current merely because no provided source contradicts it — the honest status is "not verifiable against provided sources." And never draft the corrected answer as if approved: the skill recommends the fix and routes it; re-approval belongs to the owner.

## How it works

1. **Inventory the library first.** Count entries, map coverage by topic (organization, strategy, performance, valuation, compliance, operations, ESG, terms), and note which entries carry full metadata — source, approval date, owner — and which are orphans. The metadata gaps are themselves findings: an answer with no owner has no one accountable for its accuracy.
2. **Extract every checkable fact from the library:** figures (AUM, returns, fund sizes, headcounts, dates), named people and roles, named policies and their described mechanics, fund terms, service providers. This fact ledger is what gets reconciled; narrative style is not the audit's business.
3. **Reconcile figures against the current sources,** showing both values side by side with each document's as-of date. Distinguish a genuine mismatch from a vintage difference — an answer stating AUM "as of 12/31" is not wrong for being old, but it is flagged if a newer figure exists and the answer presents itself as current.
4. **Check the people and policy references.** Answers naming departed personnel, describing superseded policy versions, or citing prior-fund terms are the highest-embarrassment category — they signal to an LP that the firm doesn't read its own materials.
5. **Run the event-driven staleness pass.** From the provided sources and any stated changes, identify what happened since the last scrub — fund closed, policy amended, team changed, regulatory event — and sweep for every answer that event touches. This catches what calendar aging misses.
6. **Flag calendar aging** against the re-approval window: answers past the window with no re-approval, oldest first, with performance and regulatory answers held to the tightest standard.
7. **Find duplicates and near-duplicates** — answers covering the same fact or topic in divergent language. For each cluster, recommend the canonical survivor (usually the most recent approved version that matches current sources) and mark the rest for retirement, not deletion — retired language may need to be traceable if it was sent to an LP.
8. **Check the library against itself.** Two answers implying different headcounts, a valuation answer inconsistent with the conflicts answer — internal contradictions get caught by LPs who read the whole DDQ, so the audit reads the whole library.
9. **Assemble the fix-list grouped by owner,** ranked by risk: performance and track record figures first, regulatory and policy statements second, personnel third, everything else after. Each item carries the recommended action — update, retire, consolidate, or re-approve as-is — with the evidence beside it.
10. **Summarize library health** — a snapshot the next audit can be compared against: entries current, stale, orphaned, duplicated, and the categories where drift concentrates.

## Output format

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# Answer Library Audit — [firm] 
Audit date: [ ] | Library export: [date, N entries] | Last audit: [date / none]
Sources reconciled against: [ADV dated __, PPM dated __, ...]
Checks skipped for missing sources: [ ]

## Library health summary
Current: [N] | Flagged stale: [N] | Duplicate clusters: [N] | Orphaned (no owner/date): [N]
Highest-risk finding: [one line]

## Figure mismatches
| Answer (ID/topic) | Value in library | As of | Current source value | Source, as of | Owner |
|---|---|---|---|---|---|

## Superseded references
| Answer | What it references | What changed | Evidence | Owner |
|---|---|---|---|---|
[Departed personnel, amended policies, prior-fund terms.]

## Aging — past re-approval window
| Answer | Approved | Age | Category | Risk tier |
|---|---|---|---|---|

## Duplicate clusters
### [Topic]
**Entries:** [IDs] | **Recommended canonical:** [ID, why]
**Retire:** [IDs] | **Divergences between versions:** [ ]

## Internal contradictions
| Fact | Answer A says | Answer B says | Which matches current sources |
|---|---|---|---|

## Fix-list by owner
### [Owner]
| Priority | Answer | Finding | Recommended action |
|---|---|---|---|
[Action: UPDATE / RETIRE / CONSOLIDATE / RE-APPROVE AS-IS]
```

## Answer-library hygiene

The principles that separate a library that compounds from one that rots — worth encoding in the firm's process, not just this audit:

- **One canonical answer per fact.** The moment a fact lives in two entries, updates become probabilistic. Consolidate aggressively; variants for different formats (short-form, long-form) should share one underlying approved fact set.
- **Source and approval date on everything.** An answer without provenance cannot be efficiently re-verified, which means under deadline it gets used unverified. Metadata is not bureaucracy — it is what makes the library fast to trust.
- **Staleness triggers are events, not calendars.** A fund close, a departure, a policy amendment, a regulatory event, a new audit — each should trigger a targeted sweep the day it happens. The calendar cycle is the backstop, not the mechanism.
- **Retire, don't delete.** Superseded language that was sent to LPs may need to be produced later — in an exam, in an ODD follow-up asking why the answer changed. Retirement keeps it traceable without keeping it findable by a drafter in a hurry.
- **Performance answers age fastest and hurt most.** They get the tightest re-approval window, and any answer combining a performance figure with narrative gets checked whole — the figure may be updated while the surrounding claim went stale.
- **Owners are per answer, not per library.** "IR owns the library" means nobody owns any answer. The audit's fix-list is grouped by owner precisely because accountability is the mechanism that gets fixes done.
- **Every completed DDQ feeds back.** New questions drafted for one LP either enter the library through approval or are lost — and lost answers get re-drafted, slightly differently, forever.

## Guardrails

- **The curator flags; owners approve.** It never rewrites an approved answer and presents the rewrite as approved. Recommended language, where offered, is clearly marked as a draft for the owner's re-approval.
- **Every flag carries evidence.** A staleness flag shows the library value and the current source value side by side, with both documents' as-of dates. Unsupported flags waste owner time and erode trust in the audit.
- **Absence of contradiction is not verification.** An answer no provided source speaks to is marked "not verifiable against provided sources" — never "current."
- **Vintage is distinguished from error.** An answer honestly dated to an earlier period is aging, not wrong; an answer presenting an old figure as current is a mismatch. The two get different flags and different urgency.
- **Performance and regulatory findings route to compliance,** not just to the answer owner — a stale performance figure that went out in a DDQ may need more than a library edit.
- **Retired language stays traceable.** Recommend retirement with an audit trail, never silent deletion of anything that may have reached an LP.
- **No inference-refreshing.** The audit never estimates the current figure from trend — it reports what the source document says, or reports that no source was provided.
- **Confidentiality:** answer libraries, fund documents, and the audit's findings are confidential — the findings especially, since a list of every stale claim the firm has on file is exactly what should not leak. Assume a firm-approved AI environment.

## Example prompts

> "Quarterly scrub. Attached: our answer library export (answer, source, approval date, owner) and the current golden sources — ADV dated [March], the [Fund IV] PPM, compliance manual, Q[2] fund report, and the team page. Full audit: figure mismatches side by side, superseded references, anything older than 12 months without re-approval, and duplicates to consolidate. Fix-list by owner, performance items first."

> "We just had [a partner departure and a final close on Fund V]. Before the next DDQ goes out, sweep the attached library for every answer those two events touch — key person, team, succession, fund sizes, AUM, track record presentation — and tell me exactly what needs updating and who owns each."

> "No formal library — just our last three completed DDQs, attached. Build the audit from those: where do they contradict each other, what looks stale against the attached ADV, and which answers should become the canonical library entries versus be retired?"

## Works well with

This is the upstream half of the questionnaire workflow: run it quarterly and after every material firm event, so **ddq-response-drafter** drafts DDQ and RFP responses from a library that is actually trustworthy, with clean facts already in place when a deadline hits. Route the performance-answer findings through **marketing-compliance-prescreen** when the fix involves how track record is presented.
