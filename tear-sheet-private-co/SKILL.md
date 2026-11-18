---
name: tear-sheet-private-co
description: >-
  Generate an investor-grade tear sheet on a venture-backed private company:
  a structured, sourced markdown brief covering company snapshot, business
  model, funding history, operating metrics, management, competitive
  landscape, and investor perspective, with every key claim labeled
  Confirmed, Reported, Estimated or Rumored. Researches from a connected
  private-market data source (PitchBook, S&P Capital IQ, Preqin, AlphaSense
  or similar) where there is one, plus public filings and the open web, plus
  anything the user attaches. For venture, growth, crossover and private
  equity investors screening a deal, monitoring a portfolio or preparing for
  a meeting. Trigger on "tear sheet", "company overview", "company profile",
  "investor brief", "private company analysis", "pull up a tear sheet on
  [company]", "research [company] for me", "what do we know about
  [company]", "give me the rundown on [company]", "diligence [company]", or
  when the user names a startup or venture-backed company and asks for a
  summary or overview in an investment context. Do NOT use for a listed
  company; use the public-company-first-pass skill. Do NOT use to map all
  the players in a sector; use the market-map-builder skill. Do NOT use for
  a brief on a person; use the professional-profile-brief or
  principal-background-brief skill. Do NOT use for simple news lookups.
license: MIT
metadata:
  author: latourai
  version: '2.0'
---

# Private Company Tear Sheet Generator

Produce an investor-grade tear sheet on a venture-backed private company. The output reads like something a buyside research analyst would hand to a portfolio manager: concise, fact-dense, well-sourced, and honest about what's confirmed vs. rumored.

## Why This Skill Exists

Investment professionals constantly need quick, structured overviews of private companies — for deal screening, portfolio monitoring, competitive mapping, or meeting prep. The challenge with private companies is that data is scattered, often unconfirmed, and mixes hard numbers with speculation. This skill enforces a consistent structure and sourcing discipline so the reader always knows what's solid and what's soft.

## How It Works

1. The user provides a company name (and optionally context like "pre-IPO" or "Series C stage", or material of their own: a deck, a data-room export, notes from a call).
2. Research the company in whatever sources are available (see Research Phase).
3. Produce a structured markdown tear sheet, saved as a file and shared with the user.

If the name could refer to more than one company, ask which. Otherwise proceed without questions and state any assumption (for example, which entity or which round is the latest) at the top of the tear sheet.

## Research Phase

Use every source that is available, and say in Section 11 which ones were used:

- **A connected private-market or company data source** (PitchBook, S&P Capital IQ, Preqin, AlphaSense or similar), if there is one: funding rounds, investors, valuations, headcount, executives. Cite it by name with the as-of date of the record.
- **Public filings and the open web**, always. Database records lag and are often estimates, so check them against primary sources.
- **Material the user attaches or pastes**, or files in connected storage (SharePoint / OneDrive, Google Drive, Box, Dropbox, a local folder) when the user names where they are. Label it "Provided by user" and keep confidential figures out of any search query.

If a data source is not connected or fails, carry on with the web and attached material, and note in Section 11 that the tear sheet was built without it.

On the web, search broadly. A thorough pass usually takes eight to twelve searches covering:

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

- **Hyperlink every important claim.** Valuation, funding amounts, revenue, headcount, customer counts, investor names — all need a source link. Where the source is a connected database or a user-provided document with no public link, name it and give its date.
- **Distinguish confidence levels.** Use these labels consistently:
  - **Confirmed** — from the company itself, SEC filings, or official investor announcements
  - **Reported** — from reputable media citing named sources
  - **Estimated** — from analysts, databases, or unnamed sources
  - **Rumored** — from unverified reports, speculation, or single unnamed sources
- **Mark gaps honestly.** Write "Not disclosed" when data isn't available. Investors respect honesty about gaps far more than they respect fabricated numbers.
- **Include source dates.** A revenue figure from 2023 means something very different from one from 2025. Always note the time period.
- **Prefer recent sources.** Prioritize the last 24 months, but include older sources when they're the best (or only) available data on a topic. Note the date so the reader can judge currency.

## Output Format

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

Save as a `.md` file named `[company-name]-tear-sheet.md` (lowercase, hyphens).

The tear sheet follows the 11-section structure below. Keep all 11 sections: where a section has no data, write "Not disclosed" in it, because the absence is itself information for an investor. The whole document should read in five to seven minutes, so prefer density to length and cut anything that does not help the reader judge the company.

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

## Edge Cases

- **Very early-stage companies** (seed/Series A): Many sections will be thin. That's fine — use "Not disclosed" liberally and focus on what's available (founders, product, early traction, investors).
- **Companies with minimal press coverage**: Note the coverage gap in Section 11. Lean harder on private-market database records, the company website, and LinkedIn for management data.
- **Recently acquired companies**: Note the acquisition in the Company Snapshot. Still complete the full tear sheet — the historical data is useful context.
- **Companies with conflicting data**: Present both figures with their sources and flag the contradiction in Section 11.
