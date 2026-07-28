# CIT AI-Native Engineering Program — Year 1, Semester 1

A complete learning path for Revature's **CIT AI-Native Engineering** track — from how
machines think through to building, evaluating, and shipping production AI.

## 🌐 Live site

**https://namratarev.github.io/CIT_AI_Academy-/**

The site is a professional, Revature-branded course website generated from the markdown
content in [`modules/`](modules). It has 15 sections and 56 lessons, with grouped sidebar
navigation, breadcrumbs, previous/next links, light/dark mode, and rendered diagrams,
tables, and code.

## Repository structure

| Path | Description |
|---|---|
| `modules/` | Course content — one folder per section, one markdown file per lesson. |
| `reference-materials/` | Supplementary resources, advanced topics, and release notes. |
| `build_site.py` | Static-site generator: converts every lesson markdown file into a branded HTML page. |
| `assets_data.py` | Branding assets (CSS, JavaScript, Revature logo) used by the generator. |
| `.github/workflows/deploy-pages.yml` | GitHub Actions workflow that builds and deploys the site to GitHub Pages. |
| `requirements.txt` | Python dependencies for the generator. |
| `site/` | Generated output (not tracked in git — built automatically in CI). |

## Building the site locally

Requires Python 3.

```bash
pip install -r requirements.txt
python build_site.py
```

The site is generated into the `site/` folder. To preview it with working diagrams and
fonts, serve it over a local web server:

```bash
cd site
python -m http.server 8000
```

Then open **http://localhost:8000**.

## Deployment

Every push to the `main` branch triggers the GitHub Actions workflow, which rebuilds the
site from source and publishes it to GitHub Pages — so the live site always reflects the
latest content in `modules/`. No generated HTML is committed to the repository.
