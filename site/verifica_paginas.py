# -*- coding: utf-8 -*-
"""Roda o verificador de layout do skill em todas as páginas (1440 e 390) e resume.

    python verifica_paginas.py
"""
import json
import os
import subprocess
import sys
from collections import Counter

RAIZ = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(RAIZ, "dist")
SKILL = os.path.expanduser("~/.claude/plugins/cache/taste-skill/taste-skill/2.5.1/skills/taste-skill")
CHECK = os.path.join(SKILL, "assets", "layout", "check.mjs")
PERFIL = os.path.join(RAIZ, ".taste-skill", "chrome-medir")


def paginas():
    for r, _, fs in os.walk(DIST):
        rr = r.replace(os.sep, "/")
        if "index.html" in fs and "/kit" not in rr and ".taste-skill" not in rr:
            rel = os.path.relpath(r, DIST).replace(os.sep, "/")
            yield ("/" if rel == "." else "/" + rel + "/"), os.path.join(r, "index.html")


def main():
    geral = Counter()
    saida = {}
    for url, arq in sorted(paginas()):
        r = subprocess.run(["node", CHECK, "--url", arq, "--root", DIST, "--profile", PERFIL,
                            "--sizes", "1440x900,390x844", "--json"],
                           capture_output=True, text=True, encoding="utf-8")
        try:
            dados = json.loads(r.stdout)
        except ValueError:
            print("falhou", url)
            continue
        info = {}
        for d in dados:
            tam = d["size"] if isinstance(d.get("size"), str) else str(d.get("size"))
            regras = Counter(f["rule"] for f in d["findings"])
            info[tam] = {"overflowX": d.get("overflowX"), "regras": dict(regras)}
            for k, v in regras.items():
                if k not in ("neighbour", "neighbour-ground", "screen-short", "screen-height",
                             "hero-fold", "hero-maxchars", "hero-lines", "sparse"):
                    geral[k] += v
        saida[url] = info
        flags = [t for t, v in info.items() if v["overflowX"]]
        print("{:42s} overflow-x: {}".format(url, ",".join(flags) or "não"))
    print("\nOutras regras (fora as de altura de tela):", dict(geral))
    with open(os.path.join(RAIZ, ".taste-skill", "verifica.json"), "w", encoding="utf-8") as f:
        json.dump(saida, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    sys.exit(main())
