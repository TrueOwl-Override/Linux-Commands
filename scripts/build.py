#!/usr/bin/env python3
"""Genera README.md, notes/*.md y docs/index.html a partir de data/*.csv.

Uso:  python3 scripts/build.py
Edita los CSV (o vuelve a exportarlos desde Google Sheets) y vuelve a ejecutarlo.
"""
import csv
import json
import re
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

SECTIONS = OrderedDict([
    ("Conceptos", {"emoji": "🧠", "desc": "Fundamentos de la terminal: usuarios, permisos, redirecciones, búsquedas y primeros scripts."}),
    ("Labs", {"emoji": "🧪", "desc": "Comandos aprendidos resolviendo laboratorios (OverTheWire Bandit): SSH, filtrado, binarios, cron, git y más."}),
    ("Scripting", {"emoji": "📜", "desc": "Herramientas para escribir scripts en Bash: opciones, condicionales, aritmética y peticiones HTTP."}),
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


def code(text):
    """Texto como código inline seguro dentro de una tabla Markdown."""
    if not text:
        return ""
    t = text.replace("|", "\\|")
    fence = "``" if "`" in t else "`"
    pad = " " if fence == "``" else ""
    return f"{fence}{pad}{t}{pad}{fence}"


def cell(text):
    return text.replace("|", "\\|")


def build_model():
    comandos = read("comandos.csv")
    parametros = read("parametros.csv")
    # Orden de temas: el de la hoja de comandos; los temas que solo aparecen en
    # parámetros se insertan justo después del último tema visto, para respetar
    # el orden del curso.
    order = {s: [] for s in SECTIONS}
    for row in comandos:
        if row["Tema"] not in order[row["Sección"]]:
            order[row["Sección"]].append(row["Tema"])
    last = {}
    for row in parametros:
        s, t = row["Sección"], row["Tema"]
        if t not in order[s]:
            base = t.split(" [")[0]
            siblings = [i for i, x in enumerate(order[s]) if x.split(" [")[0] == base]
            if siblings:  # p. ej. "Tema [2-2]" va justo después de "Tema [1-2]"
                idx = siblings[-1] + 1
            else:
                idx = order[s].index(last[s]) + 1 if s in last else 0
            order[s].insert(idx, t)
        last[s] = t
    model = OrderedDict(
        (s, OrderedDict((t, {"comandos": [], "parametros": []}) for t in order[s])) for s in SECTIONS
    )
    for row in comandos:
        model[row["Sección"]][row["Tema"]]["comandos"].append(row)
    for row in parametros:
        model[row["Sección"]][row["Tema"]]["parametros"].append(row)
    return comandos, parametros, model


def section_md(section, temas):
    meta = SECTIONS[section]
    n_c = sum(len(t["comandos"]) for t in temas.values())
    n_p = sum(len(t["parametros"]) for t in temas.values())
    out = [
        f"# {meta['emoji']} {section}",
        "",
        f"> {meta['desc']}",
        "",
        f"**{n_c}** comandos · **{n_p}** parámetros · **{len(temas)}** temas  ·  [⬅ Volver al índice](../README.md)",
        "",
        "## Temas",
        "",
    ]
    for i, tema in enumerate(temas, 1):
        out.append(f"{i}. [{tema}](#{slug(tema)})")
    out.append("")
    for tema, data in temas.items():
        out += ["---", "", f'<a id="{slug(tema)}"></a>', "", f"## {tema}", ""]
        if data["comandos"]:
            out += ["| Comando | Qué hace | Ejemplo |", "|:--|:--|:--|"]
            for c in data["comandos"]:
                out.append(f"| {code(c['Comando'])} | {cell(c['Descripción'])} | {code(c['Ejemplo'])} |")
            out.append("")
        if data["parametros"]:
            out += ["<details open>", f"<summary><b>🔧 Parámetros y usos ({len(data['parametros'])})</b></summary>", "",
                    "| Comando | Parámetro | Qué hace | Ejemplo |", "|:--|:--|:--|:--|"]
            for p in data["parametros"]:
                out.append(f"| {code(p['Comando'])} | {code(p['Parámetro'])} | {cell(p['Descripción'])} | {code(p['Ejemplo'])} |")
            out += ["", "</details>", ""]
        out += ["<sub>[⬆ Arriba](#temas)</sub>", ""]
    return "\n".join(out)


def readme_md(comandos, parametros, model):
    out = [
        '<div align="center">',
        "",
        "# 🐧 Linux Commands",
        "",
        "**Mis apuntes de comandos de Linux y Bash, organizados por tema, con ejemplos listos para copiar.**",
        "",
        f"![Comandos](https://img.shields.io/badge/comandos-{len(comandos)}-2ea44f?style=for-the-badge)"
        f" ![Parámetros](https://img.shields.io/badge/par%C3%A1metros-{len(parametros)}-0969da?style=for-the-badge)"
        f" ![Temas](https://img.shields.io/badge/temas-{sum(len(t) for t in model.values())}-8250df?style=for-the-badge)",
        "",
        "🌐 **Versión web con buscador:** [`docs/index.html`](docs/index.html)",
        "",
        "</div>",
        "",
        "---",
        "",
        "## 📚 Secciones",
        "",
        "| | Sección | Contenido | Comandos | Parámetros |",
        "|:-:|:--|:--|:-:|:-:|",
    ]
    for s, temas in model.items():
        meta = SECTIONS[s]
        nc = sum(len(t["comandos"]) for t in temas.values())
        np_ = sum(len(t["parametros"]) for t in temas.values())
        out.append(f"| {meta['emoji']} | **[{s}](notes/{s}.md)** | {meta['desc']} | {nc} | {np_} |")
    out += ["", "## 🗂️ Temas", ""]
    for s, temas in model.items():
        out += [f"<details>", f"<summary><b>{SECTIONS[s]['emoji']} {s}</b> — {len(temas)} temas</summary>", ""]
        for tema, d in temas.items():
            cmds = ", ".join(code(c["Comando"]) for c in d["comandos"]) or "<i>solo parámetros</i>"
            out.append(f"- [{tema}](notes/{s}.md#{slug(tema)}) — {cmds}")
        out += ["", "</details>", ""]

    out += ["## 🔤 Índice alfabético de comandos", "", "| Comando | Qué hace | Sección |", "|:--|:--|:--|"]
    seen = {}
    for c in comandos:
        seen.setdefault(c["Comando"], c)
    for name in sorted(seen, key=lambda x: (not x[0].isalnum(), x.lower())):
        c = seen[name]
        out.append(f"| {code(name)} | {cell(c['Descripción'])} | [{c['Sección']}](notes/{c['Sección']}.md#{slug(c['Tema'])}) |")
    out += [
        "",
        "## 🛠️ Cómo actualizar",
        "",
        "Los datos viven en [`data/comandos.csv`](data/comandos.csv) y [`data/parametros.csv`](data/parametros.csv)"
        " (exportados de la hoja *Comandos de Linux*). Tras editarlos:",
        "",
        "```bash",
        "python3 scripts/build.py",
        "```",
        "",
        "Esto regenera este README, las notas de [`notes/`](notes) y la web de [`docs/`](docs).",
        "",
        "> 💡 Para ver la web online: **Settings → Pages → Branch `main` / carpeta `/docs`**.",
        "",
    ]
    return "\n".join(out)


def build_html(comandos, parametros, model):
    data = {
        "sections": [{"name": s, **SECTIONS[s]} for s in SECTIONS],
        "temas": [
            {"section": s, "tema": t, "id": slug(s + "-" + t), "comandos": d["comandos"], "parametros": d["parametros"]}
            for s, temas in model.items() for t, d in temas.items()
        ],
        "stats": {"comandos": len(comandos), "parametros": len(parametros)},
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
    print(f"OK: {len(comandos)} comandos, {len(parametros)} parámetros")


if __name__ == "__main__":
    main()
