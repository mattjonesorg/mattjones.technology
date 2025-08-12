# mattjones.technology

This repository contains the Hugo source for the personal site [mattjones.technology](https://mattjones.technology).

## Prerequisites

- [Hugo](https://gohugo.io/) extended version 0.111 or newer.
- Git.

## Setup

Clone the repository and fetch the theme submodule:

```bash
git clone --recurse-submodules <repo-url>
cd mattjones.technology
```

If you cloned without submodules, initialize them with:

```bash
git submodule update --init --recursive
```

Hugo will render a "Page not found" home page if the theme's layouts are missing, which happens when the submodule hasn't been fetched.

## Development

Start a local development server:

```bash
hugo server
```

The site will be available at http://localhost:1313/.

## Building

To generate the static site output:

```bash
hugo
```

This writes the built site to the `public/` directory (ignored by git).

