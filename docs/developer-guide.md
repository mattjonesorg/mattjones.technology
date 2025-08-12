# Developer Guide

This guide outlines the structure of the Hugo site and how to work on it locally.

## Site Structure

- **`hugo.yaml`**: Root configuration file shared by all environments.
- **`config/`**: Environment‑specific settings in `hugo.toml` files.
- **`content/`**: Markdown files for pages and posts.
- **`layouts/`**: Template overrides and partials.
- **`static/`**: Assets copied directly to the output.
- **`themes/hugo-profile`**: Theme submodule providing base layouts and assets.

## Local Development

Start a hot‑reloading server:

```bash
hugo server
```

## Building

Generate the static site:

```bash
hugo
```

The compiled output is written to `public/`.

## Deployment

Changes to `main` are deployed to GitHub Pages via `.github/workflows/hugo.yml`.

## Contributing

When modifying templates or scripts, use Codex to explore the codebase and update files consistently.
