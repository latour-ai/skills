---
name: fund-marketing-one-pager
description: >-
  Draft a fund marketing one-pager in polished markdown from whatever inputs
  the user provides. Use this skill whenever a fund manager, GP, or IR
  professional wants to create or improve a fund overview document for LP
  outreach. Trigger on phrases like "fund one-pager," "fund overview,"
  "marketing doc," "fund summary," "LP marketing materials," "fund pitch
  summary," "write up our fund," "draft our fund overview," "fund description
  for LPs," "what do I send prospective LPs," or any request to produce a
  top-of-funnel document that describes a fund to prospective investors.
  Also trigger when the user uploads or pastes a pitch deck, DDQ, investor
  letter, prior marketing document, or strategy description and asks to turn
  it into a fund overview. This skill is input-agnostic — it works from a
  few sentences or from a full document upload.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Fund Marketing One-Pager

Draft a polished fund overview document from whatever the user provides — a few sentences, pasted bullet points, or uploaded materials.

## Why This Skill Exists

Most emerging managers and smaller funds don't have a dedicated IR team or a designer on call. Getting a clean, professional fund overview in front of a prospective LP often means starting from scratch or reformatting an unwieldy pitch deck. This skill turns raw fund information into a structured, well-written overview that's ready to share or hand off to a designer.

The output is polished markdown — structured cleanly enough to drop into a template, email, or document without heavy editing, but not a finished designed file. That keeps the skill flexible regardless of what tools the user has available.

## What This Skill Does Not Do

- It does not invent strategy, performance, team backgrounds, or differentiators. Everything in the output comes from what the user provides.
- It does not calculate or derive performance metrics. If numbers are provided, they are presented as given.
- It does not make compliance or regulatory determinations. Fund marketing materials may be subject to legal review requirements — that is the user's responsibility.
- It does not produce a designed PDF or formatted document. The output is markdown intended as a draft for further editing or design work.

## Inputs

The skill works on a spectrum. More context produces a tighter, more specific draft. Less context produces a clean placeholder-filled template. Either is useful.

**Rich inputs (if available):**
- Uploaded pitch deck, DDQ, or prior marketing document
- Investor letters or quarterly updates
- Strategy description in any form
- Team bios or LinkedIn profiles
- Performance track record or select metrics
- Target LP profile (institutional, family office, HNWI, etc.)
- Fund terms (target size, minimum, fee structure)
- Geographic or sector focus

**Minimal inputs (enough to start):**
- Fund name and strategy type (e.g., "early-stage venture," "long/short equity," "private credit")
- A sentence or two on what makes the fund different
- Manager background in any form

If the user provides only minimal inputs, produce a clean template with `[INSERT ...]` placeholders and append a list of what would strengthen the draft. Do not refuse to proceed because inputs are limited.

## Core Principles

**Only use what the user provides.** Do not invent a track record, fabricate team credentials, or add claims the user has not made. A marketing document with invented content is worse than a sparse one.

**Extract and reorganize, don't generate.** When the user uploads source materials, the job is to pull out what matters and restructure it into the one-pager format — not to rewrite the fund's strategy from scratch.

**Be specific where possible, honest about gaps otherwise.** Vague language like "experienced team with strong track record" is weaker than actual specifics. If specifics aren't provided, use placeholders that prompt the user to fill them in.

**Write for a sophisticated LP audience.** Prospective LPs — institutional allocators, family offices, fund-of-funds — are professionals. The tone should be confident and direct without being promotional or overselling.

**Shorter is better.** A genuine one-pager is 400–600 words. Resist the urge to fill space. LPs skim; every sentence should earn its place.

## Output Format

Produce the one-pager in the structure below. Omit sections where no information is available and there is no meaningful placeholder to offer. Tailor the headers and emphasis based on the fund type — a venture fund and a macro hedge fund have different priorities.

---

### One-Pager Structure

```
# [Fund Name]
**[Strategy Type] | [Vintage / Fund Number if known] | [AUM or Target Size if known]**

---

## Strategy
[2–4 sentences describing what the fund does, where it invests, and what drives returns. Be specific about stage, sector, geography, and instrument if provided. If not provided, use placeholders.]

---

## Edge
[What makes this manager or strategy differentiated. This is the most important section — if the user has a clear view on their edge, it goes here. If not, use a placeholder and note that this needs to be the sharpest section of the document.]

---

## Team
[Key principals: name, title, and the most relevant prior experience or credential. Keep to 1–2 sentences per person. Only include what the user provides — do not look up or infer backgrounds.]

---

## Track Record
[If performance data is provided, present it here exactly as given. If no track record is available (e.g., emerging manager, first fund), omit this section or acknowledge it briefly and pivot to relevant prior experience instead. Do not estimate or derive figures.]

---

## Portfolio / Investment Approach
[How the fund sources, evaluates, and manages investments. For venture: stages, check sizes, typical ownership targets. For hedge funds: instruments, risk approach, portfolio construction. Only include what the user provides.]

---

## Terms
[Fund size, minimum investment, management fee, carry, and any other terms the user provides. Use placeholders for anything missing.]

---

## Target Investor
[Who this fund is right for — e.g., institutional LPs, family offices, endowments, HNWIs. If the user hasn't specified, omit or use a light placeholder.]

---

[Contact / Firm Name]
[Website if provided]
[Contact information if provided]
```

---

## Adapting to Input Level

### When source materials are uploaded
Read the uploaded content carefully. Extract the core strategy, team, edge, and any performance data. Restructure into the one-pager format — do not simply summarize the source document, actively reorganize it into this tighter structure. Flag any sections that are weak or missing in the original.

### When only a description is provided
Use the description as-is for the sections it covers. Fill gaps with clearly marked `[INSERT ...]` placeholders. Append a completion checklist.

### When input is minimal (a sentence or two)
Produce a clean template with the fund name and strategy type populated where known, `[INSERT ...]` placeholders everywhere else, and a prioritized list of what to fill in first. The Edge section is always the highest priority — note that explicitly.

## Tone

Default to: precise, professional, understated. Fund marketing documents that oversell raise flags with experienced allocators. Avoid:

- Superlatives without evidence ("exceptional returns," "best-in-class process")
- Vague differentiation claims ("we have a unique approach")
- Buzzwords that don't mean anything ("value-add," "proprietary deal flow" without explanation)
- Excessive length — if a section can be one sentence, it should be one sentence

If the user provides prior marketing materials, match that voice and register.

## When Context Is Limited

Append the following at the end of any draft where meaningful inputs are missing:

```
---
**To sharpen this one-pager, consider adding:**
- [Prioritized list of missing inputs, starting with the most impactful]
```

Always list the Edge section first if it's missing or thin — that is the section prospective LPs most scrutinize.

## Quality Checks

Before delivering the draft, verify:

- No invented facts, credentials, or performance figures
- All missing data marked with `[INSERT ...]` placeholders
- Length is 400–600 words (excluding placeholders and the completion checklist)
- The Edge section is specific — if it reads as generic, flag it explicitly
- Tone is consistent: professional, direct, not promotional
- The document reads like something a GP would hand to a serious allocator

## Important Reminder

This is a draft. Fund marketing materials are often subject to regulatory requirements (e.g., SEC, FINRA, CFTC depending on fund type and distribution context). The user is responsible for compliance review before distributing to prospective investors.
