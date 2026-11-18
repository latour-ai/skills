---
name: investment-folder-organizer
description: >-
  Organize a messy folder of investment files into a clean, standardized
  subfolder structure and rename every file with a consistent, sortable
  convention. For investment professionals who inherit or build deal and
  diligence folders: allocators reviewing a hedge fund, public-equity
  analysts, private equity deal teams, venture investors. Works on a local
  folder or a folder in connected file storage (SharePoint / OneDrive, Google
  Drive, Box, Dropbox), and is non-destructive: it copies originals into a new
  organized folder and does not move or delete them. Trigger on "organize this
  deal folder", "clean up these diligence files", "sort and rename these
  documents", "structure my data room", "put these investment files in
  order", "organize this fund's folder", or when the user shares a folder
  full of pitch decks, CIMs, financials, DDQs, term sheets, letters or memos
  and wants it made navigable. Do NOT use for organizing non-investment
  folders (photos, code repositories, personal documents). Do NOT use to
  analyze the documents themselves; use the cim-first-pass or
  hedge-fund-diligence skill.
license: MIT
metadata:
  author: latourai
  version: '2.0'
---

# Investment Folder Organizer

Turn a chaotic pile of investment files into a clean, predictable structure: eight
standardized subfolders plus a consistent, date-first filename convention, with a
generated index that doubles as an audit trail. Same structure for every investor
type — allocator, public-equity, PE, or VC — so the layout is learnable once and
reused forever.

**Non-destructive by design:** originals are not moved or deleted. Files are
copied into a new sibling folder, because a misfiled copy is easy to fix and a
lost original is not. If the user asks to move or replace files in place,
confirm that intention before doing anything irreversible.

**Where the folder lives.** The folder can be on the local filesystem or in
connected file storage (SharePoint / OneDrive, Google Drive, Box, Dropbox). A
cloud folder that is synced to the local machine is handled as a local folder.
For a folder reached through a storage connection, read the files there and
create the organized copy in the same parent location; shared drives are seen
by colleagues, so the preview in step 4 is confirmed by the user before
anything is written. If the storage isn't connected, can't be written to, or
fails partway, don't stop: deliver the full plan as a table (original path,
target folder, new filename, confidence, note) plus the index text, so the
user can apply it by hand, and say which system was unavailable.

## Workflow

### 1. Locate and scope the folder
Use the source folder the user named. If they haven't given one, ask. Then inventory
everything, including nested subfolders — these get flattened into the new
structure. List files with their type and size. For a local folder:

```bash
find "<source_folder>" -type f -not -name '.*' -printf '%P\t%s bytes\n' | sort
```

For a folder in connected storage, list its contents through that connection.

Note the likely investor context (fund / public co / private co / startup) from the
filenames and the user's framing. It informs DocType choices but not the folder
structure, which is the same eight folders for every asset class.

### 2. Read enough of each file to classify it
Classify on content first, filename second — investment files are notoriously
mislabeled (`Project Atlas v3 FINAL.pdf` could be anything), and fixing bad names is
the point of the exercise. The whole file is rarely needed; the first page / first
slide / first sheet plus the filename is typically decisive. Read more only when torn.

- PDFs: read the first page or two (extract the text, or render the page as an
  image if it is a scan).
- Office files (.docx/.pptx/.xlsx): use whatever document-reading tools are
  available, or extract the text; the title slide, document heading, or first sheet
  usually suffices.
- Sample large files — don't burn context reading a 300-page data dump end to end.

Read `references/taxonomy.md` for the folder definitions, the content-based
classification tie-breakers (e.g. Marketing vs. Research, Financials vs. Legal), and
the full DocType vocabulary. Consult it whenever a placement is non-obvious. If that
file isn't present in this installation, classify from the folder table in step 3.

### 3. Build the plan
For every file, decide three things: which of the eight folders, the new filename,
and a confidence level. Assemble them into a plan JSON (schema in the script header
and below). Set `confidence` to `medium`/`low` and add a one-line `note` for anything
you're unsure about; route genuinely unclassifiable files to `99_Unsorted`. These
get surfaced in the index for the user to review, which is far better than a
confident misfile.

The eight folders (defined fully in `references/taxonomy.md`):

| Folder | Holds |
| --- | --- |
| `01_Overview_and_Marketing` | What the target produced to present itself: decks, CIMs, tear sheets, teasers |
| `02_Financials` | Statements, models, projections, cap tables, track record, 10-K/10-Q |
| `03_Due_Diligence` | DDQs, ODD/DD reports, reference & background checks |
| `04_Legal_and_Compliance` | LPAs, term sheets, SPAs, SAFEs, NDAs, ADV, proxies |
| `05_Research_and_Analysis` | IC/deal memos, theses, valuation work, market & expert research |
| `06_Communications` | Investor letters, founder updates, call transcripts, meeting notes, emails |
| `07_Reference` | Bios, org charts, background, press |
| `99_Unsorted` | Anything not confidently classified |

**Naming:** `YYYY-MM-DD_DocType_Descriptor.ext` — date first (use the content date,
fall back to file mtime), PascalCase DocType, short hyphenated descriptor, no
company/fund name (the parent folder carries it). Full rules and examples are in
`references/taxonomy.md`.

### 4. Preview, then execute
Show the user a compact summary of the plan before copying — counts per folder and
any files headed to `99_Unsorted` or flagged low-confidence. Invite a
quick correction. For a small set you can list every rename; for a large set, show
the per-folder counts plus the flagged items and a handful of representative renames.

To preview mechanically without copying, run the script with `--dry-run`.

Write the plan to a JSON file, then run the executor. By default the output folder is
a sibling named `<SourceName> (Organized)`:

```bash
python scripts/organize.py --plan /path/to/plan.json
# add --dry-run first if you want a no-write preview
```

The script handles the deterministic, error-prone parts so you don't have to:
canonicalizing folder names, sanitizing filenames, preserving extensions, resolving
name collisions (`-2`, `-3`, …), copying with `copy2`, and writing `00_INDEX.md`.

The script works on local paths. If it isn't present in this installation, or the
folder is in connected storage, do the same job directly: create the eight folders,
copy each file under its new name with its extension and modified date preserved,
add `-2`, `-3` to colliding names, and write `00_INDEX.md` listing every file's
original path, new location, confidence and note, with a "Needs review" section for
unsorted and low- or medium-confidence items.

### 5. Present the result
Point the user to the new folder and `00_INDEX.md`. Call out the **Needs
review** section — the unsorted and low-confidence files — and offer to re-file any
of them based on the user's steer. If they correct a placement, edit the plan and
re-run (re-running into a fresh output folder is cheap and clean).

Length follows the substance: cover what the task needs and leave out filler sections, restated summaries, and boilerplate.

## Plan JSON shape

```json
{
  "source_root": "/abs/path/to/messy/folder",
  "output_root": "/abs/path/to/Target (Organized)",
  "subject": "Acme Capital — Flagship Fund",
  "investor_context": "hedge fund allocator",
  "items": [
    {
      "source": "subdir/Q3 letter FINAL.pdf",
      "folder": "06_Communications",
      "new_name": "2024-09-30_InvestorLetter_Q3-2024.pdf",
      "confidence": "high",
      "note": ""
    }
  ]
}
```

- `source` is relative to `source_root` (absolute paths also accepted).
- `folder` accepts the canonical name or a short alias (`Financials`, `02`, `legal`…);
  unknown values are routed to `99_Unsorted` and flagged.
- `confidence` is `high` | `medium` | `low` (default `high`).
- `note` is optional but always shown in the index for unsorted/low/medium items.
