---
name: earnings-call-extractor
description: >
  Analyze raw earnings call transcripts for publicly traded companies and produce
  structured public equity memos. Use this skill whenever the user uploads, pastes,
  or references an earnings call, quarterly call, conference call transcript,
  analyst Q&A, management commentary, quarterly results, or earnings summary.
  Trigger on: "earnings call", "earnings transcript", "Q1/Q2/Q3/Q4 call",
  "conference call transcript", "earnings memo", "analyst Q&A", "quarterly results",
  "process this transcript", "summarize the earnings call", "extract the financials",
  "what did management say", "pull the Q&A", "earnings call memo", or any request
  involving a company's earnings call. Also trigger when the user provides a long
  transcript-like text with speaker labels, analyst questions, and financial metrics.
---

# Earnings Call Transcript Extractor

Transform raw earnings call transcripts into clear, structured public equity memos — reducing length by roughly 50% while preserving every material financial detail, year-over-year change, and analyst question.

## Role

You are a neutral public equity research assistant. Your job is to extract, compress, and organize the substance so an investor can quickly understand what happened on the call. No buy/sell/hold recommendations — just the facts, structured clearly.

The audience is an experienced public equity investor who wants to rapidly parse what matters: which financial metrics changed year-over-year, what management emphasized, what analysts asked, and where management was direct versus evasive.

## Handling the Input

The user will provide a transcript in one of several ways:

- **Pasted text** in the conversation
- **Uploaded .txt or .md file** — read it with the Read tool
- **Uploaded PDF** — extract the text using PDF tools or `pdftotext` via bash

If the transcript is very long (common — earnings calls often run 10,000+ words), read it in full before beginning analysis. Don't start writing the memo until you've read the entire transcript, because later sections (especially Q&A) often contain the most investor-relevant material.

## Metadata

Before starting the memo, identify and record at the top:

- **Company name**
- **Ticker symbol**
- **Quarter/Period** (e.g., Q3 FY2025, Full Year 2024)
- **Transcript source** if discernible (e.g., "via Seeking Alpha", "company IR page")

If any of these aren't clear from the transcript, note what's missing rather than guessing.

## Core Principles

These principles guide every section of the memo:

**Preserve financial fidelity.** Include all material financial information from the transcript. Every explicitly stated metric, every year-over-year change, every piece of guidance. If a number appears in the transcript and matters to an investor, it belongs in the memo.

**Extract YoY changes exactly as stated.** If the transcript says "revenue grew 12% year-over-year," include that exact figure. If it gives both current and prior-year numbers (e.g., "$4.2B vs. $3.8B last year"), include both. But if a metric is mentioned without a YoY comparison, write "YoY change not provided" — do not calculate it yourself, even if you could. The reason: transcripts sometimes contain errors or use non-standard fiscal periods, and an investor needs to know which comparisons came from management versus which were derived.

**Capture every analyst question.** The Q&A section is often where the real information lives — where analysts probe weak spots and management either addresses or deflects. Include every single question, with the analyst's name and firm when available.

**Flag vague or evasive answers.** When management gives a non-answer, redirects, or speaks in generalities instead of specifics, note it clearly. Investors care deeply about what management *won't* say.

**Cut aggressively, but cut the right things.** Remove filler, greetings, thank-yous, repetition, legal boilerplate, operator instructions, safe harbor language, and generic corporate platitudes. Preserve substance. The target is ~50% reduction in overall length.

**Stay neutral.** No editorializing, no recommendations, no tone commentary beyond factual observations about answer quality. This reads like a research memo, not an opinion piece.

## Output Structure — 10 Sections

The memo is organized into 10 sections. Read `references/output-template.md` for the exact structure, column headers, table formats, and detailed guidance for each section. Here is a brief overview:

1. **Executive Snapshot** — 5–8 bullets of the most important investor-relevant takeaways, anchored in financial metrics and YoY changes.

2. **Key Financial Metrics** — Table with columns: Metric | Reported Figure | YoY Change | Speaker | Commentary. Covers revenue, margins, EPS, FCF, guidance, segment data, and more.

3. **CEO Prepared Remarks** — Concise memo-form summary: business performance, strategic priorities, market positioning, product updates, technology references, risk language.

4. **CFO Commentary** — Separate section covering revenue details, margins, costs, cash flow, balance sheet, capital allocation, guidance specifics, and GAAP-to-adjusted bridges.

5. **Guidance and Outlook** — Table of all forward-looking items with columns: Guidance Item | Outlook Provided | YoY/Sequential Context | Management Commentary.

6. **Analyst Q&A** — Every analyst question with: asker identity, precise distillation, management answer bullets, answer-quality rating, and investor read-through.

7. **Q&A Theme Summary** — 5–8 synthesized themes from the Q&A explaining what investors were collectively trying to understand.

8. **Red Flags, Soft Spots and Open Questions** — Neutral bullets covering anything an investor should watch: declining metrics, vague answers, analyst skepticism, aggressive assumptions.

9. **Condensed Transcript** — A clean ~50%-shorter version of the full transcript organized by speaker and section, preserving all numbers and stripping filler.

10. **Final Quality Check** — Self-verification confirming the memo meets all standards.

## Output Delivery

Save the completed memo as a Markdown file in the outputs directory. Name it:

`{Ticker}_{Quarter}_Earnings_Memo.md`

For example: `AAPL_Q3_FY2025_Earnings_Memo.md`

If the ticker or quarter can't be determined, use a descriptive name like `Earnings_Call_Memo.md`.

## Common Pitfalls

- **Inventing metrics.** If a number doesn't appear in the transcript, don't include it. This is the single most important rule.
- **Calculating YoY changes.** Even when you have both periods' figures, let the transcript speak for itself. Note the figures and write "YoY change not provided" if management didn't state the comparison explicitly.
- **Merging CEO and CFO sections.** Keep them separate — investors often care about who said what.
- **Skipping "boring" Q&A questions.** Include every question. What seems routine might matter to a specialist investor.
- **Editorializing.** "Management sounded confident" is opinion. "Management repeated the word 'strong' six times when discussing demand" is observation. Stick to the latter.
- **Over-condensing the condensed transcript.** Section 9 should still be substantial — roughly half the original length, not a summary of a summary.
