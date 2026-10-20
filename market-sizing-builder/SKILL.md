---
name: market-sizing-builder
description: >-
  Build a triangulated market size for a new channel, product category, or
  end market — a top-down estimate from industry association, trade, and
  government data, and an independent bottom-up estimate built from units:
  for consumer channels, doors times velocity times price; for services,
  establishments times spend per establishment or per customer. The two are
  reconciled line by line, every assumption is sourced and dated or marked as
  an assumption, the inputs the answer moves most with are run through a
  sensitivity table, and the result is split explicitly into total,
  serviceable, and obtainable market with a range rather than a point. For
  private equity deal and portfolio teams sizing a portfolio company's
  expansion into a new channel or category, for screening the "is this a
  large, fragmented end market?" question before a thesis is written, and
  for growth-equity and long-only analysts who need a defensible number
  behind a TAM claim. Trigger on phrases like "how big is this market,"
  "size the TAM," "build a bottom-up market size," "what's the SAM for this
  channel," "is this a large fragmented market," "how many doors and what
  velocity," "how much do these establishments spend on this," "sanity-check
  management's TAM," or "reconcile the top-down and bottom-up." Do NOT use to
  list the players, segments, and whitespace in a sector — use the
  market-map-builder skill. Do NOT use for a first-pass read of a CIM against
  the fund's criteria — use the cim-first-pass skill. Do NOT use for cohort,
  retention, and CAC/LTV analysis of a company's own customers, which works
  from company data rather than the market. Do NOT use for bull/base/bear
  valuation scenarios on a model; the sensitivity table here covers market
  inputs only. A market size is
  always a range with its construction shown, never a single headline number.
license: MIT
metadata:
  author: latourai
  version: '1.0'
---

# Market Sizing Builder

Every expansion case and most screening memos contain a sentence that says the market is worth some round number of billions, and almost none of them can say where the number came from. Usually it is a market-research headline whose method is unknown, multiplied by a share assumption nobody wrote down. This skill builds the number twice — once from the top using published industry and government data, once from the bottom using units the team can check and argue about — reconciles the two, sources and dates every input, shows which assumptions the answer is most sensitive to, and splits the result into what exists, what the company can actually serve, and what it can plausibly win.

## Why this skill exists

Top-down and bottom-up estimates fail in opposite directions, which is why one without the other is not a market size. Top-down figures start from a category definition someone else chose: an industry code, a trade association's membership, a research firm's scope. They tend to overstate the market a specific company can address, because the definition is broader than the product, and they hide their method, so they cannot be adjusted when the definition is wrong. Bottom-up figures start from things that can be counted — stores, clinics, contractors, units per store per week, average ticket — and tend to understate, because the builder only counts the doors they can see. When the two land within a reasonable band of each other, the number is defensible. When they do not, the gap is the most useful output of the exercise: it points at a definition mismatch, a missing channel, or an assumption that is simply wrong.

The bottom-up build differs by business type, and choosing the wrong frame is a common error. A consumer product entering a new channel is sized as doors in the channel, times the share of doors that would carry the category, times velocity (units per store per week, or per door per year), times net price. A services business is sized as the number of establishments or customers that buy the service, times the share that buy it from an outside provider rather than doing it in-house, times annual spend. Each frame has its own weak link: velocity for consumer channels, outsourcing rate and spend for services. The skill names the weak link and puts it at the top of the sensitivity table.

Total, serviceable, and obtainable are different questions with different audiences. Total addressable market tells the investment committee whether the space is worth time. Serviceable market — limited by geography, channel, price point, customer size, and regulatory reach — tells the operating team where the company can actually sell. Obtainable market — a share of serviceable that is defensible given competitors, distribution, and a stated time horizon — is what belongs in the plan. Blending them is how a credible-sounding TAM ends up supporting a revenue forecast it cannot carry.

For the screening question, size alone is not the answer. "Large and fragmented" needs a concentration read alongside the number: the share held by the top few players, the count of providers, and the typical size of an independent. A large market with three players holding most of it is a different thesis from the same market spread across thousands of owner-operators.

## Inputs

**Required:**
- The market to size, defined in a sentence: the product or service, the customer, the channel, and the geography
- The purpose: expansion case for a named company, screening question, or a check on someone else's TAM claim
- Whether the business is a consumer product, a service, or both, so the bottom-up frame is chosen correctly

**Optional but high-value:**
- **Top-down sources the user has or names** — government statistical releases, economic census tables, trade association reports, industry studies, public-company segment disclosure — with their dates
- **Count data** for the bottom-up: store or door counts by banner, establishment counts by industry code and size band, licensed-provider registries, customer counts
- **Velocity and price data**: the company's own sell-through in existing channels, retailer scan or panel data, average selling prices, distributor quotes
- **Spend data for services**: invoices or contract values from the company, survey results, expert-call notes, published cost benchmarks
- **The company's current position**: revenue in the market today, channels and geographies served, price point, capacity constraints
- **Competitor revenue or share estimates** for the concentration read
- **A third-party TAM figure to test**, with whatever is known about how it was built
- **The time horizon** for obtainable market and any growth-rate view

**Missing-input behavior:** The skill builds with what it has and labels every gap. If no top-down source is supplied or named, the top-down leg is marked not built rather than filled from recall, and the output says which published series would close it. If a bottom-up input has no source, the skill proposes a value with its reasoning, labels it as an assumption, and moves it into the sensitivity table. If the business type is ambiguous, both frames are sketched and the user is asked which applies. If no time horizon is given for obtainable market, five years is used and stated.

## How it works

1. **Pin the definition.** Write the market definition explicitly — product, customer, channel, geography, year — and list what is in and out. Every later number is checked against this sentence, because definition drift is the most common reason two estimates disagree.
2. **Build the top-down estimate.** Start from the broadest credible published figure and narrow it to the definition in visible steps: category share of the industry total, geography share, channel share, price-tier share. Record each source with its publisher, date, and what it measures. Where a figure's method is unknown, say so beside it.
3. **Choose the bottom-up frame.** Consumer channel: doors × carrying rate × velocity × net price. Services: establishments or customers × outsourcing rate × annual spend. Mixed businesses get both, added without double-counting.
4. **Build the bottom-up estimate.** Count the units from the best available source, with the count's date and scope. Derive velocity, spend, and rates from company data, panel data, or expert input where possible. Label each input sourced, derived, or assumption.
5. **Reconcile.** Put the two estimates side by side at the same definition and year. If they differ by more than the uncertainty in either, trace the gap to a specific cause — scope mismatch, a missing channel, a stale count, an implausible velocity — and either adjust the leg that is wrong or report the gap with the candidate explanations. The reconciled figure is a range, with the reasoning for where in the range it sits.
6. **Run the sensitivity table.** Identify the three to five inputs the answer moves most with — usually velocity or spend, the carrying or outsourcing rate, and price — and show the market size at plausible low and high values for each, plus a combined low and high case. State which single input, if wrong, changes the conclusion.
7. **Split TAM, SAM, and obtainable.** Narrow total to serviceable using the company's actual channels, geographies, price points, and customer types, each step shown. Set obtainable as a share of serviceable over the stated horizon, justified by current share in comparable channels, competitor positions, and distribution reach.
8. **Add the concentration read where asked.** Top-player share, provider count, typical independent size, and the source for each, so "large and fragmented" is answered on evidence.
9. **Test any third-party figure.** Place an external TAM claim against the reconciled range, state how it was built or that its method is unknown, and say whether the difference is definition or substance.

## Output format

A skeleton to adapt — the summary range and the sensitivity table are what the committee reads; the source log is what lets someone rebuild the number.

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

```
# Market size — [market definition], [geography], [year]
Purpose: [expansion case / screen / TAM check] | Frame: [consumer channel / services / both]
In scope: [ ] | Out of scope: [ ]

## Summary
TAM: [$low – $high] | SAM: [$low – $high] | Obtainable by [year]: [$low – $high]
Top-down vs bottom-up: [$x vs $y — reconciled / gap of z% explained by ...]
Moves most with: [input] | Concentration: [top-N share, provider count] (if asked)

## Top-down build
| Step | Figure | Source (publisher, date) | Method known? | Sourced / assumption |
|---|---|---|---|---|

## Bottom-up build
| Input | Value | Basis | Source / date | Sourced / derived / assumption |
|---|---|---|---|---|
Result: [units × rate × velocity or spend × price = $ ]

## Reconciliation
[Side by side at one definition; cause of any gap; where in the range and why]

## Sensitivity
| Input | Low | Base | High | Market size at low / high |
|---|---|---|---|---|
Combined low / high: [ ] | Conclusion changes if: [ ]

## TAM → SAM → obtainable
| Step | Filter applied | Resulting $ | Basis |
|---|---|---|---|

## Third-party figures tested
[Figure, publisher, date, how built or "method unknown", vs reconciled range]

## Open questions
[Inputs that would most narrow the range, and where to get them]
```

## Where market sizing goes wrong

- **The unexplained headline.** A research-firm figure quoted without its scope or method cannot be adjusted or defended. Treat it as one data point with its construction stated, not as the answer.
- **Definition drift.** The top-down figure covers the whole industry code; the bottom-up covers one channel. The gap looks like an error and is actually a scope difference. Restate both at one definition before comparing.
- **Velocity borrowed from the wrong channel.** Units per store in a specialty channel do not transfer to mass or club. Use velocity from the target channel or a close analogue, and flag the analogue.
- **Every establishment counted as a buyer.** Many establishments do the work in-house, buy a substitute, or are too small to buy at all. The outsourcing or carrying rate is usually the weakest input and belongs in the sensitivity table.
- **Gross price instead of net.** Retail price, list price, or price before trade spend and promotions overstates the revenue pool available to a supplier.
- **TAM used as the plan.** A total market figure supports a revenue forecast only after the serviceable and obtainable filters are applied and shown.
- **Stale counts.** Door and establishment counts move with closures, banner conversions, and consolidation. Date every count.
- **Size without structure.** A large market answers half the screening question. Without concentration, it says nothing about whether a roll-up or share-gain thesis can work.

## Guardrails

- **Never a single number without its range.** Every market size — TAM, SAM, obtainable, top-down, bottom-up — is shown as a range, and any point estimate is presented inside it with the reason for its position.
- **Market-research headline figures carry their construction.** Any third-party figure is cited with publisher and date and with how it was built, or with an explicit note that the method is unknown.
- **Assumptions are marked as assumptions.** Every input is labeled sourced, derived, or assumption, with sources and dates for the first two. Unsourced inputs are never presented as data.
- **Figures come from sources supplied or named, not from recall.** Counts, spend, prices, and published market figures are taken from documents and sources the user provides or names, with as-of dates; where a leg cannot be built from sources, it is marked not built.
- **The gap is reported, not hidden.** When top-down and bottom-up disagree and the cause cannot be found, both are shown with the candidate explanations rather than averaged away.
- **Confidentiality.** Company sell-through, pricing, and expansion plans are sensitive. Assume a firm-approved AI environment and reproduce nothing beyond what the sizing requires.
- **Not investment advice.** This is an internal sizing analysis on supplied and named sources. It is not a valuation, a forecast of company results, or a recommendation to buy, sell, or invest in anything.

## Example prompts

> "Our portfolio company sells [product] through specialty retail and wants to enter grocery. Size the grocery opportunity in the US: top-down from the category data in the attached industry report and the census retail tables, bottom-up from door counts by banner (attached), our specialty velocity, and the scan data for the two closest analogues. Reconcile, show the sensitivity on velocity and carrying rate, and give me TAM, SAM for the banners we can realistically get into, and obtainable over five years."

> "Screening question: is outsourced [service] for [customer type] a large, fragmented end market? Bottom-up from establishment counts by size band in the attached census extract, an outsourcing rate and annual spend from the expert-call notes, top-down from the trade association report. Add the concentration read — top-five share and provider count — and tell me plainly whether it clears the bar."

> "Management's deck says the TAM is [$x]bn and cites a research firm. Rebuild it from the bottom using the company's own customer data and public establishment counts, tell me what the research figure likely includes that ours does not, and give me the range you would put in the IC memo."

## Works well with

**market-map-builder** is the natural companion: it names the players, segments, and whitespace, and this skill puts a number on the space the map describes. **cim-first-pass** uses the size and concentration read when a CIM claims a large, fragmented market, and **expert-call-question-guide** is where to build the questions that pin down velocity, outsourcing rates, and spend when the bottom-up leg is short of data. **expert-call-synthesis** pulls the velocity, pricing, and spend data points from completed calls into one sourced table. Once the obtainable figure is set, it can carry into the expansion plan, the returns model, and a valuation case. **ic-memo-drafter** is where the reconciled range and its construction end up.
