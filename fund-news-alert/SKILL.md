---
name: fund-news-alert
description: >-
  Monitor a standing watchlist of hedge funds for recent, diligence-relevant
  public news and produce an email-ready alert summary. The lens is
  risk-first, not general news aggregation: negative news, performance moves,
  personnel changes, fundraising shifts and credible chatter from the last 7
  days, each tagged by relevance, source quality and confidence. The
  watchlist, the recipient and sign-off, and the delivery (text to paste, or
  a draft in Outlook or Gmail that is never sent) are chosen once in a short
  first-run setup. For allocators, fund-of-funds analysts, OCIOs, family
  offices, and investment teams overseeing external managers. Trigger on
  "any news on my funds?", "did anything happen with [fund]?", "run the fund
  alerts", "run the alerts", "weekly manager monitoring", "check my
  watchlist", "anything diligence-relevant this week", "set up
  fund-news-alert", "change my fund-news-alert settings", or when the user
  names a fund and asks what's new. Do NOT use for a first-pass diligence
  note on a manager; use the hedge-fund-diligence skill. Do NOT use for a
  background review of a fund's principals; use the
  principal-background-brief skill. Do NOT use to synthesize managers'
  quarterly letters; use the quarterly-letter-synthesizer skill.
license: MIT
metadata:
  author: latourai
  version: '2.0'
---

# Fund News Alert

A lightweight, risk-first news monitor for allocators and other investment professionals who oversee a list of external hedge fund managers. It reads a simple watchlist of fund names, searches the public web for the last 7 days of diligence-relevant news on each, and returns an email-ready alert summary.

Think of it as a Google News substitute tuned for fund monitoring: the goal is not to aggregate everything written about a fund, but to surface what an allocator would actually care about — risk events, performance moves, personnel changes, fundraising shifts, and credible chatter — and to make it easy to tell the credible from the noise.

## First-run setup (once, then only when asked)

Run setup the first time the skill is used, or when the user says "set up fund-news-alert" or "change my fund-news-alert settings". Look for a saved settings file first (`fund-news-alert-settings.md`, in the project's files or the skill's working folder). If one exists, read it and skip setup.

Setup is one short round of questions, each with a default the user can accept:

1. **Detect before asking.** Check whether a watchlist file already exists and has fund names in it, and which mail system and file storage are connected. Pre-fill what detection settles.
2. **Ask, in one message:**
   - **Watchlist:** where the list of funds lives. The `funds-to-monitor.md` file that ships with the skill (default), a file in connected storage (SharePoint / OneDrive, Google Drive, Box, Dropbox, a local folder), or names pasted now and saved to that file.
   - **Recipient and sign-off:** who the alert is addressed to and whose name closes it. Default: no named recipient, signed by the user.
   - **Delivery:** email-ready text in the chat (default), or a draft in the user's mail system (Microsoft 365 / Outlook, or Google Workspace / Gmail) addressed to the recipients named here. Drafts are never sent.
   - **Search window:** the last 7 days (default), or a longer window if the scan runs less often than weekly.
   - **Emphasis (optional):** categories to weight or drop, or publications the firm wants treated as higher or lower quality. Default: all six categories below, risk-first.
   - **Firm rules (optional):** a required footer or disclaimer, for example "Public sources only; not investment advice."
3. **Save the settings** to `fund-news-alert-settings.md` in plain language the user can edit. If nothing persistent can be written, show the settings as a short block and tell the user to paste it into their project instructions.
4. **Continue straight into the scan** if the user asked for one.

On later runs, read the settings and don't re-ask. Setup never blocks a first run: if the user says "skip setup", or names funds in the request, run with the defaults and say which were used.

## Core job

For each fund in the watchlist:

1. Read the fund name.
2. Infer likely aliases and key principals automatically.
3. Generate explicit web search queries internally.
4. Search the public web for news from inside the search window only (the last 7 days unless the settings say otherwise).
5. Keep only items relevant to allocator diligence.
6. Produce an email-ready summary, organized by relevance then source quality.

The two primary use cases are (a) telling an allocator if anything bad or potentially diligence-relevant happened with monitored managers, and (b) producing a weekly digest of public news on those managers.

## The watchlist

The skill monitors the watchlist named in the settings; by default this is `funds-to-monitor.md`, a simple bulleted list of fund names that the user can edit freely. The file ships with bracketed placeholder lines only, which count as empty. If the watchlist is missing, empty, or can't be reached in connected storage, ask the user which funds to monitor (or to paste the list) rather than guessing.

The user may add or remove fund names at any time, so re-read the watchlist at the start of each run. If the user names funds in the request itself, scan those for this run without changing the saved list.

**Set once in setup:** watchlist location, recipient and sign-off, delivery, search window, emphasis, and any firm rules.

## Aliases and principals

Fund names in the wild are inconsistent — a single firm shows up under several legal and colloquial names, and a lot of the most important news is attached to a founder or key principal rather than the fund itself. Before searching, infer the obvious aliases and principal names so you don't miss coverage that uses a different label.

Infer:

- **Aliases** — common short forms, legal-entity variants, and spacing/punctuation variants. (A watchlist entry of `Northbridge Partners` → also `Northbridge Capital Partners`, `Northbridge`; `R.J. Hale` → `R. J. Hale`, `R.J. Hale Group`, `Hale & Co`.)
- **Founders / key principals** — where obvious and useful. (The founder or CIO whose name the press uses in place of the fund's, plus senior leadership where relevant.)

Only surface inferred aliases or principal names in the output when it actually helps the reader — for example when ambiguity could affect confidence, or when a key alert came in under a founder's name rather than the fund's. Don't clutter a clean summary with disambiguation the reader doesn't need.

If a fund name is genuinely ambiguous (a name shared with an unrelated company, person, or fund), add disambiguating terms to the searches — "hedge fund," "investment firm," "asset manager," the founder's name, or a known alias — and lower confidence on anything you can't cleanly tie to the right entity. Don't attribute an item to a monitored fund unless the source clearly means that fund; a wrong-entity alert is worse than a missed one.

## Search window

The window is the last 7 days from today's date unless the settings say otherwise. Hold to it strictly: the whole value of the digest is that the reader can trust everything in it is recent.

- Exclude articles, posts, filings, summaries, or recycled stories published outside the window.
- If an article is newly published but merely re-reports old news, either exclude it or label it clearly as **recycled/background** and assign low relevance.
- If the publication date is unclear or unverifiable, assign lower confidence — or exclude it if you can't reasonably place it inside the window.

## What to look for

Search across these alert categories. The first one is the priority — this is a risk-first tool.

1. **Negative fund news** — lawsuits, investigations, regulatory actions, fraud allegations, sanctions, reputational issues, redemptions, liquidity stress, fund closures, strategy problems.
2. **Performance news** — major gains or losses, drawdowns, unusual volatility or returns, performance dispersion, notable ranking changes.
3. **Personnel news** — PM departures, senior hires, team lift-outs, founder succession, leadership changes, internal disputes.
4. **Fundraising / product news** — new fund or strategy launches, closures, asset-raising updates, investor demand, capacity constraints.
5. **Portfolio / position news** — only when the article names both the fund and the company or security. Do not infer that the fund currently holds a position unless the source says so or the watchlist explicitly lists it. Include major news about a connected company only when the fund is directly mentioned.
6. **Chatter** — lower-level public commentary from blogs, newsletters, Substack, podcasts, forums, and similar. Include it, but make it visually easy to dismiss, don't overstate it or present speculation as fact, and keep its confidence low unless it's independently corroborated.

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

These queries are working scaffolding. Leave them out of the output unless the user asks to see them.

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

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

Use this structure:

```markdown
Subject: Weekly Fund News Alerts — [Date]

Hi [Recipient from settings, or omit the greeting name],

Here are the notable public news alerts from [search window] for the monitored hedge funds.

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
[Sign-off from settings]

[Footer or disclaimer from settings, if any]
```

If there are only a few alerts, drop the section headers and keep it to a short executive summary plus the handful of items. Use the full structure only when volume justifies it.

**Delivery.** By default the summary is returned in the chat, ready to paste. If the settings ask for a mail draft, create a draft in the user's mail system addressed to the recipients named in setup, and say where it is. The skill never sends the email; the user reviews and sends. If the mail system isn't connected or the draft fails, return the summary as text and say which system was unavailable.

## Style

Write like an allocator briefing a colleague: concise, risk-first, sober, factual, scannable. Be clear about uncertainty. Avoid hype, sensationalism, generic news-summary filler, and overly legalistic phrasing. Curate rather than produce an exhaustive web dump. Don't use investment-recommendation language ("buy," "avoid," "attractive entry"): this is monitoring, not advice.

## Edge cases

- **Quiet fund:** omit it entirely rather than writing a "no news" line.
- **Everything low relevance:** say in the executive summary that the week appears quiet based on the public sources reviewed, with only low-level chatter found.
- **User wants more depth:** provide an appendix listing every included alert with a one-line rationale for its relevance rating.
- **No web search available:** say so and stop. Recent news can't be reported from memory, so don't produce a digest without a live search.

## Example prompts

> "Run the fund alerts."

> "Set up fund-news-alert. The watchlist is 'Manager watchlist.md' in our SharePoint research folder, address the alert to the investment committee, sign it from me, and put it in my Outlook drafts. Add the footer 'Public sources only; not investment advice.'"

> "Did anything happen with Northbridge Capital Partners this week? Just that one, don't change my list."
