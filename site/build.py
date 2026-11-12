# -*- coding: utf-8 -*-
"""
Gerador do site da VeronaFood.

    python build.py            gera o site em site/dist/
    python build.py --servir   gera e abre um servidor local em http://localhost:8000

Sem dependências externas. Só Python 3.9 ou mais novo.
"""

import os
import re
import shutil
import sys
import datetime

RAIZ = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(RAIZ, "src")
ASSETS = os.path.join(RAIZ, "assets")
DIST = os.path.join(RAIZ, "dist")
LOGOS = os.path.abspath(os.path.join(RAIZ, "..", "VeronaFood_Alimentos", "01_Logos"))
ICONES_SRC = os.path.abspath(os.path.join(RAIZ, "..", "VeronaFood_Alimentos", "02_Icons"))

sys.path.insert(0, SRC)

import config                                    # noqa: E402
from layout import monta, SOLUCOES_NAV, SEGMENTOS_NAV   # noqa: E402
import pg_home, pg_solucoes, pg_segmentos, pg_institucional  # noqa: E402


# -------------------------------------------------------------------------
def limpa():
    """Esvazia dist/ sem remover a pasta: no Windows, um servidor aberto nela
    trava a remoção do diretório raiz, mas não a do conteúdo."""
    os.makedirs(DIST, exist_ok=True)
    for nome in os.listdir(DIST):
        caminho = os.path.join(DIST, nome)
        if os.path.isdir(caminho):
            shutil.rmtree(caminho, ignore_errors=True)
        else:
            try:
                os.remove(caminho)
            except OSError:
                pass


def copia_assets():
    shutil.copytree(os.path.join(ASSETS, "css"), os.path.join(DIST, "css"))
    shutil.copytree(os.path.join(ASSETS, "js"), os.path.join(DIST, "js"))
    img = os.path.join(DIST, "img")
    os.makedirs(img, exist_ok=True)

    # logos oficiais do pacote de identidade
    pares = [
        ("horizontal_wine.svg", "logo.svg"),
        ("horizontal_cream.svg", "logo-cream.svg"),
        ("icon_wine.svg", "favicon.svg"),
        ("icon_color.svg", "icone.svg"),
    ]
    faltando = []
    for origem, destino in pares:
        p = os.path.join(LOGOS, origem)
        if os.path.exists(p):
            shutil.copyfile(p, os.path.join(img, destino))
        else:
            faltando.append(origem)

    for nome, destino in [("app_180.png", "app-180.png"), ("app_192.png", "app-192.png"),
                          ("app_512.png", "app-512.png"), ("favicon.ico", "favicon.ico")]:
        p = os.path.join(ICONES_SRC, nome)
        if os.path.exists(p):
            shutil.copyfile(p, os.path.join(img if nome != "favicon.ico" else DIST, destino))

    # imagens próprias do projeto (fotos), quando existirem
    proprias = os.path.join(ASSETS, "img")
    if os.path.isdir(proprias):
        for nome in os.listdir(proprias):
            shutil.copyfile(os.path.join(proprias, nome), os.path.join(img, nome))
    return faltando


def grava(pagina):
    destino = pagina.get("arquivo")
    if not destino:
        destino = pagina["url"].strip("/") + "/index.html"
    caminho = os.path.join(DIST, destino.replace("/", os.sep))
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(monta(pagina))
    return destino


def extras(paginas):
    hoje = datetime.date.today().isoformat()
    base = config.SITE["url"]

    prioridade = {"/": "1.0", "/contato/": "0.9", "/solucoes/": "0.9", "/segmentos/": "0.8"}
    urls = "".join(
        "  <url><loc>{}{}</loc><lastmod>{}</lastmod><priority>{}</priority></url>\n"
        .format(base, p["url"], hoje, prioridade.get(p["url"], "0.7"))
        for p in paginas)
    with open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + urls + '</urlset>\n')

    with open(os.path.join(DIST, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: {}/sitemap.xml\n".format(base))

    with open(os.path.join(DIST, "site.webmanifest"), "w", encoding="utf-8") as f:
        f.write('{\n  "name": "%s",\n  "short_name": "%s",\n'
                '  "start_url": "/",\n  "display": "standalone",\n'
                '  "background_color": "#F5EDE4",\n  "theme_color": "#6E0F2A",\n'
                '  "icons": [\n'
                '    {"src": "/img/app-192.png", "sizes": "192x192", "type": "image/png"},\n'
                '    {"src": "/img/app-512.png", "sizes": "512x512", "type": "image/png"}\n'
                '  ]\n}\n' % (config.SITE["nome_completo"], config.SITE["nome"]))

    # redirecionamentos das URLs antigas (Netlify/Vercel leem _redirects)
    with open(os.path.join(DIST, "_redirects"), "w", encoding="utf-8") as f:
        f.write("# URLs do site antigo → novas. Sem isso, perde-se o posicionamento já conquistado.\n")
        for antigo, novo in [
            ("/empresa", "/sobre/"), ("/empresa/*", "/sobre/"),
            ("/noticias", "/conteudos/"), ("/noticias/*", "/conteudos/"),
            ("/contatos", "/contato/"), ("/contatos/*", "/contato/"),
            ("/categorias/destaque/*", "/conteudos/"),
            ("/destaque/*", "/conteudos/"),
            ("/politicas-de-privacidade", "/politica-de-privacidade/"),
        ]:
            f.write("{}  {}  301\n".format(antigo, novo))


def confere(paginas, html_por_url):
    """Checagens simples que pegam os erros mais comuns."""
    problemas = []
    conhecidas = {p["url"] for p in paginas} | {
        "/politica-de-privacidade/", "/termos-de-uso/"}
    for url, html in html_por_url.items():
        for href in set(re.findall(r'href="(/[^"#?]*)"', html)):
            if href.startswith(("/css", "/js", "/img", "/sitemap", "/robots", "/site.webmanifest")):
                continue
            if href not in conhecidas:
                problemas.append("{}: link para {} não existe".format(url, href))
        if html.count("<h1") != 1:
            problemas.append("{}: deveria ter exatamente um <h1>".format(url))
        if 'alt=""' not in html and "<img" in html and 'alt=' not in html:
            problemas.append("{}: imagem sem alt".format(url))
    return sorted(set(problemas))


def main():
    print("\n  VeronaFood — gerando o site\n  " + "-" * 44)
    limpa()
    logos_faltando = copia_assets()

    paginas = (
        [pg_home.pagina()]
        + pg_solucoes.paginas()
        + pg_segmentos.paginas()
        + pg_institucional.paginas()
    )

    html_por_url = {}
    for p in paginas:
        destino = grava(p)
        html_por_url[p["url"]] = monta(p)
        print("  ✓ {:34s} → dist/{}".format(p["url"], destino))

    extras(paginas)
    print("  ✓ sitemap.xml · robots.txt · site.webmanifest · _redirects")

    if logos_faltando:
        print("\n  ! logos não encontrados: " + ", ".join(logos_faltando))

    problemas = confere(paginas, html_por_url)
    if problemas:
        print("\n  PROBLEMAS ENCONTRADOS")
        for x in problemas:
            print("    · " + x)
    else:
        print("\n  Checagem de links e títulos: tudo certo.")

    pend = config.pendencias()
    if pend:
        print("\n  AINDA FALTA PREENCHER  (site/src/config.py)")
        for x in pend:
            print("    ⚠ " + x)

    print("\n  {} páginas em site/dist/\n".format(len(paginas)))

    if "--servir" in sys.argv:
        import http.server, socketserver, functools
        h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIST)
        with socketserver.TCPServer(("", 8000), h) as s:
            print("  servindo em http://localhost:8000  (Ctrl+C para parar)\n")
            s.serve_forever()


if __name__ == "__main__":
    main()
