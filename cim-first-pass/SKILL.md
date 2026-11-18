---
name: cim-first-pass
description: >-
  Turn a CIM, teaser, or management presentation into a first-pass private
  equity deal screen memo — what the business does, revenue model, customer
  concentration, financial snapshot with page references, what the banker is
  emphasizing vs. avoiding, red flags, fit-vs-mandate checklist, and questions
  for the banker. The fund's mandate and investment criteria are saved once in
  a short first-run setup, so every later screen is judged against them
  without re-asking. For private equity, growth equity, and private credit
  deal teams screening inbound deals. Trigger on "first pass on this CIM",
  "screen this deal", "review this teaser", "what do you think of this CIM",
  "summarize this management deck", "is this deal worth a look", "deal
  screen", "should we pursue this", "set up cim-first-pass", "change my
  cim-first-pass settings", or when the user uploads or pastes a CIM,
  confidential information memorandum, information memorandum, teaser, or
  sell-side management presentation. Do NOT use for public companies — use
  the public-company-first-pass skill. Do NOT use for hedge fund manager
  materials — use the hedge-fund-diligence skill. Do NOT use for drafting the
  full committee memo — use the ic-memo-drafter skill. Do NOT use for checking
  what's in a data room.
license: MIT
metadata:
  author: latourai
  version: '2.0'
---

# CIM First Pass

Turn a CIM, teaser, or management presentation into a deal screen memo a deal team can read in five minutes: what the business actually is, what the numbers in the document actually say, what the banker wants you to focus on, what they're steering you away from, and whether this is worth a partner conversation. The goal is a faster, sharper kill-or-advance decision — not a substitute for diligence.

## Why this skill exists

A mid-market PE associate sees dozens of CIMs a quarter. Most die at first read, but reading a 60-page CIM properly takes two hours, and the document is written by a banker whose job is to make the business look better than it is. The skill that separates good screeners from slow ones is reading *against* the document: noticing what's adjusted, what's omitted, and what the structure of the book itself reveals. This skill does that first read systematically so the human spends their time on judgment, not extraction.

## Inputs

**Required:**
- The CIM, teaser, or management deck. It can be attached, pasted, or pulled from connected file storage (SharePoint / OneDrive, Google Drive, Box, Dropbox) if the user names where it lives.

**Optional but high-value:**
- Deal context: who sent it, process stage, timeline, prior knowledge of the company
- Any specific concerns the user already has
- A mandate for this deal only, if it differs from the saved one (a different fund, a co-invest, an add-on for a platform)

**Set once in setup (step 0):** the fund's mandate (sector focus, EBITDA/revenue range, check size, control vs. minority, geography, hold period), any automatic passes, the firm's screen memo format if it has one, and where memos are saved.

**Missing-input behavior:** If no document is provided, ask once for it — there is nothing to screen without it. If no mandate is saved or supplied, proceed but label the fit section: "Mandate not provided — fit assessed against a generic mid-market buyout profile; replace with your actual criteria." Never guess the user's mandate silently.

## How it works

### 0. First-run setup (once, then only when asked)

Run setup the first time the skill is used, or when the user says "set up cim-first-pass" or "change my cim-first-pass settings". Look for a saved settings file first (`cim-first-pass-settings.md`, in the project's files or the folder where screen memos are saved). If one exists, read it and skip setup.

Setup is one short round of questions, each with a default the user can accept:

1. **Detect before asking.** If the user attached or pointed to an investment criteria document, or one is findable in connected file storage under the name the user gives, read it and pre-fill the mandate for confirmation instead of asking.
2. **Ask, in one message:**
   - **Mandate:** sector focus, EBITDA or revenue range, check size, control vs. minority, geography, hold period. Default if skipped: none saved, and each screen uses the labeled generic profile.
   - **Automatic passes:** anything the fund will not do regardless of quality (for example a customer above a set share of revenue, turnarounds, a regulated sub-sector). "None" is valid.
   - **Memo format:** the built-in format below (default), or the firm's own screen template, which then sets the section order.
   - **Where to save memos:** a folder in connected file storage, a local folder, or "just send them to me" (default).
3. **Save the settings** to `cim-first-pass-settings.md` in plain language the user can edit. If nothing persistent can be written, show the settings as a short block and tell the user to paste it into their project instructions.
4. **Continue straight into the screen** if the user gave a document with the setup request.

On every later run: read the settings and never re-ask. A mandate stated in the request overrides the saved one for that deal only. Setup never blocks a first run: if the user says "skip setup", screen against the generic profile and label it. If the save location isn't reachable, return the memo in the conversation and say so.

### Steps for each document

1. **Read the whole document before writing anything.** Note page numbers as you go — every financial figure and material claim in the memo needs a page reference.
2. **Establish what the business actually does** in plain language, stripped of banker framing. "Tech-enabled services platform" usually means a services business. Identify the real product, who pays, why they pay, and how sticky that payment is.
3. **Map the revenue model:** recurring vs. reoccurring vs. one-time, contract structure, pricing mechanism, customer concentration (top 1/5/10 customers if disclosed — and flag loudly if a sell-side doc *doesn't* disclose concentration).
4. **Build the financial snapshot strictly from figures in the document.** Revenue, gross margin, EBITDA (reported and adjusted — list the adjustments and their size), capex, working capital, growth rates. Every number gets a page reference. If the document only shows adjusted EBITDA, say so — that is itself a finding.
5. **Read the banker's hand.** What gets the most pages, the best charts, the boldest claims? What is conspicuously thin — customer churn, organic vs. acquired growth, management depth, capex history, the bridge from reported to adjusted EBITDA? Emphasis and avoidance are both signals. The avoiding section always has real content, because every CIM omits something.
6. **Compile red flags:** concentration, declining organic growth dressed as total growth, heavy add-backs, recent ownership or management changes, projections that hockey-stick off the historicals, "pro forma" anything, pending litigation or regulatory exposure mentioned in passing.
7. **Run the fit-vs-mandate checklist** against the saved or supplied mandate (or the labeled generic profile), with any automatic pass that applies stated at the top of the section.
8. **Draft the 10 questions for the banker** — specific, answerable, and ordered so the first three would change the decision.

## Output format

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

The verdict paragraph stands on its own for a partner who reads nothing else.

```
# [Company Name] — CIM First Pass
Prepared [date] | Source: [CIM/teaser title, date if shown] | Process: [if known]

## Verdict (one paragraph)
Worth a partner conversation or not, and the 2–3 facts that drive that view.

## What the Business Actually Does
Plain-language description. Product, customer, reason to buy, switching costs.

## Revenue Model & Customer Concentration
- Revenue type and mix (recurring/reoccurring/one-time) [p. X]
- Contract structure and pricing [p. X]
- Concentration: top customer __%, top 10 __% [p. X] — or "not disclosed" (flag)

## Financial Snapshot (figures as presented in the document only)
| Metric | FY-2 | FY-1 | LTM/FY0 | Proj. | Page |
|---|---|---|---|---|---|
Adjusted EBITDA bridge: list each add-back and size [p. X]

## What the Banker Is Emphasizing
3–5 bullets — the story the book is built to tell.

## What the Banker Is Avoiding
3–5 bullets — thin, buried, or missing topics, and why each matters.

## Red Flags
Ranked list. Each: the flag, the evidence [p. X], why it matters.

## Fit vs. Mandate
| Criterion | Mandate | This Deal | Fit |
|---|---|---|---|
(If mandate not provided, label assumptions.)

## 10 Questions for the Banker
Numbered, ordered by decision impact.
```

## Banker-speak decoder (use when reading against the document)

Common CIM phrasings and what they usually signal — apply as hypotheses to test, not conclusions:

- "Adjusted EBITDA" with no reported EBITDA shown → the bridge is unflattering; demand it
- "Tech-enabled" → a services business with a software wrapper; check gross margin
- "Recurring revenue" without contract terms → likely reoccurring (repeat purchase), not contracted
- "Pro forma for recent acquisitions" → organic growth is weaker than headline growth
- "Diversified customer base" with no concentration table → concentration is probably material
- "Significant whitespace opportunity" → the projection assumes share gains the historicals don't support
- "Founder will remain involved in a transition capacity" → key-person risk and a succession question
- "Asset-light model" → check whether capex was reclassified or deferred; look at maintenance capex history
- "Strong management team" with no tenure data → recent hires; ask when each executive joined
- "Limited competition" → the competitive landscape section will be the thinnest in the book

## Guardrails

- **Only figures that appear in the document, each with a page reference.** Never compute implied figures (multiples, margins) without labeling them "derived" and showing the inputs.
- **Never fill gaps with industry priors stated as facts about this company.** "SaaS businesses typically retain 90%+" is allowed as context only if labeled as general context, not as a claim about the target.
- **Quote the document sparingly and exactly.** No paraphrases presented inside quotation marks.
- **Fact vs. inference discipline:** banker claims are claims. Reported financials are "as presented" — a CIM is not audited financials. Say "the CIM states" rather than asserting truth.
- **Confidentiality:** CIMs are almost always covered by an NDA. Assume a firm-approved AI environment that complies with the NDA and the firm's information-security policies; if there is a sign the user is working in an unapproved tool, say so plainly. Quote only the short excerpts needed to support a point, and do not reproduce large sections of the document.
- This is a screen, not diligence, and never an investment recommendation. The verdict is "worth more work / not worth more work given the mandate," nothing stronger.

## Example prompts

> "Here's the CIM for Project Falcon, a residential HVAC services roll-up the sell-side sent over yesterday. Our mandate is control buyouts, $5–15M EBITDA, B2B or consumer services, US only. Give me a first pass — especially whether the organic growth is real and what's hiding in the EBITDA adjustments."

> "Set up cim-first-pass. We do control buyouts of B2B services businesses, $5–15M EBITDA, US and Canada, $30–80M equity checks, five-year hold. Automatic pass on anything with a customer over 30% of revenue. Save the memos to our 'Deal screens' folder on SharePoint."

> "Two-page teaser attached for a vertical software business. This one is for the growth fund, not the buyout fund — assume minority checks of $10–25M. Worth requesting the full book?"

> "Screen this management presentation against the attached investment criteria memo and draft the banker questions for tomorrow's call."

## Works well with

Use **tear-sheet-private-co** if you want a public-source view of the target to compare against the banker's narrative.
