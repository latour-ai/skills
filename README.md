# LaTour AI Skills Library

**16 skills** — practical AI workflows for investment firms created by [LaTour AI](https://www.latourai.com).

These skills are reusable instruction files you can copy into ChatGPT, Claude, Gemini, or any AI assistant that supports custom instructions or skill-style workflows.

*Before you begin: These skills are working examples and not finished products. Run your own tests and evaluations with your data and connectors, and modify them accordingly using your LLM's "skill-creator" skill.*

## Start here

### Meeting & Inbox Prep

| Skill | Use case |
|---|---|
| [Inbox Triage](inbox-triage/SKILL.md) | Pre-market inbox triage for hedge fund executives — ruthlessly filters hundreds of emails down to what matters before the trading day starts |
| [Executive Briefing](executive-briefing/SKILL.md) | Turn messy source material into a concise executive briefing (500 words or fewer) — source-agnostic, built for busy decision-makers |
| [Professional Profile Brief](professional-profile-brief/SKILL.md) | Pre-meeting prep note on any person — who they are, what they care about, relationship hooks, and smart conversation openers |
| [Call Transcript Follow-Up](call-transcript-followup/SKILL.md) | Turn a meeting or sales call transcript into a post-call package with summary, action items, and next steps |

### Investment Research

| Skill | Use case |
|---|---|
| [Public Company First Pass](public-company-first-pass/SKILL.md) | Generate a concise first-pass tear sheet on any US-listed public company — 11-section structured analysis from public sources, no fabricated data |
| [Public Company Unit Economics](public-co-unit-economics/SKILL.md) | Build a neutral, sourced two-page HTML unit economics memo from public filings — identify the best unit of analysis, explain the economic engine, and flag disclosure gaps |
| [Private Company Tear Sheet](tear-sheet-private-co/SKILL.md) | Generate investor-grade tear sheets on venture-backed private companies — funding history, operating metrics, competitive landscape, and investor perspective |
| [Hedge Fund Diligence](hedge-fund-diligence/SKILL.md) | First-pass diligence note on a hedge fund manager for allocators, FOFs, OCIOs, and family offices — separates known from unknown, surfaces gaps, generates meeting questions |
| [Earnings Call Extractor](earnings-call-extractor/) | Turn a raw earnings call transcript into a structured public equity memo — financial metrics, YoY changes, full analyst Q&A, and red flags |
| [Investment Folder Organizer](investment-folder-organizer/SKILL.md) | Organize a messy deal or diligence folder into eight standardized subfolders with a consistent, sortable filename convention — non-destructive, works for any asset class |

### Investor Relations & Outreach

| Skill | Use case |
|---|---|
| [LP Update Generator](lp-update-generator/SKILL.md) | Draft a polished quarterly LP update letter from raw fund inputs — performance data, portfolio updates, exits, and market commentary |
| [Fund Marketing One-Pager](fund-marketing-one-pager/SKILL.md) | Draft a polished fund overview document for LP outreach from any inputs — pitch deck, bullet points, or a few sentences |
| [Intro Email Generator](intro-email-generator/SKILL.md) | Write warm, high-signal introduction emails between two people |
| [LinkedIn Post Generator](linkedin-post-generator/SKILL.md) | Turn a rough idea, notes, or article into a polished LinkedIn post — optimized for executives building thought leadership, zero AI tells |
| [Relationship Status Summarizer](relationship-status-summarizer/SKILL.md) | Surface where a professional relationship stands by pulling from Gmail — last touchpoint, open threads, relationship temperature, and suggested next move |

### Learning

| Skill | Use case |
|---|---|
| [Teach Me](teach-me/) | Learn any company, industry, technology, or professional concept fast — structured lessons with mental models, concrete examples, and templates for cheat sheets, quizzes, and more |

## How to use

Most skills are a single `SKILL.md` file:

1. Open a skill folder.
2. Copy the `SKILL.md` file.
3. Paste it into your AI as a skill file.
4. Add your source material (if necessary).
5. Run the workflow.

### Multi-file skills

Some skills include extra reference files alongside `SKILL.md` (the [Earnings Call Extractor](earnings-call-extractor/) and [Teach Me](teach-me/) have `references/` folders). For these, download the packaged `.skill` bundle — a single file containing everything — and upload it directly to Claude:

- [Download `earnings-call-extractor.skill`](https://github.com/latour-ai/skills/raw/main/earnings-call-extractor/earnings-call-extractor.skill)
- [Download `teach-me.skill`](https://github.com/latour-ai/skills/raw/main/teach-me/teach-me.skill)

You can also browse the folder to read the files individually.

## Who this is for

These skills are designed for smart, busy professionals who want better AI outputs without becoming prompt engineers.

## Maintained by

Created by Khe Hy, founder of LaTour AI.

## Want this customized for your firm?

LaTour AI helps investment firms build practical AI workflows.

- Website: https://latourai.com
- Contact: contact@latourai.com
- Newsletter: https://khemaridh.substack.com/
