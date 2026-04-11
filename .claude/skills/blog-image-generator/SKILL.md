---
name: blog-image-generator
description: Generates styled SVG hero images for mattjones.technology blog posts. Use whenever the user asks to create a blog image, blog header, blog hero image, or post image for their blog. Also trigger when the user shares a blog post draft and asks for an image to go with it, or says they need a graphic/visual for a blog post. Produces a polished typographic SVG with the post title over a styled geometric background.
---

# Blog Image Generator for mattjones.technology

Creates visually striking SVG hero images for blog posts. The images feature the blog post title rendered over a styled geometric background. No AI image generation needed — these are clean, typographic, code-generated designs.

## Output Specs

- **Format**: SVG (saved as .svg)
- **Dimensions**: 1200×630 viewBox (standard social sharing / Open Graph size)
- **Location**: Save to `/mnt/user-data/outputs/`

## Workflow

1. **Extract the title** from the user's message or blog post content. If the title is unclear, ask.
2. **Pick a visual theme** that fits the post's subject matter. Choose from the palette and pattern options below, or invent a new combination that fits the content. Vary the theme each time — don't repeat the same look across posts.
3. **Generate the SVG** using the generation script at `scripts/generate.py`.
4. **Present the file** to the user.

## Running the Script

```bash
cd /path/to/this/skill
python3 scripts/generate.py \
  --title "Your Blog Post Title Here" \
  --theme THEME_NAME \
  --output /mnt/user-data/outputs/blog-image.svg
```

### Available Themes

| Theme | Vibe | Good for |
|-------|------|----------|
| `circuit` | Tech circuit board traces, nodes | Software engineering, architecture, AI |
| `grid` | Isometric grid with floating elements | Systems, infrastructure, cloud |
| `waves` | Layered wave forms | Culture, ministry, reflection |
| `geo` | Bold geometric shapes, overlapping | Strategy, leadership, methodology |
| `nodes` | Connected node network / constellation | Teams, collaboration, networks |
| `topo` | Topographic contour lines | Planning, exploration, depth |

### Theme Selection Guide

- **AI / Software / Claude**: `circuit` or `nodes`
- **Architecture / Systems**: `grid` or `circuit`
- **Agile / Teams / Process**: `geo` or `nodes`
- **Ministry / Faith / Reflection**: `waves` or `topo`
- **Scouting / Outdoors**: `topo` or `waves`
- **General / Mixed**: `geo`

If none of the built-in themes feel right for the content, you can also pass `--colors` with 3-4 hex colors to override the theme's palette, e.g.:
```bash
--colors "#1a1a2e,#16213e,#0f3460,#e94560"
```

## Title Text Handling

The script automatically handles:
- Word wrapping for long titles (breaks at ~28 chars per line)
- Font sizing that scales down for longer titles
- Proper vertical centering of wrapped text
- A subtle text shadow/backdrop for readability

## After Generation

Suggest a filename based on the post slug (e.g., `agile-playbook.svg`). Remind the user they may want to convert to PNG for their blog if needed (`inkscape`, `rsvg-convert`, or browser screenshot).
