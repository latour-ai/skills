---
name: lp-update-generator
description: >-
  Draft a quarterly LP update letter from raw fund inputs: performance
  figures, portfolio company notes, cash flow activity and the GP's market
  view, in whatever form they arrive. The fund's name, house voice, usual
  sections, signature block and required disclaimer are recorded once in a
  short first-run setup, so each quarter starts from the same letter shape.
  For GPs, fund managers and IR teams at private equity, venture, private
  credit and hedge fund managers. Trigger on "draft my LP update,"
  "quarterly investor letter," "write our Q[X] update," "LP communication,"
  "investor update," "write to our LPs," "quarterly letter to investors,"
  "set up lp-update-generator," "change my lp-update-generator settings," or
  when the user provides fund performance data, portfolio updates or market
  commentary and asks to turn them into an investor communication. Do NOT
  use to turn attribution output into performance commentary; use the
  performance-attribution-narrator skill. Do NOT use to synthesize other
  managers' letters; use the quarterly-letter-synthesizer skill. Do NOT use
  for a weekly market note; use the weekly-market-recap-writer skill. Do NOT
  use for a marketing overview aimed at prospective LPs; use the
  fund-marketing-one-pager skill.
license: MIT
metadata:
  author: latourai
  version: '2.0'
---

# LP Update Generator

Draft a polished quarterly LP update letter from whatever raw inputs the user provides.

## Why This Skill Exists

Writing LP updates is one of the most time-consuming IR tasks at any fund. The inputs are usually scattered — performance data in one place, portfolio notes in another, a rough market take jotted somewhere else — and turning them into a clean, professional letter takes hours. This skill does that conversion fast.

The output is a working draft, not a finished letter. Every fund has its own voice, disclosure posture, and LP relationship nuances that the GP or IR team must apply before sending. Treat this as a strong first draft that needs a human review pass.

## What This Skill Does Not Do

- It does not pull live fund data or calculate performance figures. The user must provide those.
- It does not make up numbers. If data is missing, it flags the gap.
- It does not know your fund's legal or compliance obligations. A fund's legal counsel should review before any communication goes to LPs.
- It does not guarantee completeness. Every fund has different disclosure norms — what goes in this letter is the GP's call.

## Inputs

The user may provide any combination of the following. The skill works with whatever is available — more inputs produce a better draft, but the skill will always produce something useful.

**Common inputs:**
- Fund name and quarter being reported
- Fund-level performance (net IRR, TVPI, DPI, RVPI — or none of these)
- Portfolio company updates (news, milestones, challenges, exits)
- New investments made during the period
- Exits or realizations during the period
- Cash flow activity (capital calls, distributions)
- Market or macro commentary the GP wants to include
- Notes on what tone to strike
- Prior LP letters to match style and voice
- Any topics the GP specifically wants to address or avoid

Inputs can be attached, pasted, or pulled from connected file storage (SharePoint / OneDrive, Google Drive, Box, Dropbox, a local folder) if the user names where they live. If that storage isn't connected or can't be reached, say so and work from what is attached or pasted.

**Set once in setup (see First-run setup):** firm and fund name, where prior letters live, the voice to match, the sections and metrics the letter normally carries, the signature block, and any required disclaimer or review rule.

If key inputs are missing, do not stop. Produce the best draft possible and append a clearly labeled section at the end listing what information would improve it.

## First-run setup (once, then only when asked)

Run setup the first time the skill is used, or when the user says "set up lp-update-generator" or "change my lp-update-generator settings". Look first for a saved `lp-update-generator-settings.md` in the project's files or the skill's working folder. If one exists, read it and skip setup.

Setup is one short round of questions, each with a default the user can accept; "none" is a valid answer.

1. **Detect before asking.** Check whether file storage is connected, and pre-fill anything the request or an attached prior letter already settles (fund name, section order, signature block, disclaimer). Show what was pre-filled for confirmation.
2. **Ask, in one message:**
   - **Firm and fund:** the firm name and the fund or funds the letters cover.
   - **Prior letters:** the folder where past letters live, or "I'll attach one" (default). The most recent letter sets the voice and structure.
   - **Voice:** match the prior letters, or the default (professional, measured, confident without being promotional).
   - **Standing sections and metrics:** the sections every letter carries and the performance metrics the fund reports (for example net IRR, TVPI and DPI, or net monthly return). Default: the structure below, with sections omitted when there is nothing to report.
   - **Signature block:** who signs, with title and contact line.
   - **Required disclaimer and review rule:** the firm's standard legend for investor letters, and any rule such as "counsel reviews before distribution". Default: none.
3. **Save the settings** to `lp-update-generator-settings.md` in plain language the user can edit. If nothing persistent can be written, show the settings as a short block and tell the user to paste it into their project instructions.
4. **Continue straight into the letter** if the user gave fund inputs with the setup request.

On later runs, read the settings and don't re-ask. Setup never blocks a first run: if the user says "skip setup", draft with the defaults and placeholders. Setup records how the letter is shaped, never what happened in the quarter; figures and portfolio news come only from the inputs supplied for that run.

## Core Principles

**Only use what the user provides.** Do not invent performance figures, company names, valuations, or market commentary. If the user says "we had a strong quarter" but provides no numbers, write around that directionally without fabricating specifics.

**Preserve the GP's voice.** If prior letters are provided, match their tone and structure. If not, default to a professional, measured tone — confident but not promotional.

**Be honest about gaps.** Placeholder language is better than invented language. Where data is missing, use clearly marked placeholders like `[INSERT NET IRR]` so the GP knows exactly what needs to be filled in.

**Write for sophisticated readers.** LPs at institutional funds are professional investors. Do not over-explain. Be direct.

## Output Format

Produce a complete letter draft using the structure below. Not every section is required — use judgment based on what inputs are available and what makes sense for the period. A quiet quarter with no exits or new investments does not need a section on those topics. Where setup recorded standing sections, a signature block or a disclaimer, use those in place of the defaults below, with the disclaimer word for word.

Most LP updates run 300–600 words, and longer is not better. Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

---

### Letter Structure

```
[Fund Name]
Quarterly Update — Q[X] [Year]

[Opening paragraph]
Set the tone for the letter. Acknowledge the period, reference the broader market environment if relevant, and orient the reader on what the letter covers. Keep to 2–4 sentences.

---

**Fund Performance**
[Summary of fund-level performance metrics the GP has provided. If no metrics are provided, omit this section or use placeholders. Do not derive, estimate, or calculate figures the user has not supplied.]

---

**Portfolio Update**
[Organized summary of portfolio company developments during the period. Group by theme, stage, or outcome type — whatever makes the narrative cleaner. Include milestones, notable challenges, and any management changes if provided. Write at the company level only to the extent the user has provided information.]

---

**New Investments**
[If new investments were made during the quarter, briefly describe each: company name, sector, stage, and a sentence on the thesis. Only include information the user provides.]

---

**Exits and Realizations**
[If exits or realizations occurred, summarize each: company, outcome, and implication for fund performance. Only if provided.]

---

**Cash Flow Activity**
[Capital calls or distributions made during the period, if provided. Use exact figures the user supplies — do not estimate.]

---

**Market Perspective**
[The GP's market or macro commentary, if provided. Write in the GP's voice. Keep to a short paragraph — LPs generally want the GP's perspective, not a macro research report.]

---

**Looking Ahead**
[Forward-looking paragraph: pipeline activity, themes the fund is watching, what the GP expects over the next period. Keep it directional. Do not make specific performance commitments.]

---

[Closing]
Brief closing — appreciation for LP partnership, invitation to reach out with questions, and signature block placeholder.

[GP Name / Firm Name]
[Title]
[Contact]
```

---

## Tone

Default to: professional, measured, confident without being promotional, and honest about uncertainty. Avoid:

- Superlatives ("incredible," "best-in-class," "exceptional")
- Vague reassurance with no substance ("we remain confident in our portfolio")
- Overly technical jargon unless the user's prior letters use it
- Cherry-picking language — if the period had challenges, acknowledge them proportionally

If the user provides prior letters, prioritize matching that voice over these defaults.

## When Context Is Limited

If the user provides minimal inputs (e.g., just "draft a Q2 update for our venture fund"), produce a template-style draft with clearly labeled placeholders throughout. Label the placeholders consistently — `[INSERT ...]` — so the user can work through them one by one.

Append at the end:

```
---
**To complete this draft, please provide:**
- [List specific missing inputs that would materially improve the letter]
```

A placeholder-filled draft is far more useful than a refusal to proceed.

## Example prompts

> "Set up lp-update-generator. We're Alderpoint Ventures, the letters cover Fund I and Fund II, past letters are in the 'LP Letters' folder on Google Drive, we always report net IRR, TVPI and DPI, and both managing partners sign."

> "Draft our Q3 update. Net IRR 14.2%, TVPI 1.4x, DPI 0.2x. Two new investments, one partial exit, notes on each pasted below. It was a mixed quarter and I want the letter to say so plainly."

> "Draft a Q2 update for our venture fund. I don't have the numbers yet; give me the letter with placeholders so I can fill them in when the administrator reports."
