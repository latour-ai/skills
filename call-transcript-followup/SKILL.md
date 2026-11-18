---
name: call-transcript-followup
description: >-
  Turn a raw meeting, sales call, client call, or expert-call transcript into
  a clean post-call package: an executive summary, key takeaways, decisions,
  action items with owners and due dates, open questions, risks, and a short
  CRM note. The transcript can be pasted, attached, or pulled from a
  connected meeting tool (Zoom, Teams, Fireflies, Granola, Otter). For
  investment firms, business development and lead generation teams,
  consultants, advisors, executives, and client-facing teams who need to
  convert conversations into next steps. Trigger on "process this call",
  "summarize this transcript", "action items from this meeting", "post-call
  summary", "follow-up from my call with [name]", "write the CRM note for
  this call", or when the user provides a transcript or meeting notes. Do
  NOT use when no transcript or recording exists; use the no-recording
  skill. Do NOT use for investment committee meetings; use the
  ic-minutes-generator skill. Do NOT use to combine several expert calls into
  one view; use the expert-call-synthesis skill. Do NOT use for public
  earnings calls; use the earnings-call-extractor skill.
license: MIT
metadata:
  author: latourai
  version: '2.0'
---

# Call Transcript Follow-Up

## When to Use This Skill

Load this skill when the user:

- Pastes or attaches a raw call or meeting transcript
- Shares meeting notes and asks for a structured summary
- Asks to extract action items, decisions, or takeaways from a conversation
- Needs a post-call package for a client, investor, or partner meeting
- Is in a lead generation or business development context and needs to document a prospect call

This skill is optimized for investment firms and lead generation workflows, but applies broadly to any client-facing or advisory context.

## Inputs

The user may provide:

- A raw transcript
- Meeting notes
- Speaker names
- Client or company name
- Context about the relationship or meeting goal

The transcript can be pasted or attached. If a meeting tool is connected (Zoom, Teams, Fireflies, Granola, Otter) and the user names the meeting, read the transcript from there. If the tool isn't connected or the transcript can't be found, say so and ask for it to be pasted.

If context is missing, infer carefully from the transcript but do not invent facts.

## Core Instructions

When given a transcript, produce a post-call package using the structure below.

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

### 1. Meeting Snapshot

Summarize the basic context:

- **Meeting topic:**
- **Participants:**
- **Date:** Use only if provided
- **Purpose of the call:**
- **Overall outcome:**

If any of these are unclear, write `Not specified`.

### 2. Executive Summary

Write a concise 5–8 bullet summary of the conversation.

Focus on:

- What was discussed
- What mattered most
- Any decisions made
- Any commitments made
- Any next steps
- Any tensions, blockers, or unresolved issues

Avoid generic filler. Prioritize what a busy executive or investor would need to know.

### 3. Key Takeaways

Extract the most important strategic or commercial takeaways.

Use this format:

- **Takeaway:** [Clear statement]
  - **Why it matters:** [Business implication]

Include 3–7 takeaways depending on transcript length.

### 4. Decisions Made

List explicit decisions only.

| Decision | Owner | Notes |
|----------|-------|-------|
| [Decision] | [Person or team] | [Relevant context] |

If no clear decisions were made, write:

> No explicit decisions were made in the transcript.

### 5. Action Items

Extract concrete follow-ups.

| Action Item | Owner | Due Date | Source / Context |
|-------------|-------|----------|-----------------|
| [Specific next step] | [Person] | [Date or Not specified] | [Brief context] |

Rules:

- Do not invent owners.
- If the owner is implied but not explicit, write `Likely owner: [name]`.
- If no due date is mentioned, write `Not specified`.
- Separate actual commitments from vague possibilities.
- Do not include generic "follow up" items unless the transcript supports them.

### 6. Open Questions

List unresolved questions that need clarification.

- **Question:** [Question]
  - **Why it matters:** [Impact on next step or decision]

### 7. Risks, Blockers, or Watchouts

Identify any risks, blockers, or ambiguity. Examples:

- Misalignment between participants
- Unclear ownership
- Missing data
- Legal, compliance, or approval dependencies
- Timeline risk
- Budget uncertainty
- Technical feasibility concerns

If none are apparent, write:

> No major risks or blockers were apparent from the transcript.

### 8. CRM Note

Add a short CRM-style note for sales, consulting, or client-development conversations. It is especially relevant for investment and lead generation workflows.

Use this format:

> **CRM Note:** [3–5 sentence summary of the relationship, client need, opportunity, next step, and any relevant timing.]

The note is returned as text, ready to paste into the firm's CRM (Salesforce, HubSpot, Dynamics 365, DealCloud, Affinity) or project tracker. If a CRM is connected and the user asks for the note to be logged, show the note and the matched account, and write it as an activity only after the user confirms. Do not create or edit accounts, contacts or opportunities. If the write fails, say so and leave the note as text.

## Guardrails

- Do not fabricate facts, dates, names, numbers, or commitments.
- Distinguish between what was explicitly said and what is inferred.
- Preserve uncertainty where the transcript is ambiguous.
- Do not include sensitive personal details unless directly relevant to the business purpose of the call.
- Do not quote long passages from the transcript unless specifically asked.
- Nothing is sent or shared. Any follow-up message the user asks for is a draft for them to send.
