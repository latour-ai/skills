# Icon library

Twelve line icons in one consistent style (24×24 grid, 1.2 stroke, round caps and joins, no fill). Each uses `stroke="currentColor"`, so it inherits text color and works in light and dark mode.

## Rules
- Use these icons before drawing new ones. Only draw a new icon when none of the twelve fits, and match the style: 24×24 viewBox, stroke-only, `stroke-width:1.2`, round caps/joins.
- Don't mix in the older, heavier icons from `assets/example-deck.html` on the same slide; when a slide uses icons, use this set.
- Icons support a label, never replace one. Every icon sits next to a word.
- Size: 28–48px on content slides; up to 64px for a single hero icon. Keep one size per row.
- Color: ink by default. The icon on the slide's accent element turns `var(--on-hl)` (white on the accent color); never color an icon in the accent on its own, since that adds a second accent.
- In HTML decks, paste the inline markup below and add this CSS once to the deck. In PowerPoint or Google Slides, insert the same SVG as an image or icon, keeping the stroke style and one size per row:

```css
.ico{width:36px;height:36px;flex:none;fill:none;stroke:currentColor;stroke-width:1.2;stroke-linecap:round;stroke-linejoin:round;color:var(--ink)}
.on .ico,.icard.on .ico{color:var(--on-hl)}
```

## Icons

### `email-envelope`
Use for: email, inbox triage, outreach, client correspondence

```html
<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 11v5a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h12q2 0 .4 1.2l-5.2 3.9q-1.2.9-2.4 0L7 8.25"/></svg>
```

### `calendar`
Use for: scheduling, meeting prep, deadlines, recurring cadence

```html
<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 13v5a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v1M8 4v4m8-4v4M4 11h11M15 16h2"/></svg>
```

### `document-page`
Use for: memos, notes, write-ups, generic documents

```html
<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M19 11v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h6.9a2 2 0 0 1 1.4.6l3.1 3.1M9 10h3m-3 4h6"/></svg>
```

### `pdf-file`
Use for: PDFs, CIMs, decks received, filings, data-room files

```html
<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 4h8a2 2 0 0 1 2 2v9.2q0 .8-.6 1.4l-2.8 2.8q-.6.6-1.4.6H9a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2M15 20v-2a2 2 0 0 1 2-2h2M4 8v10q0 2 2 2"/></svg>
```

### `hyperlink-chain`
Use for: links, connectors, integrations, sources tied together

```html
<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="m10 8 3-3a4.25 4.25 0 0 1 6 6l-3 3M14 16l-3 3a4.25 4.25 0 0 1-6-6l3-3m1 5 6-6"/></svg>
```

### `spreadsheet`
Use for: Excel, models, trackers, tabular data

```html
<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 13v5a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v1q0 2-2 2H4m6 0v11m-6-6h12"/></svg>
```

### `ai-agent`
Use for: an AI agent, assistant, or autonomous step

```html
<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="2.5"/><path d="M18.4 8.8a7.2 7.2 0 1 1-5.2-3.9"/><circle cx="17.5" cy="5.8" r="1.5"/></svg>
```

### `data-analysis-chart`
Use for: analysis, metrics, KPIs, charts

```html
<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 17v-4m7 4V6m7 11V9M4 21h16"/><path d="M10 3h4"/></svg>
```

### `workflow-automation`
Use for: workflows, pipelines, multi-step automation, skills

```html
<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><circle cx="5" cy="5" r="2"/><circle cx="19" cy="19" r="2"/><path d="M7 5h7a3.5 3.5 0 0 1 0 7h-4a3.5 3.5 0 0 0 0 7h5m-2-2 2 2-2 2"/></svg>
```

### `document-search`
Use for: research, diligence, search across documents, retrieval

```html
<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M10 20H7a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v3M9 8h4"/><circle cx="16" cy="15" r="4"/><path d="m19 18 3 3"/></svg>
```

### `team-training`
Use for: training sessions, workshops, team enablement

```html
<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h12a2 2 0 0 1 2 2v4M8 8h6M3 21v-1a3 3 0 0 1 6 0v1m5 0v-1a3 3 0 0 1 6 0v1"/><circle cx="6" cy="13" r="1.6"/><circle cx="17" cy="13" r="1.6"/></svg>
```

### `investment-growth`
Use for: returns, performance, growth, investment outcomes

```html
<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h16M4 16l4-4q1-1 2-.5l2 1q1 .5 1.8-.5L20 4m-5 0h3.5q1.5 0 1.5 1.5V9"/></svg>
```
