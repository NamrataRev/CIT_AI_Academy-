# -*- coding: utf-8 -*-
"""
Static-site generator for the CIT AI-Native Engineering Program content.

Reads every markdown file under ./modules, groups them by section (using the
descriptive section title, e.g. "How Machines Think" -- never "Unit N"), and
renders a branded, navigable website into ./site.

Run:  python build_site.py
Then open site/index.html in a browser (or serve with `python -m http.server`).
"""

import os
import re
import html
import shutil
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
MODULES_DIR = os.path.join(ROOT, "modules")
OUT_DIR = os.path.join(ROOT, "site")

PROGRAM_TITLE = "AI-Native Engineering"
PROGRAM_SUBTITLE = "Year 1 · Semester 1"


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def clean_section_title(h1):
    """'# Unit 1 — How Machines Think' -> 'How Machines Think'"""
    t = h1.lstrip("#").strip()
    t = re.sub(r"^Unit\s+\d+\s*[—\-–:]\s*", "", t)
    return t.strip()


def clean_topic_title(h2):
    """'## Topic 1: Understanding Computation' -> 'Understanding Computation'"""
    t = h2.lstrip("#").strip()
    t = re.sub(r"^Topic\s+\d+\s*[:\-—–]\s*", "", t)
    return t.strip()


MERMAID_RE = re.compile(r"```mermaid\s*\n(.*?)```", re.DOTALL)


def convert_markdown(body):
    """Convert markdown to HTML, preserving mermaid blocks as <pre class='mermaid'>."""
    blocks = []

    def _stash(m):
        blocks.append(m.group(1).rstrip("\n"))
        return "\n\nMERMAIDPLACEHOLDER{}\n\n".format(len(blocks) - 1)

    body = MERMAID_RE.sub(_stash, body)

    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "attr_list", "sane_lists"],
    )
    out = md.convert(body)

    for i, code in enumerate(blocks):
        placeholder = "<p>MERMAIDPLACEHOLDER{}</p>".format(i)
        replacement = '<div class="mermaid-wrap"><pre class="mermaid">{}</pre></div>'.format(
            html.escape(code)
        )
        out = out.replace(placeholder, replacement)
        # fallback if not wrapped in <p>
        out = out.replace("MERMAIDPLACEHOLDER{}".format(i), replacement)
    return out


# --------------------------------------------------------------------------- #
# Discover content
# --------------------------------------------------------------------------- #
def collect():
    sections = []  # list of dicts: {title, slug, topics:[...]}
    for unit_dir in sorted(os.listdir(MODULES_DIR)):
        full = os.path.join(MODULES_DIR, unit_dir)
        if not os.path.isdir(full):
            continue
        md_files = sorted(f for f in os.listdir(full) if f.endswith(".md"))
        if not md_files:
            continue
        section = None
        topics = []
        for fname in md_files:
            path = os.path.join(full, fname)
            with open(path, "r", encoding="utf-8") as fh:
                raw = fh.read()
            lines = raw.split("\n")

            # find first H1 and first H2
            h1 = next((l for l in lines if l.startswith("# ")), "# " + unit_dir)
            h2 = next((l for l in lines if l.startswith("## ")), "## " + fname)
            section_title = clean_section_title(h1)
            topic_title = clean_topic_title(h2)

            # build body: drop the first H1 line and the first H2 line only
            body_lines = []
            dropped_h1 = dropped_h2 = False
            for l in lines:
                if not dropped_h1 and l == h1:
                    dropped_h1 = True
                    continue
                if not dropped_h2 and l == h2:
                    dropped_h2 = True
                    continue
                body_lines.append(l)
            body = "\n".join(body_lines).strip()
            body = re.sub(r"^-{3,}\s*", "", body).strip()  # leading rule after headings

            topics.append(
                {
                    "topic_title": topic_title,
                    "slug": slugify(topic_title),
                    "body": body,
                    "src": path,
                }
            )
            if section is None:
                section = section_title

        sections.append(
            {"title": section, "slug": slugify(section), "topics": topics}
        )
    return sections


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #
def sidebar_html(sections, active_section_slug=None, active_topic_slug=None, depth=1):
    prefix = "../" * depth
    out = ['<nav class="side-nav" aria-label="Course sections">']
    for s in sections:
        open_attr = " open" if s["slug"] == active_section_slug else ""
        out.append('<details class="nav-group"{}>'.format(open_attr))
        out.append('<summary class="nav-section">{}</summary>'.format(html.escape(s["title"])))
        out.append('<ul class="nav-topics">')
        for t in s["topics"]:
            is_active = (
                s["slug"] == active_section_slug and t["slug"] == active_topic_slug
            )
            cls = ' class="active"' if is_active else ""
            href = "{}{}/{}.html".format(prefix, s["slug"], t["slug"])
            aria = ' aria-current="page"' if is_active else ""
            out.append(
                '<li{}><a href="{}"{}>{}</a></li>'.format(
                    cls, href, aria, html.escape(t["topic_title"])
                )
            )
        out.append("</ul></details>")
    out.append("</nav>")
    return "\n".join(out)


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__PAGETITLE__ · CIT Program</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="__PREFIX__assets/style.css">
<link rel="icon" href="__PREFIX__assets/favicon.svg" type="image/svg+xml">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <button class="menu-toggle" aria-label="Toggle navigation" onclick="document.body.classList.toggle('nav-open')">
    <span></span><span></span><span></span>
  </button>
  <a class="brand" href="__PREFIX__index.html">
    <img src="__PREFIX__assets/logo.svg" alt="Revature" class="brand-logo">
    <span class="brand-divider"></span>
    <span class="brand-text"><strong>CIT</strong> AI-Native Engineering</span>
  </a>
  <button class="theme-toggle" aria-label="Toggle dark mode" onclick="toggleTheme()">
    <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"></path></svg>
  </button>
</header>
<div class="layout">
  <aside class="sidebar" id="sidebar">
    __SIDEBAR__
  </aside>
  <div class="nav-scrim" onclick="document.body.classList.remove('nav-open')"></div>
  <main class="content" id="main">
    __CONTENT__
  </main>
</div>
<script src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/highlight.min.js"></script>
<script src="__PREFIX__assets/app.js"></script>
</body>
</html>
"""


def render_topic_page(sections, s, t, prev_link, next_link):
    content_html = convert_markdown(t["body"])

    breadcrumb = (
        '<nav class="breadcrumb" aria-label="Breadcrumb">'
        '<a href="__PREFIX__index.html">Home</a>'
        '<span class="sep">/</span>'
        '<span class="crumb-section">{section}</span>'
        "</nav>"
    ).format(section=html.escape(s["title"]))

    header = (
        '<div class="page-head">'
        '<p class="eyebrow">{section}</p>'
        "<h1>{topic}</h1>"
        "</div>"
    ).format(section=html.escape(s["title"]), topic=html.escape(t["topic_title"]))

    # prev / next
    pager = ['<nav class="pager" aria-label="Topic navigation">']
    if prev_link:
        pager.append(
            '<a class="pager-link prev" href="{href}"><span class="pager-dir">Previous</span>'
            '<span class="pager-title">{title}</span></a>'.format(
                href=prev_link[0], title=html.escape(prev_link[1])
            )
        )
    else:
        pager.append("<span></span>")
    if next_link:
        pager.append(
            '<a class="pager-link next" href="{href}"><span class="pager-dir">Next</span>'
            '<span class="pager-title">{title}</span></a>'.format(
                href=next_link[0], title=html.escape(next_link[1])
            )
        )
    else:
        pager.append("<span></span>")
    pager.append("</nav>")

    content = breadcrumb + header + '<article class="prose">' + content_html + "</article>" + "\n".join(pager)

    page = PAGE_TEMPLATE
    page = page.replace("__PAGETITLE__", html.escape(t["topic_title"]))
    page = page.replace("__PREFIX__", "../")
    page = page.replace("__SIDEBAR__", sidebar_html(sections, s["slug"], t["slug"], depth=1))
    page = page.replace("__CONTENT__", content)
    return page


def render_index(sections):
    total_topics = sum(len(s["topics"]) for s in sections)

    cards = []
    for i, s in enumerate(sections, 1):
        first = s["topics"][0]
        topic_items = "".join(
            '<li><a href="{slug}/{tslug}.html">{title}</a></li>'.format(
                slug=s["slug"], tslug=t["slug"], title=html.escape(t["topic_title"])
            )
            for t in s["topics"]
        )
        cards.append(
            '<article class="sec-card">'
            '<div class="sec-card-head">'
            '<span class="sec-num">{num:02d}</span>'
            '<h3><a href="{slug}/{fslug}.html">{title}</a></h3>'
            "</div>"
            '<ul class="sec-card-topics">{items}</ul>'
            "</article>".format(
                num=i,
                slug=s["slug"],
                fslug=first["slug"],
                title=html.escape(s["title"]),
                items=topic_items,
            )
        )

    hero = (
        '<section class="hero">'
        '<p class="eyebrow">Revature · Continuous Immersion Track</p>'
        "<h1>{title}</h1>"
        '<p class="hero-sub">{subtitle} — a complete learning path from how machines think '
        "to building, evaluating and shipping production AI.</p>"
        '<div class="hero-stats">'
        '<div><strong>{sec}</strong><span>Sections</span></div>'
        '<div><strong>{top}</strong><span>Lessons</span></div>'
        '<div><strong>15</strong><span>Week journey</span></div>'
        "</div>"
        '<a class="hero-cta" href="{first_slug}/{first_topic}.html">Start learning →</a>'
        "</section>"
    ).format(
        title=PROGRAM_TITLE,
        subtitle=PROGRAM_SUBTITLE,
        sec=len(sections),
        top=total_topics,
        first_slug=sections[0]["slug"],
        first_topic=sections[0]["topics"][0]["slug"],
    )

    content = hero + '<h2 class="grid-title">Course Sections</h2><div class="sec-grid">' + "".join(cards) + "</div>"

    page = PAGE_TEMPLATE
    page = page.replace("__PAGETITLE__", "Home")
    page = page.replace("__PREFIX__", "")
    page = page.replace("__SIDEBAR__", sidebar_html(sections, depth=0))
    page = page.replace("__CONTENT__", content)
    return page


# --------------------------------------------------------------------------- #
# Build
# --------------------------------------------------------------------------- #
def safe_clean(path):
    """Remove stale .html files under `path`, tolerating locked dirs.

    On Windows (esp. inside OneDrive) directory handles can be transiently
    locked. We can't always delete folders, but overwriting files is enough,
    so we best-effort delete generated pages and never abort the build.
    """
    import stat
    import time

    def _onexc(func, p, exc):
        try:
            os.chmod(p, stat.S_IWRITE)
            func(p)
        except Exception:
            pass  # leave it; files will be overwritten in place

    for attempt in range(3):
        try:
            shutil.rmtree(path, onexc=_onexc)
            return
        except TypeError:
            # Python < 3.12 uses onerror(func, path, exc_info)
            shutil.rmtree(path, onerror=lambda f, p, e: _onexc(f, p, e))
            return
        except Exception:
            time.sleep(0.4)
    # Final fallback: delete only stale .html files so no dead pages remain.
    for root, _dirs, files in os.walk(path):
        for f in files:
            if f.endswith(".html"):
                try:
                    os.remove(os.path.join(root, f))
                except Exception:
                    pass


def build():
    sections = collect()

    # clean output but keep nothing stale (resilient to Windows/OneDrive locks)
    if os.path.exists(OUT_DIR):
        safe_clean(OUT_DIR)
    os.makedirs(os.path.join(OUT_DIR, "assets"), exist_ok=True)

    # write assets
    write_assets()

    # Prevent GitHub Pages / Jekyll from processing the static output.
    with open(os.path.join(OUT_DIR, ".nojekyll"), "w", encoding="utf-8") as fh:
        fh.write("")

    # flatten for prev/next
    flat = []
    for s in sections:
        for t in s["topics"]:
            flat.append((s, t))

    for idx, (s, t) in enumerate(flat):
        sec_dir = os.path.join(OUT_DIR, s["slug"])
        os.makedirs(sec_dir, exist_ok=True)

        prev_link = None
        next_link = None
        if idx > 0:
            ps, pt = flat[idx - 1]
            prev_link = ("../{}/{}.html".format(ps["slug"], pt["slug"]), pt["topic_title"])
        if idx < len(flat) - 1:
            ns, nt = flat[idx + 1]
            next_link = ("../{}/{}.html".format(ns["slug"], nt["slug"]), nt["topic_title"])

        page = render_topic_page(sections, s, t, prev_link, next_link)
        with open(os.path.join(sec_dir, t["slug"] + ".html"), "w", encoding="utf-8") as fh:
            fh.write(page)

    with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(render_index(sections))

    print("Built {} pages across {} sections.".format(len(flat), len(sections)))
    print("Output: {}".format(OUT_DIR))


def write_assets():
    with open(os.path.join(OUT_DIR, "assets", "style.css"), "w", encoding="utf-8") as fh:
        fh.write(STYLE_CSS)
    with open(os.path.join(OUT_DIR, "assets", "app.js"), "w", encoding="utf-8") as fh:
        fh.write(APP_JS)
    with open(os.path.join(OUT_DIR, "assets", "logo.svg"), "w", encoding="utf-8") as fh:
        fh.write(LOGO_SVG)
    with open(os.path.join(OUT_DIR, "assets", "favicon.svg"), "w", encoding="utf-8") as fh:
        fh.write(FAVICON_SVG)


# Assets are defined in assets_data.py and imported here.
from assets_data import STYLE_CSS, APP_JS, LOGO_SVG, FAVICON_SVG  # noqa: E402


if __name__ == "__main__":
    build()
