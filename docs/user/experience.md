# Experience Content Front Matter

Experience entries live under `content/experience` and use YAML front matter with the following fields:

| Field | Description |
| ----- | ----------- |
| `name` | Name of the employer or project. |
| `url` | External link for additional information. |
| `position` | Job title or role. |
| `duration` | Time period for the role (for example, `2015–2017`). |
| `summary` | Short HTML or Markdown list of achievements. Use the `|` operator for multi-line content. |
| `weight` | Integer used for ordering. Lower numbers appear first. |

## Ordering

Entries are sorted by ascending `weight`. Give later items larger weights or leave gaps (10, 20, 30) to simplify future insertions. Files with the same weight fall back to alphabetical ordering by filename.

## Previewing

You can preview the site locally to check how your experience entries render and sort:

```bash
hugo server
```

Open `http://localhost:1313` in your browser to view the site. Hugo watches files and reloads automatically; add `-D` to include drafts or `--disableFastRender` to ensure all changes are rendered.
