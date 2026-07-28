# -*- coding: utf-8 -*-
"""
One-off (idempotent) transform that turns the raw lesson markdown files in
./modules into Jekyll-ready pages by injecting YAML front matter.

For each modules/unit-XX-.../NN-....md it:
  * derives the section title from the `# Unit N — ...` heading (drops "Unit N"),
  * derives the lesson title from the `## Topic N: ...` heading (drops "Topic N"),
  * pulls the "*(Covers: ...)*" line into a `covers` field,
  * removes those lines from the body,
  * writes front matter (title, section, section_order, order, nav_order,
    permalink, layout) on top.

Files that already start with front matter are left untouched, so it is safe
to re-run after adding new lessons.

Run:  python build_jekyll.py
"""

import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
MODULES_DIR = os.path.join(ROOT, "modules")


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def clean_section_title(h1):
    t = h1.lstrip("#").strip()
    return re.sub(r"^Unit\s+\d+\s*[—\-–:]\s*", "", t).strip()


def clean_topic_title(h2):
    t = h2.lstrip("#").strip()
    return re.sub(r"^Topic\s+\d+\s*[:\-—–]\s*", "", t).strip()


def yaml_quote(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def process(path, sec_num, topic_num):
    with open(path, "r", encoding="utf-8") as fh:
        raw = fh.read()

    if raw.lstrip().startswith("---"):
        return False  # already has front matter

    lines = raw.split("\n")
    h1 = next((l for l in lines if l.startswith("# ")), "# Section")
    h2 = next((l for l in lines if l.startswith("## ")), "## Lesson")
    section_title = clean_section_title(h1)
    topic_title = clean_topic_title(h2)

    covers = ""
    covers_line = None
    for l in lines:
        m = re.match(r"\*\(Covers:\s*(.+?)\)\*\s*$", l.strip())
        if m:
            covers = m.group(1).strip()
            covers_line = l
            break

    # Build body: drop first H1, first H2, and the covers line.
    body_lines = []
    dropped_h1 = dropped_h2 = False
    for l in lines:
        if not dropped_h1 and l == h1:
            dropped_h1 = True
            continue
        if not dropped_h2 and l == h2:
            dropped_h2 = True
            continue
        if covers_line is not None and l == covers_line:
            covers_line = None
            continue
        body_lines.append(l)
    body = "\n".join(body_lines).strip()
    body = re.sub(r"^-{3,}\s*", "", body).strip()  # drop leading horizontal rule

    section_slug = slugify(section_title)
    topic_slug = slugify(topic_title)
    nav_order = "{:02d}{:02d}".format(sec_num, topic_num)

    fm = [
        "---",
        "layout: lesson",
        "title: {}".format(yaml_quote(topic_title)),
        "section: {}".format(yaml_quote(section_title)),
        "section_order: {}".format(sec_num),
        "order: {}".format(topic_num),
        'nav_order: "{}"'.format(nav_order),
        "permalink: /{}/{}/".format(section_slug, topic_slug),
    ]
    if covers:
        fm.append("covers: {}".format(yaml_quote(covers)))
    fm.append("---")

    out = "\n".join(fm) + "\n\n" + body + "\n"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(out)
    return True


def main():
    changed = 0
    for unit_dir in sorted(os.listdir(MODULES_DIR)):
        full = os.path.join(MODULES_DIR, unit_dir)
        if not os.path.isdir(full):
            continue
        m = re.match(r"unit-(\d+)", unit_dir)
        sec_num = int(m.group(1)) if m else 0
        for fname in sorted(f for f in os.listdir(full) if f.endswith(".md")):
            fm = re.match(r"(\d+)", fname)
            topic_num = int(fm.group(1)) if fm else 0
            if process(os.path.join(full, fname), sec_num, topic_num):
                changed += 1
    print("Injected front matter into {} lesson file(s).".format(changed))


if __name__ == "__main__":
    main()
