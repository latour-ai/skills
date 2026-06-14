---
name: marketing-compliance-prescreen
description: Pre-screen fund marketing material against common SEC Marketing Rule pitfall categories — gross performance without net, cherry-picked track records, hypothetical/backtested performance without required context, testimonials and endorsements, unsubstantiated claims like "best-in-class", and missing disclosures — producing severity-ranked flags with the exact quoted language and what a compliance officer would likely require. Trigger on "pre-screen this deck for compliance", "check this pitch deck against the Marketing Rule", "compliance review of this one-pager", "anything in here compliance will flag?", "scrub this marketing material", "is this LP letter compliant", or when a user shares fund marketing material (pitch deck, one-pager, website copy, DDQ marketing sections, LP letter excerpts) and asks about compliance risk. This is a pre-screen to save compliance time — explicitly NOT legal advice and never a substitute for review by the firm's compliance officer or counsel. Do NOT use for creating marketing material — use the fund-marketing-one-pager skill. Do NOT use for drafting DDQ answers — use the rfp-ddq-response-drafter skill.
---

# Marketing Compliance Pre-Screen

Run fund marketing material — pitch decks, one-pagers, website copy, investor letters — through the common pitfall categories of the SEC Marketing Rule (Advisers Act Rule 206(4)-1) and produce a severity-ranked flag list: the exact language at issue, which pitfall category it hits, and what a compliance officer would likely require before it goes out. The point is to arrive at compliance review with a clean draft instead of burning two review cycles on findable problems.

**This is a pre-screen, not legal advice.** It does not replace review by your CCO, compliance consultant, or counsel, and a clean pre-screen is not a determination that material is compliant. It exists to make the human review faster and to teach the drafting team what keeps getting flagged.

## Why this skill exists

The IR team finishes the deck Thursday night; compliance flags gross-only returns, an unlabeled case study, and "top-decile manager" on Friday; the LP meeting is Monday. Repeat every quarter. Most Marketing Rule findings in routine materials are pattern-level — the same six pitfall categories account for the bulk of comment cycles, and the SEC's own risk alerts on the rule keep citing the same failures (gross-without-net and unsubstantiated claims above all). Catching pattern-level issues before compliance sees the draft saves the reviewer for actual judgment calls.

## Inputs

**Required:**
- The marketing material: deck, one-pager, website copy, letter, email campaign, or excerpts (text or file)

**Optional but high-value:**
- Audience and use: who receives it, one-on-one vs. broad distribution, prospective vs. existing investors (the rule's reach depends on this)
- Whether the adviser is SEC-registered (the Marketing Rule applies to registered investment advisers; if the user is an ERA or non-US manager, note that the analogous concerns still apply but the framework differs)
- The firm's existing disclosure pages/legends, so the screen can check whether required context exists elsewhere in the document
- Prior compliance feedback on similar materials

**Missing-input behavior:** If no material is provided, ask once. If registration status or audience is unknown, screen anyway under the assumption "SEC-registered adviser, material going to prospective investors" — the strictest common case — and label the assumption.

## How it works

1. **Read the full document first**, including footnotes and disclosure pages — many apparent violations are cured by a disclosure elsewhere, and the screen must check before flagging.
2. **Sweep for the six pitfall categories:**
   - **Gross-without-net performance.** Any gross return shown without net presented with at least equal prominence and computed over the same period. Includes the sneaky variants: gross IRR in the summary table with net buried in an appendix; deal-level gross returns; "illustrative" returns that are really performance.
   - **Cherry-picked track record.** Selected deals, funds, or periods without the context the rule requires — case studies showing only winners, "representative investments" that aren't representative, excluded predecessor funds, performance periods that conveniently start after a drawdown.
   - **Hypothetical/backtested performance without required context.** Backtests, model portfolios, projections, targets ("targeting 20% net IRR" is hypothetical performance), and pro-forma blends — all require audience-appropriateness policies, and the criteria/assumptions/risks behind them.
   - **Testimonials and endorsements.** Client quotes, LP praise, placement-agent statements, influencer or media endorsements — these trigger disclosure requirements (compensated or not, conflicts) and, where compensated, written-agreement and disqualification provisions.
   - **Unsubstantiated claims.** "Best-in-class," "top-decile," "proprietary," "market-leading," "unparalleled access," "consistently outperformed" — any statement of material fact the adviser must be able to substantiate on demand. Flag each with what substantiation would be needed.
   - **Missing or inadequate disclosures.** Performance presented without the standard accompaniments (as-of dates, fee basis, "past performance" language where applicable, benchmark definitions, material conditions behind the numbers); third-party ratings without required disclosure; SEC-registration misstatements ("SEC-approved").
3. **Quote exactly.** Every flag includes the precise language and its location (slide/page). Compliance can't act on "somewhere it says something superlative."
4. **Rank by severity:**
   - **High** — pattern matches the rule's bright lines or SEC enforcement/risk-alert priorities (gross-without-net, hypothetical performance to a general audience, fabricated-substantiation territory)
   - **Medium** — likely to draw comments; fix is usually added disclosure or reframing
   - **Low** — judgment-call territory; flag for the reviewer's attention
5. **State the likely compliance ask** per flag — the kind of remediation a CCO typically requires: add net with equal prominence, add the criteria-and-risks legend, cut the claim or attach substantiation, label the case study and disclose selection criteria. Phrase as "a compliance officer would likely require…" — not as a legal determination.
6. **Note what the screen can't see:** whether substantiation actually exists, whether the firm's policies cover hypothetical performance, whether a quoted person was compensated. These become questions for the compliance reviewer, listed explicitly.

## Output format

```
# Marketing Compliance Pre-Screen — [Document name]
Screened [date] | Assumed: [registration status, audience — stated or assumed]
**This is a pre-screen to accelerate compliance review. It is not legal advice
and is not a substitute for review by your compliance officer or counsel.**

## Summary
[n] flags: [n] High / [n] Medium / [n] Low. The 2–3 items most likely to
block distribution, in one paragraph.

## Flags (severity-ranked)
### Flag 1 — [HIGH/MED/LOW] — [Pitfall category]
**Location:** [slide/page/section]
**Exact language:** "[verbatim quote]"
**Issue:** [why this pattern draws scrutiny, in plain English]
**Likely compliance ask:** [the typical remediation]

(repeat per flag)

## Cured-Elsewhere Notes
Potential issues checked and found addressed by existing disclosures [location].

## Questions for the Compliance Reviewer
What this screen cannot determine: substantiation files, compensation behind
quotes, policy coverage for hypothetical performance, audience controls.

## Clean Categories
Pitfall categories swept with no findings — listed so the reviewer knows the
scan was complete, not selective.
```

## High-frequency flag patterns (the screen's cheat sheet)

Language patterns that account for most routine findings:

- Any % return, IRR, MOIC, or "x" multiple → check for net counterpart, equal prominence, same period, as-of date, fee basis
- "Target", "expected", "projected" + any return figure → hypothetical performance territory
- "Since inception" → verify the inception date shown and whether predecessor performance is being imported
- "Select investments", "representative deals", "case study" → selection-criteria and full-track-record context check
- Quotes from anyone outside the firm → testimonial/endorsement analysis (compensated? conflicts disclosed?)
- "Award-winning", "ranked", "rated" → third-party rating disclosure check (who, when, criteria, compensation)
- Superlatives and absolutes: "best", "top", "leading", "proven", "consistently", "uniquely", "no other firm" → substantiation flag
- "SEC-registered" → fine if accurate; "SEC-approved/endorsed" → always a finding
- Benchmark comparisons → benchmark named, defined, and apples-to-apples (net vs. net)?
- Logos of clients/LPs on a page → implied endorsement question

## Guardrails

- **Not legal advice — say it twice.** The disclaimer appears in the header and the framing never drifts into "this is compliant" / "this violates the rule." The vocabulary is "matches a pattern that draws scrutiny" and "a compliance officer would likely require."
- **A clean screen is not clearance.** If few or no flags are found, say explicitly that absence of flags is not a compliance determination.
- **Quote exactly, locate precisely.** Never paraphrase flagged language; never flag language the document doesn't contain.
- **Check before flagging:** a gross figure with compliant net presentation alongside is not a finding — read the whole document, footnotes included.
- **Don't rewrite performance language.** Suggest the *type* of fix; drafting compliant performance presentation is compliance's call, and this skill never composes net return figures or disclosure numbers itself.
- **Never invent rule citations or enforcement cases.** Refer to the Marketing Rule and its known pattern areas generally; if asked for specific cites, recommend counsel confirm.
- Jurisdiction humility: the screen is built around the SEC Marketing Rule; for non-US or exempt advisers, label the analysis as analogous-concern screening, not the applicable framework.

## Quality checks

- Disclaimer present in header and conclusion?
- Every flag: exact quote + location + category + severity + likely ask?
- All six categories swept, with clean categories listed?
- Cured-elsewhere check actually performed (footnotes and appendices read)?
- No compliant/non-compliant verdicts anywhere in the text?
- Reviewer-questions section converts the screen's blind spots into a checklist?

## Example prompts

> "Attaching our Fund IV pitch deck before it goes to compliance Monday. We're an SEC-registered adviser, deck goes to prospective institutional LPs. Pages 8–11 have the track record and there's an LP quote on page 14 I'm nervous about. Pre-screen it — exact language, severity, and what compliance will probably make us change — so I can fix the obvious stuff this weekend."

> "Pasting the new strategy page copy for our website before the redesign ships. Public audience, registered adviser. Screen it — especially the 'proven track record of outperformance' line marketing loves."

> "Our placement agent drafted this two-pager for a webinar. We're an exempt reporting adviser — screen it anyway under the strictest assumptions and label the framework caveat."

## Works well with

Run this on **fund-marketing-one-pager** and **lp-update-generator** outputs before they leave the building; performance language flagged here usually traces back to answers in **rfp-ddq-response-drafter** libraries worth cleaning at the source.
