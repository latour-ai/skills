# Slide principles and layout library

Use this to diagnose an idea (step 1) and to build (step 4).

## Content rules

**Action titles.** Every content slide's title is a full-sentence claim, not a label. "Skills overview" is a label; "Skills cut review time because every analyst gets the same output" is a claim. Two lines maximum (about 15 words). No subtitles: if a slide seems to need one, the title isn't doing its job.

**Ghost-deck test.** Read the titles alone, in order. They should tell the whole story. Where reading stumbles, the logic jumps: add, merge, or reorder.

**One message per slide.** If a slide needs two titles, split it. The body proves its title and nothing else.

**Answer first.** Lead with the conclusion; the body supports it. For teaching, state the takeaway before the demo, not after.

**Concrete before abstract.** Show a real example, then name the pattern. Abstract-only slides lose a room of practitioners.

**Gray first, color one thing.** Everything is neutral except the single element the title is about.

**Slide vs. spoken track vs. handout.** A presented slide carries one title, one visual and sparse text; dense detail goes to the handout or appendix, and thanks and transitions are usually spoken. A read deck (a pre-read or a leave-behind) can carry more words on the slide, but still one message per slide under an action title, with the detail in the body rather than the title.

**SCQA is a thinking tool.** Situation, Complication, Question, Answer help the author find the message. Turn the answers into a slide (often a comparison or the title itself) instead of displaying four SCQA rows.

**5-second test.** Cover the title; someone should be able to guess it from the visual.

## Layout library

Pick the layout from the message. Each maps to a slide in `assets/example-deck.html`.

| Message shape | Layout | Example-deck slide | Key classes |
|---|---|---|---|
| Opening / cover | Accent band, big display-font title, presenters and date | 1 | `.cover`, `.band`, `.inner`, `.tagline`, `.meta` |
| "You've done X; today Y" | Progress timeline, today in accent | 2 | `.tl`, `.node`, `.node.today`, `.node.next`, `.thx` |
| "Old way vs. new way" (general) | Comparison table with row labels, plus one accent line | 3 | `.c2`, `.hd`, `.rl`, `.now`, `.how` |
| "How the pieces fit" | Framework columns with arrows, accent on the key box | 4 | `.cio`, `.col`, `.sub`, `.tiles`, `.icard.on`, `.orow` |
| "Changing one thing improves the output" | Before / lever / after panels | 5 | `.ba`, `.panel.before`, `.lever`, `.branch`, `.mk` |
| "These N cases share a pattern" | Three examples with parallel rows | 6 | `.ex`, `.hd.first`, `.rl`, `.diff` |
| Steps in order | 3–5 step flow, last or key step in accent | Snippet below | `.flow`, `.step`, `.step.last` |

### Step-flow snippet
```html
<div class="flow">
  <div class="step"><div class="n">1</div><div class="h">Objective</div><div class="d">What they'll be able to do</div><span class="arrow" aria-hidden="true">›</span></div>
  <div class="step"><div class="n">2</div><div class="h">Demo</div><div class="d">Show a real example first</div><span class="arrow" aria-hidden="true">›</span></div>
  <div class="step last"><div class="n">3</div><div class="h">Takeaway</div><div class="d">Name the principle last</div></div>
</div>
```
Set `grid-template-columns` inline to match the step count (e.g. `style="grid-template-columns:repeat(3,1fr)"`).

### Before/after rules
- Same task and input on both sides; change one thing so the difference is the lesson.
- Use a realistic "before" (what the room does today), not a strawman.
- Name the lever between the panels.
- Excerpt 3–5 lines per side; full outputs go to the handout.
- Mirror the panels; mark only what changed on the "after" side.

### Three-examples rules
- The title states what the three share.
- Choose for range along a dimension the room cares about (difficulty, asset class, team).
- Parallel anatomy: the same fields in the same order (e.g. task today → what the skill does → watch out for), labels on the left once.
- Concrete specifics; don't invent numbers. If the author has none, say so and use one-line descriptions.
- Order from most relatable to most ambitious; accent the one to start with or demo.

### Framework diagrams
- Recreate from an uploaded image when the author provides one; keep their structure and labels.
- Add an action title so the diagram has a point.
- Accent only the box the session is about; simple line icons (inline SVG, stroke `var(--ink)`) are fine.

## Writing on slides
- Sentence case, plain verbs, no filler.
- Don't name internal people or clients on slides unless the author's idea does so on that slide's face (requests from named individuals can be folded in anonymously).
- Mark illustrative data as illustrative.
