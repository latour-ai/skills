---
name: quarterly-letter-synthesizer
description: >-
  Synthesize a stack of manager quarterly letters into a single cross-manager
  memo for allocators, fund-of-funds analysts, OCIOs, and family offices.
  Letters can be attached, or pulled from the folder or mailbox where they
  arrive (SharePoint / OneDrive, Google Drive, Box, Dropbox, a local folder,
  Outlook or Gmail); that location, the manager roster and any standing
  questions are set once in a short first-run setup, which also lets the
  skill find last quarter's letters for the comparison. Trigger on phrases
  like "synthesize these letters," "what are my managers
  saying this quarter," "summarize the quarterly letters," "cross-manager
  themes," "compare these investor letters," "read these letters and tell me
  what stands out," "set up quarterly-letter-synthesizer," "change my
  quarterly-letter-synthesizer settings," or when the user uploads multiple manager letters (PDFs
  or text) and wants themes, divergences, positioning shifts, or
  contradictions surfaced. Do NOT use for a single manager's quarterly
  check-in. Do NOT use for a first look at a new manager — use the hedge-fund-diligence skill. Do NOT use for
  drafting your own LP letter — use the lp-update-generator skill.
license: MIT
metadata:
  author: latourai
  version: '2.0'
---

# Quarterly Letter Synthesizer

Read a stack of manager quarterly letters and produce one cross-manager synthesis memo: what everyone agrees on, where they disagree, who changed their positioning, what's new, and who is contradicting their own prior letters. The reader is an allocator who has 20 letters in their inbox and one hour.

## Why this skill exists

Every quarter, allocators receive a pile of letters and most get skimmed at best. The real signal isn't in any single letter — it's *across* them: three managers independently building the same trade, one manager quietly reversing what they argued six months ago, a crowded theme nobody flags as crowded. Reading for that signal manually takes a full day. This skill compresses it into a memo and preserves the receipts (quotes and page references) so every claim can be checked against the source.

## Inputs

**Required:**
- Two or more manager letters: attached PDFs, pasted text, or the letters for the period in the folder or mailbox saved in setup. One letter is not a synthesis — if only one is provided, say so and offer a single-manager read instead.

**Optional (each one materially improves the output):**
- Prior-quarter letters from the same managers — enables the "shift vs. prior letter" and "contradictions" sections
- The user's portfolio context (which managers they're invested in, sizing)
- Specific questions ("what is everyone saying about rates?")
- Manager strategy labels, if not obvious from the letters

**Set once in setup (step 0):** where letters arrive and are archived, the manager roster (strategy labels and sizing), standing questions, and where the memo is saved.

**Missing-input behavior:** If the saved folder or mailbox isn't connected or can't be read, say which system was unavailable and ask for the letters to be attached. If letters lack dates or manager names, ask once for a quick mapping. Otherwise proceed — label any assumption explicitly (e.g., "Assumed Letter 3 is Q1 2026 based on references to March data"). Never guess a manager's strategy silently; mark it "strategy inferred from letter content."

## How it works

### 0. First-run setup (once, then only when asked)

Run setup the first time the skill is used, or when the user says "set up quarterly-letter-synthesizer" or "change my quarterly-letter-synthesizer settings". Look for a saved settings file first (`quarterly-letter-synthesizer-settings.md`, in the project's files or the letters folder). If one exists, read it and skip setup.

Setup is one short round of questions, each with a default the user can accept:

1. **Detect before asking.** Check which file storage and mail system are connected, and pre-fill what detection settles.
2. **Ask, in one message:**
   - **Where letters live:** a folder in connected storage, a mail folder or label in Outlook or Gmail where managers' letters arrive, or "I'll attach them each time" (default). If prior quarters are kept in the same place, the skill finds them for the comparison without being asked.
   - **Manager roster (optional):** the managers held, each with a strategy label and rough sizing. Default: none; strategies are inferred from the letters and marked as inferred.
   - **Standing questions (optional):** themes to check every quarter, for example rates, credit, or crowding in a named sector.
   - **Where the memo is saved,** or "just send me the file" (default).
3. **Save the settings** to `quarterly-letter-synthesizer-settings.md` in plain language the user can edit. If nothing persistent can be written, show the settings as a short block and tell the user to paste it into their project instructions.
4. **Continue straight into the synthesis** if the user asked for one.

On later runs, read the settings and don't re-ask. Setup never blocks a first run: if the user says "skip setup", work from what is attached, use the defaults, and say which were used.

### Steps for each stack

1. **Inventory the stack.** List every letter: manager, fund, period covered, length, whether a prior letter is available. Flag any letter that is marketing material rather than a true quarterly letter.
2. **Extract per letter, before comparing.** For each: macro/market views, key positioning statements, new positions or themes mentioned, exited or trimmed positions, performance commentary (only as stated — never compute or infer returns), notable tone (defensive, aggressive, apologetic), and anything unusual (personnel notes, terms changes, AUM comments).
3. **Build the theme map.** Cluster views across managers: where do 2+ managers converge? Note whether convergence is independent reasoning or everyone citing the same data point.
4. **Find the divergences.** Where do managers take opposite sides of the same question? These are the most valuable findings — quote both sides.
5. **Diff against prior letters (if provided).** For each manager: what changed in positioning, tone, or argument? Flag explicit reversals and *silent* reversals (a previously emphasized theme that simply disappeared).
6. **Flag contradictions.** A manager saying something inconsistent with their own prior letter, or with their stated strategy, gets quoted side by side with both dates.
7. **Write the memo** using the output format below, with every claim attributed to a specific manager and letter. Every manager in the stack appears at least once in the memo.

## Output format

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

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
- **Read-only on the mailbox and the archive.** The skill reads letters where they live; it does not move, label, forward or reply to anything, and it saves the memo only to the location chosen in setup.
- **A missing theme is data, not license to speculate.** If no manager discussed something, say so — don't fill the gap with your own market view.

## Example prompts

> "Set up quarterly-letter-synthesizer. Letters land in the 'Manager letters' folder in my Outlook and we file them by quarter under 'Manager reporting' in SharePoint. Every quarter I want to know what they're saying about credit and about leverage. Save the memo next to the letters."

> "Here are Q1 letters from our six hedge fund managers, plus their Q4 letters. Synthesize: what themes are shared, where they disagree, who shifted positioning, and whether anyone is contradicting what they told us last quarter. We're especially interested in what they're saying about credit."
