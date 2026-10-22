---
name: "ambition-upgrade"
description: "Use when the user wants to make a task or prompt more ambitious, or says 'make this more ambitious', 'think bigger', 'altitude/depth/range'."
---
 
# Ambition Upgrade
 
Take an idea, project, task, deliverable or prompt and make it more ambitious. Based on Felix Rieseberg's framework (felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models, Oct 2026). Speed (same work, faster) is assumed and not covered.
 
**The first response is Altitude only.** Do not include Depth or Range in the first response, not even as prompts. End by asking whether the user wants Depth and/or Range next. Run those only when the user says yes.
 
## Order of operations (first response)
 
1. State the task as you read it in one line. Do not ask clarifying questions first; take the most reasonable reading and go.
2. Fit check.
3. Climb the altitude ladder.
4. Pick the AI-ownable rung and run the work at that rung.
5. Specify the durable workflow (what the model needs to own the outcome without re-tasking).
6. Give the reusable altitude prompt.
7. Ask at most 2 questions that would improve a rerun, then ask: "Want me to run Depth, Range, or both?"
## Altitude: aim at the outcome, not the task
 
Core question: **what do you want to happen next?** What's the goal beyond the goal? Felix's example: he stopped asking Claude to fix individual crashes and asked it to keep the apps crash-free.
 
### Step 1: Fit check (one line)
- **Strong fit:** the work feeds a decision, a recurring process, or will be discussed in a meeting (Felix's tell: "are there going to be meetings about this?").
- **Weak fit:** purely creative work, or a one-off with no downstream outcome. Say so, keep the climb short, and note that Depth or Range may pay more.
### Step 2: Climb the ladder
Climb four rungs. For each, write one line: what that level is, and what the model would own if handed that level.
 
1. **The task:** the literal ask (e.g., "summarize this earnings call").
2. **The job:** what the task is done for (e.g., "know whether anything in the call changes our view").
3. **The goal:** what the job serves (e.g., "keep each position sized to the current strength of its thesis").
4. **The end goal:** the outcome the organization ultimately cares about (e.g., "compound capital while avoiding thesis-break drawdowns").
Phrase the rungs as outcomes, not artifacts. Each rung should answer "why does the one below exist?" Also note in one line whether the model is currently being fed raw or pre-digested material.
 
### Step 3: Pick the AI-ownable rung and run it
- Name the **highest rung a model can realistically own today** given the available inputs and tools, and say in one line why the next rung up is out of reach (missing data, judgment that must stay human, no feedback loop). Felix notes limits exist ("Claude, go make money" doesn't work by itself), but the ceiling rises with model capability, so push up.
- **Execute the work at that rung**, not just describe it. Gather the inputs: what the user attached, plus connected sources that bear on the task (drive, email, CRM, meeting notes, web). Prefer raw material over summaries.
- At minimum, go past the task: explain what changed, why, and what to do; surface the most urgent decisions with for/against cases.
- At the goal or end-goal rung, propose a better mechanism than the current artifact. If there's enough history, backtest it (show it would have caught things sooner). If not, specify the backtest and propose running the new mechanism in parallel with the current one for a cycle.
- If key inputs are missing, run on what's available, label assumptions inline, and note what would let a fuller run climb higher. Never stall waiting for data.
- **Verify outside the model:** reconcile figures to source with code, cite documents, or flag what needs human sign-off. Never let the model grade itself.
- **Deliver in the format the outcome needs** (memo, decision brief, deck, tracker), following the user's standing format preferences.
### Step 4: Durable workflow (the AI lens)
Altitude is where durable workflows that take the human out of the loop come from. Answer: **what would the model need so it owns this outcome on an ongoing basis instead of being re-tasked each time?** Felix's crash-free goal required crash-report access, a version-to-commit mapping, and machines to reproduce and verify fixes.
 
List concretely:
- **Data access:** sources and connectors (and which are missing).
- **Feedback loop:** how the model learns whether it worked (a metric, a backtest, a reconciliation, a human sign-off).
- **Trigger:** what starts each run (schedule, new document, event).
- **Human checkpoints:** decisions that stay with a person.
- **Workflow changes:** what the user would have to change about how the work is done today.
### Step 5: Reusable altitude prompt
Give one copy-paste-ready prompt that asks for the work at the chosen rung, naming inputs, the outcome, and the verification step.
 
## Output format (first response)
 
```
**Task as I read it:** <one line>
**Fit:** Strong / Weak, <why in one line>
 
## Altitude ladder
1. Task: ...: model owns ...
2. Job: ...: model owns ...
3. Goal: ...: model owns ...
4. End goal: ...: model owns ...
**Inputs today:** raw / pre-digested, <one line>
 
**AI-ownable rung:** <rung>, <why the next one up is out of reach>
 
## Run at that rung
**Inputs used:** ...
<the executed work>
**Assumptions & gaps:** ...
**Verification:** ...
 
## Durable workflow
- Data access: ...
- Feedback loop: ...
- Trigger: ...
- Human checkpoints: ...
- Workflow changes: ...
 
**Altitude prompt**
> ...
 
**Questions** (max 2, only if they'd change a rerun)
1. ...
 
Want me to run **Depth**, **Range**, or both?
```
 
## Follow-up lenses (only when the user asks)
 
### Depth: do it the way the field's best would
- **Use the experts' instruments, not their vocabulary.** If the model reaches for a markdown table, demand a database, a statistical model, or the tool a top practitioner uses.
- **Set an unreasonable target and treat it as achievable.** 10x the bar; tell the model to keep going if it says it's impossible.
- **Attack the house view.** Give raw data and try to reproduce (or refute) a belief the team holds.
- **Generate new knowledge.** Find a blind spot or leading signal nobody has spotted, validated on held-out data.
- **Outside judge.** Specify an external check: a script, backtest, reconciliation, second independent agent, or human expert.
In the rewrite, answer: what a top professional would do that the user didn't ask for; the rawest source material they'd start from; the methods and tools they'd use; and what external evidence would show the result is right. Deliver a copy-paste prompt plus prerequisites (data, tools, installs, access), and run it if the user wants.
 
### Range: borrow from other fields
- **Turn nouns into verbs.** Restate the deliverable as the job it does (e.g., an IC memo is "convincing skeptical partners to commit capital under uncertainty in one meeting") and use the verbs to find relevant fields.
- **Assemble the crew.** If the stakes were existential, which 3–6 disciplines would you staff it with? Include at least one adversarial seat.
- **Methods, not costumes.** Don't ask the model to write like a short seller; ask it to perform the research steps a short seller performs. Each crew member contributes a technique, tool, or check, not a voice.
- Where subagents exist, give each discipline its own workstream and reconcile with an orchestrator.
Deliver a copy-paste prompt plus prerequisites, and run it if the user wants. After running whichever follow-up lenses were requested, name the lens with the highest payoff for this task in one sentence (it may or may not be Altitude).
 
## Investment-management examples
 
**Task:** "Summarize this earnings call."
- Ladder: summarize the call → know if anything changes our view → keep sizing matched to thesis strength → compound while avoiding thesis-break drawdowns.
- AI-ownable rung: goal. Run: thesis-impact brief (pillars affected, evidence, sizing recommendation with for/against), noting if the thesis doc wasn't available. Top rung proposal: a continuous thesis-monitoring process that would have flagged past drawdowns earlier than reading calls did.
- Durable workflow: thesis docs and position data connected; trigger on each new transcript; feedback loop = backtest flags against past drawdowns; PM signs off on sizing.
- Questions: Is this a current position? Can you share the thesis doc?
- If asked, Depth: build a guidance-vs-actuals dataset from 8 quarters of raw transcripts and filings, quantify hedging-language changes, and reconcile every number with a script. Range: forensic accountant (revenue recognition, reserves), short seller (what's dodged in Q&A), linguist (certainty shifts), supply-chain analyst (cross-check supplier/customer calls).
**Task:** "Fill out this DDQ."
- Ladder: fill out the DDQ → pass the LP's operational due diligence → win the allocation → build durable LP relationships and AUM.
- AI-ownable rung: goal. Run: completed DDQ plus a one-page list of the LP's likely concerns with preemptive language.
- Durable workflow: a source-linked answer library drawn from policies and audited docs; trigger on each new DDQ; feedback loop = LP follow-up questions logged; IR and compliance sign off.
- Questions: Who is the LP and what's their known focus area?
- If asked, Depth: trace every answer to a source document and flag any that can't be traced. Range: LP-side ODD analyst (red team), compliance officer, plain-language editor.
## Guardrails
 
- Keep every prompt executable: it names inputs, methods, and a verification step.
- Deeper or higher, not just bigger. Don't inflate scope for its own sake.
- If the task is trivial, give a short ladder, run at the job rung, and skip questions if none would change the answer.
- Never send, post, or modify anything external without the user's explicit OK.
