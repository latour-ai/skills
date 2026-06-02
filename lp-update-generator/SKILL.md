---
name: lp-update-generator
description: >-
  Draft a quarterly LP update letter from raw fund inputs. Use this skill
  whenever the user wants to write or draft an LP update, investor letter,
  quarterly letter, fund update, or limited partner communication. Trigger on
  phrases like "draft my LP update," "quarterly investor letter," "write our
  Q[X] update," "LP communication," "investor update," "write to our LPs,"
  or "quarterly letter to investors." Also trigger when the user provides
  fund performance data, portfolio updates, or market commentary and asks to
  turn them into an investor communication. This skill is format-agnostic —
  it does not depend on attachments, a specific data format, or a fixed set
  of inputs.
license: MIT
metadata:
  author: latourai
  version: '1.0'
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

If key inputs are missing, do not stop. Produce the best draft possible and append a clearly labeled section at the end listing what information would improve it.

## Core Principles

**Only use what the user provides.** Do not invent performance figures, company names, valuations, or market commentary. If the user says "we had a strong quarter" but provides no numbers, write around that directionally without fabricating specifics.

**Preserve the GP's voice.** If prior letters are provided, match their tone and structure. If not, default to a professional, measured tone — confident but not promotional.

**Be honest about gaps.** Placeholder language is better than invented language. Where data is missing, use clearly marked placeholders like `[INSERT NET IRR]` so the GP knows exactly what needs to be filled in.

**Write for sophisticated readers.** LPs at institutional funds are professional investors. Do not over-explain. Be direct.

## Output Format

Produce a complete letter draft using the structure below. Not every section is required — use judgment based on what inputs are available and what makes sense for the period. A quiet quarter with no exits or new investments does not need a section on those topics.

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

## Quality Checks

Before delivering the draft, verify:

- No invented numbers, company names, or facts
- All missing data is marked with `[INSERT ...]` placeholders
- Sections with no available information are either omitted or clearly flagged
- Tone is consistent throughout
- The letter reads like something a GP would actually send — not a generic template
- Length is appropriate: most LP updates run 300–600 words. Longer is not better.

## Important Reminder

This is a first draft. It should be reviewed by the GP or IR team before distribution. Fund communications to LPs may be subject to legal, regulatory, or contractual obligations that this skill cannot assess.
