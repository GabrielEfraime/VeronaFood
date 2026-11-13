# -*- coding: utf-8 -*-
"""Layout e componentes: transforma os dados de conteúdo em HTML."""

import html
import json

from config import (SITE, CONTATO, REDES, EQUIPE, COMERCIAL, FORMULARIO,
                    DEPOIMENTOS, endereco_linha, whatsapp_link, ZAP_PADRAO)

E = html.escape


# =========================================================================
# Ícones — traço de 1,5px, derivado do vocabulário de linha do símbolo
# =========================================================================
ICONES = {
    "seguranca": '<path d="M12 3l7 3v6c0 4.4-3 8.3-7 9-4-0.7-7-4.6-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/>',
    "rotulo":    '<path d="M3 7h11l6 5-6 5H3z"/><circle cx="7.5" cy="12" r="1.2"/>',
    "custos":    '<path d="M4 19V9M10 19V5M16 19v-7M22 19H2"/>',
    "treino":    '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-5 6-5s6 1.7 6 5"/><path d="M17 7l2 2 4-4"/>',
    "processo":  '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/>',
    "completa":  '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/>',
    "relogio":   '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/>',
    "equipe":    '<circle cx="9" cy="8" r="3"/><path d="M2 20c0-3.3 2.8-5 7-5s7 1.7 7 5"/><path d="M17 5a3 3 0 010 6M19 20c0-2.2-.7-3.8-2-5"/>',
    "moeda":     '<circle cx="12" cy="12" r="9"/><path d="M12 7v10M9.5 9.5h4a1.8 1.8 0 010 3.5h-3a1.8 1.8 0 000 3.5h4"/>',
    "escudo":    '<path d="M12 3l7 3v6c0 4.4-3 8.3-7 9-4-0.7-7-4.6-7-9V6l7-3z"/>',
    "lupa":      '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
    "mapa":      '<path d="M9 3L3 6v15l6-3 6 3 6-3V3l-6 3-6-3z"/><path d="M9 3v15M15 6v15"/>',
    "chat":      '<path d="M21 12a8 8 0 01-11.6 7.1L3 21l1.9-6.4A8 8 0 1121 12z"/>',
    "doc":       '<path d="M14 3H7a2 2 0 00-2 2v14a2 2 0 002 2h10a2 2 0 002-2V8l-5-5z"/><path d="M14 3v5h5M9 13h6M9 17h4"/>',
    "check":     '<path d="M20 6L9 17l-5-5"/>',
    "restaurante": '<path d="M7 3v8a2 2 0 002 2h0v8M7 3v5M10 3v5"/><path d="M17 3c-1.5 1.5-2 3.5-2 5.5S16 12 17 12v9"/>',
    "pao":       '<path d="M4 10c0-3 2.7-5 8-5s8 2 8 5c0 1.5-1 2-2 2v7H6v-7c-1 0-2-.5-2-2z"/><path d="M9 12v5M15 12v5"/>',
    "hotel":     '<path d="M3 20V7l9-4 9 4v13"/><path d="M3 20h18M9 20v-6h6v6"/>',
    "industria": '<path d="M3 21V10l6 4V10l6 4V7l6 4v10z"/><path d="M3 21h18"/>',
    "mercado":   '<path d="M3 6h18l-1.6 9.5a2 2 0 01-2 1.5H6.6a2 2 0 01-2-1.5z"/><circle cx="9" cy="20" r="1.2"/><circle cx="17" cy="20" r="1.2"/>',
    "evento":    '<path d="M4 20l5-14 8 8-13 6z"/><path d="M14 4l1.5 1.5M19 7l1.5 1.5M17 2l.8 2.2"/>',
}

SVG_INSTAGRAM = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 1.8c-3.1 0-3.5 0-4.8.1-1.1.1-1.7.2-2.1.3-.5.2-.9.4-1.2.8-.4.3-.6.7-.8 1.2-.1.4-.3 1-.3 2.1-.1 1.3-.1 1.7-.1 4.8s0 3.5.1 4.8c.1 1.1.2 1.7.3 2.1.2.5.4.9.8 1.2.3.4.7.6 1.2.8.4.1 1 .3 2.1.3 1.3.1 1.7.1 4.8.1s3.5 0 4.8-.1c1.1-.1 1.7-.2 2.1-.3.5-.2.9-.4 1.2-.8.4-.3.6-.7.8-1.2.1-.4.3-1 .3-2.1.1-1.3.1-1.7.1-4.8s0-3.5-.1-4.8c-.1-1.1-.2-1.7-.3-2.1-.2-.5-.4-.9-.8-1.2-.3-.4-.7-.6-1.2-.8-.4-.1-1-.3-2.1-.3-1.3-.1-1.7-.1-4.8-.1zm0 3.1a4.9 4.9 0 110 9.8 4.9 4.9 0 010-9.8zm0 8.1a3.2 3.2 0 100-6.4 3.2 3.2 0 000 6.4zm6.2-8.3a1.15 1.15 0 11-2.3 0 1.15 1.15 0 012.3 0z"/></svg>')
SVG_WHATSAPP = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.5 14.4c-.3-.2-1.7-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.7 1-.9 1.2-.2.2-.3.2-.6.1-.3-.2-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.5-.5c.1-.2.2-.3.3-.5 0-.2 0-.4 0-.5 0-.2-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.2.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.7-.7 2-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.6-.3zM12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1120.2 12 8.2 8.2 0 0112 20.2z"/></svg>')


def icone(nome, classe="card__icone"):
    d = ICONES.get(nome, ICONES["doc"])
    return ('<svg class="{}" viewBox="0 0 24 24" aria-hidden="true">{}</svg>'
            .format(classe, d))


def folha(classe="folha-sep"):
    return ('<svg class="{}" viewBox="0 0 140 40" aria-hidden="true">'
            '<path d="M6 30C34 10 86 2 134 6C94 18 54 26 24 36C16 35 10 33 6 30Z"/>'
            '</svg>'.format(classe))


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
    {"rotulo": "Soluções", "href": "/solucoes/", "filhos": SOLUCOES_NAV, "id": "painel-solucoes"},
    {"rotulo": "Segmentos", "href": "/segmentos/", "filhos": SEGMENTOS_NAV, "id": "painel-segmentos"},
    {"rotulo": "Como funciona", "href": "/como-funciona/"},
    {"rotulo": "Sobre", "href": "/sobre/"},
    {"rotulo": "Conteúdos", "href": "/conteudos/"},
]


def _ativo(href, atual):
    if href == "/":
        return atual == "/"
    return atual.startswith(href)


# =========================================================================
# Botões
# =========================================================================
def rotulo_diagnostico():
    """O texto do botão muda conforme a política comercial definida."""
    tipo = COMERCIAL.get("diagnostico")
    if tipo == "gratuito":
        return "Agendar diagnóstico gratuito"
    return "Agendar diagnóstico"


def btn_primario(texto=None, href="/contato/", classe=""):
    return ('<a class="btn btn--primario {}" href="{}">{}</a>'
            .format(classe, href, E(texto or rotulo_diagnostico())))


def btn_zap(texto="Falar no WhatsApp", mensagem=None, classe="btn--secundario"):
    link = whatsapp_link(mensagem or ZAP_PADRAO)
    return ('<a class="btn {}" href="{}" target="_blank" rel="noopener">{}'
            '<span class="sr"> (abre o WhatsApp)</span>{}</a>'
            .format(classe, link, SVG_WHATSAPP, E(texto)))


def acoes(mensagem_zap=None, href_primario="/contato/", texto_primario=None):
    return ('<div class="acoes">{}{}</div>'
            .format(btn_primario(texto_primario, href_primario),
                    btn_zap(mensagem=mensagem_zap)))


# =========================================================================
# Componentes de seção
# =========================================================================
def c_hero(s):
    fig = s.get("figura", "foto real de consultoria em cozinha")
    img = ('<img src="/{}" alt="{}" width="900" height="1200">'.format(s["imagem"], E(s.get("alt", "")))
           if s.get("imagem") else
           '<div class="figura-vazia" aria-hidden="true" data-foto="{}"></div>'.format(E(fig)))
    fine = ('<p class="hero__fine">{}</p>'.format(s["fine"])) if s.get("fine") else ""
    return """
<section class="hero">
  <div class="container">
    <div class="hero__grid">
      <div>
        <p class="chapeu">{chapeu}</p>
        <h1>{h1}</h1>
        <p class="apoio">{apoio}</p>
        {acoes}
        {fine}
      </div>
      <div class="hero__fig">
        {folha}
        {img}
      </div>
    </div>
  </div>
</section>""".format(
        chapeu=E(s["chapeu"]), h1=E(s["h1"]), apoio=s["apoio"],
        acoes=acoes(s.get("zap"), s.get("href_primario", "/contato/"), s.get("btn")),
        fine=fine,
        folha=folha("folha"), img=img)


def c_hero_simples(s):
    return """
<section class="secao">
  <div class="container">
    <p class="chapeu">{chapeu}</p>
    <h1>{h1}</h1>
    <p class="apoio" style="margin-top:18px">{apoio}</p>
    <div style="margin-top:26px">{acoes}</div>
  </div>
</section>""".format(chapeu=E(s["chapeu"]), h1=E(s["h1"]), apoio=s["apoio"],
                     acoes=acoes(s.get("zap"), s.get("href_primario", "/contato/"), s.get("btn")))


def c_pills(s):
    itens = "".join(
        '<a class="pill" href="{}">{}</a>'.format(h, E(t)) if h else '<span class="pill">{}</span>'.format(E(t))
        for t, h in s["itens"])
    link = ('<p style="margin-top:20px"><a class="link-seta" href="{}">{}</a></p>'
            .format(s["link"][1], E(s["link"][0]))) if s.get("link") else ""
    return """
<section class="secao secao--claro">
  <div class="container centro">
    <p class="miudo" style="margin-bottom:16px">{intro}</p>
    <div class="pills pills--centro">{itens}</div>
    {link}
  </div>
</section>""".format(intro=E(s["intro"]), itens=itens, link=link)


def _card(c, com_icone=True):
    ic = icone(c["icone"]) if com_icone and c.get("icone") else ""
    link = ('<span class="link-seta stretch">{}</span>'.format(E(c.get("link", "Ver detalhes")))
            if c.get("href") else "")
    aberto = '<a class="card card--link" href="{}">'.format(c["href"]) if c.get("href") else '<div class="card">'
    fechado = "</a>" if c.get("href") else "</div>"
    extra = ' card--meio' if c.get("meio") else ""
    aberto = aberto.replace('class="card card--link"', 'class="card card--link{}"'.format(extra))
    aberto = aberto.replace('class="card"', 'class="card{}"'.format(extra))
    return "{}{}<h3>{}</h3><p>{}</p>{}{}".format(aberto, ic, E(c["titulo"]), c["texto"], link, fechado)


def c_cards(s):
    classe = s.get("grade", "grade--3")
    cards = "".join(_card(c) for c in s["itens"])
    destaque = ""
    if s.get("destaque"):
        d = s["destaque"]
        destaque = """
    <a class="faixa-destaque" href="{href}">
      {ic}
      <div class="tx"><h3>{titulo}</h3><p>{texto}</p></div>
      <span class="link-seta">{link}</span>
    </a>""".format(href=d["href"], ic=icone(d.get("icone", "completa")),
                   titulo=E(d["titulo"]), texto=d["texto"], link=E(d.get("link", "Ver o que inclui")))
    sub = '<p class="apoio" style="margin-top:14px">{}</p>'.format(s["sub"]) if s.get("sub") else ""
    return """
<section class="secao{fundo}" {anc}>
  <div class="container">
    <h2>{h2}</h2>
    {sub}
    <div class="grade {classe}" style="margin-top:34px">{cards}</div>
    {destaque}
  </div>
</section>""".format(fundo=s.get("fundo", ""), anc=s.get("anc", ""), h2=E(s["h2"]),
                     sub=sub, classe=classe, cards=cards, destaque=destaque)


def c_etapas(s):
    itens = "".join(
        '<div class="etapa"><div class="etapa__n">{n:02d}</div><h3>{t}</h3><p>{x}</p></div>'
        .format(n=i + 1, t=E(e["titulo"]), x=e["texto"])
        for i, e in enumerate(s["itens"]))
    link = ('<p style="margin-top:34px"><a class="link-seta" href="{}">{}</a></p>'
            .format(s["link"][1], E(s["link"][0]))) if s.get("link") else ""
    sub = '<p class="apoio" style="margin-top:14px">{}</p>'.format(s["sub"]) if s.get("sub") else ""
    return """
<section class="secao{fundo}">
  <div class="container">
    <h2>{h2}</h2>
    {sub}
    <div class="etapas etapas--home">{itens}</div>
    {link}
  </div>
</section>""".format(fundo=s.get("fundo", " secao--claro"), h2=E(s["h2"]), sub=sub, itens=itens, link=link)


def c_etapas_detalhe(s):
    blocos = []
    for i, e in enumerate(s["itens"]):
        dl = "".join('<div><dt>{}</dt><dd>{}</dd></div>'.format(E(k), v) for k, v in e["campos"])
        fig = e.get("figura", "foto da etapa")
        blocos.append("""
    <div class="etapa-longa">
      <div class="etapa-longa__fig">
        <div class="figura-vazia figura-vazia--larga" aria-hidden="true" data-foto="{fig}"></div>
      </div>
      <div>
        <div class="etapa__n">{n:02d}</div>
        <h3>{t}</h3>
        <p class="texto" style="margin-top:12px">{x}</p>
        <dl>{dl}</dl>
      </div>
    </div>""".format(fig=E(fig), n=i + 1, t=E(e["titulo"]), x=e["texto"], dl=dl))
    return """
<section class="secao{fundo}">
  <div class="container">
    <h2>{h2}</h2>
    <div class="etapas--detalhe" style="margin-top:20px">{blocos}</div>
  </div>
</section>""".format(fundo=s.get("fundo", ""), h2=E(s["h2"]), blocos="".join(blocos))


def c_beneficios(s):
    itens = "".join(
        '<div class="beneficio">{ic}<strong>{t}</strong><p>{x}</p></div>'
        .format(ic=icone(b.get("icone", "check"), "beneficio__icone"), t=E(b["titulo"]), x=b["texto"])
        for b in s["itens"])
    nota = '<div class="nota" style="margin-top:36px">{}</div>'.format(s["nota"]) if s.get("nota") else ""
    return """
<section class="secao secao--vinho">
  <div class="container">
    <h2>{h2}</h2>
    <div class="grade grade--4" style="margin-top:34px">{itens}</div>
    {nota}
  </div>
</section>""".format(h2=E(s["h2"]), itens=itens, nota=nota)


def c_checklist(s):
    itens = "".join('<li><span>{}</span></li>'.format(i) for i in s["itens"])
    sub = '<p class="apoio" style="margin-top:14px">{}</p>'.format(s["sub"]) if s.get("sub") else ""
    nota = '<div class="nota" style="margin-top:30px">{}</div>'.format(s["nota"]) if s.get("nota") else ""
    return """
<section class="secao{fundo}">
  <div class="container">
    <h2>{h2}</h2>
    {sub}
    <ul class="checklist checklist--2" style="margin-top:30px">{itens}</ul>
    {nota}
  </div>
</section>""".format(fundo=s.get("fundo", ""), h2=E(s["h2"]), sub=sub, itens=itens, nota=nota)


def c_sintomas(s):
    itens = "".join('<li>{}</li>'.format(i) for i in s["itens"])
    return """
<section class="secao{fundo}">
  <div class="container">
    <h2>{h2}</h2>
    <ul class="sintomas sintomas--2" style="margin-top:28px">{itens}</ul>
  </div>
</section>""".format(fundo=s.get("fundo", " secao--claro"), h2=E(s["h2"]), itens=itens)


def c_numerada(s):
    itens = "".join('<li><div><b>{}</b><p>{}</p></div></li>'.format(E(i["titulo"]), i["texto"])
                    for i in s["itens"])
    sub = '<p class="apoio" style="margin-top:14px">{}</p>'.format(s["sub"]) if s.get("sub") else ""
    nota = '<div class="nota" style="margin-top:32px">{}</div>'.format(s["nota"]) if s.get("nota") else ""
    return """
<section class="secao{fundo}">
  <div class="container">
    <h2>{h2}</h2>
    {sub}
    <ol class="numerada" style="margin-top:32px">{itens}</ol>
    {nota}
  </div>
</section>""".format(fundo=s.get("fundo", ""), h2=E(s["h2"]), sub=sub, itens=itens, nota=nota)


def c_rows(s):
    itens = "".join(
        '<div class="card"><h3>{}</h3><p>{}</p></div>'.format(E(r["titulo"]), r["texto"])
        for r in s["itens"])
    sub = '<p class="apoio" style="margin-top:14px">{}</p>'.format(s["sub"]) if s.get("sub") else ""
    return """
<section class="secao{fundo}">
  <div class="container">
    <h2>{h2}</h2>
    {sub}
    <div class="grade {g}" style="margin-top:32px">{itens}</div>
  </div>
</section>""".format(fundo=s.get("fundo", ""), h2=E(s["h2"]), sub=sub,
                     g=s.get("grade", "grade--3"), itens=itens)


def c_pessoa(s):
    p = EQUIPE[0]
    foto = ('<img src="/{}" alt="{}" width="700" height="875">'.format(p["foto"], E(p["nome"]))
            if p.get("foto") else
            '')
    pills = ("".join('<span class="pill pill--credencial">{}</span>'.format(E(c)) for c in p["credenciais"]))
    pills = '<div class="pills">{}</div>'.format(pills) if pills else ""
    bio = '<p class="texto">{}</p>'.format(p["bio"]) if p.get("bio") else ""
    return """
<section class="secao secao--claro">
  <div class="container">
    <div class="pessoa{semfoto}">
      {foto}
      <div>
        <p class="chapeu">{chapeu}</p>
        <h2>{nome}</h2>
        <p class="pessoa__cargo">{cargo}</p>
        {pills}
        {bio}
        <p style="margin-top:22px"><a class="link-seta" href="/sobre/">Conhecer a Verona Food</a></p>
      </div>
    </div>
  </div>
</section>""".format(foto=('<div>{}</div>'.format(foto) if foto else ''), semfoto=('' if foto else ' pessoa--sem-foto'),
                     chapeu=E(s.get("chapeu", "Quem vai te atender")),
                     nome=E(p["nome"]), cargo=E(p["cargo"]), pills=pills, bio=bio)


def c_provas(s):
    """Depoimentos quando existirem; caso contrário, os entregáveis."""
    if DEPOIMENTOS:
        itens = "".join("""
      <figure class="depoimento">
        <blockquote>“{texto}”</blockquote>
        <figcaption><b>{nome}</b>{cargo} · {estab} · {cidade}</figcaption>
      </figure>""".format(texto=E(d["texto"]), nome=E(d["nome"]), cargo=E(d["cargo"]),
                          estab=E(d["estabelecimento"]), cidade=E(d["cidade"]))
                        for d in DEPOIMENTOS)
        return """
<section class="secao">
  <div class="container">
    <h2>{h2}</h2>
    <div class="grade grade--3" style="margin-top:32px">{itens}</div>
  </div>
</section>""".format(h2=E(s.get("h2_depoimentos", "O que dizem os clientes")), itens=itens)
    return c_checklist({
        "h2": s["h2_entregaveis"], "sub": s.get("sub"), "itens": s["entregaveis"],
        "fundo": s.get("fundo", ""),
    })


def c_artigos(s):
    itens = "".join("""
      <a class="card card--link artigo-card" href="{href}">
        <div class="figura-vazia figura-vazia--larga card__img" aria-hidden="true" data-foto="{fig}" style="margin:0"></div>
        <div class="artigo-card__corpo">
          <p class="cat">{cat}</p>
          <h3>{t}</h3>
          <p class="meta">{meta}</p>
        </div>
      </a>""".format(href=a.get("href", "/conteudos/"), fig=E(a.get("figura", "imagem do artigo")),
                     cat=E(a["categoria"]), t=E(a["titulo"]), meta=E(a.get("meta", "")))
                    for a in s["itens"])
    sub = '<p class="apoio" style="margin-top:14px">{}</p>'.format(s["sub"]) if s.get("sub") else ""
    link = ('<p style="margin-top:30px"><a class="link-seta" href="{}">{}</a></p>'
            .format(s["link"][1], E(s["link"][0]))) if s.get("link") else ""
    return """
<section class="secao{fundo}">
  <div class="container">
    <h2>{h2}</h2>
    {sub}
    <div class="grade grade--3" style="margin-top:32px">{itens}</div>
    {link}
  </div>
</section>""".format(fundo=s.get("fundo", " secao--claro"), h2=E(s["h2"]), sub=sub, itens=itens, link=link)


def c_faq(s):
    itens = []
    for i, f in enumerate(s["itens"]):
        corpo = "".join("<p>{}</p>".format(p) for p in f["resposta"])
        itens.append('<details{aberto}><summary>{q}</summary><div>{a}</div></details>'
                     .format(aberto=" open" if i == 0 else "", q=E(f["pergunta"]), a=corpo))
    return """
<section class="secao{fundo}">
  <div class="container">
    <h2>{h2}</h2>
    <div class="faq" style="margin-top:28px">{itens}</div>
  </div>
</section>""".format(fundo=s.get("fundo", ""), h2=E(s["h2"]), itens="".join(itens))


def c_nota(s):
    return """
<section class="secao{fundo}" style="padding-block:clamp(28px,4vw,48px)">
  <div class="container"><div class="nota">{t}</div></div>
</section>""".format(fundo=s.get("fundo", ""), t=s["texto"])


def c_folha(s):
    return '<div class="container" style="padding-block:10px">{}</div>'.format(folha())


def c_prosa(s):
    return """
<section class="secao{fundo}">
  <div class="container">
    <div class="prosa">{html}</div>
  </div>
</section>""".format(fundo=s.get("fundo", ""), html=s["html"])


def formulario(id_sufixo="", compacto=False):
    opcoes = "".join('<option value="{0}">{0}</option>'.format(E(t)) for t in FORMULARIO["tipos_negocio"])
    endpoint = FORMULARIO.get("endpoint")
    attr_endpoint = ' data-endpoint="{}"'.format(endpoint) if endpoint else ""
    prazo = CONTATO.get("prazo_resposta")
    frase_ok = "Recebemos sua mensagem. Respondemos {}.".format(prazo) if prazo else "Recebemos sua mensagem e vamos responder em breve."
    sid = id_sufixo
    return """
<div>
  <form class="form-card" data-form-contato{endpoint} novalidate>
    <div class="campo">
      <label for="nome{s}">Nome</label>
      <input type="text" id="nome{s}" name="nome" autocomplete="name" required>
      <span class="erro" id="e-nome{s}"></span>
    </div>
    <div class="campo">
      <label for="tel{s}">WhatsApp ou telefone</label>
      <input type="tel" id="tel{s}" name="telefone" inputmode="tel" autocomplete="tel"
             placeholder="(11) 99999-9999" required>
      <span class="erro" id="e-tel{s}"></span>
    </div>
    <div class="campo">
      <label for="email{s}">E-mail <span class="opc">(opcional)</span></label>
      <input type="email" id="email{s}" name="email" autocomplete="email">
      <span class="erro" id="e-email{s}"></span>
    </div>
    <div class="campo">
      <label for="neg{s}">Tipo de negócio</label>
      <select id="neg{s}" name="negocio" required>
        <option value="">Selecione</option>
        {opcoes}
      </select>
      <span class="erro" id="e-neg{s}"></span>
    </div>
    <div class="campo">
      <label for="msg{s}">Como podemos ajudar <span class="opc">(opcional)</span></label>
      <textarea id="msg{s}" name="mensagem" rows="3"
                placeholder="Conte em duas linhas como está sua operação hoje."></textarea>
    </div>
    <div class="consent">
      <input type="checkbox" id="opt{s}" name="newsletter" value="sim">
      <label for="opt{s}" style="font-weight:400">Quero receber conteúdos sobre segurança dos alimentos e gestão por e-mail.</label>
    </div>
    <button type="submit" class="btn btn--primario">Enviar mensagem</button>
    <p class="privacidade">Usamos seus dados apenas para responder a este contato. Não enviamos newsletter sem
      autorização e não compartilhamos suas informações com terceiros.
      Veja nossa <a href="/politica-de-privacidade/">Política de Privacidade</a>.</p>
    <p class="privacidade" data-erro-envio hidden style="color:var(--erro)">Não conseguimos enviar agora.
      Tente de novo ou fale pelo WhatsApp.</p>
  </form>
  <div class="form-ok" role="status">
    <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M8 12.5l2.5 2.5L16 9.5"/></svg>
    <div><b>Mensagem enviada</b><p>{frase_ok} Se preferir falar agora, chame no WhatsApp.</p></div>
  </div>
</div>""".format(endpoint=attr_endpoint, s=sid, opcoes=opcoes, frase_ok=E(frase_ok))


def c_cta_form(s):
    tel = CONTATO["telefone"]
    return """
<section class="secao secao--vinho secao--form" data-esconde-zap>
  <div class="container">
    <div class="cta-final">
      <div>
        <h2>{h2}</h2>
        <p class="apoio" style="margin-top:16px">{texto}</p>
        <div class="cta-final__contato">
          <p><a class="link-seta" href="{zap}" target="_blank" rel="noopener">Prefere conversar agora? Chamar no WhatsApp</a></p>
          <p class="miudo">Telefone <a href="tel:{tel_link}">{tel}</a> · {horario}</p>
        </div>
      </div>
      {form}
    </div>
  </div>
</section>""".format(h2=E(s["h2"]), texto=s["texto"], zap=whatsapp_link(s.get("zap") or ZAP_PADRAO),
                     tel_link=CONTATO["telefone_link"], tel=E(tel), horario=E(CONTATO["horario"]),
                     form=formulario(s.get("sufixo", "-cta")))


def c_cta(s):
    return """
<section class="secao secao--vinho">
  <div class="container">
    <h2>{h2}</h2>
    <p class="apoio" style="margin-top:16px;margin-bottom:28px">{texto}</p>
    {acoes}
  </div>
</section>""".format(h2=E(s["h2"]), texto=s["texto"],
                     acoes=acoes(s.get("zap"), s.get("href_primario", "/contato/"), s.get("btn")))


def c_html(s):
    return s["html"]


COMPONENTES = {
    "hero": c_hero, "hero_simples": c_hero_simples, "pills": c_pills, "cards": c_cards,
    "etapas": c_etapas, "etapas_detalhe": c_etapas_detalhe, "beneficios": c_beneficios,
    "checklist": c_checklist, "sintomas": c_sintomas, "numerada": c_numerada, "rows": c_rows,
    "pessoa": c_pessoa, "provas": c_provas, "artigos": c_artigos, "faq": c_faq,
    "nota": c_nota, "folha": c_folha, "prosa": c_prosa, "cta_form": c_cta_form,
    "cta": c_cta, "html": c_html,
}


# =========================================================================
# Cabeçalho, rodapé e documento
# =========================================================================
def cabecalho(atual):
    itens = []
    for m in MENU:
        ativo = ' aria-current="page"' if _ativo(m["href"], atual) else ""
        if m.get("filhos"):
            links = "".join('<a href="{}"><b>{}</b><span>{}</span></a>'.format(h, E(t), E(d))
                            for t, h, d in m["filhos"])
            itens.append("""
        <li class="nav__item">
          <button class="nav__link" data-painel="{pid}" aria-expanded="false" aria-controls="{pid}"{ativo}>
            {rot}<svg class="nav__seta" viewBox="0 0 12 12" aria-hidden="true"><polyline points="2,4 6,8 10,4"/></svg>
          </button>
          <div class="painel" id="{pid}" hidden>
            <a href="{href}"><b>Ver todas</b><span>Visão geral de {rotlow}.</span></a>
            {links}
          </div>
        </li>""".format(pid=m["id"], rot=E(m["rotulo"]), rotlow=E(m["rotulo"].lower()),
                        href=m["href"], links=links, ativo=ativo))
        else:
            itens.append('<li class="nav__item"><a class="nav__link" href="{}"{}>{}</a></li>'
                         .format(m["href"], ativo, E(m["rotulo"])))

    # menu mobile
    mob = []
    for m in MENU:
        if m.get("filhos"):
            links = "".join('<a href="{}">{}</a>'.format(h, E(t)) for t, h, d in m["filhos"])
            mob.append('<details><summary>{rot}</summary><div><a href="{href}">Ver todas</a>{links}</div></details>'
                       .format(rot=E(m["rotulo"]), href=m["href"], links=links))
        else:
            mob.append('<a href="{}">{}</a>'.format(m["href"], E(m["rotulo"])))

    return """
<header class="topo">
  <div class="container topo__in">
    <a class="marca" href="/" aria-label="{nome} — página inicial">
      <img src="/img/logo.svg" alt="{nome}" width="700" height="210">
    </a>
    <nav class="nav" aria-label="Principal"><ul style="display:flex;gap:4px;list-style:none;margin:0;padding:0">{itens}</ul></nav>
    <div class="topo__cta">{cta}</div>
    <button class="menu-btn" data-abre-menu aria-expanded="false" aria-controls="menu-mobile" aria-label="Abrir menu">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
  </div>
</header>

<div class="mobile" id="menu-mobile" hidden>
  <div class="mobile__topo">
    <a class="marca" href="/"><img src="/img/logo.svg" alt="{nome}" width="700" height="210"></a>
    <button class="menu-btn" data-fecha-menu aria-label="Fechar menu">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>
  </div>
  <nav class="mobile__lista" aria-label="Menu">
    <a href="/">Início</a>
    {mob}
    <a href="/contato/">Contato</a>
  </nav>
  <div class="mobile__pe">
    {btn}
    {zap}
  </div>
</div>""".format(nome=E(SITE["nome_completo"]), itens="".join(itens),
                 cta='<a class="btn btn--primario btn--compacto" href="/contato/">Falar com a Verona Food</a>',
                 mob="".join(mob), btn=btn_primario(), zap=btn_zap())


def rodape():
    c = CONTATO
    email = ('<li><a href="mailto:{0}">{0}</a></li>'.format(c["email"])) if c["email"] else ""
    cnpj = (" · CNPJ {}".format(c["cnpj"])) if c["cnpj"] else ""
    sociais = '<a href="{}" target="_blank" rel="noopener" aria-label="Instagram da Verona Food">{}</a>'.format(
        REDES["instagram"], SVG_INSTAGRAM)
    if REDES.get("linkedin"):
        sociais += '<a href="{}" target="_blank" rel="noopener" aria-label="LinkedIn">in</a>'.format(REDES["linkedin"])

    sol = "".join('<li><a href="{}">{}</a></li>'.format(h, E(t)) for t, h, d in SOLUCOES_NAV)
    inst = "".join('<li><a href="{}">{}</a></li>'.format(h, E(t)) for t, h in [
        ("Sobre a Verona Food", "/sobre/"), ("Como funciona", "/como-funciona/"),
        ("Segmentos atendidos", "/segmentos/"), ("Conteúdos", "/conteudos/"), ("Contato", "/contato/")])

    return """
<footer class="rodape">
  <div class="container">
    <div class="rodape__grid">
      <div class="rodape__marca">
        <img src="/img/logo-cream.svg" alt="{nome}" width="700" height="210">
        <p>{posic}</p>
        <div class="rodape__social">{sociais}</div>
      </div>
      <div>
        <h2>Soluções</h2>
        <ul>{sol}</ul>
      </div>
      <div>
        <h2>Institucional</h2>
        <ul>{inst}</ul>
      </div>
      <div>
        <h2>Contato</h2>
        <ul>
          <li><a href="{zap}" target="_blank" rel="noopener">WhatsApp {wpp}</a></li>
          <li><a href="tel:{tel_link}">{tel}</a></li>
          {email}
          <li>{endereco}</li>
          <li>{horario}</li>
        </ul>
      </div>
    </div>
    <div class="rodape__base">
      <span>© <span data-ano>2026</span> {nome}{cnpj}</span>
      <nav aria-label="Rodapé">
        <a href="/politica-de-privacidade/">Política de Privacidade</a>
        <a href="/termos-de-uso/">Termos de Uso</a>
      </nav>
    </div>
  </div>
</footer>

<a class="zap" href="{zap}" target="_blank" rel="noopener" aria-label="Falar no WhatsApp">{svgzap}</a>""".format(
        nome=E(SITE["nome_completo"]), posic=E(SITE["posicionamento"]), sociais=sociais,
        sol=sol, inst=inst, zap=whatsapp_link(ZAP_PADRAO), wpp=E(CONTATO["whatsapp"]),
        tel_link=CONTATO["telefone_link"], tel=E(CONTATO["telefone"]), email=email,
        endereco=E(endereco_linha()), horario=E(CONTATO["horario"]), cnpj=E(cnpj),
        svgzap=SVG_WHATSAPP)


def migalhas(trilha):
    if not trilha:
        return ""
    itens, ld = [], []
    for i, (nome, href) in enumerate(trilha):
        if href:
            itens.append('<li><a href="{}">{}</a></li>'.format(href, E(nome)))
        else:
            itens.append('<li><span aria-current="page">{}</span></li>'.format(E(nome)))
        ld.append({"@type": "ListItem", "position": i + 1, "name": nome,
                   "item": SITE["url"] + (href or "")})
    schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": ld}
    return ('<nav class="container migalhas" aria-label="Você está aqui"><ol>{}</ol></nav>'
            '<script type="application/ld+json">{}</script>'
            .format("".join(itens), json.dumps(schema, ensure_ascii=False)))


def schema_negocio():
    c = CONTATO
    dados = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": SITE["nome_completo"],
        "description": SITE["descricao_curta"],
        "url": SITE["url"],
        "logo": SITE["url"] + "/img/logo.svg",
        "telephone": c["telefone"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": c["endereco_rua"],
            "addressLocality": c["endereco_cidade"],
            "addressRegion": c["endereco_uf"],
            "postalCode": c["endereco_cep"],
            "addressCountry": "BR",
        },
        "openingHours": c["horario_schema"],
        "sameAs": [u for u in REDES.values() if u],
        "areaServed": COMERCIAL.get("regiao_atendimento") or "Brasil",
    }
    if c["email"]:
        dados["email"] = c["email"]
    return '<script type="application/ld+json">{}</script>'.format(json.dumps(dados, ensure_ascii=False))


def schema_faq(itens):
    dados = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{
            "@type": "Question", "name": f["pergunta"],
            "acceptedAnswer": {"@type": "Answer",
                               "text": " ".join(html.unescape(p) for p in f["resposta"])},
        } for f in itens],
    }
    return '<script type="application/ld+json">{}</script>'.format(json.dumps(dados, ensure_ascii=False))


def documento(pagina, corpo, extras_head=""):
    url = SITE["url"] + pagina["url"]
    return """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="{nome}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{base}/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#6E0F2A">{noindex}
<link rel="icon" href="/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/img/app-180.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="/css/site.css">
{schema}
{extras}
</head>
<body>
<a class="pular" href="#conteudo">Pular para o conteúdo</a>
{cabecalho}
<main id="conteudo">
{migalhas}
{corpo}
</main>
{rodape}
<script src="/js/site.js" defer></script>
</body>
</html>
""".format(lang=SITE["lang"], title=E(pagina["title"]), desc=E(pagina["description"]),
           url=url, base=SITE["url"], nome=E(SITE["nome"]),
           noindex=('\n<meta name="robots" content="noindex, nofollow">'
                    '\n<!-- previa: nao indexar, para nao competir com o site real -->'
                    if SITE.get("preview") else ""),
           schema=schema_negocio(), extras=extras_head,
           cabecalho=cabecalho(pagina["url"]),
           migalhas=migalhas(pagina.get("trilha")),
           corpo=corpo, rodape=rodape())


def monta(pagina):
    partes = []
    faq_itens = None
    for s in pagina["secoes"]:
        fn = COMPONENTES.get(s["tipo"])
        if not fn:
            raise ValueError("Componente desconhecido: " + s["tipo"])
        partes.append(fn(s))
        if s["tipo"] == "faq":
            faq_itens = s["itens"]
    extras = schema_faq(faq_itens) if faq_itens else ""
    return documento(pagina, "\n".join(partes), extras)
