---
name: hedge-fund-diligence
description: Create a first-pass diligence note on a hedge fund manager for allocators, fund-of-funds analysts, OCIOs, and family offices. Use this skill whenever the user wants to form an initial view on a hedge fund or its manager, prepare for an intro manager meeting, review a pitch deck / DDQ / tear sheet / investor letter, identify diligence gaps, or draft diligence and reference-check questions. Trigger on phrases like "first pass on [manager/fund]", "should I take this meeting", "review this hedge fund deck", "diligence note", "what should I ask this manager", "look into [fund name]", "prep me for a call with [manager]", or when the user pastes/uploads hedge fund marketing materials. Also trigger when given only a manager or fund name and the user wants a starting point. This is NOT full investment diligence, operational due diligence, or an investment recommendation.
---

# Hedge Fund Diligence — First Pass

## What this skill does

Produce a first-pass diligence note on a hedge fund manager. The reader is an allocator, fund-of-funds analyst, outsourced CIO, or family-office professional who needs an initial view fast. The note helps them decide whether to take a meeting, prepare sharper diligence questions, and identify what materials to request next.

This is explicitly **not** full investment diligence, operational due diligence (ODD), or a recommendation to invest. The value is in separating what's known from what's unknown and turning that gap into a concrete next-step list. Be useful, not exhaustive.

## The five core questions

Organize the analysis around these five questions. They are the spine of the note — every section should ultimately serve one of them:

1. **Are incentives aligned?** (GP commit, fees vs. liquidity vs. alpha, side letters)
2. **Is the edge real?** (what inefficiency, why it persists, differentiation)
3. **Is performance repeatable?** (skill vs. beta/factor/style, consistency)
4. **Are drawdowns explainable?** (what caused them, recovery, behavior after)
5. **Is the team stable?** (key-person risk, institutionalized vs. CIO-driven)

## Working from sources

Use whatever the user has. Common inputs: manager/fund name, pitch deck, DDQ, tear sheet, investor letter, meeting notes, public website, Form ADV/IAPD, Form D filings, news, LinkedIn/public bios, user notes.

Always lead with user-provided materials — they're the most relevant. Use public sources to fill gaps. Do not assume access to any specific database, subscription service, or private data room.

### No-materials mode (name only)

If the user gives only a manager or fund name, don't stop — search public sources by default to build a lightweight profile. Useful public sources include SEC IAPD / Form ADV, SEC EDGAR Form D filings, the firm website, reputable news, and public bios/LinkedIn.

When operating in this mode, open the note with this exact framing so expectations are clear:

> *This is not diligence. This is a public-information starting point for deciding whether to take a meeting and what to ask next.*

In no-materials mode, include: the lightweight public profile, a meeting-prep read, the Known/Unknown/Ask Next table, suggested diligence questions, a suggested materials request list, and sources reviewed. Do not infer performance, AUM, terms, exposures, or operational details unless they are publicly available from a reliable source — and cite it.

## Tone and style

Write like a fund-of-funds analyst note: neutral, direct, evidence-based, concise, practical, skeptical without being cynical. Memo style — short paragraphs, bullets and tables where they help. Avoid promotional language, generic consultant filler, and unsupported criticism.

The core discipline throughout: **distinguish what the manager claims, what the evidence supports, and what still needs diligence.** Marketing claims are not facts until verified.

## Output length

Scale the note to the quality of available information — usefulness over completeness:

- **Limited materials:** concise 1–2 page note
- **Rich materials:** 2–4 page analyst note
- **Meeting prep only:** keep to ~1 page

## Output structure

Use this structure unless the user asks otherwise. Omit or compress sections where there's genuinely nothing to say, but keep Team, Terms, and Performance near the top — those drive the meeting decision.

```
# [Manager / Fund Name] — Hedge Fund Diligence (First Pass)

## 1. First Impression
Concise initial read: what the manager appears to do, whether it seems worth a
meeting on available info, what's interesting, what's unclear, the biggest gaps.
Do NOT recommend investing.

## 2. Team
Founder/CIO background, key investment pros, team depth, relevant prior
experience, stability/turnover if known, key-person considerations.
Core question: is the edge tied to one person or institutionalized?

## 3. Terms, Liquidity and Alignment
If available: mgmt fee, incentive fee, hurdle/pref, lock-up, redemption
frequency, gate, notice period, side pockets, GP commit/founder capital,
high-water mark, capacity, fee breaks/share classes. Flag missing terms as a
gap. Assess alignment only on available info.

## 4. Performance and Drawdowns
Include ONLY if user-provided or publicly available from a reliable source.
Never estimate performance. If present: returns, vol, drawdowns, benchmark/peer
context, consistency, recovery, changing return profile, whether drawdowns look
explainable. If absent, state: "Performance was not available in the reviewed
materials and remains a primary diligence gap."

## 5. Strategy and Edge
Strategy description, universe, source of alpha, research/idea generation,
portfolio construction, horizon, shorting approach, leverage if disclosed, where
it should work vs. struggle. Core question: is the edge real, repeatable, and
differentiated? Separate claim vs. evidence vs. still-to-diligence.

## 6. Portfolio, Risk and Capacity
If available: gross/net exposure, concentration, position sizing, liquidity,
drawdown controls, risk limits, financing, prime brokerage, capacity, crowding,
derivatives/leverage. Missing items go to the gaps.

## 7. Key Counterparties and ODD Snapshot
NOT full ODD. Pull only disclosed key facts: administrator, auditor, prime
broker, custodian, legal counsel, compliance consultant, valuation agent. Flag
missing counterparties as gaps. Do not speculate about operational quality,
controls, or fraud without evidence.

## 8. Known / Unknown / Ask Next
Table with rows: Team, Terms/Liquidity, Performance, Strategy/Edge,
Risk/Exposures, Capacity, ODD/Counterparties, Alignment.
Columns: What We Know | What We Don't Know | Ask Next.
Be explicit when something is not available. Do not confuse "not found" with
"not true."

## 9. Diligence Questions
Practical intro-meeting questions, grouped: Incentive Alignment; Edge &
Repeatability; Performance & Drawdowns; Team Stability; Risk, Financing &
Capacity.

## 10. Reference Check Prep (if useful)
Grouped by reference type: Current Investors; Former Investors; Former
Employees; Service Providers.

## 11. Suggested Materials Request List
Tailored to what's missing. Prioritize: pitch deck, DDQ, monthly net returns,
AUM history, exposure history, drawdown history, annual attribution, current
portfolio summary, risk reports, sample investor letter, Form ADV Part 2, fund
terms summary, service provider list, reference list, compliance summary.

## 12. Sources Reviewed
List sources with title, type, and date when available. E.g., "Form ADV Part 2,
filed [date]"; "Firm website, accessed [date]"; "Pitch deck, dated [date]".
```

### Diligence question bank (use/adapt these)

**Incentive Alignment** — How much partner capital is in the fund? How has GP capital changed over time? How do terms compare to liquidity and expected alpha? Are there side letters or differing liquidity terms across investors?

**Edge & Repeatability** — What core inefficiency does the strategy exploit? Why should the edge persist? Which returns came from skill vs. beta/factor/style tailwinds? What's changed in the opportunity set over the last three years?

**Performance & Drawdowns** — What explains the largest drawdowns? Which positions/themes drove gains and losses? How did the portfolio change after drawdowns? What environments are hardest for the strategy?

**Team Stability** — Who owns idea generation? How are analysts compensated and retained? What turnover has occurred? Which parts of the process depend most on the CIO?

**Risk, Financing & Capacity** — Typical gross/net ranges? Max position size? How is liquidity monitored? Who are the prime brokers? How is financing risk managed? Realistic strategy capacity?

### Reference-check question bank

**Current investors** — Communication during difficult periods? Drawdowns explained clearly and promptly? Behavior consistent with stated strategy? Surprises on liquidity, terms, transparency?

**Former investors** — Why did you redeem? Issues with performance, transparency, liquidity, trust? How were difficult conversations handled?

**Former employees** — Institutionalized vs. CIO-driven? How are investment debates handled? Real culture? Concerns on risk, valuation, compliance, turnover?

**Service providers** — How long have you worked together? Recurring operational issues? Responsive and professional? Concerns on valuation, reporting, controls?

## Language for missing information

Precision here is what keeps the note credible. Use careful, neutral phrasing:

- "Not available in the reviewed materials."
- "Not found in the reviewed public sources."
- "Not disclosed in the reviewed documents."
- "This remains a primary diligence gap."
- "This should be confirmed directly with the manager."
- "The available information is insufficient to assess this."

Avoid these unless evidence clearly supports them, because they assert facts you don't have: "The manager does not have…", "This is a red flag…", "This proves…", "The strategy is flawed…", "The manager is not credible…"

## What to avoid

The note loses its value the moment it overreaches. So:

- Don't recommend investing (or recommend passing, unless the user explicitly asks for a screen).
- Don't invent performance, or infer AUM, terms, or exposures without support.
- Don't treat marketing claims as facts, and don't treat lack of public information as negative evidence — absence of data is a gap, not a finding.
- Don't speculate about fraud or misconduct.
- Don't use stale information without flagging the date.
- Don't over-index on AUM, and don't use numeric scoring.
- Don't use strong red-flag language unless the evidence clearly supports it.

## Quality checks before finalizing

Confirm the note: gives a clear first impression; helps the meeting decision; produces useful diligence questions; separates known from unknown; treats marketing claims as claims, not verified facts; includes performance only if provided/public and flags it as a primary gap when missing; keeps team, terms, liquidity, and performance near the top; addresses all five core questions; reads like an allocator analyst note; and is proportional to the quality of available information.
