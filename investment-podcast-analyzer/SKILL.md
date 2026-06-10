---
name: investment-podcast-analyzer
description: Turn an investment podcast episode into a skimmable, citation-backed HTML investment brief for allocators, fund-of-funds analysts, family office CIOs, OCIO analysts, and other investment professionals. Use whenever the user provides a podcast link (YouTube, Spotify, Apple Podcasts, or other public source) or transcript and wants it analyzed through an investing lens — e.g. "analyze this podcast", "break down this episode", "what companies/theses were discussed", "pull the investment ideas from this episode", "turn this episode into a brief", or pastes a podcast URL with a company/ticker/sector/theme focus. Trigger even when the user just drops a podcast URL and asks what was said about investing. Extracts public and private companies, bullish/bearish theses with speaker attribution, explicit metrics, and themes. Produces a neutral, sourced HTML report — NOT a buy/sell recommendation. Do NOT use for earnings-call transcripts (use earnings-call-extractor) or generic non-investment podcasts.
---

# Investment Podcast Analyzer

Turn an investment podcast episode into a skimmable, citation-backed HTML investment brief. The user is an allocator, fund-of-funds analyst, family office CIO, OCIO analyst, or other investment professional who listens to podcasts for idea discovery, manager insight, thematic research, and company-level thesis extraction.

The job is to analyze the episode through an investing lens: identify every public and private company discussed, extract bullish/bearish theses, attribute every claim to guest or host, capture explicit metrics, and organize the output so the user can skim companies and themes in under five minutes.

This skill does **not** give buy/sell recommendations and does **not** add model-generated investment advice. The output helps the user understand what was said, why it matters, and what to research next.

## Accepted Inputs

The user may provide any of:

* YouTube URL
* Spotify podcast URL
* Apple Podcasts URL
* A podcast episode URL from another public source
* An optional transcript (pasted or uploaded)
* An optional company, ticker, sector, or theme focus

If a focus is provided (e.g. "focus on the semiconductor names"), prioritize those entities in the analysis but still index everything material.

## Step 1: Get a Usable Transcript

Follow this order. The goal is a real transcript of what was actually said — never hallucinate podcast content from show notes alone.

1. If the user provides a transcript, use it as the primary source.
2. If the user provides a YouTube URL or ID and code execution is available, run the bundled extraction script first:

   ```bash
   pip install youtube-transcript-api --break-system-packages -q   # yt-dlp optional, improves reliability
   python scripts/fetch_youtube_transcript.py "<url-or-id>"          # add --json for structured output
   ```

   The script tries the caption API, then yt-dlp, and prints a timestamped transcript on success. If it exits non-zero with a line beginning `FALLBACK:`, read that line and act on it:
   * `network-blocked` / `access-blocked` — the environment firewalls YouTube (common in the hosted sandbox) or YouTube is throttling. **Do not re-run the script.** Go straight to step 3.
   * `no-transcript` — captions are disabled or the video is restricted. Go to step 3.

   Disclose the exact track the script reports (manual / auto-generated / translated) as the transcript source.
3. If the script is unavailable or returned `FALLBACK`, or the user gave a Spotify / Apple Podcasts / other URL, search the public web for: the episode page, a published transcript (publisher Substack/blog/show notes often post the full transcript), a re-uploaded video version, and the publisher's show notes. A publisher-posted transcript is the most authoritative fallback — fetch it and use it as the primary source.
4. If no usable transcript or video version is found, tell the user verbatim:

   > I could not find a usable transcript or YouTube version for this episode. Please submit a YouTube link or transcript.

   Then stop — do not generate a report from show notes alone.

**Always disclose the transcript source used** in the report. If the transcript is partial or low quality, say so.

## Step 2: Public Web Research (supplement only)

Use public web research to supplement — never to invent podcast claims. Podcast claims must come from the transcript. Use the web for:

* Guest bio (current role, firm, strategy, fund, prior experience, area of expertise)
* Host / podcast context when relevant
* Company ticker identification when obvious
* Basic company validation
* Public vs. private company status

Do not use web research to put words in a speaker's mouth.

## Step 3: Build the Guest Bio (investing lens)

Write a concise bio using two inputs: how the guest describes themselves in the episode, and publicly available information from the web. Frame it through an investing lens — focus on current role, firm/company, strategy or asset class, prior relevant experience, why their perspective matters, and any incentives, biases, or context that may shape their views (e.g. they run a long book in the names they're discussing).

## Step 4: Extract Entities

Identify:

* Public companies
* Private companies
* Parent companies and subsidiaries when relevant
* Funds, managers, platforms, or assets — only when important to the investment thesis

For public companies, include ticker and exchange **only when obvious or easily verifiable**. If uncertain, write `Ticker unclear`. Do not force ticker mapping for ambiguous company names.

Do not summarize every casual mention. Focus on investment-relevant mentions.

## Step 5: Extract and Classify Theses

For each company, extract the guest's or host's thesis and classify it:

* **Bullish**
* **Bearish**
* **Mixed** — sounds bullish but includes meaningful risk, or vice versa
* **Undefined** — mentioned factually, no clear directional view

A thesis can be bullish or bearish even without the words "buy," "sell," "long," or "short." Infer the label from the substance — but label the inference clearly as an inference.

## Step 6: Attribution Standard

Every material claim must be attributed. For each thesis or major point capture:

* Speaker: guest or host
* Speaker name when available
* Timestamp when available
* Short supporting quote or paraphrase (keep quotes brief)
* Bullish / Bearish / Mixed / Undefined label
* Why the label was assigned

Never attribute a claim to the guest if it was made by the host. If attribution is unclear, write `Speaker unclear`.

## Step 7: Extract Metrics

Always call out explicit metrics shared in the episode. Examples: revenue growth, same-store sales, gross/EBITDA margin, free cash flow, unit economics, TAM, market share, customer count, churn, retention, CAC, LTV, valuation, multiples, price targets, production volumes, capacity, backlog, guidance, IRR/MOIC, fund returns.

Rules:

* Only extract metrics **explicitly stated** in the podcast/transcript.
* Do not calculate new metrics unless the math is simple and clearly shown.
* If a metric sounds important but is vague, flag it as qualitative rather than inventing a number.

## Step 8: Apply Investment Framing

For each company, think about what matters to an investor: What is the company? What is the thesis? What is the variant perception? What is the key debate? What metric supports or weakens the thesis? What is the time horizon if implied? What would need to be diligenced? What could prove the thesis wrong?

Do not give buy/sell recommendations. Do not add model-generated investment advice.

## Step 9: Produce the HTML Report

Generate a standalone, print-friendly HTML report using the template in `assets/report_template.html`. Read that file, then fill every `{placeholder}` with extracted content and remove any sections that genuinely have no content (rather than padding them).

Requirements:

* HTML only, inline CSS, print-friendly, no JavaScript, no external images. Tables encouraged.
* Easy to skim in under five minutes.
* Analyst tone: precise, neutral, skeptical, useful.

If file creation is available, save to:

`reports/{podcast_slug}_{episode_slug}_brief.html`

If file creation is not available, return the full HTML in the response.

### Report sections (in order)

1. **Episode Snapshot** — podcast name, episode title, episode URL, platform, episode date (if available), transcript source used, host name, guest name, guest firm/affiliation, one-sentence episode summary.
2. **Guest Bio and Investing Context** — self-description from the episode, public bio summary, current role, prior relevant experience, investment style/sector/strategic lens, why this view may matter, potential bias or incentive context.
3. **Top Investment Themes** — a table of 5–10 themes phrased the way an investor would phrase them. Columns: Theme | Companies mentioned | Directional tone | Why it matters | Best supporting quote or timestamp. (Example phrasings: "AI infrastructure demand is pulling forward data center capex"; "Luxury weakness is spreading from aspirational to higher-end buyers"; "Private credit remains attractive but underwriting dispersion is widening".)
4. **Company Index** — a table of every company discussed. Columns: Company | Public/Private | Ticker (if obvious) | Sector | Speaker | Thesis label | Main theme | Metrics mentioned | Diligence priority (High/Medium/Low). Diligence priority reflects how much investment-relevant substance appeared — not whether the company is attractive.
5. **Company-by-Company Analysis** — for each company: status, ticker (if obvious), sector, speaker(s), thesis label, main theme; a "What was said" paragraph in plain English; a supporting-evidence table (Speaker | Timestamp | Quote or paraphrase | Label | Reason for classification); a metrics table (Metric | Value | Period | Speaker | Timestamp | Why it matters), or the line "No explicit company-level metrics were mentioned." if none; an "Investment interpretation" paragraph (business quality, growth, margins, competition, valuation, market structure, capital intensity, cyclicality, unit economics, or management quality); and 3–7 open diligence questions.
6. **Cross-Company Takeaways** — most important bullish signal, most important bearish signal, most important metric mentioned, most interesting private company, most actionable public-company research lead, biggest unresolved question.
7. **Source Notes** — podcast URL, transcript source, public sources used for guest bio, public sources used for company/ticker validation.

## Quality Rules

* Be concise but complete.
* **Paraphrase first.** The transcript is a single copyrighted source, so the default in every "supporting evidence" cell is a paraphrase plus a timestamp — not a verbatim quote. Reserve direct quotation for a small number of meaning-critical phrases across the whole report, each kept short (well under 15 words) and clearly attributed. Never reconstruct large stretches of the episode through stacked quotes.
* Do not fabricate metrics, tickers, timestamps, or quotes.
* If the transcript is incomplete, say so.
* If a company mention is ambiguous, flag the ambiguity.
* If a thesis is unclear, use `Undefined`. If it cuts both ways, use `Mixed`.
* Analyst tone throughout: precise, neutral, skeptical, useful.

## Final Response to User

After creating the report, briefly tell the user: which episode was analyzed, the transcript source used, the number of companies indexed and how many carry a directional thesis, the single most actionable research lead, and where the HTML file was saved (if applicable). Do not include an investment recommendation unless explicitly requested.
