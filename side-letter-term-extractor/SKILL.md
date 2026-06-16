---
name: side-letter-term-extractor
description: Summarize a hedge fund side letter and extract its key commercial, operational, and legal terms from the GP/manager's perspective, producing a Word (.docx) review memo. Use whenever an IR, fundraising, COO, legal, or compliance professional at a hedge fund manager uploads, pastes, or references a side letter (or folder of side letters) and wants it summarized, reviewed, term-extracted, risk-flagged, or checked for MFN/precedent/operational issues. Trigger on "review this side letter", "summarize this side letter", "what did we promise this investor", "what are our obligations under this side letter", "does this trigger MFN", "flag the risky terms", "side letter review", or any request to understand what a side letter commits the firm to. Works on a single letter (default) or across funds, vintages, or vehicles. Manager-side screen — does NOT give legal advice or make legal conclusions. For inbound NDA review use pe-nda-review; for full contract review against a playbook use legal:review-contract.
---

# Side Letter Term Extractor

Read a hedge fund side letter the way an experienced IR or fundraising professional reads one when they need to know, quickly and precisely, **what the firm actually promised an investor and what obligations that creates**. A side letter is a bilateral agreement that grants a specific LP terms beyond the fund's standard documents — fee breaks, better liquidity, MFN rights, capacity guarantees, custom reporting. Each of those is a commercial concession, an operational obligation the firm now has to honor, and a potential precedent or MFN trigger that can ripple across the investor base.

The reader is on the **manager / GP side**, not the LP side. The job is to translate the legal language into a plain-English picture of the firm's commitments, surface the terms that legal, compliance, the COO, or IR need to track, and flag where a term may collide with the fund's governing documents or set a precedent for the next negotiation. The default deliverable is a **Word (.docx) review memo**.

This skill **extracts and flags**; it does not give legal advice, draw legal conclusions, or rewrite clauses. It is the first-pass analytical screen that tells the team where to focus.

## What this skill is careful about

These guardrails exist because the cost of getting a side letter review wrong is real — a missed obligation becomes an operational failure, an overstated risk wastes legal time, and an invented term is worse than no answer at all. Hold to them:

- **No legal advice and no legal conclusions.** Describe what a term says and why it may matter; do not opine on enforceability, validity, or what the firm "should" agree to legally. Where a judgment call belongs to counsel, route it there.
- **Quote the source language for every extracted term.** The value of the memo is the translation, but the reader must be able to check it against the document. A term without a supporting quote is unverifiable and must not appear.
- **Never infer missing terms.** Analyze only the language in the document. If a category isn't addressed, the honest and correct answer is "Not found" — not a guess about what's "probably" there.
- **Preserve defined terms exactly as written.** If the letter defines "Eligible Investor" or "Quarterly Report," use that capitalized term verbatim; do not paraphrase defined terms into something that reads similar but isn't.
- **Flag conflicts as conflicts, not verdicts.** If a provision may collide with fund governing documents, say: *"Potential conflict item. Cannot fully assess without reviewing the LPA, PPM, subscription documents and related governing documents."* That's the honest ceiling of what can be assessed from the side letter alone.
- **Name ambiguity and document status.** If a clause is ambiguous, say so. If the document is a draft, state that the analysis is based on draft language. If it's unsigned or execution status is unclear, flag that — an unexecuted promise carries different weight.
- **Don't overstate.** Use careful, calibrated language: "may create," "could require," "potentially," "cannot fully assess without." Precision builds trust with a legal/compliance reader; inflation destroys it.

## Workflow

1. **Read the whole letter first.** It usually arrives as an uploaded PDF or .docx in `/mnt/user-data/uploads/`, or pasted inline. Read it in full before extracting anything — side letters lean heavily on defined terms and cross-references, so a clause means what its definitions make it mean. If a defined term is used but its definition lives in the LPA/PPM (not the letter), note that the definition is external.
2. **Establish the header facts.** Investor name, fund / vehicle name, date or effective date, and execution status (signed, draft, unsigned, unclear). These frame everything else and belong at the top of the memo.
3. **Walk the five term categories.** Go through `references/term-categories.md` and extract every term that falls under Economics, Liquidity, MFN, Capacity, and Transparency/Reporting. For each: capture what right or obligation it creates, the short source quote, and an initial risk read.
4. **Score risk** with the rubric below. Reserve High for terms that genuinely constrain the firm, create preferential treatment, may conflict with fund documents, or impose hard/recurring operational burden. Don't inflate — a memo where everything is High is as useless as one where nothing is.
5. **Build the obligation checklist.** Translate every term that requires the firm to *do* something (report, notify, seek consent, honor a deadline) into an actionable row with an owner, trigger, cadence/deadline, and status. This is what turns a legal review into an operational one.
6. **Run the MFN analysis** if any MFN language exists — it gets its own section because MFN is the term most likely to ripple across the whole investor base.
7. **Write the .docx memo** using the structure below.

## Risk rubric

Apply consistently. The point of three tiers is triage: High demands review before reliance, Medium needs an owner and tracking, Low is noted for awareness.

**🔴 High** — any of: preferential economics; preferential liquidity; broad or ambiguous MFN rights; possible conflict with the LPA, PPM, subscription documents, or other governing documents; portfolio-level transparency that may expose sensitive positions; a hard operational deadline; a recurring custom reporting obligation; a term likely to set precedent for future LPs; or a term that should get legal, compliance, or COO review before execution.

**🟡 Medium** — custom but operationally manageable; important for IR/COO/compliance to track; potentially precedent-setting but narrow; a reporting, notice, or consent right that needs a workflow owner; commercially meaningful but not obviously problematic.

**🟢 Low** — administrative, standard, narrow, easily operationalized, and unlikely to create material precedent, MFN, or conflict issues.

## Memo structure

Produce the .docx with these sections, in this order. The title carries the key identifiers so the file is self-describing when it lands in someone's inbox.

```
# Side Letter Review: [Investor / Fund / Date]

## 1. Executive Summary
Concise, plain-English, and written for a senior IR, COO, or legal reader who wants
the answer fast. Cover: investor name; fund / vehicle name; date or effective date;
execution status if known; the overall posture of the letter (light / standard /
aggressive in what it grants); the most important commercial terms; the highest-risk
provisions; and the most important operational obligations. If the document is a draft
or unsigned, say so here.

## 2. Key Terms Table
A real table:
| Category | Term | Extracted Right / Obligation | Risk | Source Language | Notes |
Every row carries a short, precise source quote — quote only the most relevant part of
a long clause, but never paraphrase a term without including its quote. Use "Not found"
where a category has nothing. Risk is Low / Medium / High.

## 3. Obligation Checklist
A real table:
| Owner | Obligation | Trigger | Deadline / Cadence | Risk | Source Language | Status |
Default owners: IR, COO, Legal, Compliance, Fund Admin, Investment Team. If ownership is
unclear, write "To assign." Status defaults to one of: Open, Needs legal review,
Needs operational owner, Not applicable.

## 4. MFN Analysis
If MFN language exists, a table:
| MFN Element | Extracted Term | Risk | Source Language | Notes |
Cover: whether MFN is granted; eligible-investor threshold; exclusions; election
process; notice requirements; timing; whether it reaches future rights; confidentiality
limits; and any carve-outs for strategic, seed, founder, regulatory, tax, or ERISA
investors. Note whether the MFN applies to existing side letters, future side letters,
or both. If absent, write exactly: "MFN: Not found."

## 5. Risk Flags
Grouped under High, Medium, Low. For each flag: a short description; why it matters; the
source language; and a suggested review owner. Use calibrated language ("may create…",
"could require…", "potentially…", "cannot fully assess without…"). For a possible
governing-document conflict, use the standard conflict sentence.

## 6. Missing / Not Found
A real table covering each core category:
| Category | Status | Notes |
Rows: Economics, Liquidity, MFN, Capacity, Transparency / Reporting. Status is
Found / Not found.

## 7. Review Questions for Human Team
A short list of pointed questions for legal, COO, compliance, or IR — e.g. whether a
liquidity right conflicts with the LPA/PPM, whether a reporting obligation needs a new
workflow, whether MFN language requires notice to other investors, whether an economic
term fits the firm's current side-letter playbook, whether a term should be excluded
from future MFN elections, or whether it creates precedent for similarly situated LPs.
```

End with a single operational line: *First-pass manager-side screen — route High-risk and potential-conflict items to legal/COO/compliance before relying on this analysis.* Don't pad with broader legal disclaimers.

## Quoting discipline

Keep quotes short and surgical — the operative phrase, not the whole clause. The reader has the document; the memo's value is the translation and the flagging, not transcription. But every extracted term needs its quote, because an extraction the reader can't verify against the source is worse than useless.

## When facts are missing

If the document doesn't give you something you'd want (no execution date, an externally defined term, an investor name redacted), don't stall and don't invent. State plainly what's missing, then proceed with the best extraction the available language supports. A memo that says "execution status unclear from the document provided" is doing its job; one that quietly assumes the letter is signed is not.

## Multiple side letters

The default and best-supported workflow is **one side letter at a time** — it produces the cleanest, most verifiable memo. If the user points at a folder or asks to compare letters across funds, vintages, or vehicles, still analyze each letter individually and faithfully first, then add a short comparison layer on top (e.g., which investors hold MFN, where economics diverge, which obligations recur). Never blend letters together in a way that loses which term came from which document — the source-attribution discipline matters even more across a set.

## Generating the .docx

This skill owns the analysis; the **docx skill owns the rendering**. Before writing the file, read `/mnt/skills/public/docx/SKILL.md` and follow it. Make the output genuinely scannable: a real heading hierarchy; real tables for sections 2, 3, 4, and 6 (not pipe-delimited text); and risk shown as a labeled tag ("HIGH" / "MEDIUM" / "LOW") plus the color/emoji so it survives if color is stripped. Save the finished file to `/mnt/user-data/outputs/` and present it.

## Reference

`references/term-categories.md` is the working map of what to look for in each of the five categories, with the specific kinds of terms that show up under each. Read it on every run — it's what keeps the extraction complete instead of catching only the obvious fee break.
