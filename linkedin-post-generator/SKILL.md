---
name: linkedin-post-generator
description: >-
  Turn a rough idea, notes, a link, or an existing article into a polished
  LinkedIn post in the user's own voice. Focuses on a first one to three
  lines that earn the "see more" click (a curiosity gap, a contrarian
  statement, or a direct statement of value), a short-paragraph rhythm that
  is casual and concise without being melodramatic, and none of the phrases
  that mark a post as machine-written. The user's voice samples, audience,
  topics, phrases to avoid and any firm rules on social posts are set once in
  a short first-run setup. For executives and professionals building a
  reputation in their field. Trigger on "write a LinkedIn post", "LinkedIn
  post about", "turn this into a post", "adapt this for LinkedIn", "draft a
  LinkedIn update", "rewrite this post", "set up linkedin-post-generator",
  "change my linkedin-post-generator settings", or when the user shares an
  idea or article and asks for LinkedIn content. Do NOT use for long-form
  articles, newsletters or email. Do NOT use to check a post against
  marketing rules; use the marketing-compliance-prescreen skill. Do NOT use
  for a weekly market recap; use the weekly-market-recap-writer skill. The
  post is returned as text to copy; the skill never publishes.
license: MIT
metadata:
  author: latourai
  version: '2.0'
---

# LinkedIn Post Writer

## When to Use This Skill

Load this skill whenever the user:

- Shares an idea, rough notes, or article and asks for a LinkedIn post
- Asks to write, draft, or improve a LinkedIn post
- Wants help with thought leadership content for LinkedIn
- Is an executive or professional building personal brand awareness

The source material can be typed, pasted, attached, or given as a link to read. If a link can't be opened, ask for the text.

Set once in setup (see First-Run Setup): voice samples, role and audience, topics, words to avoid, and firm rules on social posts.

---

## First-Run Setup (once, then only when asked)

Run setup the first time the skill is used, or when the user says "set up linkedin-post-generator" or "change my linkedin-post-generator settings". Look first for a saved `linkedin-post-generator-settings.md` in the project's files or the skill's working folder. If it exists, read it and skip setup.

Ask one short round of questions, each with a default; "none" is a valid answer to any of them:

- **Voice samples:** two or three of the user's own posts, pasted. Default none, in which case the skill follows the principles and reference examples below.
- **Role and audience:** what the user does and who they want reading, in a line. Default: a senior professional writing for peers in their industry.
- **Topics:** the two to four subjects the user wants to be known for. Default none.
- **Words and habits to avoid or keep:** phrases the user never uses, and preferences on emoji, hashtags and how posts end. Default: no emoji, no hashtags.
- **Firm rules on social posts:** for example no client names, no fund performance or return figures, nothing about live deals, or review by compliance before posting. Default none.

Save the answers to `linkedin-post-generator-settings.md` in plain language the user can edit. If nothing persistent can be written, show the settings as a short block and tell the user to paste it into their project instructions. If the user gave an idea with the setup request, carry on and write the post.

On later runs, read the settings and do not re-ask. Setup never blocks a run: if the user says "skip setup", write with the defaults. When voice samples are saved, they are the main guide to voice: match their vocabulary, sentence length and level of formality, and use the reference examples below only for structure.

---

## Core Philosophy

The goal is to sound like a sharp, self-aware human, not a brand account, a motivational poster, or a chatbot. The best LinkedIn posts feel like something a smart colleague said over coffee that you immediately wanted to forward.

**Three principles:**
1. The first 1-3 lines earn the "see more" click on their own merit
2. The voice is conversational: specific words, not polished words
3. Sincerity over performance: executives who sound real build trust faster than executives who sound impressive

---

## The Hook (Lines 1–3): Above the Fold

LinkedIn truncates posts after roughly 2-3 lines. Everything above that fold is your headline. It has one job: stop the scroll.

**Choose one of these three opening modes:**

### 1. Curiosity Gap
Create information asymmetry. The reader knows something is missing and wants the answer.

> "Most feedback conversations fail before they start. Not because the feedback is wrong. Because the timing is."

> "I've hired 40+ people. The best interview question I ever used wasn't a question at all."

### 2. Contrarian Statement
Disagree with a widely held belief in your industry. Be specific — vague contrarianism is noise.

> "Async-first culture sounds great in theory. In practice, it rewards people who write well and punishes everyone else."

> "We talk about 'founder mode' like it's a superpower. For most companies, it's the single biggest bottleneck."

### 3. Value Delivery / Direct Claim
State the payoff upfront. The reader knows exactly what they're getting.

> "Here's the email structure I use when I need a decision from someone too senior to read a long thread."

> "Three things I stopped doing in 1:1s that made them 10x more useful."

**Hook writing rules:**
- Don't start with "I" (it is a weak opener, and posts that open that way tend to travel less)
- Don't open with a question word as the very first word (it reads like a quiz)
- No setup before the setup: the first sentence is the hook
- Keep each line to one thought
- Leave a gap between lines 1, 2, and 3 (white space increases readability and click-through)

---

## The Body: Staccato Without Drama

After the hook, the post should breathe. Short paragraphs. Single-sentence bursts followed by brief elaboration. Not tweet-length fragments, but not paragraphs either.

**Rhythm pattern:**
- One sharp claim (1 sentence)
- Brief expansion (1-2 sentences max)
- [White space]
- Next point

**What to avoid:**
- Numbered lists of more than 5 items (feels like a blog, not a post)
- Bullet points for every single thought (lazy structure)
- Transition phrases: "The thing is...", "Here's the deal...", "Let's be honest..."
- Ending every sentence with a period on its own line for fake drama
- Rhetorical stacking: "Not X. Not Y. Not Z." (overused pattern)
- Any sentence that could appear in a corporate press release

**What works:**
- Specific examples over general principles ("When I was running a team of 12 at [X]" beats "In my experience as a leader")
- Numbers and specifics ("took 4 months" not "took a long time")
- The personal moment that proves the point — brief, not confessional
- An honest admission that creates contrast ("I got this wrong for two years")

---

## AI Tells to Eliminate

These phrases and patterns signal AI-generated content, and readers discount a post as soon as they spot one. Leave them out:

**Phrases to avoid:**
- "In today's fast-paced world..."
- "Game-changer" / "paradigm shift" / "unlock your potential"
- "It's not about X, it's about Y" (overused LinkedIn cliché)
- "Here's what I've learned:" (as a standalone transition line)
- "The truth is..." / "The reality is..."
- "This is your sign to..."
- "Swipe right if..." / "Double tap if..."
- "Let that sink in."
- "Full stop." / "Period."
- "No fluff." / "No gatekeeping."
- Em dashes used for dramatic effect every other sentence
- Ending with "Agree?" or "Thoughts?" as the only CTA

**Structural AI tells:**
- Hook → 5-item numbered list → closing question (the most common machine-written format)
- Every paragraph being exactly 1-2 sentences (robotic rhythm)
- Overuse of parenthetical asides (like this) (and this) (and another one)
- Alliteration in headers or bullets ("Plan, Prepare, Perform")

---

## Closing

End with one of:
- A single honest observation that reframes the whole post
- An open question that invites real debate (specific, not "Agree?")
- A quiet call to action — something they can actually do in the next 10 minutes
- A callback to the opening line that reframes it

Avoid a closing that announces itself ("So what's the takeaway?"). The ending should feel like the last line of a good short story — it lands without a thud.

---

## Reference Examples

These six posts were written for this skill to show the patterns above at full length. The people, firms and figures in them are invented. Study the rhythm, the specificity, and what each one leaves unsaid. They are models of structure, not text to reuse: a post built from the user's idea should share their shape and none of their sentences.

---

### Contrarian / Identity

> Most quarterly letters are written for the investor who might leave.
>
> The best ones are written for the investor who is staying.
>
> You can tell which is which by the second paragraph. One spends it explaining why the quarter wasn't the manager's fault. The other spends it on the position that went wrong, what the thesis was, and what changed.
>
> The first kind of letter gets skimmed. The second gets forwarded to the investment committee with a note that says "read this one."
>
> Nervous investors don't want reassurance. They want to see how you think when you're wrong.
>
> Write to the people who already trust you, and the others get what they needed too.

**What works:** Short declarative sentences that don't explain themselves. One concrete tell ("the second paragraph") carries the argument. The ending turns the opening around instead of repeating it.

---

### Process / Scroll-Stopper

> How to run a meeting people don't dread:
>
> 1. Send the decision you need in the invite. (Why am I in this room?)
> 2. Open with the answer you'd give today. (What do you already think?)
> 3. Spend the time on the two things you're unsure of. (Where do you need me?)
> 4. End when the decision is made, even at minute 12. (Can I have my afternoon back?)
>
> Nobody ever complained that a meeting ended early.

**What works:** The numbered list earns its place because each item answers the question the attendee is silently asking. Four items, not ten. The last line is dry, not a slogan.

---

### Contrarian / Credibility

> The memo that reads like it took an hour took three weeks.
>
> Every analyst learns this the hard way. My first investment memo ran 31 pages, and the partner who read it sent back one line: "What do you want me to do?"
>
> It stung. He was right. The recommendation was on page 19.
>
> Since then every draft gets what our team calls the Elevator Page: one sheet that has to survive a ride from the lobby to the 14th floor. If the Elevator Page doesn't hold, the other thirty don't matter yet.
>
> Getting to one page is slower than getting to thirty. It means deciding what you believe, which is the part the long version lets you postpone.
>
> So when a junior colleague hands over something short and sharp, the right question isn't "is this all?" Ask how long the cutting took.

**What works:** A coined term ("the Elevator Page") becomes the anchor the reader remembers. The admission is specific (31 pages, page 19) and brief, so it reads as experience and not confession. The close gives the reader a different question to ask on Monday.

---

### Practical / Value Delivery

> How to ask a senior person for a decision by email:
>
> Before: "Hi, hope you're well. Following up on the vendor discussion from a few weeks ago, there have been some developments and a couple of options have come up, each with pros and cons. Would love your thoughts when you have a moment."
>
> After: "Need your yes or no by Thursday: renew the current vendor for one year at the same price. I recommend yes. The alternative saves 8% but means a migration during year-end close. Two paragraphs of detail below if you want them."
>
> Same situation, same sender. The second one gets answered from a phone in the back of a car.
>
> The work is doing the thinking before you hit send, so the reader doesn't have to do it for you.

**What works:** The before/after makes an abstract skill concrete in ten seconds. Numbers and a deadline do the persuading. It teaches by showing, with one line of commentary at the end.

---

### Observation / Emotional Hook

> Most career advice on this platform has the same problem.
>
> It's written from the finish line.
>
> "Take the risk." "Bet on yourself." Easy to say once the bet has paid off. Nobody posts from month seven, when the savings are half gone and the first client hasn't signed.
>
> Some of that advice has come from me. It's embarrassing to reread.
>
> What would have helped at month seven was someone describing month seven: what they cut, who they called, what they told their family.
>
> If you're going to tell people to jump, show them the part of the fall you remember.

**What works:** The admission ("Some of that advice has come from me") earns the right to criticize. "Month seven" is a specific image doing the work a paragraph of explanation would otherwise do. The close is a practical instruction, not a platitude.

---

### Reframe / Curiosity Gap

> When people say they want a mentor, they usually picture the wrong person.
>
> Not someone twenty years ahead. Someone two.
>
> The person twenty years ahead tells you what worked in a market that no longer exists. The person two years ahead remembers which interview question tripped them up, what the first review was like, and who on the team answers email on Sundays.
>
> The best advice of my career came from an associate eighteen months my senior, over a sandwich, in about four minutes.
>
> Look for the people one rung up. They still remember the ladder.

**What works:** Opens by overturning the expected meaning of a familiar word. The contrast is carried by concrete details, not adjectives. The last line is an image, and it is short enough to quote.

---

## Workflow

When the user provides input (idea, notes, article, or rough draft), read the saved settings if there are any, then:

1. **Identify the real message** — what is the one true thing this person wants to say? Strip the content to its core claim.

2. **Choose the opening mode** — curiosity gap, contrarian, or value delivery. Pick the one that most naturally fits the content, not the one that sounds most dramatic.

3. **Write the hook (lines 1-3)** — treat this as its own deliverable. It must stand alone.

4. **Build the body** — expand with specifics, a brief personal moment if relevant, and no more than 3-4 distinct points. Use only facts, numbers and experiences the user supplied or the source contains; where a specific would help and none was given, ask for it or leave a marked placeholder instead of inventing one.

5. **Close cleanly** — one landing line, not a paragraph.

6. **Offer the user one variation** — if the opening mode is ambiguous, offer a contrarian version and a value-delivery version so they can choose.

---

## Output Format

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

Present:
- The full post, ready to copy/paste
- A brief note on which opening mode was used and why
- One optional alternate hook if the choice was close

Do not explain every structural decision unless the user asks. Keep the meta-commentary minimal.

The post is text for the user to publish themselves; the skill does not post to LinkedIn. If the settings include firm rules, apply them, and if the post touches something they cover (a client, performance, a live deal, a required review), say so in one line under the post.

---

## Example Prompts

> "Write a LinkedIn post from these notes: we cut our weekly reporting meeting from 60 minutes to 15 by sending the numbers the day before. Three things surprised me."

> "Set up linkedin-post-generator. I'm a COO at an asset manager writing for other operations leaders. Here are three of my past posts for voice. No emoji, no hashtags, never mention clients or fund performance."

> "Adapt this article for LinkedIn." [pastes article]
