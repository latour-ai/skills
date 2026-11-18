---
name: ic-memo-drafter
description: >-
  Draft a complete investment committee memo from the deal materials already
  gathered — CIM, diligence findings, model output, QoE, management call
  notes, market research — assembled into the firm's memo structure with
  thesis, business and market overview, financial summary, risks and
  mitigants, valuation and returns, and recommendation. Every claim is tagged
  by evidence quality, so management assertions never read as verified facts.
  The firm's memo template, investment criteria, and the committee's standing
  concerns are saved once in a short first-run setup. For private equity, growth equity, and private credit deal teams;
  associates, VPs, and principals writing for an investment or credit
  committee. Trigger on phrases like "draft the IC memo," "write the
  investment memo," "first draft for committee," "turn our diligence into a
  memo," "IC deck narrative," "credit committee memo," "we're going to
  committee on Thursday," "set up ic-memo-drafter," "change my
  ic-memo-drafter settings," or when a user provides a stack of deal materials
  and asks for a memo. Do NOT use for a first-pass screen of an unread CIM —
  use the cim-first-pass skill. Do NOT use for writing up the committee's
  decision afterward — use the ic-minutes-generator skill. Do NOT use for
  attacking a thesis — use the thesis-red-team skill. Not investment advice.
license: MIT
metadata:
  author: latourai
  version: '2.0'
---

# IC Memo Drafter

Turn six workstreams of deal material into a first-draft investment committee memo, structured the way your committee expects to read it — and with a discipline most drafts lack: every material claim tagged by where the evidence came from, so what management told you never reads like something you verified.

## Why this skill exists

The IC memo is where deal teams lose their nights. Forty pages synthesizing a CIM, a QoE, four diligence workstreams, a model, and a dozen call notes, written under deadline by the person who has the least time. Two things suffer predictably under that pressure.

The first is the risk section. It is written last, when the author is exhausted and has already spent two weeks becoming an advocate for the deal, so risks that were real in week one get compressed into three bullets and a mitigant. The second is evidence discipline: under time pressure, "management indicated that churn is under 5%" quietly becomes "churn is under 5%," and the committee reads an assertion as a finding. Both failures are structural, not personal, and both are fixable by making the draft mechanical enough that the human's remaining time goes to judgment instead of assembly.

## Inputs

**Required:**
- At least one substantive deal document — the CIM, management presentation, or a diligence readout. A memo cannot be drafted from a description of the deal. Materials can be attached, pasted, or pulled from the deal folder in connected file storage (SharePoint / OneDrive, Google Drive, Box, Dropbox) if the user names where it lives.

**Optional, and each one materially improves the draft:**
- The financial model output: base and downside cases, returns, entry and exit assumptions, debt structure and quantum
- Quality of earnings report and the adjusted EBITDA bridge
- Diligence readouts by workstream: commercial, financial, legal, tax, IT, insurance, environmental
- Management meeting and expert call notes
- Market and competitive research
- Deal context: process stage, competitive dynamics, timeline, bid range
- Concerns the committee has already raised about this deal

**Set once in setup (step 0):** the firm's memo template or a prior approved memo, the mandate and investment criteria, the committee's standing concerns, and where drafts are saved. The template is the highest-value of these, because committees read for structure and a memo in the wrong shape gets rejected on form.

**Missing-input behavior:** Draft from what exists and be explicit about what is missing. Where a standard memo section cannot be supported — no model means no returns section, no QoE means the EBITDA bridge is unverified — write the section header with an explicit `[NOT PROVIDED: ...]` placeholder rather than filling it with plausible-sounding content. A committee memo with a labeled hole is honest; a committee memo with an invented paragraph is dangerous. Never infer a financial figure that was not supplied.

## How it works

### 0. First-run setup (once, then only when asked)

Run setup the first time the skill is used, or when the user says "set up ic-memo-drafter" or "change my ic-memo-drafter settings". Look for a saved settings file first (`ic-memo-drafter-settings.md`, in the project's files or the folder where memo drafts are saved). If one exists, read it and skip setup.

Setup is one short round of questions, each with a default the user can accept:

1. **Detect before asking.** If a memo template, a prior approved memo, or an investment criteria document is attached, or is findable in connected file storage under the name the user gives, read it and pre-fill the answers for confirmation.
2. **Ask, in one message:**
   - **Memo structure:** the firm's template or a prior approved memo to match (attach it or say where it lives), or the default structure below (default).
   - **Committee type:** investment committee or credit committee, and any section the committee always expects (for example a downside case page, an ESG section, a covenant summary). Default: investment committee, no additions.
   - **Mandate and investment criteria:** in a few lines or as a document. "None" is valid; the memo then makes no fit statement.
   - **Standing committee concerns:** the questions this committee asks on every deal. "None" is valid.
   - **Where to save drafts**, and the file format (Markdown by default; Word if a document tool is available). Default: return the draft in the conversation.
3. **Save the settings** to `ic-memo-drafter-settings.md` in plain language the user can edit, recording the template as an outline of its section headings and order plus where the original lives. If nothing persistent can be written, show the settings as a short block and tell the user to paste it into their project instructions.
4. **Continue straight into the draft** if the user gave deal materials with the setup request.

On every later run: read the settings and never re-ask. A template or instruction given with a request overrides the saved one for that memo. Setup never blocks a first run: if the user says "skip setup", draft in the default structure and say so. If the save location isn't reachable, return the draft in the conversation and say so.

### Steps for each memo

1. **Read everything before writing anything,** noting the source document and page for every material fact as you go. The tagging in step 3 depends on this and cannot be reconstructed later.
2. **Establish the structure.** Use the firm's template if one is saved or provided. If not, use the default structure in the output format below and say at the top that a generic structure was used.
3. **Tag every material claim by evidence quality** as you draft — see the evidence tiers below. This tagging is the core discipline of the skill.
4. **Write the thesis as three or four pillars,** each stated as a proposition that could be false, with the evidence supporting it and the evidence that would undermine it. A pillar that cannot be falsified is a platitude, not a thesis.
5. **Build the financial summary strictly from provided figures,** with reported and adjusted EBITDA shown separately and the bridge itemized. Never present adjusted EBITDA alone.
6. **Write the risks section first among the analytical sections, not last** — and write it before the author's advocacy sets. Each risk gets: what it is, how likely, what it costs if it happens, what mitigates it, and honestly whether the mitigant is real or aspirational. A mitigant that amounts to "we will monitor this" should say so.
7. **Reconcile the model to the thesis.** Every value-creation assumption in the returns should map to a thesis pillar and to a diligence finding. Flag any assumption that appears in the model but is supported nowhere in the diligence record — this is one of the most useful outputs and it takes a machine to catch reliably.
8. **List open diligence items** with what each would change, so the committee can weigh conditionality rather than being told everything is resolved.
9. **Write the executive summary last,** to one page, readable standalone by a partner who reads nothing else.
10. **Anticipate committee questions** — the five to eight that will actually be asked, starting from the committee's standing concerns where they apply to this deal, ordered by how much they would change the decision.

## Output format

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# [Company / Project Name] — Investment Committee Memo
Prepared [date] | Deal team: [ ] | Structure: [firm template / generic]
Materials reviewed: [list each with date]
Materials not provided: [list]

## Executive Summary & Recommendation
[One page maximum. The recommendation, the transaction, the thesis in three
sentences, headline returns, the two risks that matter, and what is being asked
of the committee.]

## Transaction Overview
Structure, price and multiple, sources and uses, our check, ownership,
governance and board rights, management rollover, timeline. [Provided figures only.]

## Investment Thesis
### Pillar 1: [stated as a falsifiable proposition]
Support: [evidence, tagged] | What would break it: [ ]
### Pillar 2 … [3–4 pillars]

## Business Overview
What the company does in plain language. Product, customer, why they buy,
switching costs, unit economics if provided.

## Market & Competition
Size and growth [tagged by source], structure, competitive position,
and what the diligence actually established versus what the CIM claimed.

## Financial Performance
| Metric | FY-2 | FY-1 | LTM | Proj | Source |
|---|---|---|---|---|---|
Reported EBITDA vs. Adjusted EBITDA — bridge itemized, each add-back tagged.
Quality of earnings findings. Working capital and capex. Cash conversion.

## Valuation & Returns
Entry multiple and comparables basis, exit assumptions, leverage, base and
downside returns, and the sensitivity that matters most.
| Value-creation assumption | Model impact | Thesis pillar | Diligence support |
|---|---|---|---|
**Assumptions with no diligence support: [list — or "none"]**

## Key Risks & Mitigants
| # | Risk | Likelihood | Impact if realized | Mitigant | Mitigant is real or aspirational? |
|---|---|---|---|---|---|
[Ordered by expected cost. The honest assessment of each mitigant is required.]

## Open Diligence Items
| Item | Owner | By when | What it would change |
|---|---|---|---|

## Recommendation
[What the team is asking for, and the conditions attached.]

## Anticipated Committee Questions
Numbered, ordered by decision impact, each with the current best answer or an
explicit "we don't know yet."

---
### Evidence tag key
[A] Audited or third-party verified  [D] Established by our diligence
[M] Management-asserted, unverified  [B] Banker/CIM claim, unverified
[E] Our estimate or model output
```

## Evidence tiers

Every material claim carries one tag. This is what stops a memo from laundering assertions into facts.

- **[A] Audited / third-party verified** — audited financials, a QoE report's conclusions, a legal opinion, a signed contract, a third-party market study the firm commissioned.
- **[D] Established by our diligence** — customer references we ran, expert calls we commissioned, data we analyzed ourselves, site visits.
- **[M] Management-asserted** — anything the company or its executives told us that we have not independently confirmed. Most operating metrics in most deals start here and many never leave.
- **[B] Banker or CIM claim** — from the sell-side materials, unverified. Treat with the same skepticism as [M], plus the seller's incentive.
- **[E] Our estimate or model output** — derived by us, dependent on stated assumptions.

Two rules that follow: a thesis pillar supported only by [M] and [B] evidence must say so prominently, and any single figure that drives the returns and carries an [M] or [B] tag belongs in the open diligence items.

## Guardrails

- **Never invent a number.** Not a market size, not a comparable multiple, not a growth rate, not a headcount. If it was not provided, the memo says `[NOT PROVIDED]`. This holds even when the missing figure is obviously needed and even when a plausible estimate is easy — a committee memo is a decision document.
- **Never upgrade an evidence tag.** Management-asserted stays management-asserted no matter how reasonable it sounds or how many times it is repeated across documents. Repetition in the seller's materials is not corroboration.
- **The risks section is not a formality.** Every risk gets a real likelihood and impact assessment, and every mitigant gets an honest label. "We will have board representation" is not a mitigant for customer concentration.
- **Show reported EBITDA whenever adjusted EBITDA appears,** with the bridge itemized. If only adjusted was provided, say that explicitly — it is itself a finding.
- **Distinguish the deal team's view from the evidence.** Advocacy is legitimate in a memo; disguising advocacy as finding is not.
- **This drafts a memo; it does not make an investment decision.** The recommendation reflects what the deal team is asking for based on the materials provided, and it is never a substitute for the committee's judgment or for completing diligence.
- **Confidentiality:** deal materials are NDA-covered. This skill assumes a firm-approved AI environment that complies with the firm's NDAs and information-security policies. Do not reproduce large verbatim sections of the CIM.

## Example prompts

> "IC is Thursday. Attached: the CIM, our QoE, commercial and legal DD readouts, the model output with base and downside, and my notes from two management sessions. Draft it — and be genuinely tough in the risks section, the partners will be."

> "Set up ic-memo-drafter. Our template is the attached Word file — match its section order exactly. We're a lower-mid-market buyout fund, control deals, $10–30M EBITDA. The committee always asks about customer concentration and what happens to the returns if the exit multiple is two turns lower. Save drafts as Word files in the deal folder I name each time."

> "Credit committee memo for a $60M unitranche. Attached are the lender presentation, our credit analysis, and the covenant abstract. Flag anything in the model that our diligence doesn't actually support."

> "Early draft — we only have the CIM and one round of management calls, no QoE and no model yet. Draft what you can and mark clearly what's missing, so the partners see how thin the evidence base still is."

## Works well with

Run **cim-first-pass** before diligence starts and **thesis-red-team** on the draft before it goes to committee — the red team will find what advocacy hid. Use **ic-minutes-generator** to record the committee's decision, and **hundred-day-plan-drafter** once the deal closes to turn the memo's value-creation assumptions into owned workstreams.
