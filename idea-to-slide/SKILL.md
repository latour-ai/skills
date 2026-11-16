---
name: idea-to-slide
description: >-
  Turn a rough slide idea into finished slides through a short interview. The
  user pastes a slide title, loose notes, an outline or a draft deck; the
  skill asks the three highest-leverage questions one at a time (what the
  slide must say, how it should look, and the one change that would make it
  great), offers more, and builds as soon as the user says stop. Builds an
  HTML deck, a PowerPoint file, or Google Slides, in the firm's own brand or
  PowerPoint template, chosen once in a short first-run setup. For corporate
  and investment professionals who present to a room or circulate decks:
  trainers, analysts, IR and business development teams, managers preparing
  a team update. Trigger on "turn this into a slide", "make a slide from
  this", "slide this idea", "help me build this deck", "fix this slide",
  "set up idea-to-slide", "change my slide settings", or when the user dumps
  slide content in a slide-building context. Do NOT use for a fund marketing
  one-pager; use the fund-marketing-one-pager skill. Do NOT use to summarize
  source material into a written briefing; use the executive-briefing skill.
  Do NOT use to check an external deck against marketing rules; use the
  marketing-compliance-prescreen skill.
license: MIT
metadata:
  author: latourai
  version: '2.0'
---

# Idea to Slide

Turn a half-formed idea into slides that communicate. The user pastes each slide's idea straight into the prompt: usually a slide title and a loose description, sometimes just a few lines of notes. The value of this skill is the interview: a few sharp questions that surface what the slide must say and how it should look before anything is built. Building first and revising later produces generic slides; asking first produces the slide the user actually meant.

It builds in whatever the user's firm presents with (an HTML deck, PowerPoint or Google Slides) and in the firm's own look. A one-time setup records those choices, and every later run goes straight to the idea.

## Why this skill exists

Most weak slides are not badly designed; they are unclear about what they are trying to say. A topic label sits where a claim should be, three ideas compete for one slide, and the visual decorates rather than proves. The author usually knows the point, but it is still in their head, and no amount of formatting gets it onto the slide.

Asking an AI to "make a slide" skips that step. It fills the gaps with plausible defaults: a generic title, a bulleted list, a stock layout. The result looks finished and says little, and the author spends longer correcting it than they would have spent answering three questions up front.

So the skill asks first, and keeps the asking cheap. Each question carries a recommended answer the user can accept with one word, so a busy presenter gets the benefit of a good editor's questions in a minute or two, not an interview.

## Inputs

**Required:**
- The slide idea, pasted into the prompt: a title, notes, an outline, or a draft deck. That is the whole input; don't go looking for a source document elsewhere.

**Optional:**
- Images the idea refers to (a chart, a framework diagram, a screenshot to recreate). Ask for them if they aren't attached; never guess what an image shows.
- Facts to look up, but only when the user asks (step 2).

**Set once in setup (step 0):** firm name, default format, brand or template, presented or read decks, usual audience, required footer or disclaimer, and where files are saved.

**Missing-input behavior:** Never invent numbers, quotes or examples. If a slide needs a figure the user hasn't given, ask for it in Question 1, offer to look it up, or build with a clearly marked placeholder. Illustrative data is labeled as illustrative on the slide.

## How it works

### 0. First-run setup (once, then only when asked)

Run setup the first time the skill is used, or when the user says "set up idea-to-slide" or "change my slide settings". Look for a saved settings file first (`idea-to-slide-settings.md`, in the project's files or the user's slides folder). If one exists, read it and skip setup.

Setup is one short round of questions, each with a default the user can accept with "yes":

1. **Detect before asking.** Check what this environment can produce: a PowerPoint tool or skill, a Google Slides connection, HTML files. Pre-fill what detection settles.
2. **Ask, in one message:**
   - **Firm name**, for the footer.
   - **Default format:** HTML deck (default; opens in any browser and presents full-screen), PowerPoint (.pptx), or Google Slides.
   - **Look:** the built-in style (default; near-white paper, dark ink text, one deep-blue accent, a serif title font and a clean sans-serif body); or the firm's brand (one accent color, title and body fonts, and a logo if wanted); or the firm's PowerPoint or Google Slides template, which then overrides everything else about the look.
   - **Deck type:** presented to a room (default; sparse text, one visual) or read on its own as a pre-read or leave-behind (more words on the slide allowed).
   - **Usual audience**, in a line (for example "portfolio managers at our firm" or "prospective clients"), so questions don't re-ask it.
   - **Required footer or disclaimer**, if any: "Confidential", "For internal use only", or the firm's standard disclosure for external decks.
   - **Where to save files**, or "just send them to me".
3. **Save the settings** to `idea-to-slide-settings.md` in plain language the user can edit. If nothing persistent can be written, show the settings as a short block and tell the user to paste it into their project instructions.
4. **Carry on with the idea** if the user gave one with the setup request.

On every later run: read the settings and never re-ask. The user can override any of them for one deck ("make this one a PowerPoint").

### 1. Read the idea

- If the idea references an image that isn't attached, ask the user to upload it. Never guess what an image shows. If one is attached, look at it.
- If the prompt describes several slides, treat the set as one deck and aim the questions at the slides with the biggest gaps.
- Notes like an SCQA block or a "one sentence answer" are the author's thinking, not slide content. Use them to write titles and choose structure; don't paste them onto a slide as-is.

Before asking anything, silently diagnose each slide against `references/slide-principles.md` and note what's missing in two buckets: **content** (message, title, audience, facts, examples, numbers) and **visual** (layout, evidence element, focus).

Don't run any web or connector lookups yet. Go straight to Question 1.

### 2. Lookups are opt-in

Only look things up when the user asks: in their answer to Question 1 ("yes, look those up"), or any time they name something to find ("check my meeting notes with them", "get the latest figure"). Then:

- **Connected apps:** documents in the firm's file storage, meeting-notes tools, email threads, or any other connected app the user names.
- **Web search:** public facts, current figures, product names and versions, a company's description. Keep the source so it can go in the slide footer.

Keep to what they asked for. Report results in a few lines (one per fact, with source) at the top of your next message, then carry on with the next question. Never look up confidential detail the user didn't point you to.

### 3. Ask three questions, one at a time

The round has a fixed shape. Ask one question per message, wait for the answer, then ask the next with that answer in mind.

**Question 1 of 3: framing, title and missing info.** Settle what the slide says and what it needs. Cover, in one message:
- **The framing:** what the audience should believe or do after the slide, and who the audience is (only if neither the idea nor the settings answer it).
- **The title:** propose a specific action title (a full-sentence claim, not a topic label) the user can accept with "yes", plus one or two alternative framings.
- **The info:** a short list of what's missing: a number, an example, a screenshot, a detail. For each, say whether the user needs to supply it or you could look it up (web or a named connected app), and offer: "Want me to look up any of these?"

If the idea already settles the framing and title, say so in a line and spend the question on the missing info.

**Question 2 of 3: visual setup.** Settle how the slide looks and carries the message. Cover, in one message:
- **Layout:** which pattern from the layout library in `references/slide-principles.md` fits (before/after, three examples, flow, comparison, framework diagram, timeline, single big number). Recommend one and give one or two alternatives.
- **The evidence element:** what visual proves the title: a screenshot, a chart, a diagram, a table, a quote.
- **Icons** (only when the layout has parallel items, such as three examples or a flow): name the icon from `references/icon-library.md` you'd put on each item, so the user can swap any with one word.
- **Focus:** the one element the accent color lands on.
- **Split** (decks only): whether any slide should become two, or two should merge.

Never ask about colors or fonts; those come from the settings.

**Question 3 of 3 (optional): make it as good as possible.** Say this one is optional and they can reply "skip" or "build it". Then propose the single change most likely to lift the slide from good to great, with your recommendation. Pick from whatever applies most:
- A sharper or more surprising example the audience will remember.
- A "so what" callout or annotation that lands the point.
- A tighter title (fewer words, stronger verb).
- What to cut from the slide and move to the spoken track, the notes, or an appendix.
- The transition line into the next slide.
- An objection the audience will raise, and whether the slide should answer it first.

**How to ask (all three):**
- Number them: "Question 1 of 3", "Question 2 of 3", "Question 3 of 3 (optional)".
- Keep each to a short message, and say briefly what it decides ("This sets the title", "This decides the layout").
- Always attach a recommended answer the user can accept with "yes", plus alternatives when the options are discrete. A good default turns a question into a one-word reply.
- Never ask what the idea or the settings already answer.

**After Question 3** (or if it's skipped), end with one line offering another question or "stop and turn it into a slide". If they ask for more, keep going one at a time ("Question 4", "Question 5"), each aimed at the biggest remaining gap, offering the same choice after each. Build as soon as they say stop, skip, "build it", "go" or anything like it.

### 4. Build

Read `references/slide-principles.md` (content rules and layout library) and `references/icon-library.md` before writing. Then build in the format from the settings, or the one the user asked for this time.

**The look, whatever the format:**
- Neutral everywhere (background, body text, supporting elements in grays), with **one accent color used only on the slide's single most important element**.
- Built-in style: near-white paper, dark ink text, deep blue `#2E4A85` accent with white text, titles in Lora 600, body in IBM Plex Sans. Firm brand: the same rules with the firm's accent color and fonts. Firm template: the template's own masters, fonts and colors, still with only one accented element per slide.
- A footer line on every content slide: the source, or the firm name, on the left; the page number on the right; plus any required footer or disclaimer from the settings. When a fact came from a lookup, its source goes in the footer.

**HTML deck.** Start from `assets/template.html`, which holds the style, the 1280×720 scaling stage, and keyboard and swipe navigation. `assets/example-deck.html` is a finished six-slide deck showing every main layout; copy its markup patterns rather than inventing new CSS. For a firm brand, change only the color variables (`--hl`, `--blue`) and font variables (`--display`, `--body`, and the font link) at the top of the template. Fill in `{{DECK_TITLE}}` and `{{N}}` (the slide count), and replace the `{{SLIDES}}` comment with the slide sections. Make the first slide visible and give every other slide the `hidden` attribute. Use the icon markup and CSS from `references/icon-library.md`.

**PowerPoint.** Use the environment's PowerPoint tool or skill. Start from the firm's template if one is set; otherwise set a 16:9 layout with the look above. Build each layout from the library with native, editable shapes, text boxes and tables (never a picture of an HTML slide), so colleagues can edit it. Put the spoken track in the speaker notes when the user gave one.

**Google Slides.** If a Google Slides connection is available, build there the same way as PowerPoint, starting from the firm's template if one is set. If not, build a .pptx and tell the user it imports into Google Slides cleanly.

Save the file with a short name to the location in the settings, if any, and send it to the user.

### 5. Look before delivering

If you can render the slides to images (a browser or screenshot tool for HTML; a converter for PowerPoint), look at each slide and fix:
- Titles longer than two lines (shorten the words; don't shrink the font).
- Content overflowing its area or colliding with the footer.
- More than one accent on a slide.
- Icons missing a label, mixed sizes in one row, or icons not from the icon library.
- In HTML, class-name collisions (for example two layouts both defining `.sub`) that draw stray borders.

Then reply in a few lines: what each slide now says (its title), anything you assumed, and anything the user still needs to supply (real screenshots, numbers, an image you couldn't see). Don't restate the whole deck.

## Output format

The deliverable is the slide file in the chosen format; the reply around it stays short.

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

Each content slide has:
- An action title: a full-sentence claim, two lines at most.
- One body that proves the title, in a layout from the library.
- One accented element.
- A footer: source or firm name, page number, and any required disclaimer.

The closing reply follows this shape:

```
[file name], [N] slides, [format]

1. [Slide 1 title]
2. [Slide 2 title]

Assumed: [anything decided without the user]
Still needed: [real screenshots, numbers, images]
```

## Guardrails

- **Never invent facts.** No made-up numbers, quotes, client results or examples. Missing figures get a labeled placeholder, and illustrative data is marked as illustrative on the slide.
- **Lookups only on request,** and only of what the user named. Confidential documents or client details the user didn't point to stay untouched.
- **No names the author didn't put on the slide.** Don't name clients, colleagues or counterparties on a slide unless the user's idea does so on that slide's face.
- **The firm's look wins.** When a template or brand is set, follow it; never reintroduce the built-in style on top of it.
- **External decks need the firm's checks.** If a deck is going to clients, prospects or investors, include the required disclaimer from the settings and remind the user that the firm's marketing or compliance review still applies. The skill does not approve external material.
- **Nothing is sent or shared.** The skill saves and delivers the file to the user; it never emails, uploads to a shared location beyond the configured folder, or presents on the user's behalf.

## Example exchange

Pasted idea: a slide titled "Your repeating tasks run themselves" with three pasted workflow descriptions and the note "examples increase in difficulty."

> **Question 1 of 3: framing, title, info.** This sets the title. I'd go with "Start with the inbox, then build up to monthly reporting," so the slide reads as a path, not a list. Alternative: "All three are the same pattern: gather, check, summarize." Missing: a time-saved number for any of the three (yours to supply, or I can show a one-line "what the skill does" instead), and the details of the monthly-reporting workflow (I could pull these from your meeting notes). Want me to look that up?

User: yes to the title, pull the meeting notes, one line each

> From your meeting notes (team call, October 2): the report combines three data pulls and a commentary draft.
>
> **Question 2 of 3: visual setup.** This decides the layout. I'd use three columns stepping up left to right (a staircase), with a one-line output under each and the accent on the third, hardest example. Alternative: a flow diagram showing the shared gather → check → summarize pattern. Any screenshots to drop in?

User: staircase, no screenshots

> **Question 3 of 3 (optional): make it great.** Skip or say "build it" if you're happy. My one suggestion: add a "so what" callout under the staircase, "Your first automation should take 20 minutes, not 2 weeks", so the audience leaves with a starting point, not just a ladder.

…then: "Want another question, or should I stop and turn it into a slide?"

## Works well with

**executive-briefing** turns messy source material into a short written briefing; its key points make good action titles for a deck built here. **fund-marketing-one-pager** covers the single-page fund overview this skill doesn't. **marketing-compliance-prescreen** checks a fund pitch deck against SEC Marketing Rule pitfalls before it goes to compliance.
