---
name: quarterly-letter-synthesizer
description: >-
  Synthesize a stack of manager quarterly letters into a single cross-manager
  memo for allocators, fund-of-funds analysts, OCIOs, and family offices.
  Trigger on phrases like "synthesize these letters," "what are my managers
  saying this quarter," "summarize the quarterly letters," "cross-manager
  themes," "compare these investor letters," "read these letters and tell me
  what stands out," or when the user uploads multiple manager letters (PDFs
  or text) and wants themes, divergences, positioning shifts, or
  contradictions surfaced. Do NOT use for a single manager's quarterly
  check-in — use the manager-monitoring-note skill. Do NOT use for a first
  look at a new manager — use the hedge-fund-diligence skill. Do NOT use for
  drafting your own LP letter — use the lp-update-generator skill.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Quarterly Letter Synthesizer

Read a stack of manager quarterly letters and produce one cross-manager synthesis memo: what everyone agrees on, where they disagree, who changed their positioning, what's new, and who is contradicting their own prior letters. The reader is an allocator who has 20 letters in their inbox and one hour.

## Why this skill exists

Every quarter, allocators receive a pile of letters and most get skimmed at best. The real signal isn't in any single letter — it's *across* them: three managers independently building the same trade, one manager quietly reversing what they argued six months ago, a crowded theme nobody flags as crowded. Reading for that signal manually takes a full day. This skill compresses it into a memo and preserves the receipts (quotes and page references) so every claim can be checked against the source.

## Inputs

**Required:**
- Two or more manager letters (PDFs, pasted text, or files in a folder). One letter is not a synthesis — if only one is provided, suggest the manager-monitoring-note skill instead.

**Optional (each one materially improves the output):**
- Prior-quarter letters from the same managers — enables the "shift vs. prior letter" and "contradictions" sections
- The user's portfolio context (which managers they're invested in, sizing)
- Specific questions ("what is everyone saying about rates?")
- Manager strategy labels, if not obvious from the letters

**Missing-input behavior:** If letters lack dates or manager names, ask once for a quick mapping. Otherwise proceed — label any assumption explicitly (e.g., "Assumed Letter 3 is Q1 2026 based on references to March data"). Never guess a manager's strategy silently; mark it "strategy inferred from letter content."

## How it works

1. **Inventory the stack.** List every letter: manager, fund, period covered, length, whether a prior letter is available. Flag any letter that is marketing material rather than a true quarterly letter.
2. **Extract per letter, before comparing.** For each: macro/market views, key positioning statements, new positions or themes mentioned, exited or trimmed positions, performance commentary (only as stated — never compute or infer returns), notable tone (defensive, aggressive, apologetic), and anything unusual (personnel notes, terms changes, AUM comments).
3. **Build the theme map.** Cluster views across managers: where do 2+ managers converge? Note whether convergence is independent reasoning or everyone citing the same data point.
4. **Find the divergences.** Where do managers take opposite sides of the same question? These are the most valuable findings — quote both sides.
5. **Diff against prior letters (if provided).** For each manager: what changed in positioning, tone, or argument? Flag explicit reversals and *silent* reversals (a previously emphasized theme that simply disappeared).
6. **Flag contradictions.** A manager saying something inconsistent with their own prior letter, or with their stated strategy, gets quoted side by side with both dates.
7. **Write the memo** using the output format below, with every claim attributed to a specific manager and letter.

## Output format

```
# Quarterly Letter Synthesis — [Period]
Letters reviewed: [N] | Managers: [list] | Prior letters available: [Y/N per manager]

## 1. One-paragraph read
[The 3–4 sentences you'd say to the CIO in the hallway.]

## 2. Shared themes (convergence)
- **[Theme]** — held by [Manager A, B, C]. [1–2 sentences each on how they express it.]
  > "[Short supporting quote]" — [Manager], [period letter], p.[X]
- Crowding note: [is this theme consensus across the stack?]

## 3. Divergent views
- **[Question]**: [Manager A] argues [X]; [Manager B] argues the opposite.
  > A: "[quote]"  |  B: "[quote]"

## 4. Positioning shifts vs. prior letters
| Manager | Then ([prior period]) | Now ([current period]) | Shift |
|---|---|---|---|

## 5. Notable new / exited positions and themes
[Per manager, only as explicitly disclosed in the letter.]

## 6. Contradictions and silent reversals
- **[Manager]**: said "[quote]" ([prior date]) vs. "[quote]" ([current date]). [Why it matters; possible benign explanation.]

## 7. Tone and red-flag watch
[Defensiveness, blame-shifting, benchmark switching, AUM/personnel mentions.]

## 8. Questions for manager calls
[3–7 specific questions, each tied to a finding above.]

## Not covered in these letters
[Topics the user might expect that no manager addressed.]
```

Adjust length to the stack: 5 letters → ~2 pages; 20 letters → 4–5 pages with the table doing more work.

## Guardrails

- **Quote, don't paraphrase, for anything contentious.** Every contradiction, reversal, or red flag must carry a verbatim quote with manager name and letter date. If you can't find the quote, drop the claim.
- **Never invent or compute performance figures.** Report returns only as stated in a letter, with the as-of date. Do not annualize, net, or compare returns the managers didn't compare themselves.
- **Separate fact from inference.** "Manager A exited the position" (stated) vs. "Manager A appears to have reduced conviction" (inference — label it as such).
- **No investment advice.** The memo informs manager conversations; it does not recommend allocations, redemptions, or trades.
- **Confidentiality.** Manager letters are typically confidential LP communications. Remind the user not to circulate the synthesis outside the team that is entitled to see the underlying letters.
- **A missing theme is data, not license to speculate.** If no manager discussed something, say so — don't fill the gap with your own market view.

## Quality checks

Before delivering, verify:
- [ ] Every manager in the stack appears at least once in the memo
- [ ] Every quote has a manager name and letter period attached
- [ ] No performance number appears that isn't verbatim from a letter
- [ ] Each contradiction shows both quotes and both dates
- [ ] Inferences are labeled as inferences
- [ ] The manager-call questions map back to specific findings

## Example prompt

> "Here are Q1 letters from our six hedge fund managers, plus their Q4 letters. Synthesize: what themes are shared, where they disagree, who shifted positioning, and whether anyone is contradicting what they told us last quarter. We're especially interested in what they're saying about credit."
