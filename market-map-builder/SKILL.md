---
name: market-map-builder
description: Build a sourced market map of a sector for VC and growth investors — segmentation logic, players per segment with funding stage and amounts from public sources (each dated), recent entrants and exits, and whitespace observations. Trigger on "market map of [sector]", "map the [space] landscape", "who's building in [category]", "competitive landscape for [sector]", "what companies are in [space]", "whitespace in [market]", "landscape analysis", or when a user names a sector/theme and wants to know the players, funding activity, and gaps. Uses your AI's web search; flags stale or conflicting funding data; never invents companies. Do NOT use for deep research on a single company — use the tear-sheet-private-co or public-company-first-pass skill. Do NOT use for prepping on a specific LP or person — use the lp-prospect-brief or professional-profile-brief skill.
---

# Market Map Builder

Build a structured, sourced market map of a sector: a defensible segmentation, the named players in each segment with public funding data (every figure dated), who's entered and exited recently, and where the whitespace might be. The output is a memo with a table — the kind of artifact a VC associate produces before a thesis discussion or a first call in a new space.

## Why this skill exists

Market maps are how venture teams turn "AI for logistics is interesting" into a thesis, but they're brutal to build honestly. Funding data scattered across press releases, conflicting round sizes, dead companies still listed as active, and the constant temptation to fill an empty segment with a half-remembered name. A map with one fabricated company or a 2021 round presented as current is worse than no map. This skill front-loads the discipline: real companies only, every funding figure dated and sourced, conflicts surfaced instead of averaged away.

## Inputs

**Required:**
- The sector, category, or theme to map (e.g., "vertical AI for insurance claims", "industrial robotics for warehouses")

**Optional but high-value:**
- The investing lens: stage focus (seed/A/growth), geography, check size — shapes which players matter
- A working segmentation hypothesis to test rather than build from scratch
- Companies already known/portfolio companies in the space (to position, and to avoid awkward omissions)
- Time horizon for "recent" (default: last 24 months)

**Missing-input behavior:** If the sector is too broad to map usefully ("fintech"), ask once for a narrower cut or a lens; if the user declines, pick the 2–3 most fundable sub-segments, map those, and label the choice. For all other missing inputs, proceed with defaults stated at the top of the memo.

## How it works

1. **Define the market boundary first.** One sentence on what's in and what's out, with the edge cases named ("includes claims-automation startups; excludes core policy-admin systems"). A map without a boundary is a list.
2. **Build the segmentation** from how the market actually divides — by customer, by workflow stage, by business model, or by technology approach. Pick the single axis that best predicts who competes with whom, and say why. 3–6 segments; more means the axis is wrong.
3. **Populate segments via web search.** For each segment, find real, verifiable companies. For each: one-line description, HQ/geography if relevant, last known funding round (stage, amount, lead if notable), and **the date of the source for that funding data**. Prioritize primary-ish sources: company announcements, credible press, regulatory filings. 
4. **Handle data quality explicitly:**
   - Funding data older than ~18 months: tag **[stale — as of {date}]**
   - Conflicting figures across sources: report both with sources — never average or pick silently
   - Unverifiable companies (no findable site, no press, no filings): exclude; do not pad segments
   - Possibly dead companies (site down, no activity in 2+ years): tag **[activity unclear]**
5. **Track entrants and exits** within the recency window: notable new companies/launches, acquisitions (acquirer + date), shutdowns, and pivots into or out of the space.
6. **Identify whitespace** — and earn it. A whitespace claim needs reasoning: an underserved customer segment, a workflow step nobody covers, a geography gap. Distinguish "I found no company doing X" (absence of evidence, clearly labeled) from "X is structurally unserved because…" (an argument).
7. **Position the user's known companies** (if provided) on the map neutrally.

## Output format

```
# Market Map — [Sector]
Prepared [date] | Lens: [stage/geo/check size or "none specified"] | Recency window: [X months]

## Market Boundary
What's in, what's out, edge cases.

## Segmentation Logic
The axis chosen and why it beats the alternatives considered.

## The Map
| Segment | Company | What They Do (one line) | Stage | Last Known Raise | As-of / Source | Flags |
|---|---|---|---|---|---|---|
(Flags: [stale], [conflicting data], [activity unclear])

## Conflicting / Uncertain Data
Each conflict spelled out: figure A (source, date) vs. figure B (source, date).

## Recent Entrants & Exits ([window])
Entrants: company, segment, what signal it sends.
Exits: company, type (acquisition/shutdown), acquirer, date, read-through.

## Whitespace Observations
Each: the gap, the reasoning, and whether it's evidenced absence or structural argument.
Honest counter-case: why the whitespace might be empty for a reason.

## Sources
Numbered list: publication/site, title or description, date accessed/published.

## Limitations
What this map can't see: stealth companies, unannounced rounds, private revenue data.
```

## Choosing the segmentation axis

The axis decision makes or breaks the map. Candidate axes, with when each wins:

- **By customer segment** (enterprise vs. SMB; carrier vs. broker) — wins when go-to-market, not product, determines who competes
- **By workflow stage** (intake → processing → resolution) — wins in process-heavy verticals where companies own a step, not the whole flow
- **By business model** (software vs. tech-enabled service vs. marketplace) — wins when economics, margins, and exit comps differ sharply across models
- **By technology approach** (rules-based vs. ML-native vs. agentic) — wins early in a platform shift; ages fastest, so date it
- **Avoid axis salad.** If the map needs two axes, use one for segments and mention the second as a column attribute — a 2x3 grid of micro-segments with one company each means the boundary was too narrow or the axis is wrong.

Test the chosen axis: do companies in the same segment actually lose deals to each other? If not, the segmentation is taxonomy, not competition.

## Guardrails

- **Never invent a company.** Every named company must come from a verifiable source found during research. An empty segment cell is a finding, not a failure.
- **Every funding figure carries an as-of date and source.** No date, no figure.
- **Never reconcile conflicting data silently** — surface both numbers.
- **Funding ≠ quality.** Don't rank companies by capital raised or imply the best-funded player wins; note it as one signal among several.
- **Whitespace humility:** "no company found" is a search result, not a market fact. Always include the counter-case (the gap may exist because the economics don't work).
- Private company data is inherently incomplete and lagged — the Limitations section is mandatory, not decorative.
- No investment recommendations; the map informs a thesis, it isn't one.

## Quality checks

- Boundary sentence present and segments mutually exclusive on the stated axis?
- Every company verifiable, every funding figure dated and sourced?
- Stale/conflicting/unclear tags actually used (a map with zero flags is suspicious)?
- Entrants/exits within the stated window only?
- Each whitespace claim has reasoning plus a counter-case?
- Sources list complete enough that a colleague could re-verify any cell?

## Example prompts

> "Map the AI-for-construction space for me — preconstruction through field operations, North America, Series A to C is our zone. We already know Procore's orbit; I care about who's emerged since 2024 and whether there's anything left in field-safety. Flag anything where the funding data looks old."

> "We have a thesis that compliance tooling for registered investment advisers is consolidating. Build the map, test our three-segment hypothesis (monitoring / marketing review / trade surveillance), and tell me if the segmentation holds."

> "Quick landscape: who's building agentic AI for insurance claims? Seed through B, global. I need it before a first call tomorrow — flag everything you couldn't verify."

## Works well with

Drill into a single name with **tear-sheet-private-co**; if a mapped player is public, switch to **public-company-first-pass**. For learning the sector itself first, use **teach-me**.
