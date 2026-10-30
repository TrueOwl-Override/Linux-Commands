#!/usr/bin/env python3
"""Builds README.md, notes/*.md and docs/index.html from data/*.csv.

Usage:  python3 scripts/build.py
Edit the CSV files (or re-export them from Google Sheets) and run it again.
"""
import csv
import json
import re
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

SECTIONS = OrderedDict([
    ("Concepts", {"emoji": "🧠", "desc": "Terminal fundamentals: users, permissions, redirection, searching and package management."}),
    ("Labs", {"emoji": "🧪", "desc": "Commands learned solving labs (OverTheWire Bandit): SSH, filtering, binaries, cron, git and more."}),
])


def read(name):
    with open(DATA / name, encoding="utf-8") as f:
        return [{k: (v or "").strip() for k, v in row.items()} for row in csv.DictReader(f)]


def slug(text):
    text = text.lower()
    for a, b in zip("áéíóúñü", "aeiounu"):
        text = text.replace(a, b)
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "x"


def code(text, table=True):
    """Text as inline code that is safe inside a Markdown table."""
    if not text:
        return ""
    t = text.replace("|", "\\|") if table else text
    fence = "``" if "`" in t else "`"
    pad = " " if fence == "``" else ""
    return f"{fence}{pad}{t}{pad}{fence}"


def cell(text):
    return text.replace("|", "\\|")


def build_model():
    comandos = read("commands.csv")
    parametros = read("parameters.csv")
    # Topic order follows the commands sheet; topics that only appear in the
    # parameters sheet are inserted right after the last topic seen, so the
    # course order is kept.
    order = {s: [] for s in SECTIONS}
    for row in comandos:
        if row["Topic"] not in order[row["Section"]]:
            order[row["Section"]].append(row["Topic"])
    last = {}
    for row in parametros:
        s, t = row["Section"], row["Topic"]
        if t not in order[s]:
            base = t.split(" [")[0]
            siblings = [i for i, x in enumerate(order[s]) if x.split(" [")[0] == base]
            if siblings:  # e.g. "Topic [2-2]" goes right after "Topic [1-2]"
                idx = siblings[-1] + 1
            else:
                idx = order[s].index(last[s]) + 1 if s in last else 0
            order[s].insert(idx, t)
        last[s] = t
    model = OrderedDict(
        (s, OrderedDict((t, {"commands": [], "parameters": []}) for t in order[s])) for s in SECTIONS
    )
    for row in comandos:
        model[row["Section"]][row["Topic"]]["commands"].append(row)
    for row in parametros:
        model[row["Section"]][row["Topic"]]["parameters"].append(row)
    return comandos, parametros, model


def section_md(section, temas):
    meta = SECTIONS[section]
    n_c = sum(len(t["commands"]) for t in temas.values())
    n_p = sum(len(t["parameters"]) for t in temas.values())
    out = [
        f"# {meta['emoji']} {section}",
        "",
        f"> {meta['desc']}",
        "",
        f"**{n_c}** commands · **{n_p}** parameters · **{len(temas)}** topics  ·  [⬅ Back to index](../README.md)",
        "",
        "## Topics",
        "",
    ]
    for i, tema in enumerate(temas, 1):
        out.append(f"{i}. [{tema}](#{slug(tema)})")
    out.append("")
    for tema, data in temas.items():
        out += ["---", "", f'<a id="{slug(tema)}"></a>', "", f"## {tema}", ""]
        if data["commands"]:
            out += ["| Command | What it does | Example |", "|:--|:--|:--|"]
            for c in data["commands"]:
                out.append(f"| {code(c['Command'])} | {cell(c['Description'])} | {code(c['Example'])} |")
            out.append("")
        if data["parameters"]:
            out += ["<details open>", f"<summary><b>🔧 Parameters & usage ({len(data['parameters'])})</b></summary>", "",
                    "| Command | Parameter | What it does | Example |", "|:--|:--|:--|:--|"]
            for p in data["parameters"]:
                out.append(f"| {code(p['Command'])} | {code(p['Parameter'])} | {cell(p['Description'])} | {code(p['Example'])} |")
            out += ["", "</details>", ""]
        out += ["<sub>[⬆ Back to top](#topics)</sub>", ""]
    return "\n".join(out)


def readme_md(comandos, parametros, model):
    out = [
        '<div align="center">',
        "",
        "# 🐧 Linux Commands",
        "",
        "**My Linux command notes, organized by topic, with copy-ready examples.**",
        "",
        f"![Commands](https://img.shields.io/badge/commands-{len(comandos)}-2ea44f?style=for-the-badge)"
        f" ![Parameters](https://img.shields.io/badge/parameters-{len(parametros)}-0969da?style=for-the-badge)"
        f" ![Topics](https://img.shields.io/badge/topics-{sum(len(t) for t in model.values())}-8250df?style=for-the-badge)",
        "",
        "🌐 **Searchable web version:** [`docs/index.html`](docs/index.html)",
        "",
        "</div>",
        "",
        "---",
        "",
        "## 📚 Sections",
        "",
        "| | Section | Contents | Commands | Parameters |",
        "|:-:|:--|:--|:-:|:-:|",
    ]
    for s, temas in model.items():
        meta = SECTIONS[s]
        nc = sum(len(t["commands"]) for t in temas.values())
        np_ = sum(len(t["parameters"]) for t in temas.values())
        out.append(f"| {meta['emoji']} | **[{s}](notes/{s}.md)** | {meta['desc']} | {nc} | {np_} |")
    out += ["", "## 🗂️ Topics", ""]
    for s, temas in model.items():
        out += [f"<details>", f"<summary><b>{SECTIONS[s]['emoji']} {s}</b> — {len(temas)} topics</summary>", ""]
        for tema, d in temas.items():
            cmds = ", ".join(code(c["Command"], table=False) for c in d["commands"]) or "<i>parameters only</i>"
            out.append(f"- [{tema}](notes/{s}.md#{slug(tema)}) — {cmds}")
        out += ["", "</details>", ""]

    out += ["## 🔤 Alphabetical command index", "", "| Command | What it does | Section |", "|:--|:--|:--|"]
    seen = {}
    for c in comandos:
        seen.setdefault(c["Command"], c)
    for name in sorted(seen, key=lambda x: (not x[0].isalnum(), x.lower())):
        c = seen[name]
        out.append(f"| {code(name)} | {cell(c['Description'])} | [{c['Section']}](notes/{c['Section']}.md#{slug(c['Topic'])}) |")
    out += [
        "",
        "## 🛠️ How to update",
        "",
        "The data lives in [`data/commands.csv`](data/commands.csv) and [`data/parameters.csv`](data/parameters.csv)."
        " After editing them, run:",
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


def build_html(comandos, parametros, model):
    data = {
        "sections": [{"name": s, **SECTIONS[s]} for s in SECTIONS],
        "temas": [
            {"section": s, "tema": t, "id": slug(s + "-" + t), "commands": d["commands"], "parameters": d["parameters"]}
            for s, temas in model.items() for t, d in temas.items()
        ],
        "stats": {"commands": len(comandos), "parameters": len(parametros)},
    }
    tpl = (ROOT / "scripts" / "template.html").read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return tpl.replace("/*__DATA__*/null", payload)


def main():
    comandos, parametros, model = build_model()
    (ROOT / "notes").mkdir(exist_ok=True)
    (ROOT / "docs").mkdir(exist_ok=True)
    for s, temas in model.items():
        (ROOT / "notes" / f"{s}.md").write_text(section_md(s, temas), encoding="utf-8")
    (ROOT / "README.md").write_text(readme_md(comandos, parametros, model), encoding="utf-8")
    (ROOT / "docs" / "index.html").write_text(build_html(comandos, parametros, model), encoding="utf-8")
    print(f"OK: {len(comandos)} commands, {len(parametros)} parameters")


if __name__ == "__main__":
    main()
