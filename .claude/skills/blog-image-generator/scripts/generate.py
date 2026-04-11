#!/usr/bin/env python3
"""Generate styled SVG hero images for mattjones.technology blog posts."""

import argparse
import hashlib
import math
import random
import textwrap
import html

# ── Theme palettes ──────────────────────────────────────────────────────────
# Each theme: (bg_color, accent1, accent2, accent3, text_color)
THEMES = {
    "circuit": {
        "colors": ["#0a192f", "#112240", "#1d3557", "#00d4aa", "#e6f1ff"],
        "text": "#e6f1ff",
        "accent": "#00d4aa",
    },
    "grid": {
        "colors": ["#1a1a2e", "#16213e", "#0f3460", "#53a8b6", "#e2e2e2"],
        "text": "#e2e2e2",
        "accent": "#53a8b6",
    },
    "waves": {
        "colors": ["#2d1b69", "#3a1d8e", "#5c3d99", "#e8a87c", "#f1f1f1"],
        "text": "#f1f1f1",
        "accent": "#e8a87c",
    },
    "geo": {
        "colors": ["#0b0c10", "#1f2833", "#c5c6c7", "#66fcf1", "#45a29e"],
        "text": "#c5c6c7",
        "accent": "#66fcf1",
    },
    "nodes": {
        "colors": ["#141e30", "#243b55", "#2a5298", "#e8b84b", "#f0f0f0"],
        "text": "#f0f0f0",
        "accent": "#e8b84b",
    },
    "topo": {
        "colors": ["#1b2a1b", "#2d4a2d", "#3e6b3e", "#a8d5a2", "#f0f4ef"],
        "text": "#f0f4ef",
        "accent": "#a8d5a2",
    },
}

W, H = 1200, 630


def seed_from_title(title: str) -> int:
    return int(hashlib.md5(title.encode()).hexdigest()[:8], 16)


def wrap_title(title: str, max_chars: int = 28) -> list[str]:
    """Word-wrap title, respecting long words."""
    words = title.split()
    lines: list[str] = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        if len(test) <= max_chars:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def font_size_for_lines(n_lines: int, max_line_len: int) -> int:
    """Pick font size based on content volume."""
    if n_lines <= 1 and max_line_len <= 20:
        return 64
    if n_lines <= 2:
        return 56
    if n_lines <= 3:
        return 48
    return 40


# ── Pattern generators ──────────────────────────────────────────────────────

def gen_circuit(rng, colors):
    bg, c1, c2, accent, _ = colors
    elements = []
    # Gradient background
    elements.append(f'''<defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{bg}"/>
      <stop offset="100%" stop-color="{c1}"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>''')

    # Circuit traces
    for _ in range(18):
        x = rng.randint(0, W)
        y = rng.randint(0, H)
        length = rng.randint(60, 250)
        horizontal = rng.choice([True, False])
        opacity = rng.uniform(0.08, 0.25)
        x2 = x + length if horizontal else x
        y2 = y if horizontal else y + length
        elements.append(
            f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" '
            f'stroke="{accent}" stroke-width="2" opacity="{opacity:.2f}"/>'
        )
        # Node at end
        elements.append(
            f'<circle cx="{x2}" cy="{y2}" r="4" fill="{accent}" opacity="{opacity:.2f}"/>'
        )

    # Larger glowing nodes
    for _ in range(8):
        cx = rng.randint(50, W - 50)
        cy = rng.randint(50, H - 50)
        r = rng.randint(3, 8)
        opacity = rng.uniform(0.15, 0.5)
        elements.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{accent}" opacity="{opacity:.2f}"/>'
        )
        elements.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r * 3}" fill="{accent}" opacity="{opacity * 0.15:.3f}"/>'
        )

    # Corner accent bracket (top-left)
    elements.append(
        f'<polyline points="40,100 40,40 100,40" fill="none" '
        f'stroke="{accent}" stroke-width="2" opacity="0.4"/>'
    )
    # Bottom-right bracket
    elements.append(
        f'<polyline points="{W-40},{H-100} {W-40},{H-40} {W-100},{H-40}" fill="none" '
        f'stroke="{accent}" stroke-width="2" opacity="0.4"/>'
    )
    return "\n  ".join(elements)


def gen_grid(rng, colors):
    bg, c1, c2, accent, _ = colors
    elements = []
    elements.append(f'''<defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0.5" y2="1">
      <stop offset="0%" stop-color="{bg}"/>
      <stop offset="100%" stop-color="{c1}"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>''')

    # Isometric grid lines
    spacing = 50
    for i in range(-10, 30):
        x = i * spacing
        opacity = rng.uniform(0.04, 0.12)
        elements.append(
            f'<line x1="{x}" y1="0" x2="{x + H * 0.5}" y2="{H}" '
            f'stroke="{c2}" stroke-width="1" opacity="{opacity:.2f}"/>'
        )
        elements.append(
            f'<line x1="{x}" y1="0" x2="{x - H * 0.5}" y2="{H}" '
            f'stroke="{c2}" stroke-width="1" opacity="{opacity:.2f}"/>'
        )

    # Floating cubes / rectangles
    for _ in range(6):
        x = rng.randint(50, W - 100)
        y = rng.randint(50, H - 100)
        w = rng.randint(30, 80)
        h = rng.randint(30, 80)
        opacity = rng.uniform(0.08, 0.2)
        elements.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
            f'fill="none" stroke="{accent}" stroke-width="1.5" '
            f'opacity="{opacity:.2f}" rx="2"/>'
        )

    # Accent dots at intersections
    for _ in range(12):
        cx = rng.randint(0, W)
        cy = rng.randint(0, H)
        elements.append(
            f'<circle cx="{cx}" cy="{cy}" r="3" fill="{accent}" opacity="0.2"/>'
        )

    return "\n  ".join(elements)


def gen_waves(rng, colors):
    bg, c1, c2, accent, _ = colors
    elements = []
    elements.append(f'''<defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{bg}"/>
      <stop offset="60%" stop-color="{c1}"/>
      <stop offset="100%" stop-color="{c2}"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>''')

    # Layered wave curves
    for i in range(5):
        y_base = 150 + i * 100
        amplitude = rng.uniform(20, 50)
        freq = rng.uniform(0.003, 0.008)
        phase = rng.uniform(0, math.pi * 2)
        opacity = 0.06 + i * 0.03
        points = []
        for x in range(0, W + 10, 10):
            y = y_base + math.sin(x * freq + phase) * amplitude
            points.append(f"{x},{y:.1f}")
        path_d = "M" + " L".join(points)
        color = accent if i == 3 else c2
        elements.append(
            f'<path d="{path_d}" fill="none" stroke="{color}" '
            f'stroke-width="1.5" opacity="{opacity:.2f}"/>'
        )

    # Soft circles
    for _ in range(5):
        cx = rng.randint(0, W)
        cy = rng.randint(0, H)
        r = rng.randint(50, 150)
        elements.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{accent}" opacity="0.03"/>'
        )

    return "\n  ".join(elements)


def gen_geo(rng, colors):
    bg, c1, _, accent, accent2 = colors
    elements = []
    elements.append(f'''<defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{bg}"/>
      <stop offset="100%" stop-color="{c1}"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>''')

    # Large geometric shapes
    for _ in range(4):
        shape = rng.choice(["circle", "rect", "triangle"])
        opacity = rng.uniform(0.05, 0.15)
        color = rng.choice([accent, accent2])
        if shape == "circle":
            cx = rng.randint(-100, W + 100)
            cy = rng.randint(-100, H + 100)
            r = rng.randint(80, 250)
            elements.append(
                f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" '
                f'stroke="{color}" stroke-width="2" opacity="{opacity:.2f}"/>'
            )
        elif shape == "rect":
            x = rng.randint(-50, W - 50)
            y = rng.randint(-50, H - 50)
            w = rng.randint(100, 300)
            h = rng.randint(100, 300)
            angle = rng.randint(-30, 30)
            elements.append(
                f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" '
                f'stroke="{color}" stroke-width="2" opacity="{opacity:.2f}" '
                f'transform="rotate({angle},{x + w // 2},{y + h // 2})"/>'
            )
        else:
            cx = rng.randint(100, W - 100)
            cy = rng.randint(100, H - 100)
            size = rng.randint(60, 180)
            pts = " ".join(
                f"{cx + size * math.cos(a):.0f},{cy + size * math.sin(a):.0f}"
                for a in [math.radians(d) for d in [-90, 150, 30]]
            )
            elements.append(
                f'<polygon points="{pts}" fill="none" '
                f'stroke="{color}" stroke-width="2" opacity="{opacity:.2f}"/>'
            )

    # Small accent dots
    for _ in range(20):
        cx = rng.randint(0, W)
        cy = rng.randint(0, H)
        r = rng.uniform(1.5, 4)
        elements.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="{accent}" opacity="0.15"/>'
        )

    # Diagonal accent line
    elements.append(
        f'<line x1="0" y1="{H}" x2="{W}" y2="0" '
        f'stroke="{accent}" stroke-width="1" opacity="0.08"/>'
    )

    return "\n  ".join(elements)


def gen_nodes(rng, colors):
    bg, c1, c2, accent, _ = colors
    elements = []
    elements.append(f'''<defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="0.8">
      <stop offset="0%" stop-color="{bg}"/>
      <stop offset="100%" stop-color="{c1}"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>''')

    # Generate node positions
    nodes = [(rng.randint(30, W - 30), rng.randint(30, H - 30)) for _ in range(25)]

    # Draw connections between nearby nodes
    for i, (x1, y1) in enumerate(nodes):
        for j, (x2, y2) in enumerate(nodes):
            if i >= j:
                continue
            dist = math.hypot(x2 - x1, y2 - y1)
            if dist < 250:
                opacity = max(0.02, 0.12 - dist / 2500)
                elements.append(
                    f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                    f'stroke="{accent}" stroke-width="1" opacity="{opacity:.3f}"/>'
                )

    # Draw nodes
    for x, y in nodes:
        r = rng.uniform(2, 6)
        opacity = rng.uniform(0.15, 0.5)
        elements.append(
            f'<circle cx="{x}" cy="{y}" r="{r:.1f}" fill="{accent}" opacity="{opacity:.2f}"/>'
        )

    return "\n  ".join(elements)


def gen_topo(rng, colors):
    bg, c1, c2, accent, _ = colors
    elements = []
    elements.append(f'''<defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0.3" y2="1">
      <stop offset="0%" stop-color="{bg}"/>
      <stop offset="100%" stop-color="{c1}"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>''')

    # Contour line rings (concentric-ish ellipses from a few centers)
    centers = [(rng.randint(100, W - 100), rng.randint(100, H - 100)) for _ in range(3)]
    for cx, cy in centers:
        for ring in range(3, 10):
            rx = ring * rng.randint(25, 45)
            ry = ring * rng.randint(20, 35)
            angle = rng.randint(-20, 20)
            opacity = max(0.03, 0.15 - ring * 0.012)
            elements.append(
                f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" '
                f'fill="none" stroke="{accent}" stroke-width="1" '
                f'opacity="{opacity:.3f}" '
                f'transform="rotate({angle},{cx},{cy})"/>'
            )

    return "\n  ".join(elements)


GENERATORS = {
    "circuit": gen_circuit,
    "grid": gen_grid,
    "waves": gen_waves,
    "geo": gen_geo,
    "nodes": gen_nodes,
    "topo": gen_topo,
}


def build_text_block(lines: list[str], font_size: int, text_color: str, accent: str) -> str:
    """Build the centered title text with subtle backdrop."""
    n = len(lines)
    line_height = font_size * 1.3
    total_height = n * line_height
    start_y = (H - total_height) / 2 + font_size * 0.35

    parts = []

    # Semi-transparent backdrop
    pad_x, pad_y = 60, 30
    backdrop_h = total_height + pad_y * 2
    backdrop_y = start_y - font_size * 0.35 - pad_y + line_height * 0.5
    parts.append(
        f'<rect x="{pad_x}" y="{backdrop_y:.0f}" '
        f'width="{W - pad_x * 2}" height="{backdrop_h:.0f}" '
        f'rx="8" fill="black" opacity="0.35"/>'
    )

    # Accent bar above title
    bar_y = backdrop_y + 1
    parts.append(
        f'<rect x="{W // 2 - 40}" y="{bar_y:.0f}" width="80" height="3" '
        f'rx="1.5" fill="{accent}" opacity="0.7"/>'
    )

    # Title text lines
    for i, line in enumerate(lines):
        y = start_y + i * line_height
        escaped = html.escape(line)
        parts.append(
            f'<text x="{W // 2}" y="{y:.0f}" '
            f'text-anchor="middle" '
            f'font-family="\'Segoe UI\', \'Helvetica Neue\', Arial, sans-serif" '
            f'font-weight="700" font-size="{font_size}" '
            f'fill="{text_color}" letter-spacing="-0.5">'
            f'{escaped}</text>'
        )

    # Accent bar below title
    bar_y2 = start_y + (n - 1) * line_height + pad_y
    parts.append(
        f'<rect x="{W // 2 - 40}" y="{bar_y2:.0f}" width="80" height="3" '
        f'rx="1.5" fill="{accent}" opacity="0.7"/>'
    )

    # mattjones.technology watermark
    parts.append(
        f'<text x="{W // 2}" y="{H - 24}" '
        f'text-anchor="middle" '
        f'font-family="\'Segoe UI\', \'Helvetica Neue\', Arial, sans-serif" '
        f'font-weight="400" font-size="14" '
        f'fill="{text_color}" opacity="0.4" letter-spacing="2">'
        f'mattjones.technology</text>'
    )

    return "\n  ".join(parts)


def generate_svg(title: str, theme: str, custom_colors: list[str] | None = None) -> str:
    theme_data = THEMES[theme]
    colors = custom_colors if custom_colors and len(custom_colors) >= 5 else theme_data["colors"]
    text_color = theme_data["text"]
    accent = theme_data["accent"]

    rng = random.Random(seed_from_title(title))
    pattern = GENERATORS[theme](rng, colors)
    lines = wrap_title(title)
    max_len = max(len(l) for l in lines)
    fs = font_size_for_lines(len(lines), max_len)
    text_block = build_text_block(lines, fs, text_color, accent)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  {pattern}
  {text_block}
</svg>'''


def main():
    parser = argparse.ArgumentParser(description="Generate blog hero SVG")
    parser.add_argument("--title", required=True, help="Blog post title")
    parser.add_argument("--theme", required=True, choices=list(THEMES.keys()))
    parser.add_argument("--output", required=True, help="Output SVG path")
    parser.add_argument("--colors", help="Comma-separated hex colors (5 values) to override theme")
    args = parser.parse_args()

    custom = args.colors.split(",") if args.colors else None
    svg = generate_svg(args.title, args.theme, custom)

    with open(args.output, "w") as f:
        f.write(svg)
    print(f"Generated: {args.output}")


if __name__ == "__main__":
    main()
