#!/usr/bin/env python3
"""Builds README.md, notes/*.md and docs/index.html from data/*.csv.

Usage:  python3 scripts/build.py
Edit the CSV files and run it again:
  data/categories.csv  Category, Emoji, Description   (order = display order)
  data/commands.csv    Category, Command, Description, Example
  data/parameters.csv  Command, Parameter, Description, Example
"""
import csv
import json
import re
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def read(name):
    with open(DATA / name, encoding="utf-8") as f:
        return [{k: (v or "").strip() for k, v in row.items()} for row in csv.DictReader(f)]


def slug(text):
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return text or "x"


def code(text, table=True):
    """Text as inline code; pipes are escaped when used inside a Markdown table."""
    if not text:
        return ""
    t = text.replace("|", "\\|") if table else text
    fence = "``" if "`" in t else "`"
    pad = " " if fence == "``" else ""
    return f"{fence}{pad}{t}{pad}{fence}"


def cell(text):
    return text.replace("|", "\\|")


def build_model():
    cats = OrderedDict()
    for c in read("categories.csv"):
        cats[c["Category"]] = {"name": c["Category"], "emoji": c["Emoji"], "desc": c["Description"],
                               "id": slug(c["Category"]), "commands": []}
    by_name = {}
    for row in read("commands.csv"):
        cmd = {"name": row["Command"], "desc": row["Description"], "ex": row["Example"],
               "category": row["Category"], "params": []}
        cats[row["Category"]]["commands"].append(cmd)
        by_name[cmd["name"]] = cmd
    params = read("parameters.csv")
    for p in params:
        by_name[p["Command"]]["params"].append(
            {"flag": p["Parameter"], "desc": p["Description"], "ex": p["Example"]})
    return cats, by_name, params


def cmd_anchor(name):
    s = slug(name)
    if s == "x" or not any(ch.isalnum() for ch in name):
        s = "sym-" + "-".join(str(ord(ch)) for ch in name if ch != " ")
    return "cmd-" + s


def category_md(cat, n_params):
    out = [
        f"# {cat['emoji']} {cat['name']}",
        "",
        f"> {cat['desc']}",
        "",
        f"**{len(cat['commands'])}** commands · **{n_params}** parameters  ·  [⬅ Back to index](../README.md)",
        "",
        '<a id="commands"></a>',
        "",
        "| Command | What it does |",
        "|:--|:--|",
    ]
    for c in cat["commands"]:
        out.append(f"| [{code(c['name'])}](#{cmd_anchor(c['name'])}) | {cell(c['desc'])} |")
    out.append("")
    for c in cat["commands"]:
        out += ["---", "", f'<a id="{cmd_anchor(c["name"])}"></a>', "", f"## {code(c['name'], table=False)}", "",
                c["desc"], ""]
        if c["ex"]:
            out += ["```bash", c["ex"], "```", ""]
        if c["params"]:
            out += ["| Parameter | What it does | Example |", "|:--|:--|:--|"]
            for p in c["params"]:
                out.append(f"| {code(p['flag'])} | {cell(p['desc'])} | {code(p['ex'])} |")
            out.append("")
        out += ["<sub>[⬆ Back to top](#commands)</sub>", ""]
    return "\n".join(out)


def readme_md(cats, by_name, params):
    n_cmd = len(by_name)
    out = [
        '<div align="center">',
        "",
        "# 🐧 Linux Commands",
        "",
        "**A personal reference of Linux commands, grouped by what they do, with copy-ready examples.**",
        "",
        f"![Commands](https://img.shields.io/badge/commands-{n_cmd}-2ea44f?style=for-the-badge)"
        f" ![Parameters](https://img.shields.io/badge/parameters-{len(params)}-0969da?style=for-the-badge)"
        f" ![Categories](https://img.shields.io/badge/categories-{len(cats)}-8250df?style=for-the-badge)",
        "",
        "🌐 **Searchable web version:** [`docs/index.html`](docs/index.html)  ·  🐚 **Companion repo:** [Bash-Scripting-From-Scratch](https://github.com/TrueOwl-Override/Bash-Scripting-From-Scratch)",
        "",
        "</div>",
        "",
        "---",
        "",
        "## 📚 Categories",
        "",
        "| | Category | What's inside | Commands |",
        "|:-:|:--|:--|:--|",
    ]
    for cat in cats.values():
        cmds = " ".join(code(c["name"]) for c in cat["commands"])
        out.append(f"| {cat['emoji']} | **[{cat['name']}](notes/{cat['id']}.md)** | {cat['desc']} | {cmds} |")
    out += ["", "## 🔤 A–Z index", "", "| Command | What it does | Category |", "|:--|:--|:--|"]
    for name in sorted(by_name, key=lambda x: (not x[0].isalnum(), x.lower())):
        c = by_name[name]
        cat = cats[c["category"]]
        out.append(f"| [{code(name)}](notes/{cat['id']}.md#{cmd_anchor(name)}) | {cell(c['desc'])} | {cat['emoji']} {cat['name']} |")
    out += [
        "",
        "## 🛠️ How to update",
        "",
        "The data lives in [`data/`](data): [`categories.csv`](data/categories.csv), "
        "[`commands.csv`](data/commands.csv) and [`parameters.csv`](data/parameters.csv). After editing them, run:",
        "",
        "```bash",
        "python3 scripts/build.py",
        "```",
        "",
        "This rebuilds this README, the notes in [`notes/`](notes) and the web page in [`docs/`](docs).",
        "",
        "> 💡 To publish the web page: **Settings → Pages → Branch `main` / folder `/docs`**.",
        "",
    ]
    return "\n".join(out)


def build_html(cats, by_name, params):
    data = {
        "categories": list(cats.values()),
        "stats": {"commands": len(by_name), "parameters": len(params), "categories": len(cats)},
    }
    tpl = (ROOT / "scripts" / "template.html").read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return tpl.replace("/*__DATA__*/null", payload)


def main():
    cats, by_name, params = build_model()
    notes = ROOT / "notes"
    notes.mkdir(exist_ok=True)
    for old in notes.glob("*.md"):
        old.unlink()
    for cat in cats.values():
        n_p = sum(len(c["params"]) for c in cat["commands"])
        (notes / f"{cat['id']}.md").write_text(category_md(cat, n_p), encoding="utf-8")
    (ROOT / "README.md").write_text(readme_md(cats, by_name, params), encoding="utf-8")
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs" / "index.html").write_text(build_html(cats, by_name, params), encoding="utf-8")
    print(f"OK: {len(by_name)} commands, {len(params)} parameters, {len(cats)} categories")


if __name__ == "__main__":
    main()
