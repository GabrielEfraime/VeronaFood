# -*- coding: utf-8 -*-
"""Mede a altura do conteúdo de cada seção (1440x900) e grava src/alturas.json.

Uma seção com conteúdo até 708 px cabe em uma tela; de 708 a 1320, em duas (.g2);
acima disso é preciso dividir. Rode depois de `python build.py`, e `python build.py`
de novo para aplicar.

    python medir_alturas.py
"""

import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(RAIZ, "dist")
SKILL = os.path.expanduser("~/.claude/plugins/cache/taste-skill/taste-skill/2.5.1/skills/taste-skill")
CHECK = os.path.join(SKILL, "assets", "layout", "check.mjs")
PERFIL = os.path.join(RAIZ, ".taste-skill", "chrome-medir")


def paginas():
    for r, _, fs in os.walk(DIST):
        if "index.html" in fs and ".taste-skill" not in r and os.sep + "kit" not in r:
            rel = os.path.relpath(r, DIST).replace(os.sep, "/")
            yield ("/" if rel == "." else "/" + rel + "/"), os.path.join(r, "index.html")


def main():
    alturas, altos = {}, []
    so = sys.argv[1:]
    if so and os.path.exists(os.path.join(RAIZ, "src", "alturas.json")):
        with open(os.path.join(RAIZ, "src", "alturas.json"), encoding="utf-8") as f:
            alturas = {k: v for k, v in json.load(f).items() if k.split("#")[0] not in so}
    for url, arquivo in sorted(paginas()):
        if so and url not in so:
            continue
        r = subprocess.run(
            ["node", CHECK, "--url", arquivo, "--root", DIST, "--profile", PERFIL,
             "--sizes", "1440x900", "--json"], capture_output=True, text=True, encoding="utf-8")
        try:
            dados = json.loads(r.stdout)[0]
        except (ValueError, IndexError):
            print("  falhou:", url, r.stderr[-200:])
            continue
        for sec in dados["sections"]:
            m = re.match(r"#(\S+)", sec["where"])
            if not m:
                continue
            c = sec["content"]
            if c > 708:
                alturas[url + "#" + m.group(1)] = 2
            if c > 1320:
                altos.append((url, m.group(1), c))
        print("  medida:", url)
    with open(os.path.join(RAIZ, "src", "alturas.json"), "w", encoding="utf-8") as f:
        json.dump(alturas, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("\n{} seções em duas telas.".format(len(alturas)))
    for u, s, c in altos:
        print("  alta demais (dividir):", u, s, c)


if __name__ == "__main__":
    sys.exit(main())
