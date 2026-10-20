---
name: fund-doc-consistency-checker
description: >-
  Cross-check the firm's governing and disclosure documents — PPM, LPA,
  Form ADV Parts 1 and 2A, DDQ, pitch deck, website disclosures — against
  each other whenever any of them changes, and surface every contradiction
  with the exact conflicting passages side by side, cited to document, page,
  and section: fee terms and offsets, capacity, strategy and concentration
  limits, key-person provisions, expense allocation, redemption terms. Rates
  each conflict as direct contradiction, material inconsistency, or wording
  drift, recommends conforming edits with a view on which document governs,
  and summarizes what must change before the revised document is used. For
  CCOs, compliance teams, and fund counsel liaisons at investment advisers
  and fund managers. Trigger on phrases like "check the revised PPM against
  everything," "does the deck match the ADV," "consistency sweep before the
  amendment," "cross-check our fund docs," "did the fee language drift,"
  "compare the DDQ to the LPA," or when a user uploads multiple fund
  documents with one revised. Do NOT use for prescreening a single marketing
  piece against the Marketing Rule — use the marketing-compliance-prescreen
  skill. Do NOT use for extracting side letter terms — use the
  side-letter-term-extractor skill. Surfaces conflicts for the compliance
  officer and counsel to resolve; never rewrites a governing document on its
  own, and never invents a passage or citation.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Fund Doc Consistency Checker

Your disclosure documents were drafted at different times, by different people, for different audiences — and every amendment is a fresh chance for them to drift apart. The drift is exactly what examiners are trained to hunt: the ADV that says one thing about fees while the PPM says another is a deficiency finding waiting for its exam. This makes the cross-check automatic whenever any document changes, and delivers conflicts the only way they're actionable — exact passages side by side, cited to page and section, rated by severity, with a recommended conforming edit and a view on which document should govern.

## Why this skill exists

No one reads the document set as a set. Each document has an owner and a revision cycle — counsel amends the LPA, IR refreshes the deck, compliance files the ADV amendment — and each revision is checked against its own prior version, not against its five siblings. Consistency is everyone's assumption and no one's job. The drift accumulates one reasonable edit at a time: the deck rounds a fee breakpoint for readability, the DDQ paraphrases the concentration limit from memory, the website summarizes the strategy in language two amendments old. Every individual edit was fine; the set is now internally contradictory.

The stakes are asymmetric by document pair. An inconsistency between the ADV and the PPM is a regulatory finding — the examiner's cross-reading is precisely this comparison, and "your own documents disagree" is the deficiency that requires no interpretive work to write up. An inconsistency between the LPA and the PPM is worse: investors were offered terms the governing contract doesn't deliver. Deck-vs.-DDQ drift, meanwhile, is what ODD analysts catch, and it costs credibility in diligence even when it's cosmetic. Treating all drift as equal makes the report unusable; the severity call is most of the value.

Manual cross-checking fails on combinatorics. Six documents is fifteen pairs, each pair touching a dozen topics, and the conflicting statements rarely share vocabulary — the LPA's "management fee offset" is the DDQ's "fee credits," and drift hides in the paraphrase. The comparison has to run on meaning, exhaustively, at the redline stage — because a contradiction found in a deficiency letter costs a remediation project, and the same contradiction found at the redline costs one conforming edit.

## Inputs

**Required:**
- Two or more of the firm's governing or disclosure documents (uploaded or pasted). The intended set: PPM/OM, LPA (or equivalent governing agreement), Form ADV Parts 1 and 2A, most recent completed DDQ, pitch deck, website disclosure pages. Any subset of two or more works; the more of the set provided, the more pairs get checked.
- **Which document changed and what changed in it** — a redline, an amendment, or a plain description ("we revised the management fee breakpoints and the capacity language"). This scopes the primary sweep.

**Optional but high-value:**
- **The prior version of the revised document** — lets the check distinguish newly introduced conflicts from pre-existing ones, which changes who fixes what and how urgently
- Side letters or a side letter summary, because the LPA is not the whole deal and an "all investors" statement elsewhere may be contradicted by a side letter, not by the LPA
- The firm's view on the document hierarchy, if it has one settled
- Any known open items from prior consistency reviews, so resolved-vs.-still-open is tracked
- Recent regulatory correspondence touching disclosure language, so known sensitivities get swept harder

**Missing-input behavior:** With no change identified, run a full-set consistency sweep across the standing topics rather than a change-scoped one, and say that's what happened. With only two documents, check that pair and list the pairs that couldn't be checked — an unchecked pair is never reported as consistent. Without the prior version, conflicts can't be sorted into new-vs.-pre-existing; label them undated rather than guessing. Never fill a missing document from memory of what such documents usually say, and never quote a passage that isn't in the provided text.

## How it works

1. **Establish the set and the trigger.** List the documents provided with their versions and dates, identify the revised document and the specific changes, and enumerate the document pairs in scope — including the pairs that *cannot* be checked because a document wasn't provided. The unchecked list is part of the deliverable.
2. **Extract the changed statements** from the revised document — each discrete assertion the revision added, deleted, or altered, cited to its page and section. A single redline sentence often carries several assertions (a fee rate, its base, its timing); split them, because they can each conflict independently.
3. **Sweep every other document for statements on the same subjects,** matching by meaning, not vocabulary. The fee offset, the fee credit, and the "reduction of the management fee" are one topic wearing three names; the sweep has to catch paraphrase, summary, and rounding, which is where real drift lives.
4. **Run the standing-topics sweep even where nothing changed** — fees and offsets, capacity, strategy and concentration limits, key person, expense allocation, redemption/withdrawal and transfer terms, valuation, conflicts disclosures. Amendments have a way of making pre-existing drift newly material, and the standing sweep is what catches the conflict nobody's edit caused.
5. **For each candidate conflict, quote both passages exactly,** cited to document, page, and section. Exact quotation is non-negotiable: the reader must be able to verify the conflict without opening either document, and a paraphrased "conflict" that evaporates on checking the source destroys the report's credibility.
6. **Rate severity honestly** on the three-tier scale: direct contradiction (the statements cannot both be true), material inconsistency (reconcilable, but an investor or examiner would fairly read them differently), wording drift (same substance, divergent language that will become a conflict at the next unsynchronized edit). Resist grade inflation in both directions — a report that cries contradiction at every rounding difference gets ignored, and one that soft-pedals a fee conflict as "drift" fails at its one job.
7. **Recommend the conforming edit for each conflict,** with a view on which document should govern. The default logic: the governing agreement controls economic and legal terms; regulatory filings control what was represented to the regulator; offering and marketing documents conform to both. But say when the fix should run the other way — sometimes the LPA has the typo — and mark that call for counsel.
8. **Sort conflicts by origin where the prior version allows:** introduced by this revision (fix before the document is used) versus pre-existing (fix on a managed timeline). This sorting is what turns the report into a work plan instead of an indictment.
9. **Write the CCO summary:** what must change before the revised document goes into use, what goes on the remediation list, which calls need counsel, and which pairs remain unchecked.

## Output format

A skeleton to adapt to the document set — the side-by-side quotation with full citations is the part that must survive any adaptation.

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# Fund Document Consistency Report — [firm / fund]
Trigger: [revised document, version/date] — changes to [ ]
Set reviewed: [documents with versions] | Pairs checked: [N] | Pairs unchecked: [ ]
Conflicts: [N] (direct: [N] / material: [N] / drift: [N]) | New vs. pre-existing: [N]/[N]

## What must change before the revised document is used
[The direct contradictions and material inconsistencies, one line each.]

## Conflicts
### [#] — [topic] — [severity]
| [Document A], p.[ ], §[ ] | [Document B], p.[ ], §[ ] |
|---|---|
| "[exact passage]" | "[exact passage]" |
**Why this conflicts:** [one or two sentences]
**Origin:** [introduced by this revision / pre-existing / undated]
**Recommended conforming edit:** [which document changes, to what]
**Governing view:** [which document should control, and why — counsel to confirm]

## Standing-topics sweep
| Topic | Documents stating it | Consistent? | Notes |
|---|---|---|---|
[Fees/offsets, capacity, strategy limits, key person, expenses, redemption,
valuation, conflicts — swept even where unchanged.]

## Unchecked pairs and gaps
[Pairs not checkable from the provided set; topics a missing document would
normally speak to.]

## Summary for the CCO
[Blockers, remediation list with suggested sequence, calls routed to counsel.]
```

## Where fund documents drift — and which conflicts are exam findings

The topics where the set comes apart, and how to read severity:

- **Fees and offsets** — the highest-yield sweep. Breakpoints rounded in the deck, offset percentages that moved in the LPA amendment but not the ADV brochure, fee bases described as committed capital in one document and invested capital in another. Almost never cosmetic: a fee inconsistency between ADV and offering documents is a classic deficiency, and between LPA and PPM it is an investor-terms problem.
- **Expense allocation** — the current enforcement sweet spot. What the fund bears versus the manager, especially consultants, travel, broken-deal costs, and anything the ADV describes more narrowly than the LPA permits. Treat any expense-language divergence as material until shown otherwise.
- **Capacity and fund size** — the deck's "capacity-constrained at $X" against the LPA's absence of any cap, or a hard cap amended away while the DDQ still cites it. Exam-relevant when capacity was used as a selling point.
- **Strategy and concentration limits** — the PPM's "up to 15% in a single position" against the DDQ's "typically 10%, maximum 12." Investors diligenced the tighter number; the governing document permits the looser one. Material almost by definition, because limits are what LPs actually rely on.
- **Key person** — the provision's named individuals versus the team the deck currently markets; departures that updated the website but not the DDQ. A stale key-person answer in diligence materials is an ODD credibility hit and, where the LPA provision no longer matches reality, a governance problem.
- **Redemption and withdrawal terms** — gates, notice periods, and lock-ups summarized generously in marketing against the governing document's actual mechanics. For open-ended vehicles this is the pair examiners read first.
- **Wording drift proper** — strategy descriptions that evolved narratively in the deck while the PPM stayed put. Usually cosmetic today; it becomes tomorrow's material inconsistency when the next edit builds on the drifted language. Worth logging precisely because it's cheap to fix now.

The severity heuristic: anything touching what investors pay, what they can rely on (limits, liquidity, key people), or what was represented to a regulator is presumptively material; language-only divergence with identical substance is drift — but say which and why, every time.

## Guardrails

- **Quote exactly, cite precisely.** Every conflict shows both passages verbatim with document, page, and section. No paraphrased conflicts, no approximate citations, and never a quoted passage that does not appear in the provided text — a fabricated or misquoted citation in a compliance report is a defect worse than any drift it reports.
- **Assists the compliance officer's judgment; never replaces it.** The skill surfaces conflicts, rates them, and recommends edits; the CCO and counsel decide what is material, which document governs, and what changes. Severity ratings and governing views are analysis, not determinations.
- **Never fabricates or backfills a review record.** No asserting a pair was checked when its document wasn't provided, no "consistent" verdicts on unchecked topics, no reconstructing what a prior version presumably said. Unchecked is reported as unchecked — a consistency report that overstates its own coverage is itself an inconsistent document.
- **Never rewrites the documents.** Recommended conforming edits are proposals for counsel's drafting; governing agreements and regulatory filings change only through their own amendment processes.
- **Absence of a conflict is not a clean bill.** The report's scope is the provided set on the swept topics; it says so, and lists what a fuller set would add.
- **Side letters qualify everything.** Where side letters were not provided, any "all investors are treated identically"-type statement is flagged as unverifiable against the actual deal set, not confirmed.
- **Not legal advice.** Which document governs, whether an inconsistency creates liability or a disclosure obligation, and how to amend are questions for counsel. This skill finds and organizes the conflicts those questions are about.
- **Confidentiality:** PPMs, LPAs, DDQs, and internal decks are confidential offering and governing materials. Assume a firm-approved AI environment, and reproduce passages only to the extent the side-by-side comparison requires.

## Example prompts

> "Attached: revised PPM (redline included), current LPA, ADV Parts 1 and 2A, our March DDQ, the current deck, and the website disclosure pages. The revision changed the management fee breakpoints and the capacity language. Full cross-check — everything affected by the changes plus the standing sweep, severity-rated, with what has to change before we can use the new PPM."

> "No revision — I just don't trust the set. Here are the deck, the DDQ, and ADV Part 2A. Sweep fees, strategy limits, key person, and liquidity terms across all three and show me every divergence side by side, even the cosmetic ones."

> "Counsel amended the LPA's expense allocation section last quarter — prior and current LPA attached, plus the ADV brochure and PPM. Which inconsistencies did the amendment introduce versus which were already there, and what's the remediation order?"

## Works well with

Run **marketing-compliance-prescreen** on the deck and website pages for Marketing Rule issues — this skill checks them against the governing set, which is a different question. **side-letter-term-extractor** supplies the side-letter terms this check needs before it can trust any uniform-treatment language, and a clean consistency report is one of the strongest artifacts **regulatory-exam-binder** can put in front of an examiner.
