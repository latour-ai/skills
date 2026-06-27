---
name: fund-news-alert
description: Monitor a watchlist of hedge funds for recent, diligence-relevant public news and produce an email-ready alert summary. Acts as a lightweight Google News substitute for fund monitoring by allocators, fund-of-funds analysts, OCIOs, family offices, and investment teams overseeing external managers. Use this skill whenever the user wants to check for news on monitored managers, run a weekly fund news scan, asks "any news on my funds?", "did anything happen with [fund]?", "run the fund alerts", "weekly manager monitoring", "check my watchlist", "anything diligence-relevant this week", or maintains a funds-to-monitor list and wants recent risk/performance/personnel/fundraising news surfaced. Trigger even when the user just says "run the alerts" or names a fund and asks what's new, and especially for recurring weekly monitoring digests. The default lens is risk-first, not general news aggregation.
---

# Fund News Alert

A lightweight, risk-first news monitor for allocators and other investment professionals who oversee a list of external hedge fund managers. It reads a simple watchlist of fund names, searches the public web for the last 7 days of diligence-relevant news on each, and returns an email-ready alert summary.

Think of it as a Google News substitute tuned for fund monitoring: the goal is not to aggregate everything written about a fund, but to surface what an allocator would actually care about — risk events, performance moves, personnel changes, fundraising shifts, and credible chatter — and to make it easy to tell the credible from the noise.

## Core job

For each fund in the watchlist:

1. Read the fund name.
2. Infer likely aliases and key principals automatically.
3. Generate explicit web search queries internally.
4. Search the public web for news from the **last 7 days only**.
5. Keep only items relevant to allocator diligence.
6. Produce an email-ready summary, organized by relevance then source quality.

The two primary use cases are (a) telling an allocator if anything bad or potentially diligence-relevant happened with monitored managers, and (b) producing a weekly digest of public news on those managers.

## The watchlist

The skill monitors `funds-to-monitor.md`, a simple bulleted list of fund names that the user can edit freely. Read it first. If the file is missing or empty, ask the user which funds to monitor (or to populate the file) rather than guessing.

The user may add or remove fund names at any time, so always re-read the file at the start of each run. Don't assume the list is the same as last time.

## Aliases and principals

Fund names in the wild are inconsistent — a single firm shows up under several legal and colloquial names, and a lot of the most important news is attached to a founder or key principal rather than the fund itself. Before searching, infer the obvious aliases and principal names so you don't miss coverage that uses a different label.

Infer:

- **Aliases** — common short forms, legal-entity variants, and spacing/punctuation variants. (`Millennium Partners` → also `Millennium Management`, `Millennium`; `Viking Global` → `Viking Global Investors`; `D.E. Shaw` → `D. E. Shaw`, `D.E. Shaw Group`.)
- **Founders / key principals** — where obvious and useful. (`Millennium` → Israel Englander; `Viking Global` → Andreas Halvorsen; `D.E. Shaw` → David Shaw, plus senior leadership where relevant.)

Only surface inferred aliases or principal names in the output when it actually helps the reader — for example when ambiguity could affect confidence, or when a key alert came in under a founder's name rather than the fund's. Don't clutter a clean summary with disambiguation the reader doesn't need.

If a fund name is genuinely ambiguous (a name shared with an unrelated company, person, or fund), add disambiguating terms to the searches — "hedge fund," "investment firm," "asset manager," the founder's name, or a known alias — and lower confidence on anything you can't cleanly tie to the right entity. Never confuse similarly named funds, companies, or managers; a wrong-entity alert is worse than a missed one.

## Search window — be strict

The default window is the **last 7 days** from today's date. (Check today's date if unsure.) Be disciplined about this — the whole value of the digest is that the reader can trust everything in it is recent.

- Exclude articles, posts, filings, summaries, or recycled stories published outside the 7-day window.
- If an article is newly published but merely re-reports old news, either exclude it or label it clearly as **recycled/background** and assign low relevance.
- If the publication date is unclear or unverifiable, assign lower confidence — or exclude it if you can't reasonably place it inside the window.

## What to look for

Search across these alert categories. The first one is the priority — this is a risk-first tool.

1. **Negative fund news** — lawsuits, investigations, regulatory actions, fraud allegations, sanctions, reputational issues, redemptions, liquidity stress, fund closures, strategy problems.
2. **Performance news** — major gains or losses, drawdowns, unusual volatility or returns, performance dispersion, notable ranking changes.
3. **Personnel news** — PM departures, senior hires, team lift-outs, founder succession, leadership changes, internal disputes.
4. **Fundraising / product news** — new fund or strategy launches, closures, asset-raising updates, investor demand, capacity constraints.
5. **Portfolio / position news** — only when the article names **both** the fund and the company/security. Do not infer that the fund currently holds a position unless the source says so or the watchlist explicitly lists it. Include major news about a connected company only when the fund is directly mentioned.
6. **Chatter** — lower-level public commentary from blogs, newsletters, Substack, podcasts, forums, and similar. Include it, but make it visually easy to dismiss, never overstate it, and keep its confidence low unless it's independently corroborated.

## Search queries (internal)

Generate explicit searches per fund. Cover, at minimum:

- fund name + news
- each alias + news
- fund name + lawsuit / investigation / SEC / regulatory
- fund name + performance / returns / drawdown
- fund name + redemption / outflows / capital
- fund name + PM departure / hire / founder / leadership
- fund name + portfolio company / position / stake
- founder name + fund name
- fund name + blog / Substack / newsletter / chatter

Do **not** show these queries in the output. They are working scaffolding. Only reveal the queries if the user explicitly asks to see them.

## Source quality tiers

Tag every item with a tier. Used together with relevance to order the output and to calibrate confidence.

**Tier 1 — Mainstream / institutional.** Bloomberg, Reuters, WSJ, Financial Times, CNBC, New York Times, Business Insider, Institutional Investor, Pensions & Investments, Hedge Fund Alert, SEC, court filings, regulatory filings.

**Tier 2 — Specialist finance / industry.** Hedgeweek, HFM, Alternatives Watch, ValueWalk, PitchBook, Preqin, industry newsletters, fund-database summaries, reputable trade publications.

**Tier 3 — Chatter / blogs.** Substack, independent blogs, podcasts, investor forums, social-media-derived commentary, lightly sourced newsletters. De-emphasize these visually and keep them easy to skip.

## Relevance ranking

Organize output by **relevance first**, then by source quality within each relevance bucket.

- **High** — directly names a monitored fund and relates to risk, performance, personnel, fundraising, regulatory/legal matters, reputation, or a position/company where the fund is explicitly mentioned. Likely to matter to an allocator.
- **Medium** — mentions the fund, founder, senior person, strategy, or a connected company, but the diligence implication is moderate or indirect.
- **Low** — weakly connected items, chatter, recycled news, low-quality sources, or general market/sector commentary. Should be fast to scan and dismiss.

## Confidence

Rate each alert:

- **High** — direct fund mention, Tier 1 source, recent date confirmed, clear relevance.
- **Medium** — credible source but somewhat indirect, or relevant but not fully specific.
- **Low** — chatter, blog, weak source, unclear implication, or you only saw a limited snippet.

## Paywalled sources

Include paywalled items when the headline and snippet are enough to convey relevance. Mark them `Paywalled / snippet only` and don't imply you read the full article when you only saw a snippet.

## Output format

Default output is an **email-ready summary**. Length should scale with the number of meaningful alerts — keep it short when there's little to report, expand when there's a lot.

Use this structure:

```markdown
Subject: Weekly Fund News Alerts — [Date]

Hi [Name],

Here are the notable public news alerts from the last 7 days for the monitored hedge funds.

## Executive Summary

- [1–3 bullets on the most important developments.]
- [Call out if the week was mostly quiet except for low-level chatter.]
- [Call out anything that may warrant follow-up.]

## High Relevance

### [Fund Name] — [Short Alert Headline]

**Why it matters:** [One or two sentences on allocator relevance.]

**Source:** [Publication], [date]
**Source quality:** Tier [1/2/3]
**Confidence:** [High/Medium/Low]
**Link:** [URL]
**Note:** [Optional — paywalled, snippet-only, or ambiguity.]

## Medium Relevance

### [Fund Name] — [Short Alert Headline]

**Why it matters:** [One or two sentences.]

**Source:** [Publication], [date]
**Source quality:** Tier [1/2/3]
**Confidence:** [High/Medium/Low]
**Link:** [URL]

## Low Relevance / Chatter

- **[Fund Name]** — [Short item].
  Source: [Publication/blog], [date]. Confidence: Low.
  Why it is low relevance: [brief reason].

## Suggested Follow-Ups

- [Optional follow-up for a manager call, IC meeting, or ODD check.]
- [Optional reminder to verify a paywalled or snippet-only source.]

Best,
[Sender]
```

If there are only a few alerts, drop the section headers and keep it to a short executive summary plus the handful of items. Use the full structure only when volume justifies it.

## Style

Write like an allocator briefing a colleague: concise, risk-first, sober, factual, scannable. Be clear about uncertainty. Avoid hype, sensationalism, generic news-summary filler, and overly legalistic phrasing. Never use investment-recommendation language ("buy," "avoid," "attractive entry") — this is monitoring, not advice.

## What not to do

- Don't confuse similarly named funds, companies, or managers.
- Don't include stale news outside the 7-day window, or treat old events as new.
- Don't infer a current position unless the source supports it.
- Don't overstate blogs, rumors, or chatter, or present speculation as fact.
- Don't use investment-recommendation language.
- Don't say "no news found." If a fund is quiet, simply omit it.
- Don't produce an exhaustive web dump — curate.
- Don't show the search queries by default.

## Edge cases

- **Quiet fund:** omit it entirely rather than writing a "no news" line.
- **Everything low relevance:** say in the executive summary that the week appears quiet based on the public sources reviewed, with only low-level chatter found.
- **Ambiguous fund name:** add disambiguating terms to searches and lower confidence on anything you can't cleanly attribute.
- **User wants more depth:** provide an appendix listing every included alert with a one-line rationale for its relevance rating.

## Success criteria

A good run lets an allocator paste in a short list of funds, run it once a week, and quickly answer: Did anything risky or diligence-relevant happen? What deserves follow-up? What's credible versus chatter? Is everything actually within the window? What can be ignored?
