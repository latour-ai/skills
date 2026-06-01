---
name: executive-briefing
description: >-
  Turn messy source material into a concise executive briefing (500 words or fewer). For executives, founders, investors, consultants, and operators who need to quickly understand a topic, meeting, company, market, project, or decision context. Use whenever the user says "brief me," "executive summary," "executive briefing," "decision brief," "what do I need to know," "catch me up," "prepare me for," "summarize this for a meeting," "key takeaways," "background context," "what's important here," "TL;DR," "bottom line," "prep me," "distill this," "boil this down," or "what matters here." Also trigger when the user provides articles, meeting notes, PDFs, memos, or pasted text and wants a summary for a busy reader or decision-maker — even without the word "briefing." If the user is preparing for a meeting, board session, or investor call and wants to understand background material quickly, this skill applies. Source-agnostic.
---

# Executive Briefing

Turn messy, lengthy, or scattered source material into a concise executive briefing that a busy reader can absorb in under two minutes.

## Why this skill exists

Executives, founders, and operators constantly receive dense material — articles, meeting transcripts, research notes, memos, PDFs — and need the essential facts extracted and organized fast. The goal is not a generic summary. It's a briefing: neutral, thorough within its scope, and honest about what it doesn't know.

## Core principle

Only include what the provided source material supports. Do not invent facts, fill in missing background from general knowledge, speculate beyond the sources, or make recommendations unless the user explicitly asks. If the source says something ambiguous, flag it as an open question rather than resolving it with assumptions.

This matters because executives make decisions based on briefings. An unsupported claim presented as fact can lead to bad decisions. Err on the side of "here's what we don't know" over "here's my best guess."

## How to produce the briefing

1. Read all available source material carefully — attachments, pasted text, linked pages, conversation context.
2. Identify the main topic, the apparent purpose, and who the briefing is for (infer from context or ask).
3. Extract the most relevant facts. Relevance means: would an executive preparing for a decision or meeting need this?
4. Separate confirmed facts from open questions. This distinction is the backbone of a good briefing.
5. Preserve important background context — history, stakeholders, prior events, market dynamics — but only what appears in the sources.
6. Strip out duplication, filler, promotional language, and unsupported interpretation.
7. Write the briefing in the output format below.

## Output format

Use this exact structure. Keep the total briefing to 500 words or fewer unless the user requests otherwise.

```
**TL;DR**
2-4 sentences capturing the single most important takeaway. A reader who only sees this section should walk away informed.

**Key Facts**
- Bullet points with the most relevant facts, each grounded in the provided source material.
- Attribute or qualify where the source is ambiguous ("according to the memo," "the transcript suggests").

**Background Context**
Briefly explain what a reader needs to understand the topic — history, stakeholders, prior events, business or market context. Only include what the sources support.

**Open Questions**
Important unresolved questions surfaced by the material. Do not answer these unless the answer is directly supported by the sources. These are genuinely open — flag them so the reader knows where the gaps are.

**Source Notes**
One or two sentences identifying what source material the briefing drew from (e.g., "Based on the attached article and meeting transcript from May 15").
```

## When context is limited

Don't stop. Produce a lightweight version using whatever is available, then append:

```
**Additional Context That Would Improve This Briefing**
- [List specific missing information: intended audience, the decision being made, relevant prior meetings, additional source documents, the user's objective, time sensitivity, etc.]
```

This is more useful than refusing to produce anything. A partial briefing with clearly identified gaps is better than "I don't have enough information."

## Tone

Neutral executive voice — clear, direct, thorough, and non-promotional. Avoid corporate-speak ("synergies," "leverage," "align"), generic filler ("it's worth noting that"), and unnecessary hedging. If the source material uses specialized terminology the reader would expect (financial terms, technical concepts), keep it — but don't add jargon that isn't in the source.

Write as if you're briefing a smart, busy person who respects your judgment and has zero patience for fluff.

## Quality checks

Before delivering the briefing, verify:

- Total length is 500 words or fewer (unless the user requested otherwise)
- Tone is neutral and executive-appropriate
- Every factual claim traces back to the provided source material
- Facts and open questions are clearly separated
- No unsupported recommendations or speculation
- Concise but not shallow — important nuance is preserved
- No generic filler sentences that could appear in any briefing
- A reader unfamiliar with the topic could act on this

## Example prompt

"Brief me on the attached article and meeting notes. I'm meeting with the CEO tomorrow and need to understand the key facts, background context, and open questions."

In this case, read both sources, cross-reference where they overlap or conflict, and produce the briefing focused on what matters for that CEO meeting.
