---
name: tear-sheet-private-co
description: >-
  Generate investor-grade tear sheets on venture-backed private companies.
  Produces a structured, sourced markdown brief covering company snapshot,
  business model, funding history, operating metrics, management, competitive
  landscape, and investor perspective. Use this skill whenever the user asks
  for a "tear sheet," "company overview," "company profile," "investor brief,"
  "due diligence summary," "company research," "private company analysis,"
  "investment memo," or says things like "pull up a tear sheet on [company],"
  "research [company] for me," "what do we know about [company]," "give me
  the rundown on [company]," "prep a company overview," or "diligence
  [company]." Also trigger when the user names a specific startup or
  venture-backed company and asks for a summary, profile, or overview in an
  investment context. Do NOT use for public-company equity research (10-K
  analysis, DCF models) or for simple news lookups — this is for structured
  private-company tear sheets.
---

# Private Company Tear Sheet Generator

Produce an investor-grade tear sheet on a venture-backed private company. The output reads like something a buyside research analyst would hand to a portfolio manager: concise, fact-dense, well-sourced, and honest about what's confirmed vs. rumored.

## Why This Skill Exists

Investment professionals constantly need quick, structured overviews of private companies — for deal screening, portfolio monitoring, competitive mapping, or meeting prep. The challenge with private companies is that data is scattered, often unconfirmed, and mixes hard numbers with speculation. This skill enforces a consistent structure and sourcing discipline so the reader always knows what's solid and what's soft.

## How It Works

1. The user provides a company name (and optionally context like "pre-IPO" or "Series C stage").
2. You research the company extensively using WebSearch.
3. You produce a structured markdown tear sheet saved to the outputs directory.

## Research Phase

Use WebSearch aggressively. Run at least 8–12 searches to cover:

- Company name + "funding" / "valuation" / "Series [A/B/C/D/E]"
- Company name + "revenue" / "ARR" / "customers"
- Company name + "CEO" / "founders" / "leadership"
- Company name + "competitors" / "market"
- Company name + "IPO" / "acquisition" / "exit"
- Company name + recent year (e.g., "2025" or "2026") for fresh coverage
- Industry/sector searches for competitive context

Prioritize these source types (in order of reliability):

1. Company press releases, official blog posts
2. SEC filings, regulatory documents
3. Investor press releases (from lead investors)
4. Reputable business media (WSJ, Bloomberg, Reuters, FT, The Information, TechCrunch)
5. Credible private-market databases (PitchBook, Crunchbase, CB Insights references)
6. Founder/CEO interviews and conference presentations
7. Industry analyst reports

Fetch the most promising URLs to get detailed data. Don't stop at search snippets when a full article would give you funding round details, revenue figures, or management bios.

## Sourcing Rules

These matter because investors make decisions based on this information:

- **Hyperlink every important claim.** Valuation, funding amounts, revenue, headcount, customer counts, investor names — all need a source link.
- **Distinguish confidence levels.** Use these labels consistently:
  - **Confirmed** — from the company itself, SEC filings, or official investor announcements
  - **Reported** — from reputable media citing named sources
  - **Estimated** — from analysts, databases, or unnamed sources
  - **Rumored** — from unverified reports, speculation, or single unnamed sources
- **Mark gaps honestly.** Write "Not disclosed" when data isn't available. Investors respect honesty about gaps far more than they respect fabricated numbers.
- **Include source dates.** A revenue figure from 2023 means something very different from one from 2025. Always note the time period.
- **Prefer recent sources.** Prioritize the last 24 months, but include older sources when they're the best (or only) available data on a topic. Note the date so the reader can judge currency.

## Output Format

Save as a `.md` file to the outputs directory. Name it `[company-name]-tear-sheet.md` (lowercase, hyphens).

The tear sheet follows this exact 11-section structure:

---

### Template

```markdown
# [Company Name] — Investor Tear Sheet

*Generated: [today's date]*
*Sources current as of: [date of most recent source cited]*

---

## 1. Company Snapshot

| Field | Detail |
|-------|--------|
| **Company** | [Full legal name] |
| **Website** | [URL] |
| **Headquarters** | [City, State/Country] |
| **Founded** | [Year] |
| **Founder(s)** | [Names] |
| **CEO** | [Name] |
| **Status** | [e.g., Private, Pre-IPO, Acquired] |
| **Most Recent Valuation** | [Amount, date, confidence level] |
| **Total Funding** | [Amount] |
| **Major Investors** | [Names] |

**Company Description:** [One paragraph — what the company does, who it serves, and why it matters. Keep it to 3–4 sentences.]

**Core Customer Segments:** [Bullet list of primary buyer personas or segments]

---

## 2. Business Description

- **Problem:** [What pain point or gap the company addresses]
- **Buyer/User:** [Who purchases and who uses the product — these may differ]
- **Why It Matters:** [The "so what" — why this problem is worth solving at scale]
- **Value Chain Position:** [Where the company sits — infrastructure, platform, application, services]
- **Differentiation:** [What makes this company defensible or hard to replicate]

---

## 3. Funding and Valuation History

| Date | Round | Amount Raised | Reported Valuation | Lead Investor(s) | Other Notable Investors | Source |
|------|-------|---------------|--------------------|--------------------|--------------------------|--------|
| [Date] | [Series X] | [$XXM] | [$X.XB] | [Name] | [Names] | [Link] |

**Summary:**
- Total funding raised: $[X]
- Most recent valuation: $[X] ([date], [confidence level])
- Valuation trajectory: [Up/flat/down rounds, any recaps]
- Secondary market activity: [Any known secondary sales, pricing if available]
- IPO/exit rumors: [Any credible reporting]

---

## 4. Revenue, Profitability, and Operating Metrics

| Metric | Reported Value | Time Period | Source | Confidence |
|--------|---------------|-------------|--------|------------|
| Revenue / ARR | | | | |
| Revenue Growth (YoY) | | | | |
| GMV (if applicable) | | | | |
| Gross Margin | | | | |
| EBITDA / Net Income | | | | |
| Customer Count | | | | |
| Enterprise Customer Count | | | | |
| User Count | | | | |
| Net Revenue Retention | | | | |
| Churn | | | | |
| Headcount | | | | |

Use "Not disclosed" for any metric without a credible source. Do not estimate revenue from valuation multiples unless clearly labeled as an estimate with the methodology shown.

---

## 5. Management Team

| Name | Role | Prior Experience | Investor-Relevant Notes | Source |
|------|------|-----------------|------------------------|--------|
| [Name] | [Title] | [Key prior roles] | [Board seats, domain expertise, founder status] | [Link] |

Focus on the top 4–6 executives. Prior experience should emphasize roles relevant to investors (prior exits, scaled companies, domain expertise).

---

## 6. Products and Services

| Product | Description | Target Customer | Pricing Model | Source |
|---------|-------------|-----------------|---------------|--------|
| [Name] | [What it does] | [Who buys it] | [SaaS/usage/transaction/etc.] | [Link] |

---

## 7. Business Model

- **Revenue Model:** [How the company makes money — subscriptions, transactions, usage-based, etc.]
- **Pricing Structure:** [Price points if disclosed, tier structure]
- **Sales Motion:** [Self-serve, inside sales, enterprise field sales, channel/partner]
- **Gross Margin Profile:** [What's known or estimated about unit economics]
- **Key Revenue Drivers:** [What levers drive top-line growth]
- **Key Cost Drivers:** [Largest expense categories — R&D, S&M, infrastructure]

---

## 8. Market and Competitive Landscape

**Market Size:** [TAM/SAM if available, with source]

**Industry Tailwinds:** [What macro or sector trends help this company]

**Industry Risks:** [What could slow the market — regulatory, macro, technology shifts]

| Competitor | Public/Private | Description | How It Competes | Relative Strengths | Relative Weaknesses | Source |
|------------|---------------|-------------|-----------------|--------------------|--------------------|--------|
| [Name] | [Public/Private] | [One line] | [Direct/indirect, which segments] | [vs. subject company] | [vs. subject company] | [Link] |

**Substitution Risks:** [What alternatives exist outside direct competitors — incumbents, DIY, status quo]

**Regulatory Risks:** [Any pending or potential regulation that could affect the business]

---

## 9. Investor Perspective

**Bull Case:**
[3–4 sentences on why an investor would be excited]

**Bear Case:**
[3–4 sentences on the key risks and concerns]

**Key Diligence Questions:**
1. [Question an investor should ask management]
2. [Question]
3. [Question]
4. [Question]
5. [Question]

**Potential Exit Paths:** [IPO, strategic acquisition, private equity buyout — what's most likely and why]

**Valuation Justification:** [What would need to be true — in terms of revenue, growth, market share — to justify the latest valuation]

---

## 10. Five Recent Investor-Relevant Articles

| # | Title | Publisher | Date | Link | Summary | Why It Matters |
|---|-------|-----------|------|------|---------|----------------|
| 1 | [Title] | [Publisher] | [Date] | [URL] | [One sentence] | [Investor relevance] |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |

Prefer articles from the last 12 months. If fewer than five recent articles exist, include the best older ones and note the age.

---

## 11. Source Quality and Confidence Assessment

- **Well-Sourced Claims:** [Which sections have strong, primary-source backing]
- **Uncertain Claims:** [Which data points rely on single sources, unnamed sources, or estimates]
- **Unavailable Data:** [What information could not be found — and whether that absence is notable]
- **Contradictions:** [Any cases where sources disagreed, and how you resolved it]
- **Recommended Follow-Up:** [Specific diligence steps an investor should take — e.g., "request audited financials," "verify customer count via reference calls"]
```

---

## Quality Checklist

Before delivering the tear sheet, verify:

- Every section is present (all 11). If a section has no data, include it with "Not disclosed" rather than omitting it.
- Valuation, funding, and revenue claims all have hyperlinked sources.
- Confidence labels (Confirmed / Reported / Estimated / Rumored) are used for key financial claims.
- Tables are well-formed markdown that will render cleanly.
- The document reads in 5–7 minutes — cut ruthlessly if it's running long. Investors skim; density beats length.
- No invented facts. If you're uncertain about something, say so. The reader is making investment decisions.

## Edge Cases

- **Very early-stage companies** (seed/Series A): Many sections will be thin. That's fine — use "Not disclosed" liberally and focus on what's available (founders, product, early traction, investors).
- **Companies with minimal press coverage**: Note the coverage gap in Section 11. Lean harder on Crunchbase/PitchBook references, company website, and LinkedIn for management data.
- **Recently acquired companies**: Note the acquisition in the Company Snapshot. Still complete the full tear sheet — the historical data is useful context.
- **Companies with conflicting data**: Present both figures with their sources and flag the contradiction in Section 11.
