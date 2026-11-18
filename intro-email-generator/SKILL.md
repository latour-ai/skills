---
name: intro-email-generator
description: >-
  Write a warm introduction email connecting two people and save it as a
  draft in the user's mail system: Microsoft 365 (Outlook) or Google
  Workspace (Gmail), or as copy-paste text when no mailbox is connected.
  Researches both parties from public sources, then formats a structured
  introduction with each person's name, title, company link, one-sentence
  company description, and confirmed profile links. The user's sign-off,
  closing line and mail system are set once in a short first-run setup. For
  business development, investor relations, fundraising and any professional
  who makes introductions often. Trigger on "intro email for X and Y",
  "connect these two people", "make an intro between", "draft an intro
  email", "write an email introduction", "set up intro-email-generator",
  "change my intro-email-generator settings", or when the user pastes two
  LinkedIn URLs or two names with firms, even without further instruction.
  Do NOT use to find who at the firm can make an introduction; use the
  network-referral-path-mapper skill. Do NOT use for a briefing on one person
  before a meeting; use the professional-profile-brief skill. The email is
  always a draft and is never sent.
license: MIT
metadata:
  author: latourai
  version: '2.0'
---

# Intro Email Generator

Generate polished, warm introduction emails connecting two people. The skill researches both parties, assembles structured profiles, and saves the email as a draft in the user's mail system.

## Inputs Required

1. **Who the two people are.** For each person, any of: a LinkedIn URL, a name with their firm, or a pasted bio or profile.
2. **Reason for connecting:** a sentence or phrase explaining why this intro is valuable. If it is missing, ask for it before drafting ("What's the reason you're connecting these two?"). The opening line depends on it and a guessed reason can embarrass the user with both recipients.

**Set once in setup (step 0):** mail system, the user's sign-off and name, the closing line, and whether to fill in recipients.

---

## Step 0: First-run setup (once, then only when asked)

Run setup the first time the skill is used, or when the user says "set up intro-email-generator" or "change my intro-email-generator settings". Look first for a saved `intro-email-generator-settings.md` in the project's files or the skill's working folder. If it exists, read it and skip setup.

1. **Detect before asking.** Check which mail system is connected, and pre-fill the user's name from the mail account if it is available.
2. **Ask, in one message, with defaults:**
   - **Mail system for drafts:** Microsoft 365 (Outlook), Google Workspace (Gmail), or none (the email is returned as text to copy).
   - **Sign-off:** default "All the best," followed by the user's first name. No title or company tagline unless the user wants one; intro emails read better when they stay personal.
   - **Closing line:** default "I'll let you two take it from here!"
   - **Recipients:** leave the To line blank (default), or fill it in when the user supplies both email addresses.
3. **Save the settings** to `intro-email-generator-settings.md` in plain language the user can edit. If nothing persistent can be written, show the settings as a short block and tell the user to paste it into their project instructions.
4. **Continue straight into the introduction** if the user gave the two people and a reason.

On later runs, read the settings and do not re-ask. Setup never blocks a run: if the user says "skip setup", use the defaults and return the email as text.

---

## Step 1: Research Both Parties

For each person, search the web and read the public sources found to gather:

| Field | Source |
|-------|--------|
| Full name | LinkedIn profile or the pasted bio |
| Title | LinkedIn profile, company bio page |
| Company name | LinkedIn profile, company bio page |
| Company URL | Company website (for hyperlinking) |
| Company description | 1-sentence summary of what the company does |
| X (Twitter) handle | Search "[Name] X profile" |
| Personal website | Search "[Name] personal site" or check the profile's bio |

Include only links confirmed through research. If a profile can't be read (LinkedIn often blocks automated access), use what the user pasted and other public pages, and say which fields could not be confirmed.

---

## Step 2: Assemble the Email

### Subject Line
`Intro: [Person A First Name] <> [Person B First Name]`

### Body Structure

```
Hi [Person A First Name] and [Person B First Name],

[One-sentence greeting that states why you're making this connection: a shared goal, mutual benefit, or opportunity.]

[Person A Full Name]
• [Title] at [Company Name as hyperlink to company URL]
• [1-sentence company description]
LinkedIn: [LinkedIn URL]
[X: profile URL, only if confirmed]
[Web: personal site URL, only if confirmed]

[Person B Full Name]
• [Title] at [Company Name as hyperlink to company URL]
• [1-sentence company description]
LinkedIn: [LinkedIn URL]
[X: profile URL, only if confirmed]
[Web: personal site URL, only if confirmed]

[Closing line from setup]

[Sign-off from setup]
```

### Formatting Rules
- The company name in the bullet is a clickable hyperlink (an HTML link in a mail draft, a standard markdown link `[Company](URL)` when the email is returned as text).
- LinkedIn, X and personal site links appear as labeled bare URLs on their own lines (e.g., `LinkedIn: [URL]`).
- Keep the company description to one sentence about what the company does, without promotional adjectives.
- The greeting sentence is specific and warm. It references the actual reason for connecting, not a generic "I think you two should meet".
- The email contains only what the user said and what public sources confirm. Private details about either person stay out unless the user supplied them for this email.

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

---

## Step 3: Save the Draft

Create a draft in the mail system from setup, with the subject line above, the full body, and the To line handled as setup says. The skill creates the draft only; the user adds or checks recipients and sends.

After creating the draft, tell the user:
> "Draft created in [Outlook / Gmail], subject: *Intro: [A] <> [B]*. You can open it, add recipients, and send when ready."

If no mail system is connected, or creating the draft fails, return the full email as formatted text to copy and say which system was unavailable.

---

## Edge Cases

| Situation | Handling |
|-----------|----------|
| X profile not found | Omit the X line entirely |
| Personal site not found | Omit the Web line entirely |
| Company URL not found | Use the company name as plain text, not a hyperlink |
| LinkedIn URL not given and not found | Omit the LinkedIn line; don't construct a URL from the name |
| LinkedIn URL is a vanity URL (not the full profile) | Use as-is; it's still a valid link |
| Two people share the name and the firm doesn't settle it | Ask which one before drafting |

## Example prompts

> "Intro email for Priya Raman, COO at Larkfield Partners, and Tomas Ek, who runs data at Brightwater Analytics. Priya is rebuilding their reporting stack and Tomas did the same thing last year."

> "Set up intro-email-generator. Drafts go to Outlook, sign off as 'Best, Sam', and keep the default closing line."
