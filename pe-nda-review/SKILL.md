---
name: pe-nda-review
description: >-
  Review an inbound NDA or confidentiality agreement from the buy-side
  perspective and produce a severity-ranked issue memo with suggested markup
  language — non-solicit scope and duration, standstills, affiliate and
  portfolio company attribution, term length, definition breadth, residuals,
  employee and customer contact restrictions, financing tree exclusivity, and
  return-or-destroy obligations — ending in a sign-as-is / sign-with-markups /
  send-to-counsel call. For private equity, growth equity, credit, and
  corporate development teams turning routine process NDAs; associates, VPs,
  and in-house counsel. Trigger on phrases like "review this NDA," "can we
  sign this," "check this confi," "what's wrong with this NDA," "mark up this
  confidentiality agreement," "is this standstill a problem," "banker sent an
  NDA," or when a user uploads an NDA, confidentiality agreement, or CA from a
  sell-side process. Do NOT use for a hedge fund side letter — use the
  side-letter-term-extractor skill. Do NOT use for a credit agreement — use
  the credit-agreement-covenant-extractor skill. This is a commercial screen,
  not legal advice.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# PE NDA Review

NDAs arrive weekly and each one is a small tax: too routine to enjoy sending to counsel, too consequential to sign unread. This reads one the way a deal lawyer who knows your fund's standard positions would — ranked issue list, quoted language, drafted markups, and a clear call on whether it can go back today or needs a lawyer.

## Why this skill exists

The economics of NDA review are backwards. Most of them are standard paper that a partner could clear in four minutes, but nobody has four uninterrupted minutes, so they queue — and a queued NDA is delayed data room access in a process where the first movers set the pace. The ones that are not standard contain provisions that bind the fund for years, and they hide in exactly the clauses that look boilerplate.

The buy-side issues are also specific and repetitive in a way that suits systematic review. A non-solicit that reaches every employee rather than the executives you met. A standstill you did not notice you were agreeing to. Most importantly, an affiliate definition broad enough to bind every portfolio company in the fund — which is how a routine NDA on a small process quietly restricts hiring across a dozen companies you own. These recur, and a checklist catches them more reliably than a tired associate at 9pm.

## Inputs

**Required:**
- The NDA, confidentiality agreement, or CA (uploaded or pasted)

**Optional but high-value:**
- **Your firm's house positions** — the things you never accept and the fallbacks you will take. Without these the review runs against general market convention and says so.
- Deal context: who sent it, the target and sector, process stage, whether the process is competitive, how much you want the book
- Whether you own or are looking at competing or adjacent assets in the sector — this changes how much the non-solicit and non-use provisions cost you
- Your fund's structure: number of portfolio companies, whether they hire in this sector, and whether your affiliates include an operating group or a credit arm
- Any prior NDA with the same counterparty or banker, for a precedent comparison
- Who has signing authority and whether counsel review is required above a threshold

**Missing-input behavior:** The NDA alone is enough to run. Without house positions, judge against general market convention for buy-side confidentiality agreements and label the recommendation section accordingly — "assessed against typical market positions; substitute your house standards." Ask once for house positions if the user seems likely to have them, but do not block on it. If the document is partial or has unreadable exhibits, say which sections are missing rather than reviewing around the gap silently.

## How it works

1. **Identify the document type and posture.** One-way or mutual, who the disclosing party is, governing law, term, and whether this is the banker's standard form or something bespoke. A bespoke form deserves more attention.
2. **Read the definitions first.** "Confidential Information," "Representatives," "Affiliates," and "Person" determine the reach of everything else. The affiliate definition in particular decides whether this agreement binds your portfolio companies.
3. **Work the clause checklist below,** flagging every provision that departs from market or from stated house positions.
4. **Assess each issue on two axes:** how much it constrains the fund, and how likely the counterparty is to concede it. A deal-blocker they will never move on is a different problem from a deal-blocker that is standard to negotiate away.
5. **Draft markup language for everything rated negotiate or worse** — actual replacement text, not a description of what you want. Include the fallback position where a clean win is unlikely.
6. **Check for the buy-side-specific traps** — portfolio company attribution, restrictions on looking at competing deals, non-use provisions broad enough to constrain ordinary investing, and financing tree exclusivity that limits your lender options.
7. **Give the bottom line:** sign as-is, sign with the attached markups, or send to counsel — and when it is counsel, say specifically which provisions need a lawyer rather than sending the whole document.

## Output format

```
# NDA Review — [target / project name]
From: [banker / seller] | Received: [date] | Type: [one-way / mutual]
Governing law: [ ] | Term: [ ] | Assessed against: [house positions / market convention]

## Bottom line
**[SIGN AS-IS / SIGN WITH MARKUPS / SEND TO COUNSEL]**
[Two sentences. If counsel: which specific provisions, and why.]
Issues: [N] deal-blocker / [N] negotiate / [N] acceptable

## Issue list (ranked)
### 1. [Issue title] — [DEAL-BLOCKER / NEGOTIATE / ACCEPTABLE]
- **Clause:** [§]
- **Language:** > "[exact quote]"
- **What it does to us:** [1–3 sentences, concrete]
- **Market:** [what the standard formulation looks like]
- **Likelihood they concede:** [high / medium / low]
- **Proposed markup:**
  > [actual replacement language]
- **Fallback:** [the position to take if they push back]

[Repeat per issue.]

## Scope-of-reach check
| Question | Answer | § |
|---|---|---|
| Does this bind our portfolio companies? | | |
| Does it bind our other funds / affiliates / credit arm? | | |
| Does it restrict looking at competing or adjacent deals? | | |
| Does it restrict hiring generally, or only people we meet? | | |
| Does it restrict contacting customers, suppliers, or lenders? | | |
| Does it restrict our financing sources? | | |
| Does the confidentiality obligation survive indefinitely? | | |

## Clause summary
| Provision | This NDA | Market range | Assessment |
|---|---|---|---|
| Term of confidentiality | | | |
| Non-solicit — scope | | | |
| Non-solicit — duration | | | |
| Standstill | | | |
| Definition of Confidential Info | | | |
| Residuals | | | |
| Return / destroy | | | |
| Affiliate reach | | | |
| Governing law / jurisdiction | | | |
| Remedies / fee shifting | | | |

## Redline-ready markup block
[All proposed changes in one copy-paste block for the turn.]
```

## Buy-side clause checklist

The recurring issues, roughly in order of how much damage they do:

- **Affiliate / portfolio company attribution.** Does the definition of "Affiliates" or "Representatives" sweep in portfolio companies? If so, a non-solicit on a small process can restrict hiring across every company the fund owns. Standard fix: carve portfolio companies out entirely, or limit the agreement's reach to the deal team and named representatives who actually receive information.
- **Non-solicit scope.** Should cover only employees you actually met or were introduced to during the process, not all employees. Watch for "any employee, officer, or consultant" and for coverage of people you learn about from the materials rather than meet.
- **Non-solicit carve-outs.** General advertisements, searches by third-party recruiters not directed at the company, and inbound applicants must be excluded. Their absence turns a reasonable clause into an unreasonable one.
- **Non-solicit duration.** 12 months is common; 18 is negotiable; 24+ is aggressive for a process you may not even proceed in.
- **Standstill.** Frequently buried in a paragraph about "no acquisition of securities." Note whether it is deal-specific or general, whether it includes a "don't ask, don't waive" provision (which prevents even privately requesting a waiver), and whether it falls away on a competing bid or a signed agreement with another party.
- **Competing-deal restrictions.** Any provision limiting your ability to evaluate, pursue, or invest in similar or adjacent businesses. This is occasionally drafted to look like a non-use clause. For a sector-focused fund it can be the most expensive term in the document.
- **Non-use breadth.** "Solely for the purpose of evaluating the Transaction" is standard; language that restricts using anything you *learn* is not, since it can constrain ordinary investment activity in the sector.
- **Definition of Confidential Information.** Should carry the standard exceptions — already known, publicly available, independently developed, received from a third party without restriction. Also check whether the existence of the process itself is confidential and whether that conflicts with your LP or lender reporting.
- **Term of confidentiality.** 2–3 years is typical for a process NDA; perpetual obligations should be limited to trade secrets if accepted at all.
- **Residuals.** A residuals clause protecting unaided memory is favorable to you as a recipient; its absence is common and worth a request but rarely worth a fight.
- **Return or destroy.** Must carve out routine electronic backups and archived copies made in the ordinary course, and documents retained for legal or compliance purposes — otherwise you are agreeing to something your IT systems make impossible.
- **Contact restrictions** on customers, suppliers, and employees — reasonable during a process, but check whether they extend past the process or block ordinary commercial contact.
- **Financing tree / lender exclusivity.** Provisions restricting which lenders you may approach, or requiring the seller's consent to speak with financing sources, limit your ability to run a competitive financing.
- **Remedies.** Injunctive relief is standard. Liquidated damages, fee shifting, and indemnification for the disclosing party's costs are not, and are worth pushing back on.
- **Assignment and successors,** and whether the obligations follow a portfolio company you later sell.

## Guardrails

- **This is a commercial screen, not legal advice.** It does not create an attorney-client relationship and does not replace review by counsel. Anything unusual, bespoke, or high-stakes goes to a lawyer — and the recommendation should say so specifically rather than defensively hedging on everything.
- **Quote exactly.** Every issue reproduces the operative language verbatim with its section. No paraphrase inside quotation marks, and no characterization of a clause without the text that supports it.
- **Never assert a provision is absent without checking the whole document,** including exhibits, schedules, and defined terms. Standstills and competing-deal restrictions in particular are often placed away from where they belong.
- **"Market" varies.** Market convention differs by deal size, sector, geography, and whether the process is competitive. State what you are comparing against, and note where the user's own house positions would change the call.
- **Markup language is a starting draft.** Proposed text must be flagged as subject to counsel review before it goes back, especially anything touching governing law, remedies, or the standstill.
- **Do not counsel the user to breach an obligation** or to work around a provision they have already agreed to elsewhere.
- **Confidentiality:** the NDA itself and the existence of the process are usually confidential. Assume a firm-approved AI environment.

## Quality checks

- [ ] Every issue has a section cite and a verbatim quote
- [ ] Affiliate / portfolio company reach addressed explicitly, even when the answer is "no reach"
- [ ] Standstill addressed explicitly, including its absence
- [ ] Competing-deal and non-use breadth assessed for a sector-focused buyer
- [ ] Non-solicit assessed on scope, duration, and carve-outs as three separate questions
- [ ] Every negotiate-or-worse issue has actual replacement language, plus a fallback
- [ ] Likelihood-of-concession stated, so the user knows what to spend capital on
- [ ] The scope-of-reach table is fully answered
- [ ] Bottom line commits to one of the three calls
- [ ] If "send to counsel," the specific provisions are named

## Example prompts

> "NDA from the banker on Project Cardinal, attached. Standard mid-market services process, we want the book. Our house positions: no non-solicit past 12 months, never accept anything covering non-management employees, never accept a standstill on a sell-side process. Can we sign it today?"

> "Mutual NDA for a proprietary conversation with a founder. Attached. We own two companies in the adjacent space — flag anything that constrains what we can do with them."

> "Review this and mark it up. Also compare it to the NDA we signed with the same banker last quarter, attached as the second file — I want to know what they changed."

## Works well with

Once the NDA is signed and the book arrives, run **cim-first-pass**. Use **investment-folder-organizer** to set up the deal folder before diligence materials start landing.
