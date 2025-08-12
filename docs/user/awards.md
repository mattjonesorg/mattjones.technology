# Managing Awards Content

This guide explains how to add awards or education entries to the site.

## Creating a new award

1. Choose where the file will live:
   - Use the existing `content/education/` directory to keep education and awards together.
   - Create a dedicated `content/awards/` directory if you prefer to separate them.

2. Add a new Markdown file, for example `content/awards/my-award.md`, and include front matter like:

```markdown
---
title: "Award Title"
organization: "Awarding Organization"
year: "2024"
summary: "Short description of the award."
weight: 1
---
```

### Front matter fields

- **title** – Name of the award.
- **organization** – Group that presented the award.
- **year** – When the award was received.
- **summary** – Brief description that appears in lists or cards.
- **weight** – Determines ordering; lower numbers appear first.

## Linking awards in navigation

To surface awards in the site navigation, update `config/_default/hugo.toml`.

### Menu entry
Add a menu item pointing to the awards section:

```toml
[menu]
  [[menu.main]]
    identifier = "awards"
    name = "Awards"
    url = "/awards"
    weight = 2
```

The file already contains a `menu.main` block for other links such as the blog【F:config/_default/hugo.toml†L22-L28】.

### Navbar section
If using the combined Education/Awards section, ensure the navigation entry is enabled by leaving `disableEducation` set to `false`:

```toml
[params.navbar.menus]
  disableEducation = false
```

This setting appears with other navigation toggles in the config【F:config/_default/hugo.toml†L57-L63】. Adjust the `education` section title (`params.education.title`) if you want it to read "Awards" or similar.

