# -*- coding: utf-8 -*-
"""Layout e componentes: transforma os dados de conteúdo em HTML.

Usa o sistema de design do kit (assets/kit): uma seção por tela, bordas iguais,
tipografia e botões do sistema. As páginas continuam descritas em pg_*.py.
"""

import html
import json
import os
import re

from config import (SITE, CONTATO, REDES, EQUIPE, COMERCIAL, FORMULARIO,
                    DEPOIMENTOS, endereco_linha, whatsapp_link, ZAP_PADRAO)

E = html.escape
_AQUI = os.path.dirname(os.path.abspath(__file__))

# Alturas medidas por página/seção (1 ou 2 telas). Gerado por medir_alturas.py.
try:
    with open(os.path.join(_AQUI, "alturas.json"), encoding="utf-8") as _f:
        ALTURAS = json.load(_f)
except (OSError, ValueError):
    ALTURAS = {}

ARROW = ('<svg class="m-arrow" viewBox="0 0 12 12" aria-hidden="true"><path class="m-arrow__stem" d="M1 6h8"/>'
         '<path class="m-arrow__head" d="M4.5 2.5 8 6l-3.5 3.5"/></svg>')

PAGINA_ATUAL = {"url": "/", "n": 0}

#SVGLINES#


def slug(txt):
    t = html.unescape(re.sub(r"<[^>]+>", "", txt or "")).lower()
    for a, b in (("áàâãä", "a"), ("éèêë", "e"), ("íìîï", "i"), ("óòôõö", "o"), ("úùûü", "u"), ("ç", "c")):
        for ch in a:
            t = t.replace(ch, b)
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t[:32] or "secao"


def sid_novo(h2):
    PAGINA_ATUAL["n"] += 1
    return "{}-{}".format(slug(h2), PAGINA_ATUAL["n"])


def altura(sid):
    """1 ou 2 telas, medidas pelo medir_alturas.py. Padrão: 1."""
    return ALTURAS.get(PAGINA_ATUAL["url"] + "#" + sid, 1)


# =========================================================================
# Navegação
# =========================================================================
SOLUCOES_NAV = [
    ("Segurança dos alimentos", "/solucoes/seguranca-dos-alimentos/", "Boas práticas, POPs, checklists e adequação sanitária."),
    ("Rotulagem", "/solucoes/rotulagem/", "Tabela nutricional, ingredientes e alergênicos."),
    ("Custos e ficha técnica", "/solucoes/custos-e-ficha-tecnica/", "Custo real por prato, porcionamento e perdas."),
    ("Treinamento de equipe", "/solucoes/treinamentos/", "Capacitação por função, na sua operação."),
    ("Padronização de processos", "/solucoes/padronizacao-de-processos/", "Procedimentos, checklists e rotina de conferência."),
    ("Consultoria completa", "/solucoes/consultoria-completa/", "Tudo junto, com acompanhamento contínuo."),
]

SEGMENTOS_NAV = [
    ("Restaurantes e bares", "/segmentos/restaurantes-e-bares/", "Padrão que aguenta o pico e a troca de equipe."),
    ("Padarias e confeitarias", "/segmentos/padarias-e-confeitarias/", "Validade, rotulagem e produção de madrugada."),
    ("Hotéis e buffets", "/segmentos/hoteis-e-buffets/", "Exposição, reposição e volume variável."),
    ("Cozinhas industriais", "/segmentos/cozinhas-industriais/", "Resfriamento, transporte e distribuição."),
    ("Mercados e varejo", "/segmentos/mercados-e-varejo/", "Açougue, rotisseria, padaria e fatiados."),
    ("Eventos", "/segmentos/eventos/", "Operação montada fora da base."),
]

MENU = [
    {"rotulo": "Soluções", "href": "/solucoes/", "filhos": SOLUCOES_NAV},
    {"rotulo": "Segmentos", "href": "/segmentos/", "filhos": SEGMENTOS_NAV},
    {"rotulo": "Como funciona", "href": "/como-funciona/"},
    {"rotulo": "Sobre", "href": "/sobre/"},
    {"rotulo": "Conteúdos", "href": "/conteudos/"},
]

CHEV = ('<svg class="chev" viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5l3 3 3-3" fill="none" '
        'stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def _ativo(href, atual):
    if href == "/":
        return atual == "/"
    return atual.startswith(href)


def rotulo_diagnostico():
    """O texto do botão principal muda conforme a política comercial definida."""
    if COMERCIAL.get("diagnostico") == "gratuito":
        return "Agendar diagnóstico gratuito"
    return "Agendar diagnóstico"


def href_acao():
    return "#contato" if PAGINA_ATUAL["url"] == "/contato/" else "/contato/#contato"


def btn_primario(texto=None, href=None, seta=True):
    return '<a class="btn btn--primary" href="{}">{}{}</a>'.format(
        href or href_acao(), E(texto or rotulo_diagnostico()), ARROW if seta else "")


def btn_zap(texto="Falar no WhatsApp", mensagem=None, classe="btn--secondary"):
    link = whatsapp_link(mensagem or ZAP_PADRAO)
    return ('<a class="btn {}" href="{}" target="_blank" rel="noopener">{}'
            '<span class="sr-only"> (abre o WhatsApp)</span></a>'.format(classe, link, E(texto)))


def acoes(mensagem_zap=None, href_primario=None, texto_primario=None):
    return '<div class="btn-row">{}{}</div>'.format(
        btn_primario(texto_primario, href_primario), btn_zap(mensagem=mensagem_zap))


def cabecalho(atual):
    itens = []
    for m in MENU:
        ativo = ' aria-current="page"' if _ativo(m["href"], atual) else ""
        if m.get("filhos"):
            metade = (len(m["filhos"]) + 1) // 2
            cols = "".join(
                '<div class="menu-col span-6"><p class="t-label">{}</p>{}</div>'.format(
                    E(m["rotulo"]) if i == 0 else "&nbsp;",
                    "".join('<a href="{}">{}<span>{}</span></a>'.format(h, E(t), E(d)) for t, h, d in grupo))
                for i, grupo in enumerate((m["filhos"][:metade], m["filhos"][metade:])))
            itens.append(
                '<div class="nav__item"><a class="nav__link" href="{}"{}>{} {}</a>'
                '<div class="nav__menu"><div class="wrap grid">{}</div></div></div>'
                .format(m["href"], ativo, E(m["rotulo"]), CHEV, cols))
        else:
            itens.append('<div class="nav__item"><a class="nav__link" href="{}"{}>{}</a></div>'
                         .format(m["href"], ativo, E(m["rotulo"])))
    return """
<header class="nav nav--centre">
  <div class="wrap nav__bar">
    <a class="skip-link" href="#top">Pular para o conteúdo</a>
    <a class="nav__logo" href="/" aria-label="{nome}, página inicial"><img src="/img/logo.svg" alt="{nome}" width="700" height="210"></a>
    <nav class="nav__links" aria-label="Principal">{itens}</nav>
    <div class="nav__actions">{btn}</div>
    <button class="nav__toggle" type="button" aria-expanded="false" aria-label="Menu">
      <svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true"><path d="M2 5h14M2 13h14" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
    </button>
  </div>
</header>""".format(nome=E(SITE["nome_completo"]), itens="".join(itens), btn=btn_primario(seta=False))


# =========================================================================
# Blocos de seção
# =========================================================================
def titulo_h2(sid, h2, sub=None):
    p = '<p class="t-lead">{}</p>'.format(sub) if sub else ""
    return '<div class="section-head"><h2 id="{}-h">{}</h2>{}</div>'.format(sid, E(h2), p)


def secao(sid, h2, sub, grupos, fundo="", classe="", raw_head=None):
    """grupos: lista de HTML. Com altura 2 e dois grupos ou mais, o primeiro bloco vai junto do
    título e o resto numa segunda linha (.g2). Com altura 1, tudo na mesma linha."""
    head = raw_head if raw_head is not None else titulo_h2(sid, h2, sub)
    h = altura(sid)
    ground = " ground-inverse" if fundo == "inverso" else ""
    estilo = ""
    if h >= 2 and len(grupos) >= 2:
        k = (len(grupos) + 1) // 2
        corpo = '<div class="group">{}{}</div>{}'.format(head, "".join(grupos[:k]), "".join(grupos[k:]))
        cl = "section g2"
    else:
        corpo = head + "".join(grupos)
        cl = "section"
        if h >= 2:
            estilo = ' style="--h: 2"'
    return ('<section class="{}{}{}" id="{}" aria-labelledby="{}-h"{}><div class="wrap">{}</div></section>'
            .format(cl, ground, (" " + classe) if classe else "", sid, sid, estilo, corpo))


def partir_item(txt):
    """'<b>Título</b> — texto' ou '<b>Título:</b> <span>texto</span>' em (título, texto)."""
    m = re.match(r"\s*<b>(.*?)</b>\s*(?:<span>)?\s*[—:\-]*\s*(.*?)(?:</span>)?\s*$", txt, re.S)
    if m:
        return m.group(1).strip(" :."), m.group(2).strip().lstrip("—:- ").strip()
    return None, txt


def lista_rows(itens):
    lis = []
    for i in itens:
        if isinstance(i, dict):
            nome, linha, href = i.get("titulo"), i.get("texto"), i.get("href")
            nome = E(nome)
        else:
            nome, linha = partir_item(i)
            href = None
        if nome is None:
            lis.append('<li><span class="rows__name">{}</span></li>'.format(linha))
        elif href:
            lis.append('<li><a class="rows__name" href="{}">{}</a><p>{}</p></li>'.format(href, nome, linha))
        else:
            lis.append('<li><span class="rows__name">{}</span><p>{}</p></li>'.format(nome, linha))
    return '<ul class="rows">{}</ul>'.format("".join(lis))


def colunas(itens, n, numerar=False):
    """n colunas de span 12/n; item: dict(titulo, texto) ou texto com <b>título</b>."""
    span = 12 // n
    out = []
    for i, it in enumerate(itens):
        if isinstance(it, dict):
            nome, texto = it.get("titulo"), it.get("texto")
            nome = E(nome) if nome else None
        else:
            nome, texto = partir_item(it)
        num = '<span class="step-num">{:02d}</span>'.format(i + 1) if numerar else ""
        cab = '<h3 class="t-card">{}</h3>'.format(nome) if nome else ""
        out.append('<article class="span-{} stack-2">{}{}<p>{}</p></article>'.format(span, num, cab, texto))
    return '<div class="grid">{}</div>'.format("".join(out))


def nota_html(t):
    return '<p class="nota t-small">{}</p>'.format(t) if t else ""
