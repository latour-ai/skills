---
name: ai-workflow-audit
description: >-
  Interview a team about their recurring workflows, bottlenecks, data sources,
  and tools — one question batch at a time — then map the workflows to AI
  opportunities scored on impact × feasibility and deliver a prioritized AI
  adoption roadmap with quick wins, skill candidates to build, and risks.
  For investment firms and professional teams of any function. Trigger on
  phrases like "audit our workflows for AI," "where should we use AI,"
  "AI opportunity assessment," "interview me about our processes," "help us
  figure out what to automate," "AI readiness review," "build our AI
  roadmap," or "which of our tasks should AI do." Do NOT use for generating
  specific skill ideas from an already-known workflow — use the
  investment-skill-creator skill. Do NOT use for learning what AI can do in
  general — use the teach-me skill.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# AI Workflow Audit

Run a structured, interview-style audit of a team's recurring work, then turn the answers into a prioritized AI adoption roadmap: opportunities scored on impact × feasibility, quick wins for the next 30 days, the skills worth building, and the risks worth respecting. The interview comes first because the bottleneck in AI adoption is almost never the technology — it's that nobody has mapped the work.

## Why this skill exists

Most teams approach AI backwards: they start from tools ("should we buy X?") instead of from their own workflows. The result is pilots that demo well and die, while the actual time sinks — the Friday report assembled by hand, the inbox triage eating the analyst's mornings, the data that gets retyped between systems — go untouched. The fix is an audit: inventory the recurring work, find where time and judgment actually go, and only then match AI to it. Consultants charge real money for this mapping. The interview structure matters: one batch of questions at a time, because a 40-question form gets abandoned and a conversation doesn't.

## Inputs

**Required:**
- A willing interviewee (or several, answering together) who knows the team's actual day-to-day work. That's it — the skill generates everything else through the interview.

**Optional (shortens the interview):**
- Team description: function, headcount, roles
- Existing documentation: process docs, tool lists, an org chart
- Known pain points the team already suspects
- Constraints: compliance regime, data sensitivity, budget, IT restrictions
- Current AI usage, if any

**Missing-input behavior:** This skill *asks by design* — but in disciplined batches of 3–5 questions, never a wall of questions. If the user wants to skip the interview and dump a description instead, accept it, then ask one batch of targeted gap-filling questions before scoring.

## How it works

1. **Set the frame (one message).** Explain the process: ~3–4 short question batches, then a roadmap. Ask Batch 1 — the team: function, headcount, roles, and "describe a typical week in 5 lines."
2. **Batch 2 — the recurring work.** The 5–10 tasks that recur daily/weekly/monthly; roughly how long each takes and who does it; which one the team would pay to never do again; where deadlines get missed.
3. **Batch 3 — inputs, outputs, and tools.** For the biggest tasks: what goes in (documents, data, emails, calls) and what comes out (memos, models, updates, decisions); which systems/tools are involved; where information gets manually moved between systems; what data is sensitive or regulated.
4. **Batch 4 — judgment and appetite.** Which parts of each task are pure mechanics vs. real judgment; what's been tried with AI already and what happened; the team's appetite and constraints (compliance review requirements, client-data rules, IT posture). Skip or compress batches the earlier answers already covered — never re-ask what's been answered.
5. **Build the workflow map.** Consolidate into an inventory: each workflow with frequency, time cost, people involved, inputs/outputs, judgment intensity, and data sensitivity. Play it back for correction *before* scoring — the playback catches the misunderstandings that would otherwise corrupt the roadmap.
6. **Score AI opportunities.** For each workflow, assess: **Impact** (hours saved × frequency × who's freed up, plus quality/risk-reduction upside) and **Feasibility** (how structured the inputs are, how checkable the output is, data sensitivity, how much judgment must stay human). Score each High/Medium/Low with one line of reasoning — the reasoning is the deliverable, not the letter grade.
7. **Deliver the roadmap** in the output format: quick wins (high impact, high feasibility, start this month), build candidates (worth a designed, reusable skill or workflow), watch list (high impact but blocked by data, risk, or maturity — with what would unblock them), and don't-automate (judgment-core work where AI assists at most). Include risks and a realistic first-30-days plan.

## Output format

```
# AI Workflow Audit — [Team] | [Date]
Interviewed: [who] | Batches completed: [N] | Constraints noted: [compliance/data/IT]

## Workflow inventory (as confirmed by you)
| # | Workflow | Frequency | Time cost | Who | Judgment intensity | Data sensitivity |
|---|---|---|---|---|---|---|

## Opportunity scoring
| Workflow | Impact | Feasibility | Reasoning (one line) |
|---|---|---|---|

## Quick wins — start within 30 days
1. **[Workflow → AI approach]** — [what to do, with which generic tool category
   (e.g., "your AI assistant + the documents you already have")]; expected
   saving: [estimate, labeled as estimate]; how to verify it's working.

## Build candidates — reusable skills/workflows worth designing
- **[Candidate]** — [what it would do; inputs it needs; who owns it; rough effort]

## Watch list — high value, not yet
- **[Workflow]** — blocked by [data/risk/tooling]; unblocks when [condition]

## Keep human — don't automate
- **[Workflow]** — [why the judgment core should stay human; where AI can assist at the edges]

## Risks and guardrails
[Data sensitivity, compliance review needs, over-reliance risks, verification
habits to instill — specific to this team's answers.]

## First 30 days
Week 1: [...] | Weeks 2–3: [...] | Week 4: [review — what worked, what to kill]

## Open questions
[What the interview didn't resolve; who else to talk to.]
```

## Guardrails

- **One batch at a time, 3–5 questions, always numbered.** Never dump the full question set. Never re-ask answered questions.
- **Time savings are estimates and say so.** Derive them from the user's own stated time costs — never invent "industry benchmark" hours or ROI figures.
- **No tool-vendor recommendations.** Describe approaches generically ("an AI assistant with web search," "a reusable skill/prompt your team shares," "your email tool if connected"). Specific procurement is the team's decision.
- **Respect the judgment line.** Where the interviewee says judgment lives, the roadmap keeps humans in the loop — the audit's credibility rests on knowing what *not* to automate.
- **Data sensitivity is a first-class constraint,** not a footnote: anything touching client data, MNPI, or regulated records gets flagged in scoring, and the roadmap notes where compliance sign-off is needed before piloting.
- **The roadmap reflects what the team said,** not a generic playbook. Every scored opportunity must trace to something from the interview. If the interview was thin, the roadmap is honest about its confidence level.

## Quality checks

- [ ] Interview ran in batches; playback step confirmed the inventory before scoring
- [ ] Every opportunity score has a one-line reasoning traceable to interview answers
- [ ] All savings figures labeled as estimates from the user's own numbers
- [ ] "Keep human" section present and substantive
- [ ] Data-sensitivity and compliance flags carried into the roadmap
- [ ] First-30-days plan is small enough to actually happen

## Example prompt

> "We're a 6-person IR and client-service team at a credit fund. Interview us about our recurring workflows — a few questions at a time — and then give us a prioritized roadmap for where AI could actually help, what to try first, and what to keep away from it."
