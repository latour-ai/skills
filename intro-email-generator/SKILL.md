---
name: intro-email-generator
description: "Generate warm introduction emails connecting two people via Gmail draft. Use this skill whenever the user wants to introduce two people over email, says things like 'intro email for X and Y', 'connect these two people', 'make an intro between', 'draft an intro email', 'write an email introduction', or provides two LinkedIn profile URLs and asks to connect them. This skill researches both parties, formats a structured introduction with their names, titles, company hyperlinks, company descriptions, and social/web links, then drafts the email directly in Gmail via the Gmail MCP. Trigger even if the user just pastes two LinkedIn URLs without explicit instructions."
---
 
# Intro Email Generator
 
Generate polished, warm introduction emails connecting two people. Researches both parties, assembles structured profiles, and drafts directly into Gmail.
 
## Inputs Required
 
The user must provide:
1. **LinkedIn URLs** for both Person A and Person B
2. **Reason for connecting** — a sentence or phrase explaining why this intro is valuable
If the reason for connecting is missing, ask for it before proceeding.
 
---
 
## Step 1: Research Both Parties
 
For each person, use `web_search` to gather:
 
| Field | Source |
|-------|--------|
| Full name | LinkedIn profile |
| Title | LinkedIn profile |
| Company name | LinkedIn profile |
| Company URL | Company website (for hyperlinking) |
| Company description | 1-sentence summary of what the company does |
| Twitter/X handle | Search "[Name] Twitter" or "[Name] X profile" |
| Personal website/homepage | Search "[Name] personal site" or check LinkedIn bio |
 
Do not guess URLs — only include links that are confirmed through search.
 
---
 
## Step 2: Assemble the Email
 
### Subject Line
`Intro: [Person A First Name] <> [Person B First Name]`
 
### Body Structure
 
```
Hi [Person A First Name] and [Person B First Name],
 
[One-sentence greeting that states WHY you're making this connection — tie it to a shared goal, mutual benefit, or opportunity.]
 
[Person A Full Name]
• [Title] at [Company Name as hyperlink to company URL]
• [1-sentence company description]
LinkedIn: [LinkedIn URL]
[Twitter: Twitter URL — only if confirmed]
[Web: Personal site URL — only if confirmed]
 
[Person B Full Name]
• [Title] at [Company Name as hyperlink to company URL]
• [1-sentence company description]
LinkedIn: [LinkedIn URL]
[Twitter: Twitter URL — only if confirmed]
[Web: Personal site URL — only if confirmed]
 
I'll let you two take it from here!
 
[sign-off]
```
 
### Formatting Rules
- Company name in the bullet must be a clickable hyperlink (use HTML `<a>` tag when drafting via Gmail MCP, or standard markdown link `[Company](URL)` when composing)
- LinkedIn, Twitter, and personal site links appear as labeled bare URLs on their own lines (e.g., `LinkedIn: [URL]`) — only include links that were confirmed through research
- Do NOT fabricate any URLs — if a Twitter or personal site is not found, omit the line entirely
- Keep the company description to one sentence, focused on what the company does (not fluffy adjectives)
- The greeting sentence should be specific and warm — reference the actual reason for connecting, not a generic "I think you two should meet"
---
 
## Step 3: Draft in Gmail
 
Use the **Gmail MCP** (`Gmail:create_draft`) to create the draft.
 
### Gmail Draft Parameters
- `to`: Leave blank (or ask the user if they want to pre-populate recipients)
- `subject`: `Intro: [Person A First Name] <> [Person B First Name]`
- `body`: Full email body as composed above
After successfully creating the draft, tell the user:
> "Draft created in Gmail — subject: *Intro: [A] <> [B]*. You can open it, add recipients, and send when ready."
 
---
 
## Edge Cases
 
| Situation | Handling |
|-----------|----------|
| Twitter not found | Omit the Twitter line entirely |
| Personal site not found | Omit the Web line entirely |
| Company URL not found | Use company name as plain text, not a hyperlink |
| LinkedIn URL is a vanity URL (not full profile) | Use as-is; it's still a valid link |
| User doesn't provide reason for connecting | Ask before drafting: "What's the reason you're connecting these two?" |
| Gmail draft fails | Output the full email as formatted text so user can copy-paste manually |
 
---
 
## Sign-off
 
Always sign off as:
```
All the best,
[Your Name]
```
 
No title or company tagline needed for intro emails — keep it personal.