# Writing Blog Posts

Follow these steps to create and publish a new blog post.

## Create a draft

Generate a new post from the `blogs` archetype:

```bash
hugo new blogs/<slug>.md
```

This creates a file at `content/blogs/<slug>.md` with front matter you can edit. Update the values to match your post:

```yaml
---
title: "Your Title"
date: 2023-01-01T00:00:00Z
categories: ["Category"]
draft: true
---
```

## Publish the post

1. Set `draft: false` in the front matter.
2. Preview the site locally:
   ```bash
   hugo server
   ```
   Visit `http://localhost:1313` to verify the post.
3. Commit the post:
   ```bash
   git add content/blogs/<slug>.md
   git commit -m "Add <slug> blog post"
   ```
