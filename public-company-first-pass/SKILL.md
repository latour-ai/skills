---
name: public-company-first-pass
description: >-
  Create a first-pass tear sheet on a US-listed public company: what it does,
  how it makes money, a financial snapshot, valuation context, competitors,
  recent developments, bull and bear cases, and the questions to diligence
  next. Researches from a connected market data source (Bloomberg, FactSet,
  S&P Capital IQ, AlphaSense, Daloopa) where there is one, otherwise SEC
  filings and the open web, otherwise filings the user attaches. For equity
  analysts, portfolio managers and allocators deciding whether a name
  deserves more work. Trigger on "tear sheet", "first pass", "company
  overview", "company profile", "what does [company] do", "tell me about
  [ticker]", "quick look at [company]", "pull up [ticker]", "who competes
  with [company]", "bull/bear case for [ticker]", "is [ticker] interesting",
  "run me through [company]", or when the user gives a ticker and expects
  research, or uploads SEC filings for synthesis. Do NOT use for private
  companies; use the tear-sheet-private-co skill. Do NOT use for a focused
  memo on the revenue build and unit of analysis; use the
  public-co-unit-economics skill. Do NOT use to digest one earnings call;
  use the earnings-call-extractor skill. Do NOT use to attack a thesis the
  user has already written; use the thesis-red-team skill. Not for crypto,
  mutual funds, ETFs or non-US securities. No rating, price target or
  recommendation.
license: MIT
metadata:
  author: latourai
  version: '2.0'
---

# Public Company First Pass

Generate a concise (~3 page) first-pass tear sheet on a US-listed public company. The output is a `.md` file covering 11 sections: TL;DR, business overview, revenue breakdown, financials, valuation context, competitive landscape, recent developments, bull/bear cases, and an initial investment view with sources.

This is not a full initiation report, financial model, price target, or buy/sell/hold recommendation. It is a structured first look — the kind of thing an analyst prepares before deciding whether to dig deeper.

## Workflow

1. **Identify the company.** Resolve the name, ticker, and exchange and state them at the top of the tear sheet. Ask only if a name could refer to more than one listed company.
2. **Research.** Use a connected market and company data source (Bloomberg, FactSet, S&P Capital IQ, AlphaSense, Daloopa or similar) if there is one; otherwise search SEC filings and the open web; otherwise work from filings the user attaches, pastes, or points to in connected file storage. If a source is not connected or fails, move to the next and say in the Sources section which was used. Pull the 10-K, 10-Q, latest earnings results, investor presentations, and reputable financial data, following the Source Rules below.
3. **Build the tear sheet** following the 11-section output format below.
4. **Save as `[TICKER]-first-pass.md`** (e.g., `CRM-first-pass.md`) and share with the user.

## Source Rules (priority order)

Use the best available public information in this order:

1. Latest Form 10-K or annual report
2. Latest Form 10-Q
3. Latest earnings release
4. Latest earnings call transcript
5. Investor presentation
6. Company website
7. Reputable financial data sources (SEC EDGAR, Yahoo Finance, Bloomberg, FactSet)
8. Reputable news sources (WSJ, FT, Reuters, Bloomberg News)
9. Public competitor information

Do not use blogs, anonymous commentary, message boards, promotional stock-picking sites, social media posts, or unsourced claims. If data is unavailable, say so clearly; do not fabricate numbers, market share, competitors, or valuation metrics.

## Time Period

Use latest fiscal year and LTM (last twelve months) where available. Reference the latest quarter when relevant. Only use older history to explain the current state.

## Core Principles

These matter because the tear sheet needs to be trustworthy enough for a professional to act on — even if that action is just "worth more work."

- Be neutral and concise. Separate facts from interpretation.
- Prefer specific numbers over vague descriptions ("revenue grew 12% YoY" not "revenue grew nicely").
- No buy/sell/hold recommendation. No price target. Do not overstate precision in valuation.
- Include a balanced bull and bear case — don't softball either one.
- Flag missing, stale, or inconsistent information explicitly.
- Use bullets and tables to keep it scannable.

## Output Format — 11 Sections

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

### Section 1: TL;DR

3-5 bullets: what it does, why it matters now, financial profile, valuation context, bull/bear tension.

**Example:**

```markdown
## TL;DR

- **What it does:** Leading cloud-based CRM platform serving enterprises across sales, service, marketing, and commerce.
- **Why it matters:** Dominant CRM market share (~23%) with expanding platform play into data/AI via recent acquisitions.
- **Financial profile:** $34.9B revenue (FY24), 11% YoY growth, 30.5% non-GAAP operating margin, $12.2B FCF.
- **Valuation context:** Trading at ~26x NTM EV/EBITDA vs. 5-year average of ~35x; FCF yield ~4.5%.
- **Bull/bear tension:** Bulls see margin expansion + AI monetization; bears worry about decelerating organic growth and acquisition integration risk.
```

### Section 2: Business Overview

What the company does, core products/services, primary customers, end markets, geographic exposure, and business model. Keep it concise — avoid corporate history. Focus on what someone needs to understand the business today.

### Section 3: How the Company Makes Money

Table format breaking down revenue streams. This answers "where do the dollars actually come from?"

**Example:**

```markdown
| Revenue Stream / Segment | What It Includes | Key Drivers | Notes |
|---|---|---|---|
| Subscription & Support | Cloud CRM licenses, premium support | Seat expansion, upsell to higher tiers | ~94% of revenue, highly recurring |
| Professional Services | Implementation, consulting, training | New deployments, platform migrations | ~6% of revenue, lower margin |
```

### Section 4: Key Financial Snapshot

Table of core financial metrics. Only include what's actually available.

**Example:**

```markdown
| Metric | Latest FY (FY24) | LTM / Latest Available | Notes |
|---|---|---|---|
| Revenue | $34.9B | $35.6B (LTM) | FY ends Jan 31 |
| Revenue Growth (YoY) | 11% | 10% (LTM) | Decelerating from 18% two years prior |
| Gross Margin | 76.1% | 76.4% | Stable; subscription mix supports margin |
| Operating Income (non-GAAP) | $10.6B | $11.0B | 30.5% margin, up from 22% prior year |
| Net Income (GAAP) | $4.1B | $4.5B | Includes SBC of ~$3.8B |
| Free Cash Flow | $12.2B | $12.8B | FCF margin ~35%, strong conversion |
| Cash & Equivalents | $14.2B | — | Net debt ~$4B after long-term debt |
| Total Debt | $18.3B | — | Primarily acquisition financing |
```

Include relevant items like segment revenue (if not in Section 3), capex, R&D, dividends/buybacks, or anything material. Caveat stale or estimated figures.

### Section 5: Basic Valuation Context

Current valuation metrics with caveats. These are context, not conclusions.

**Example:**

```markdown
| Valuation Metric | Value | Notes |
|---|---|---|
| Market Cap | $265B | As of [date] |
| Enterprise Value | $269B | Includes net debt of ~$4B |
| P/E (NTM) | ~28x | Based on consensus NTM EPS |
| EV / Revenue (NTM) | ~7.0x | vs. large-cap SaaS median of ~8x |
| EV / EBITDA (NTM) | ~26x | vs. 5-year average of ~35x |
| FCF Yield | ~4.5% | Based on LTM FCF / market cap |
| 52-Week Performance | -8% | Underperforming S&P 500 by ~15pp |
```

If data is stale or unavailable, say so (e.g., "Consensus estimates not available; using trailing metrics only").

### Section 6: Competitive Landscape

Table mapping competitors — direct, adjacent, and substitutes.

**Example:**

```markdown
| Competitor | Relationship to Company | Relevant Difference |
|---|---|---|
| Microsoft Dynamics 365 | Direct competitor in CRM/ERP | Bundled with Office 365; enterprise integration advantage |
| HubSpot | Direct competitor in SMB CRM | Freemium model, stronger in inbound marketing |
| SAP | Adjacent (ERP with CRM module) | Stronger in manufacturing/supply chain verticals |
| ServiceNow | Adjacent (ITSM expanding into CX) | Competing in service/workflow automation |
| Freshworks | Substitute (lower-cost CRM) | Price-competitive for SMB segment |
```

### Section 7: Recent Developments

Last 6-12 months. Use bullets. Be specific with dates and numbers. Cover:

- Latest earnings results and guidance changes
- Product launches or strategic pivots
- M&A activity (completed, announced, rumored)
- Management changes
- Regulatory developments
- Major customer wins/losses or market developments
- Capital allocation changes (buybacks, dividends, debt paydown)

### Section 8: Bull Case

What needs to go right? Growth drivers, margin expansion, competitive advantages, market structure, capital allocation upside, valuation re-rating catalysts.

Ground every point in evidence. "Revenue could accelerate" is weak. "Revenue could accelerate as the $2B AI/Data Cloud segment (growing 35% YoY) scales and drives platform upsell" is useful.

No recommendation — this is "here's why an optimist would be interested."

### Section 9: Bear Case

What could go wrong? Growth deceleration, margin pressure, competitive threats, customer concentration, cyclicality, balance sheet risk, regulatory risk, valuation downside.

Don't exaggerate for false balance, but don't softball either. A useful bear case identifies scenarios that would actually cause losses, not just "competition could increase."

### Section 10: Initial Investment View

Synthesize Sections 8 and 9 into a framework for further work:

- **Central investment debate:** The one question that most determines outcome (e.g., "Can the company sustain 10%+ organic growth while expanding margins, or is this a maturing platform?")
- **What needs to be true for the bull case:** 2-3 specific, falsifiable conditions
- **What needs to be true for the bear case:** 2-3 specific, falsifiable conditions
- **Key variables to diligence next:** What would you study before forming a stronger view?

Keep this a framing of what matters, without a view on the stock.

### Section 11: Sources Used

List every source referenced with title, publisher/filing type, and date.

**Example:**

```markdown
| Source | Publisher / Filing Type | Date |
|---|---|---|
| Salesforce FY24 10-K | SEC Filing (Annual Report) | March 2024 |
| Q4 FY24 Earnings Release | Company Press Release | February 2024 |
| Q4 FY24 Earnings Call Transcript | Company / Seeking Alpha | February 2024 |
| "Salesforce Raises Full-Year Outlook" | Reuters | November 2023 |
```

## Handling Missing Information

If information isn't available, say so directly:

- "Not available in the reviewed public sources"
- "Not disclosed in the reviewed filings"
- "Consensus estimates not available; using trailing metrics only"

If the source set is incomplete (e.g., couldn't access the 10-K or latest transcript), add a note at the end explaining what's missing and how it affects the analysis.
