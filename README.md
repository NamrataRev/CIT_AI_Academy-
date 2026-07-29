# Foundations of Responsible AI Engineering — Year 1, Semester 1

A complete learning path for Revature's **Foundations of Responsible AI Engineering**
track — from how machines think through to building, evaluating, and shipping production
AI. The course is published as a **Jekyll** website hosted on GitHub Pages.

## 🌐 Live site

**https://namratarev.github.io/CIT_AI_Academy-/**

15 sections · 56 lessons · Revature-branded, with grouped sidebar navigation, breadcrumbs,
previous/next links, light/dark mode, and rendered tables, code, and Mermaid diagrams.

## How it works

The site is a Jekyll project that GitHub Pages builds automatically on every push to
`main` — no build step to run or commit yourself.

| Path | Description |
|---|---|
| `modules/` | Course content — one markdown file per lesson, each with Jekyll front matter (`title`, `section`, `order`, `permalink`). These files **are** the site pages. |
| `_layouts/` | Page templates: `default`, `lesson`, `home`. |
| `_includes/` | Reusable partials: site `<head>` and the section sidebar. |
| `assets/` | CSS, JavaScript (theme toggle + Mermaid), and the Revature logo. |
| `index.md` | Home page (hero + section cards). |
| `_config.yml` | Jekyll configuration (base URL, Markdown/Rouge settings, excludes). |
| `build_jekyll.py` | One-off helper that injected front matter into `modules/*.md`. Re-runnable and idempotent — new lesson files that lack front matter get it added. |
| `reference-materials/` | Supplementary notes (excluded from the built site). |

Sections are labelled by their descriptive titles (e.g. *How Machines Think*), not by unit
numbers.

## Editing content

Edit the markdown under `modules/` and push to `main` — the live site rebuilds
automatically. Keep the front matter block at the top of each file intact.

To add a **new lesson**, create a markdown file in the relevant `modules/unit-XX-.../`
folder and either add a front matter block by hand or run:

```bash
python build_jekyll.py
```

## Running locally (optional)

Requires Ruby + Bundler.

```bash
bundle install
bundle exec jekyll serve
```

Then open the local URL Jekyll prints (typically http://localhost:4000/CIT_AI_Academy-/).

## Deployment (one-time setup)

In the GitHub repo: **Settings → Pages → Build and deployment → Source → Deploy from a
branch**, then choose branch **`main`** and folder **`/ (root)`**. GitHub builds the Jekyll
site and publishes it at the live URL above.
