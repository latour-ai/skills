---
name: public-co-unit-economics
description: >
  Create a public-source unit economics memo for a US-listed public company, focused on
  understanding how the business actually makes money using only web-accessible filings and
  disclosures. Use this skill whenever the user wants to understand a public company's
  business model, economic engine, revenue build, or "unit economics" — e.g. "how does
  [company/ticker] make money", "what's the unit economics of [ticker]", "break down
  [company]'s business model", "what drives revenue/margin for [ticker]", "build me a unit
  economics memo", "what's the right unit of analysis for [company]", or pastes/links an
  investor presentation, earnings release, or 10-Q and wants the model explained. Trigger
  even when the user only gives a ticker plus a model question. Produces a neutral, sourced,
  two-page HTML memo — NOT a full financial model or an investment recommendation. For private
  companies, ask for a public ticker instead.
---

# Public Company Unit Economics Memo

Create a concise, HTML-formatted unit economics memo for the public company the user specifies (a company name or ticker, optionally with a segment, investor-presentation URL, earnings-transcript URL, or the current browser page).

This skill is designed for a public equity analyst who wants to understand how a business makes money using only public sources. The goal is not to build a full financial model or produce an investment recommendation. The goal is to identify the best available unit of analysis, explain the company's economic engine, and clearly flag what public disclosure does not reveal.

## Available Sources

Use only public, web-accessible sources, including:

* SEC filings: 10-K, 10-Q, 8-K, S-1 if relevant
* Company investor relations pages
* Earnings releases
* Earnings call transcripts
* Investor presentations
* Shareholder letters
* Press releases
* Public company websites
* Current browser page, if available through a Chrome extension or browsing context

Do not assume access to proprietary datasets, paid terminals, private databases, Daloopa, FactSet, Bloomberg, CapIQ, PitchBook, Tegus, AlphaSense, visible APIs, or local files unless the user explicitly provides them.

## Core Standard

Do not fabricate missing unit metrics.

If the company does not disclose a clean unit-level KPI, say so directly and use the highest-confidence public proxy. If no useful proxy exists, shorten the relevant section instead of padding the memo.

Every numerical claim and every company-specific business model claim must be sourced. If a claim is an inference, label it clearly as an inference.

## Scope

Analyze public companies only.

If the user provides a private company, explain that this skill is designed for public companies and ask for a public ticker or company with public filings.

## Default Time Period

Use the latest reported quarter and the same quarter from the prior year.

Example:

* Latest quarter: Q3 FY2026
* Prior-year comparison: Q3 FY2025

If the company reports semiannually or annually, adapt to the latest available comparable period and explain the limitation.

## Step 1: Identify the Company and Relevant Sources

Determine:

* Company name
* Ticker
* Exchange, if available
* Latest reported quarter
* Fiscal year convention
* Whether the user specified a segment or business line

Prioritize sources in this order:

1. Latest quarterly earnings release or shareholder letter
2. Latest 10-Q
3. Prior-year comparable 10-Q
4. Latest 10-K
5. Latest investor presentation
6. Earnings transcript, if useful for management commentary

Capture source URLs for citation in the HTML memo.

## Step 2: Classify the Business Archetype

Identify the company's primary business model. Use the simplest useful archetype. If the company is multi-segment, focus on the largest or most analytically relevant segment unless the user specified a segment.

Use these archetypes as guides, not rigid categories:

| Archetype                          |                               Likely Unit | Common Public Metrics                                                       |
| ---------------------------------- | ----------------------------------------: | --------------------------------------------------------------------------- |
| SaaS / subscription software       |                  Customer or subscription | ARR, revenue, customers, net retention, gross margin, operating margin      |
| Marketplace / transaction platform | Transaction, order, booking or GMV dollar | GMV, bookings, orders, take rate, active users, gross margin                |
| Consumer subscription              |                                Subscriber | Subscribers, ARPU, churn, content cost, gross margin                        |
| Retail / restaurant / unit rollout |                         Store or location | Store count, same-store sales, AUV, store-level margin, openings            |
| Hardware / manufacturing           |                              Unit shipped | Units, ASP, revenue, gross margin, cost of goods sold                       |
| Digital advertising / platform     |                        User or impression | MAU, DAU, ARPU, ad impressions, engagement, revenue per user               |
| Travel / lodging / transport       |             Room night, seat mile or trip | RevPAR, occupancy, ADR, trips, utilization                                  |
| Asset manager / alternatives       |                             Dollar of AUM | AUM, fee rate, management fees, FRE, performance fees, flows, margin        |
| General industrial / diversified   |            Segment revenue or output unit | Revenue by segment, volume, price/mix, margin, backlog                      |
| No clean unit disclosed            |                      Best available proxy | Segment revenue, gross margin, operating leverage, disclosed operating KPIs |

For asset managers and alternative asset managers, treat AUM and fee-related earnings as first-class unit economics. Useful decomposition may include:

* AUM
* Fee-earning AUM
* Management fee revenue
* Implied fee rate
* Fee-related earnings
* FRE margin
* Performance fees
* Net flows
* Deployment and realizations, if disclosed

Do not force a SaaS-style or marketplace-style framework onto an asset manager.

## Step 3: Define the Unit

Write a clear unit definition:

* What is the "unit"?
* Why is this the best available unit?
* Is the unit directly disclosed or inferred?
* What revenue formula best approximates the business?

Examples:

* SaaS: customers × revenue per customer
* Marketplace: GMV × take rate
* Restaurant: stores × average unit volume
* Asset manager: fee-earning AUM × management fee rate
* Bank-like or lending-adjacent business: earning assets × spread, if relevant
* Diversified company: segment revenue × segment margin

If no clean unit exists, state:

> The company does not disclose a clean unit-level KPI. This memo uses [proxy] as the highest-confidence public proxy because [reason].

## Step 4: Gather the Latest Quarter and Prior-Year Comparison

Create a compact table comparing the latest quarter to the same quarter in the prior year.

Include only metrics that are actually disclosed or can be calculated from disclosed figures.

Preferred metrics:

* Revenue
* Gross profit or gross margin
* Operating income or operating margin
* Segment revenue, if relevant
* Key operating unit metric
* Revenue per unit or implied rate, if defensible
* Asset manager metrics, if applicable: AUM, fee-earning AUM, management fees, FRE, FRE margin, performance fees, net flows

For every calculated metric:

* Label it as calculated
* Show the formula in plain English
* Use only sourced inputs

Do not estimate CAC, LTV, churn, take rate, revenue per user, unit margin or contribution margin unless the company discloses enough information to support the calculation.

## Step 5: Explain the Business Model

Write this section for a smart public equity analyst who is trying to quickly understand the company.

Cover:

* What the company sells
* Who pays
* What the customer or economic buyer is
* How pricing works, if disclosed
* What drives revenue growth: volume, price, mix, retention, AUM, utilization or transaction activity
* What drives margin: scale, gross margin, mix, fixed-cost absorption, credit, content costs, compensation, distribution or other relevant costs

Avoid generic language. Tie each point to the company's actual disclosures.

## Step 6: Explain the Unit Economics

Use the best available data to answer:

* What is the best unit of analysis?
* Is revenue growth being driven more by volume, price/rate, mix or scale?
* Are margins improving, stable or deteriorating?
* What does the latest quarter suggest about the economic engine?
* What cannot be known from public disclosure?

Stay neutral. Do not say "buy," "sell," "cheap," "expensive," "attractive" or "unattractive" unless the user explicitly asks for an investment view.

Use language like:

* "The disclosed data suggests…"
* "The best public proxy is…"
* "The company does not disclose enough information to determine…"
* "The key analytical question is…"
* "The main driver to monitor is…"

## Step 7: Produce a Two-Page HTML Memo

Generate a standalone HTML document.

Requirements:

* HTML only
* Inline CSS
* Print-friendly
* No charts
* No external images
* No JavaScript
* Tables are allowed
* Keep the memo approximately two printed pages
* Include source links as footnotes or inline links
* Use clear analyst-style headings
* Use concise prose
* Avoid generic filler

If the environment allows file creation, save the memo as:

`reports/{TICKER}_public_unit_economics.html`

If file creation is not available, return the full HTML in the response.

## Required HTML Structure

Use this structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{Company Name} ({Ticker}) — Public-Source Unit Economics Memo</title>
  <style>
    body {
      font-family: Arial, Helvetica, sans-serif;
      color: #111;
      line-height: 1.45;
      max-width: 900px;
      margin: 40px auto;
      padding: 0 32px;
      background: #fff;
    }
    h1 {
      font-size: 26px;
      margin-bottom: 4px;
    }
    h2 {
      font-size: 18px;
      margin-top: 28px;
      border-bottom: 1px solid #ddd;
      padding-bottom: 4px;
    }
    h3 {
      font-size: 15px;
      margin-top: 18px;
    }
    .meta {
      color: #555;
      font-size: 13px;
      margin-bottom: 24px;
    }
    .summary-box {
      border: 1px solid #ddd;
      background: #fafafa;
      padding: 14px 16px;
      margin: 18px 0;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 14px 0 20px;
      font-size: 13px;
    }
    th, td {
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
      vertical-align: top;
    }
    th {
      background: #f3f3f3;
    }
    .note {
      color: #555;
      font-size: 13px;
    }
    .sources {
      font-size: 12px;
      color: #444;
    }
    @media print {
      body {
        margin: 20px auto;
        padding: 0 24px;
      }
      h2 {
        page-break-after: avoid;
      }
      table {
        page-break-inside: avoid;
      }
    }
  </style>
</head>
<body>

<h1>{Company Name} ({Ticker}) — Public-Source Unit Economics Memo</h1>
<div class="meta">
  Generated: {date} | Period analyzed: {latest quarter} vs. {prior-year quarter}
</div>

<div class="summary-box">
  <strong>Executive summary:</strong>
  {3-5 sentences. Explain what the company does, the best available unit of analysis, the key public-data limitation and the most important neutral takeaway.}
</div>

<h2>1. Business Model</h2>
<p>{Explain what the company sells, who pays, how revenue is generated and what drives the model.}</p>

<h2>2. Unit Definition</h2>
<table>
  <tr>
    <th>Item</th>
    <th>Assessment</th>
  </tr>
  <tr>
    <td>Business archetype</td>
    <td>{Archetype}</td>
  </tr>
  <tr>
    <td>Best available unit</td>
    <td>{Unit or proxy}</td>
  </tr>
  <tr>
    <td>Revenue build</td>
    <td>{Formula-style explanation, e.g. fee-earning AUM × fee rate}</td>
  </tr>
  <tr>
    <td>Disclosure quality</td>
    <td>{Strong / moderate / limited, with explanation}</td>
  </tr>
</table>

<h2>3. Latest Quarter vs. Prior Year</h2>
<table>
  <tr>
    <th>Metric</th>
    <th>{Latest quarter}</th>
    <th>{Prior-year quarter}</th>
    <th>Change</th>
    <th>Why it matters</th>
  </tr>
  {Rows for disclosed and defensibly calculated metrics only}
</table>

<p class="note">
  Calculated metrics are labeled and use only disclosed inputs. Missing metrics are not estimated.
</p>

<h2>4. Unit Economics Interpretation</h2>
<p>{Explain what the available unit metrics suggest. Discuss volume, price/rate, mix, utilization, margin or AUM dynamics as relevant. Stay neutral.}</p>

<h2>5. What Public Disclosure Does Not Tell You</h2>
<ul>
  <li>{Missing KPI or analytical limitation}</li>
  <li>{Missing KPI or analytical limitation}</li>
  <li>{Missing KPI or analytical limitation}</li>
</ul>

<h2>6. Analyst Takeaways</h2>
<ul>
  <li>{Neutral takeaway about the business model}</li>
  <li>{Neutral takeaway about what changed year over year}</li>
  <li>{Neutral takeaway about what to monitor next}</li>
</ul>

<h2>Sources</h2>
<ol class="sources">
  <li><a href="{source_url}">{Source title}</a></li>
  <li><a href="{source_url}">{Source title}</a></li>
  <li><a href="{source_url}">{Source title}</a></li>
</ol>

</body>
</html>
```

## Analytical Standards

Follow these standards:

1. Use public sources only.
2. Source every numerical claim.
3. Source every company-specific business model claim.
4. Label all calculated metrics.
5. Do not fabricate missing KPIs.
6. Do not pad with generic filler.
7. Prefer plain English over jargon.
8. Keep the memo neutral.
9. Keep the memo to approximately two printed pages.
10. Produce HTML as the final deliverable.

## Final Response to User

After creating the memo, briefly tell the user:

* Which company was analyzed
* Which latest quarter was used
* What the best available unit was
* Where the HTML file was saved, if applicable
* Any major disclosure limitation

Do not include an investment recommendation unless explicitly requested.
