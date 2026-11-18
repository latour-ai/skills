---
name: sop-documenter
description: >-
  Turn a narrated walkthrough (a screen-recording transcript, a talked-through
  process, or rough notes from watching someone do the job) into a formal SOP
  a new hire could follow: purpose, scope, frequency, and owner; numbered
  steps stating the system, the action, and the expected result, with
  screenshot capture points noted; every control point, approval, and
  four-eyes check marked; exception handling for when the standard path
  fails; tribal-knowledge callouts; and a closing list of ambiguities to
  resolve with the process owner before the SOP is finalized. Also maintains
  existing SOPs as processes change and flags ones untouched for over a year.
  The walkthrough can be pasted, attached, or pulled from a connected meeting
  or recording tool or file storage; the firm's SOP template, systems list
  and SOP library location are saved once in a short first-run setup. For
  operations, finance, and compliance teams at investment firms and other
  companies, and anyone whose critical process lives in two people's heads.
  Trigger on "write an SOP", "document this process", "turn this walkthrough
  into procedures", "we need this for the ops manual", "ODD asked for our
  procedures", "what happens if [person] is out", "set up sop-documenter",
  "change my sop-documenter settings", or when a user pastes a narrated
  process transcript and asks for documentation. Do NOT use for assembling
  regulatory exam materials; use the regulatory-exam-binder skill. Do NOT use
  for mapping workflows to find automation opportunities; use the
  ai-workflow-audit skill. Do NOT use for general meeting notes; use the
  call-transcript-followup skill. Never invents steps or controls the
  walkthrough did not describe.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# SOP Documenter

Your critical processes live in the heads of the two people who run them, and "write real SOPs" has been on the ops list for three years because writing procedure documents is miserable work that never beats the live fire. Talking through the process once while doing it, though, is easy — and this turns that one narrated walkthrough into a formal SOP: numbered steps a new hire could follow, every control point marked, exception handling captured, and the gaps flagged as questions instead of papered over. When someone is out sick during a NAV close, the SOP is the difference between a delay and a non-event.

## Why this skill exists

The gap between "documented process" and "process someone can actually run" is where operational risk hides. Most firms technically have procedures — a paragraph of prose written for an ODD questionnaire, describing the process at an altitude from which nothing can go wrong and nothing can be executed. What they don't have is the real sequence: which report, from which system, reconciled against what, and who signs off before the wire goes out. That version exists only as muscle memory, and muscle memory doesn't take questions when its owner is on a plane.

Writing it down fails for a predictable reason: the person who knows the process can't see it anymore. Experts narrate the happy path and skip the judgment calls they no longer notice making — which exception is routine, which number "looks wrong," whom you call when the feed is late. A blank page asks the expert to do the hardest kind of recall. A walkthrough transcript flips the problem: the knowledge is already externalized, in the wrong shape, and reshaping it is exactly the work an expert's time shouldn't go to.

The transcript is also where the gold is. The asides — "oh, and it always fails on the first Monday of the month," "if it's off by more than a rounding error, call the fund accountant first" — are the tribal knowledge that never survives into formal documentation, because formal documentation is written from memory and asides don't get remembered. Captured and labeled, they are the most valuable lines in the SOP. And the honest byproduct — a list of what the walkthrough *didn't* cover — is worth as much as the document, because an SOP that marks its gaps is safer than one that quietly smooths over them.

## Inputs

**Required:**
- A narrated walkthrough of the process: a screen-recording transcript, a transcribed talk-through, or detailed notes from watching someone perform it end to end. It can be pasted, attached, or pulled from a connected meeting or recording tool (Zoom, Teams, Loom, Fireflies, Granola, Otter) or from file storage if the user names where it is. If that system isn't connected, ask for the transcript to be pasted or attached.

**Optional but high-value:**
- Systems used by this process that are not on the saved systems list
- Who owns the process and how often it runs, if not stated in the walkthrough
- The prior version of the SOP, if one exists — enables a what-changed comparison and preserves controls the narrator forgot to mention, flagged for confirmation
- Screenshots or screen descriptions keyed to moments in the narration
- The compliance or BCP requirement driving the request — it changes how control points are emphasized

**Set once in setup (step 0):** the firm's SOP template, the systems list with names as the firm uses them, where the SOP library or ops manual lives, the review cycle, and where drafts are saved.

**Missing-input behavior:** A walkthrough alone is enough to produce a draft SOP. Without a systems list, use system names as narrated and flag each as unverified. Without an owner or frequency, leave labeled placeholders, because a guessed owner is worse than a blank one. If the prior SOP mentions a control the walkthrough skipped, carry it in flagged as "in prior SOP, not observed in walkthrough — confirm," never silently dropped and never silently trusted. Where the narrator's sequence is ambiguous or contradictory, the ambiguity goes in the open-questions list; the skill never resolves it by inventing an order, and it never fabricates exception procedures the narrator didn't describe.

## How it works

### 0. First-run setup (once, then only when asked)

Run setup the first time the skill is used, or when the user says "set up sop-documenter" or "change my sop-documenter settings". Look for a saved settings file first (`sop-documenter-settings.md`, in the project's files or the SOP library folder). If one exists, read it and skip setup.

Setup is one short round of questions, each with a default the user can accept; "none" is a valid answer to any of them:

1. **Detect before asking.** Check which file storage, wiki and meeting tools are connected. If the user points to an existing SOP or the ops manual, read it and pre-fill the template and the systems list from it for confirmation.
2. **Ask, in one message:**
   - **SOP template:** the built-in format below (default), or the firm's own template, which then sets the section order and headings.
   - **Systems list:** the firm's systems, named the way staff see them on screen. Default: none, and system names are used as narrated and flagged as unverified.
   - **SOP library:** where finished SOPs live, for example a folder in SharePoint / OneDrive, Google Drive or Box, or a space in Confluence or Notion. This is what the staleness sweep reads. Default: none, and the sweep covers only what the user attaches.
   - **Review cycle:** how long before an SOP is due for review. Default: 12 months.
   - **Where drafts are saved and in what format:** a drafts folder, or "just send it to me" (default); Word or Markdown.
3. **Save the settings** to `sop-documenter-settings.md` in plain language the user can edit. If nothing persistent can be written, show the settings as a short block and tell the user to paste it into their project instructions.
4. **Continue straight into the SOP** if the user gave a walkthrough with the setup request.

On every later run: read the settings and never re-ask. Setup never blocks a first run: if the user says "skip setup", draft in the built-in format and say what was assumed.

### Steps for each walkthrough

1. **Treat the walkthrough as evidence, not as the SOP.** A narration is ordered by what the narrator remembered when, complete with backtracking, tangents, and "oh wait, before that." The transcript's sequence and the process's sequence are different things, and untangling them is the first job.
2. **Establish the header facts:** purpose in two sentences, scope (what this SOP covers and pointedly does not), frequency, owner, and the systems touched. If the walkthrough never says *why* the process exists, flag it — a new hire who doesn't know what the process protects can't judge when something matters.
3. **Reconstruct the true step sequence.** Resolve the backtracks, pull the asides out of the flow, and separate the happy path from everything else. Where two readings of the order are possible, pick neither — log it as an open question.
4. **Write numbered steps at new-hire altitude.** Each step states the system, the action, and the expected result — what the screen should show when the step worked. "Reconcile the cash balances" is a topic; "In [system], run the [report], compare the closing balance to the custodian file line by line; the variance column should be zero" is a step. Note a screenshot capture point at every state-changing screen and every UI moment the narration had to describe rather than name.
5. **Mark every decision point.** Wherever the path branches, state the criterion in operational terms — the threshold, the field, the condition. A judgment call hidden inside a step ("check that it looks reasonable") is where the process breaks in unfamiliar hands; if the narrator's criterion was implicit, flag it as a question rather than inventing a threshold.
6. **Extract the control points** — every approval, four-eyes check, reconciliation, maker-checker split, and sign-off — and mark them visibly in place plus in a consolidated table. These are the lines an ODD reviewer and an auditor read first, and the lines most dangerous to lose in prose.
7. **Capture exception handling.** Everything the narrator said about failure — the feed that arrives late, the break that won't clear, the system timeout — becomes a what-if entry: symptom, response, escalation trigger. Where the walkthrough is silent on an obvious failure mode, write the gap as a named question for the process owner. An invented recovery procedure is worse than a marked gap.
8. **Label the tribal knowledge.** The asides, timing quirks, informal workarounds, and who-to-call facts get their own callouts, attached to the steps they concern. This is the content that exists nowhere else; losing it back into prose defeats the exercise.
9. **Attach maintenance metadata:** version, effective date, owner, and a review-by date set from the review cycle in setup. If an SOP library is saved in setup or an inventory was provided, sweep it and flag anything past its review cycle, including the prior version of this SOP, for review.
10. **Close with the open-questions list:** every ambiguity, unverified system name, implicit threshold, and unobserved failure path, phrased as specific questions the process owner can answer in one sitting. The SOP is a draft until this list is resolved, and it says so on its face.

## Output format

The skeleton is a default; when setup holds the firm's template, follow that instead.

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# SOP — [process name]
Owner: [ ] | Frequency: [ ] | Systems: [ ]
Version: [draft 0.1] | Effective: [ ] | Review by: [ ]
Status: DRAFT — open questions below must be resolved before finalization

## Purpose and scope
[Two sentences: what this process does and what it protects.]
In scope: [ ] | Out of scope: [ ]

## Procedure
1. [System] — [action]. Expected result: [ ]. 📷 [screenshot point]
2. [System] — [action]. Expected result: [ ]
   ⚠ Decision point: if [criterion], go to step [n]; otherwise continue.
3. ...
   ✓ CONTROL: [approval / four-eyes / reconciliation — who performs, who verifies]
   ℹ Tribal knowledge: [the aside, verbatim-close, attributed to the walkthrough]

## Control points (consolidated)
| Step | Control | Type | Performed by | Verified by |
|---|---|---|---|---|

## Exception handling
| Symptom | Response | Escalate when | Escalate to |
|---|---|---|---|
[Unobserved failure modes appear as OPEN QUESTION rows, not invented rows.]

## Escalation contacts
| Situation | Contact | Backup |
|---|---|---|
[Placeholder — fill from firm directory.]

## Open questions for the process owner
1. [specific, answerable question]
2. ...
```

## The new-hire test — SOP versus documentation theater

The single test for every line: could a competent new hire, alone on day three, execute from this — and know when to stop and call someone? Documentation theater fails that test in recognizable ways:

- **Prose instead of steps.** A paragraph "describing our reconciliation process" satisfies a questionnaire and executes nothing. Real SOPs are numbered, one action per step, with an expected result to check against.
- **Hidden decision points.** "Review for reasonableness," "as appropriate," "if necessary" — each one is a judgment call with an unstated criterion, which means the process silently requires the one person who already knows it.
- **No failure modes.** A happy-path-only SOP works right up until the first exception, which is precisely the moment the regular operator's absence matters. The exceptions section is why the document exists.
- **Tribal knowledge left tribal.** If the timing quirk and the who-to-call live only in someone's head, the SOP documents a process nobody actually runs.
- **No expected results.** Steps without "what you should see" give the operator no way to know a step failed until three steps later.
- **No owner, no review date.** An SOP nobody owns drifts from the real process within two quarters; staleness is the default state, and only a review-by date fights it.
- **Gaps papered over.** Theater fills unknowns with plausible text to look complete. A real SOP marks them — a reviewer can close a marked gap in minutes, while an invented step can misdirect someone during an actual incident.

## Guardrails

- **Never invent a step, threshold, or recovery procedure.** Everything in the procedure traces to the walkthrough, the prior SOP (flagged as such), or an explicit user input. Gaps become open questions — this is the rule the skill exists to enforce, and it holds even when the missing step seems obvious.
- **Never drop a control.** Every approval, check, and sign-off the narrator mentioned appears in the output, marked. If a control in the prior SOP went unobserved in the walkthrough, it is carried in flagged for confirmation — the alternative is an SOP that documents the erosion of a control as if it were the design.
- **Ambiguity is surfaced, not resolved by fiat.** Contradictions in the narration, uncertain orderings, and implicit criteria go to the open-questions list.
- **The draft says it's a draft.** Until the process owner resolves the open questions, the SOP is marked DRAFT on its face, so it cannot quietly enter the ops manual half-verified.
- **This documents the process; it does not bless it.** Writing down a workflow with a missing four-eyes check does not make the workflow adequate. Note visible control weaknesses as observations for the owner, and leave the compliance judgment to compliance — this is not a substitute for the firm's compliance manual or its counsel.
- **Drafts are saved beside the library, never over it.** The skill saves a new draft file where setup says and does not edit, replace, move or delete an existing SOP; putting a finished SOP into the ops manual is the process owner's step. If the save location isn't reachable, return the draft in the conversation and say which system was unavailable.
- **Confidentiality:** walkthroughs of operational processes expose account structures, system names, counterparties, and control design — the exact map an attacker or a fraudster wants. Assume a firm-approved AI environment and treat the output as internal-only.

## Example prompts

> "Here's the transcript of [person] talking through our daily cash reconciliation while doing it: [paste]. Systems are [list]. Turn it into a formal SOP — steps, controls, exceptions — and end with the questions I should take back to her before we finalize."

> "Attached: our old wire-approval SOP from 2023 and a fresh walkthrough transcript from last week. Rebuild the SOP from the walkthrough, tell me what changed, and flag anything the old version had — especially approvals — that nobody mentioned this time."

> "Set up sop-documenter. Use our SOP template (attached), our systems are [list], finished SOPs live in the 'Ops manual' folder on SharePoint, review cycle is 12 months, and save drafts as Word files in 'Ops manual / Drafts'."

> "ODD visit in three weeks and our NAV-close 'procedure' is one paragraph. Here's a recording transcript of the close from Tuesday: [paste]. Draft the real SOP, mark every control point clearly, and be explicit about what the walkthrough didn't cover so I know what's still undocumented."

## Works well with

Feed finished SOPs into **regulatory-exam-binder** when the "show us your procedures" request arrives; the binder is only as good as the SOPs behind it. Run **ai-workflow-audit** across the documented processes to find which steps are automation candidates. When a documented process turns out to be a good candidate for a reusable AI skill, **investment-skill-creator** helps shape the idea.
