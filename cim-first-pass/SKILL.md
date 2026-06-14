---
name: cim-first-pass
description: Turn a CIM, teaser, or management presentation into a first-pass private equity deal screen memo — what the business does, revenue model, customer concentration, financial snapshot with page references, what the banker is emphasizing vs. avoiding, red flags, fit-vs-mandate checklist, and questions for the banker. Trigger on "first pass on this CIM", "screen this deal", "review this teaser", "what do you think of this CIM", "summarize this management deck", "is this deal worth a look", "deal screen", "should we pursue this", or when the user uploads/pastes a CIM, confidential information memorandum, information memorandum, teaser, or sell-side management presentation. Do NOT use for public companies — use the public-company-first-pass skill. Do NOT use for hedge fund manager materials — use the hedge-fund-diligence skill. Do NOT use for checking what's in a data room — use the data-room-gap-checker skill.
---

# CIM First Pass

Turn a CIM, teaser, or management presentation into a deal screen memo a deal team can read in five minutes: what the business actually is, what the numbers in the document actually say, what the banker wants you to focus on, what they're steering you away from, and whether this is worth a partner conversation. The goal is a faster, sharper kill-or-advance decision — not a substitute for diligence.

## Why this skill exists

A mid-market PE associate sees dozens of CIMs a quarter. Most die at first read, but reading a 60-page CIM properly takes two hours, and the document is written by a banker whose job is to make the business look better than it is. The skill that separates good screeners from slow ones is reading *against* the document: noticing what's adjusted, what's omitted, and what the structure of the book itself reveals. This skill does that first read systematically so the human spends their time on judgment, not extraction.

## Confidentiality first

CIMs are almost always covered by an NDA. Before doing anything else, note this assumption in your head and, if there is any sign the user may be on an unapproved tool, say so plainly: **this skill assumes you are using a firm-approved AI environment that complies with your NDA and information-security policies.** Do not encourage pasting CIM contents into consumer tools. Never reproduce large verbatim sections of the CIM in the output — quote only short excerpts needed to support a point.

## Inputs

**Required:**
- The CIM, teaser, or management deck (uploaded file or pasted text)

**Optional but high-value:**
- The fund's mandate: sector focus, EBITDA/revenue range, check size, control vs. minority, geography, hold period
- Deal context: who sent it, process stage, timeline, prior knowledge of the company
- Any specific concerns the user already has

**Missing-input behavior:** If no document is provided, ask once for it — there is nothing to screen without it. If the mandate is missing, proceed but label the fit section: "Mandate not provided — fit assessed against a generic mid-market buyout profile; replace with your actual criteria." Never guess the user's mandate silently.

## How it works

1. **Read the whole document before writing anything.** Note page numbers as you go — every financial figure and material claim in the memo needs a page reference.
2. **Establish what the business actually does** in plain language, stripped of banker framing. "Tech-enabled services platform" usually means a services business. Identify the real product, who pays, why they pay, and how sticky that payment is.
3. **Map the revenue model:** recurring vs. reoccurring vs. one-time, contract structure, pricing mechanism, customer concentration (top 1/5/10 customers if disclosed — and flag loudly if a sell-side doc *doesn't* disclose concentration).
4. **Build the financial snapshot strictly from figures in the document.** Revenue, gross margin, EBITDA (reported and adjusted — list the adjustments and their size), capex, working capital, growth rates. Every number gets a page reference. If the document only shows adjusted EBITDA, say so — that is itself a finding.
5. **Read the banker's hand.** What gets the most pages, the best charts, the boldest claims? What is conspicuously thin — customer churn, organic vs. acquired growth, management depth, capex history, the bridge from reported to adjusted EBITDA? Emphasis and avoidance are both signals.
6. **Compile red flags:** concentration, declining organic growth dressed as total growth, heavy add-backs, recent ownership or management changes, projections that hockey-stick off the historicals, "pro forma" anything, pending litigation or regulatory exposure mentioned in passing.
7. **Run the fit-vs-mandate checklist** against the criteria provided (or the labeled generic profile).
8. **Draft the 10 questions for the banker** — specific, answerable, and ordered so the first three would change the decision.

## Output format

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
- **Confidentiality:** assume NDA coverage; firm-approved AI environments only; no bulk reproduction of the document.
- This is a screen, not diligence, and never an investment recommendation. The verdict is "worth more work / not worth more work given the mandate," nothing stronger.

## Quality checks

- Every number in the memo traceable to a page reference?
- Adjusted EBITDA add-backs itemized, not just netted?
- Customer concentration addressed — including its absence?
- "Avoiding" section has real content (a CIM always omits something)?
- Fit section uses the user's mandate, or clearly labels the generic substitute?
- First three banker questions would actually change the decision?
- Verdict readable on its own by a partner who reads nothing else?

## Example prompts

> "Here's the CIM for Project Falcon, a residential HVAC services roll-up the sell-side sent over yesterday. Our mandate is control buyouts, $5–15M EBITDA, B2B or consumer services, US only. Give me a first pass — especially whether the organic growth is real and what's hiding in the EBITDA adjustments."

> "Two-page teaser attached for a vertical software business. No mandate doc handy — assume generic lower-mid-market buyout. Worth requesting the full book?"

> "Screen this management presentation against the attached investment criteria memo and draft the banker questions for tomorrow's call."

## Works well with

Run **data-room-gap-checker** once you're past the CIM and into the room; **tear-sheet-private-co** if you want a public-source view of the target to compare against the banker's narrative.
