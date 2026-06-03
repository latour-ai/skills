---
name: professional-profile-brief
description: "Prepare a busy executive for a meeting, introduction, networking conversation, or professional interaction by quickly explaining who a person is and how to open the conversation well. Use this skill whenever the user says things like 'brief me on [Name]', 'I'm meeting [Name] tomorrow', 'prep me for a meeting/intro with this person', 'help me understand this person's background', 'profile brief', 'pre-meeting prep', or pastes a LinkedIn profile, bio, company page, article, podcast page, calendar invite, meeting notes, or email and wants to understand the person before talking to them. Trigger even if the user just drops a name or a LinkedIn URL plus a meeting context. This is for understanding an individual person, not for fund-manager diligence calls or company research — those belong to the diligence and company-research skills. It is NOT a sales-automation, scraping, or bulk-prospecting tool and does NOT draft outreach by default."
---

# Professional Profile Brief

Produce a concise, relationship-aware prep note that helps a busy executive walk into a meeting understanding who the other person is, why they matter, and how to open the conversation naturally. The output should read like an executive assistant's pre-meeting brief — specific, useful, and professionally appropriate — not a sales script and not a dossier.

## Inputs

Accept any of the following, in any combination:
- A person's name and/or LinkedIn URL
- Pasted profile text, bio, or company "About" page
- An article, interview, or podcast appearance
- A calendar invite, email thread, or prior meeting notes
- Any user-provided background

The meeting context (what the meeting is for) makes the brief sharper. If it's missing and not obvious, you can still produce the brief — just note in the relevant sections what context would tighten it.

## Sourcing

Use any relevant source available to you, prioritizing primary and authoritative ones:
- LinkedIn profile and recent LinkedIn posts
- Company website and the person's bio page
- Personal website
- Podcast appearances, articles, and interviews
- General web/search results
- Public professional databases
- User-provided notes, emails, prior meeting notes, calendar invites

If browser, Chrome, or MCP tools are available, use them to review **public** information. If `web_search` is available, use it to confirm current role, company, and any notable recent activity rather than relying on memory.

**Only include a fact if it is sourced.** Do not guess URLs, titles, or affiliations. If you can't confirm something, it belongs in "Unknowns / Things to Confirm," not in the body.

## Hard Rules (non-negotiable)

These protect the user's reputation and the subject's privacy. A brief that crosses these lines is worse than no brief.

- Use **public information only**.
- Do **not** scrape LinkedIn or any site in bulk; do not collect or export contact lists.
- Do **not** automate connection requests or messages.
- Do **not** fabricate mutual connections. If you can't verify a shared connection, don't claim one.
- Do **not** infer sensitive personal attributes (e.g., health, religion, ethnicity, sexual orientation, political affiliation, family status).
- Do **not** include private personal details unless the user provided them and they are professionally relevant.
- Do **not** use creepy personalization, manufactured familiarity, or flattery.
- Do **not** guess about someone's personal life or overconfidently psychologize them.
- Do **not** write "I saw on LinkedIn..." unless the information was actually sourced from LinkedIn. Attribute honestly.

## Output

Keep the final brief to **500 words maximum** unless the user explicitly asks for more depth. Use a neutral, executive-assistant voice: concise, specific, free of filler, no hype. Do **not** include an outreach draft unless the user explicitly asks for one.

ALWAYS use this exact section structure:

```markdown
# Professional Profile Brief: [Person Name]

## 1. Summary
[2–4 sentences: who they are and why they matter for this meeting.]

## 2. Current Role
- **Title:** [current title]
- **Company:** [company]
- **Likely responsibilities / scope:** [based only on available info]

## 3. Company Description
[1–3 sentences: what the company does and why it may matter for the conversation.]

## 4. Career Background
[Their professional arc: notable roles, transitions, industries, recurring themes, accomplishments.]

## 5. What They Likely Care About
[INFERENCE. Open with framing like "Based on their role and public activity, they may care about…" Do not present inferred motivations as fact.]

## 6. Relationship Hooks
[Specific, verifiable connection points only. See list below. Omit the section's bullets you can't support; if none, say so plainly.]

## 7. Conversation Angles
[3–5 specific ways to open or guide the conversation. Relationship-building, not selling.]

## 8. Smart Questions
[3–5 thoughtful, person-specific questions grounded in their background. No generic questions.]

## 9. Unknowns / Things to Confirm
[What is unclear or should not be assumed.]

## 10. Sources Used
[Each source by name, with date where available. If sources were limited, say so.]
```

### Section guidance

- **Section 5 must be clearly labeled as inference.** Tie every inference to something observable (a role, a post, an interview), and phrase it as a possibility, not a finding.
- **Section 6 (Relationship Hooks)** — useful, verifiable connection points such as: shared companies, schools, cities, investors, or industries; mutual connections (only if real); similar career transitions; recent posts or ideas; public professional interests. Include a personal detail only if it is professionally appropriate **and** publicly available or user-provided. When in doubt, leave it out.
- **Section 7 vs. Section 8** — angles are openers and threads to pull on; questions are specific things to actually ask. Both should be impossible to copy-paste into a brief for a different person.

## No-Access Mode

If you cannot reach LinkedIn or browser tools, still help — don't stall.

1. Use whatever other public sources you can reach.
2. Use all user-provided context.
3. Produce a **lightweight** version of the brief using the same structure, filling what you can and being explicit about thin sections.
4. Close by inviting the user to paste the LinkedIn profile, bio, company page, recent article, or calendar invite for a stronger brief — name the specific input that would help most.

## Quality Checks

Before returning the brief, confirm:
- [ ] 500 words or fewer (unless the user asked for more).
- [ ] It actually helps the user open the meeting well.
- [ ] It reads like an executive-assistant prep note — neutral, specific, no filler or flattery.
- [ ] Relationship hooks are specific and professionally appropriate.
- [ ] Inferences (esp. Section 5) are labeled as inferences, not stated as fact.
- [ ] No sensitive personal attributes are inferred.
- [ ] No private or creepy details included.
- [ ] No mutual connections fabricated.
- [ ] No outreach draft unless explicitly requested.
- [ ] Sources are listed; unknowns are clearly separated from facts.

## Example User Prompts

- "Use this skill to brief me on Jane Doe. I'm meeting her tomorrow and want to understand her background and how to open the conversation."
- "Create a professional profile brief from this LinkedIn profile and company bio." [pastes both]
- "Use this person's bio, recent article, and calendar invite to prep me for a 30-minute meeting."
- "LinkedIn is blocked, but here's their company bio and a few notes. Make the best lightweight brief you can."
