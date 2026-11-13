

# =========================================================================
# Componentes
# =========================================================================
def _inv(s):
    return "inverso" if s.get("_inverso") else ""


def c_hero(s):
    fatos = ""
    if s.get("fatos"):
        fatos = '<dl class="hero__facts">{}</dl>'.format("".join(
            '<div><dt>{}</dt><dd>{}</dd></div>'.format(E(k), E(v)) for k, v in s["fatos"]))
    botoes = ('<div class="btn-row">{}</div>'.format(btn_primario(s.get("btn"), s.get("href_primario")))
              if s.get("sem_zap") else acoes(s.get("zap"), s.get("href_primario"), s.get("btn")))
    if s.get("sem_botoes"):
        botoes = ""
    return """
<section class="hero hero--statement" data-enter aria-labelledby="hero-h">
  <div class="wrap"><div class="hero-text hero__in">
    <div>
      <h1 id="hero-h">{h1}</h1>
      <p class="hero__lead">{apoio}</p>
      {botoes}
    </div>
    {fatos}
  </div></div>
</section>""".format(h1=E(s["h1"]), apoio=s["apoio"], botoes=botoes, fatos=fatos)


def c_hero_simples(s):
    return c_hero(s)


def c_pills(s):
    itens = "".join('<a class="pill" href="{}">{}</a>'.format(h, E(t)) if h
                    else '<span class="pill">{}</span>'.format(E(t)) for t, h in s["itens"])
    link = ('<p><a class="link" href="{}">{}</a></p>'.format(s["link"][1], E(s["link"][0]))
            if s.get("link") else "")
    return ('<div class="pills-bloco"><p class="t-small muted">{}</p><div class="pills">{}</div>{}</div>'
            .format(E(s["intro"]), itens, link))


def c_cards(s):
    itens = list(s["itens"])
    d = s.get("destaque")
    if d:
        itens.append({"titulo": d["titulo"], "texto": d["texto"], "href": d["href"]})
    sid = sid_novo(s["h2"])
    return secao(sid, s["h2"], s.get("sub"), [lista_rows(itens)], fundo=_inv(s))


def c_etapas(s):
    sid = sid_novo(s["h2"])
    link = ('<p class="mais"><a class="link" href="{}">{}</a></p>'.format(s["link"][1], E(s["link"][0]))
            if s.get("link") else "")
    return secao(sid, s["h2"], s.get("sub"), [colunas(s["itens"], len(s["itens"]), numerar=True), link],
                 fundo=_inv(s))


def c_etapas_detalhe(s):
    saidas = []
    for i, e in enumerate(s["itens"]):
        sid = sid_novo(e["titulo"])
        campos = "".join('<article class="span-4 stack-2"><h3 class="t-card">{}</h3><p>{}</p></article>'
                         .format(E(k), v) for k, v in e["campos"])
        head = ('<div class="section-head"><span class="step-num">{:02d}</span><h2 id="{}-h">{}</h2>'
                '<p class="t-lead">{}</p></div>'.format(i + 1, sid, E(e["titulo"]), e["texto"]))
        saidas.append(secao(sid, e["titulo"], None, ['<div class="grid">{}</div>'.format(campos)], raw_head=head))
    return "\n".join(saidas)


def c_beneficios(s):
    sid = sid_novo(s["h2"])
    return secao(sid, s["h2"], None, [colunas(s["itens"], len(s["itens"])), nota_html(s.get("nota"))],
                 fundo="inverso")


def c_checklist(s):
    sid = sid_novo(s["h2"])
    return secao(sid, s["h2"], s.get("sub"), [lista_rows(s["itens"]), nota_html(s.get("nota"))], fundo=_inv(s))


def c_sintomas(s):
    sid = sid_novo(s["h2"])
    lis = []
    for it in s["itens"]:
        nome, texto = partir_item(it)
        if nome:
            lis.append('<li><span class="rows__name">{}</span><p>{}</p></li>'.format(nome, texto))
        else:
            lis.append('<li><p>{}</p></li>'.format(texto))
    return secao(sid, s["h2"], None, ['<ul class="rows">{}</ul>'.format("".join(lis))], fundo=_inv(s))


def c_numerada(s):
    sid = sid_novo(s["h2"])
    return secao(sid, s["h2"], s.get("sub"),
                 [colunas(s["itens"], len(s["itens"]), numerar=True), nota_html(s.get("nota"))], fundo=_inv(s))


def c_rows(s):
    sid = sid_novo(s["h2"])
    return secao(sid, s["h2"], s.get("sub"), [lista_rows(s["itens"])], fundo=_inv(s))


def c_pessoa(s):
    p = EQUIPE[0]
    pills = "".join('<span class="pill">{}</span>'.format(E(c)) for c in p["credenciais"])
    pills = '<div class="pills">{}</div>'.format(pills) if pills else ""
    bio = '<p class="t-lead">{}</p>'.format(p["bio"]) if p.get("bio") else ""
    foto = ('<div class="frame frame--photo span-6 start-7"><img class="frame__img" src="/{}" alt="{}" '
            'loading="lazy"></div>'.format(p["foto"], E(p["nome"])) if p.get("foto") else "")
    sid = sid_novo(s.get("chapeu", "Quem atende"))
    texto = ('<div class="span-6 stack-4"><h2 id="{sid}-h">{nome}</h2><p class="t-lead">{cargo}</p>{pills}{bio}'
             '<p><a class="link" href="/sobre/">Conhecer a Verona Food</a></p></div>'
             .format(sid=sid, nome=E(p["nome"]), cargo=E(p["cargo"]), pills=pills, bio=bio))
    return ('<section class="section" id="{sid}" aria-labelledby="{sid}-h"><div class="wrap">'
            '<p class="t-label muted">{chapeu}</p><div class="grid grid--top">{texto}{foto}</div>'
            '</div></section>'.format(sid=sid, chapeu=E(s.get("chapeu", "Quem atende")),
                                      texto=texto, foto=foto))


def c_provas(s):
    sid = sid_novo(s["h2_entregaveis"])
    if DEPOIMENTOS:
        sid = sid_novo(s["h2_depoimentos"])
        qs = "".join(
            '<figure class="quote span-6"><blockquote>{}</blockquote><figcaption class="person">'
            '<span><span class="person__name">{}</span><span class="person__role">{}</span></span>'
            '</figcaption></figure>'.format(E(d["texto"]), E(d["nome"]),
                                            E(", ".join(x for x in (d.get("cargo"), d.get("estabelecimento")) if x)))
            for d in DEPOIMENTOS)
        return secao(sid, s["h2_depoimentos"], None, ['<div class="grid">{}</div>'.format(qs)])
    return secao(sid, s["h2_entregaveis"], s.get("sub"), [lista_rows(s["entregaveis"])], fundo=_inv(s))


def c_artigos(s):
    sid = sid_novo(s["h2"])
    itens = [{"titulo": a["titulo"], "texto": "{} · {}".format(a["categoria"], a.get("meta", "")).strip(" ·"),
              "href": a.get("href")} for a in s["itens"]]
    link = ('<p class="mais"><a class="link" href="{}">{}</a></p>'.format(s["link"][1], E(s["link"][0]))
            if s.get("link") else "")
    return secao(sid, s["h2"], s.get("sub"), [lista_rows(itens), link])


def c_faq(s):
    sid = sid_novo(s["h2"])
    itens = "".join('<div class="faq__item"><h3>{}</h3>{}</div>'.format(
        E(f["pergunta"]), "".join("<p>{}</p>".format(p) for p in f["resposta"])) for f in s["itens"])
    grid = ('<div class="grid"><div class="span-5"><div class="section-head"><h2 id="{sid}-h">{h2}</h2>'
            '<p><a class="link" href="{href}">Tirar outra dúvida</a></p></div></div>'
            '<div class="span-6 start-7 faq">{itens}</div></div>'
            .format(sid=sid, h2=E(s["h2"]), href=href_acao(), itens=itens))
    return secao(sid, s["h2"], None, [grid], raw_head="", fundo=_inv(s))


def c_nota(s):
    return nota_html(s["texto"])


def c_folha(s):
    return ""


def c_declaracao(s):
    sid = sid_novo(s["rotulo"])
    return ('<section class="section statement" id="{sid}" data-moment="word-highlight" aria-label="{rot}">'
            '<div class="wrap"><p class="t-label">{rot}</p><p class="mo-wh__text">{texto}</p></div></section>'
            .format(sid=sid, rot=E(s["rotulo"]), texto=s["texto"]))


def c_prosa(s):
    h = s["html"]
    m1 = re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S)
    if m1:                                    # página legal: h1 vira o herói, o resto em seções
        resto = h[m1.end():]
        m_p = re.match(r"\s*<p[^>]*>(.*?)</p>", resto, re.S)
        lead = m_p.group(1) if m_p else ""
        resto = resto[m_p.end():] if m_p else resto
        saida = [c_hero({"h1": re.sub(r"<[^>]+>", "", m1.group(1)), "apoio": lead, "sem_botoes": True})]
        blocos = re.split(r"(?=<h2)", resto)
        blocos = [b for b in blocos if b.strip()]
        for i in range(0, len(blocos), 3):
            grupo = blocos[i:i + 3]
            titulo = re.match(r"<h2[^>]*>(.*?)</h2>", grupo[0], re.S)
            if not titulo:
                continue
            sid = sid_novo(re.sub(r"<[^>]+>", "", titulo.group(1)))
            corpo = grupo[0][titulo.end():]
            for g in grupo[1:]:
                corpo += re.sub(r"<h2([^>]*)>(.*?)</h2>", r"<h3 class='t-card'\1>\2</h3>", g, flags=re.S)
            saida.append(secao(sid, re.sub(r"<[^>]+>", "", titulo.group(1)), None,
                               ['<div class="measure stack-4">{}</div>'.format(corpo)]))
        return "\n".join(saida)
    t = re.match(r"\s*<h2[^>]*>(.*?)</h2>", h, re.S)
    titulo = re.sub(r"<[^>]+>", "", t.group(1)) if t else ""
    corpo = h[t.end():] if t else h
    corpo = re.sub(r'\sstyle="[^"]*"', "", corpo)
    corpo = corpo.replace('class="texto"', "")
    sid = sid_novo(titulo)
    return secao(sid, titulo, None, ['<div class="measure stack-4">{}</div>'.format(corpo)], fundo=_inv(s))


# ------------------------------------------------------------------ contato
def formulario(id_sufixo="", compacto=False):
    opcoes = "".join('<option value="{0}">{0}</option>'.format(E(t)) for t in FORMULARIO["tipos_negocio"])
    endpoint = FORMULARIO.get("endpoint")
    attr_endpoint = ' data-endpoint="{}"'.format(endpoint) if endpoint else ' data-endpoint=""'
    prazo = CONTATO.get("prazo_resposta")
    enviado = "Recebi sua mensagem. Respondo {}.".format(prazo) if prazo else "Recebi sua mensagem e respondo em breve."
    email = CONTATO.get("email") or ""
    s = id_sufixo
    resposta = ('<p class="t-small muted">Respondo {}.</p>'.format(E(prazo)) if prazo else "")
    return """
<form class="form" action="mailto:{email}" method="post" enctype="text/plain"{endpoint} data-sent="{enviado}" novalidate>
  <div class="field"><label for="nome{s}">Nome</label>
    <input id="nome{s}" name="nome" type="text" autocomplete="name" required aria-describedby="e-nome{s}">
    <p class="field__error" id="e-nome{s}" hidden>Escreva o seu nome.</p></div>
  <div class="field"><label for="tel{s}">WhatsApp ou telefone</label>
    <input id="tel{s}" name="telefone" type="tel" inputmode="tel" autocomplete="tel" required aria-describedby="e-tel{s}">
    <p class="field__error" id="e-tel{s}" hidden>Escreva um telefone com DDD, por exemplo (11) 99999-9999.</p></div>
  <div class="field"><label for="email{s}">E-mail (opcional)</label>
    <input id="email{s}" name="email" type="email" autocomplete="email" inputmode="email" aria-describedby="e-email{s}">
    <p class="field__error" id="e-email{s}" hidden>Escreva um e-mail com @, como nome@exemplo.com.br.</p></div>
  <div class="field"><label for="neg{s}">Tipo de negócio</label>
    <select id="neg{s}" name="negocio" required aria-describedby="e-neg{s}">
      <option value="">Selecione</option>
      {opcoes}
    </select>
    <p class="field__error" id="e-neg{s}" hidden>Escolha o tipo de negócio.</p></div>
  <div class="field field--full"><label for="msg{s}">Como posso ajudar (opcional)</label>
    <textarea id="msg{s}" name="mensagem" rows="3"></textarea></div>
  <p class="consent"><label><input type="checkbox" name="newsletter" value="sim"> Quero receber conteúdos sobre segurança dos alimentos e gestão por e-mail.</label></p>
  <div class="btn-row"><button class="btn btn--primary" type="submit">{acao}</button></div>
  <p class="form__status" role="status" data-form-status></p>
  {resposta}
  <p class="t-small muted">Uso seus dados só para responder a este contato. Veja a <a href="/politica-de-privacidade/">Política de Privacidade</a>.</p>
</form>""".format(email=E(email), endpoint=attr_endpoint, enviado=E(enviado), s=s, opcoes=opcoes,
                  acao=E(rotulo_diagnostico()), resposta=resposta)


def c_contato(s):
    c = CONTATO
    sid = "contato"
    PAGINA_ATUAL["n"] += 1
    linhas = ['<li><span class="rows__name">WhatsApp</span><p><a class="link" href="{}" target="_blank" '
              'rel="noopener">{}</a></p></li>'.format(whatsapp_link(ZAP_PADRAO), E(c["whatsapp"])),
              '<li><span class="rows__name">Telefone</span><p><a class="link" href="tel:{}">{}</a><br>'
              '<span class="muted">{}</span></p></li>'.format(c["telefone_link"], E(c["telefone"]), E(c["horario"]))]
    if c.get("email"):
        linhas.append('<li><span class="rows__name">E-mail</span><p><a class="link" href="mailto:{0}">{0}</a></p></li>'
                      .format(E(c["email"])))
    linhas.append('<li><span class="rows__name">Onde fica</span><p>{}</p></li>'.format(E(endereco_linha())))
    prazo = c.get("prazo_resposta")
    sub = s.get("texto") or ""
    esq = ('<div class="span-5 stack-6"><div class="section-head"><h2 id="{sid}-h">{h2}</h2>'
           '<p class="t-lead">{sub}</p></div><ul class="rows">{linhas}</ul></div>'
           .format(sid=sid, h2=E(s["h2"]), sub=sub, linhas="".join(linhas)))
    dire = '<div class="span-6 start-7">{}</div>'.format(formulario(s.get("sufixo", "")))
    return ('<section class="section" id="{sid}" aria-labelledby="{sid}-h"><div class="wrap">'
            '<div class="grid grid--top">{esq}{dire}</div></div></section>'
            .format(sid=sid, esq=esq, dire=dire))


def c_cta_form(s):
    return c_contato(s)


def c_cta(s):
    return c_contato({"h2": s["h2"], "texto": s["texto"], "sufixo": "-cta"})


def c_html(s):
    return s["html"]


COMPONENTES = {
    "hero": c_hero, "hero_simples": c_hero_simples, "pills": c_pills, "cards": c_cards,
    "etapas": c_etapas, "etapas_detalhe": c_etapas_detalhe, "beneficios": c_beneficios,
    "checklist": c_checklist, "sintomas": c_sintomas, "numerada": c_numerada, "rows": c_rows,
    "pessoa": c_pessoa, "provas": c_provas, "artigos": c_artigos, "faq": c_faq,
    "nota": c_nota, "folha": c_folha, "prosa": c_prosa, "declaracao": c_declaracao,
    "cta_form": c_cta_form, "cta": c_cta, "contato": c_contato, "html": c_html,
}


# =========================================================================
# Rodapé e documento
# =========================================================================
def rodape():
    c = CONTATO
    prazo = c.get("prazo_resposta")
    lead = "Respondo {}.".format(prazo) if prazo else "Resposta por WhatsApp ou telefone."
    sol = "".join('<li><a href="{}">{}</a></li>'.format(h, E(t)) for t, h, d in SOLUCOES_NAV)
    seg = "".join('<li><a href="{}">{}</a></li>'.format(h, E(t)) for t, h, d in SEGMENTOS_NAV)
    emp = "".join('<li><a href="{}">{}</a></li>'.format(h, E(t)) for t, h in [
        ("Sobre a Verona Food", "/sobre/"), ("Como funciona", "/como-funciona/"),
        ("Conteúdos", "/conteudos/"), ("Contato", "/contato/")])
    email = ('<li><a href="mailto:{0}">{0}</a></li>'.format(E(c["email"]))) if c.get("email") else ""
    cnpj = (" · CNPJ {}".format(c["cnpj"])) if c.get("cnpj") else ""
    insta = REDES.get("instagram")
    social = ('<li><a href="{}" target="_blank" rel="noopener">Instagram</a></li>'.format(insta)) if insta else ""
    return """
<footer class="footer closing" id="contact" aria-labelledby="close-h">
  <div class="wrap">
    <div class="closing__cta close--word">
      <div class="section-head--split">
        <div><h2 id="close-h">Vamos conversar sobre a sua operação.</h2><p class="t-lead">{lead}</p></div>
        {btn}
      </div>
    </div>
    <div class="closing__links">
      <div class="grid">
        <div class="span-4 stack-4">
          <a class="nav__logo" href="/" aria-label="{nome}, página inicial"><img src="/img/logo.svg" alt="{nome}" width="700" height="210"></a>
          <p class="footer__lede">{posic}</p>
        </div>
        <div class="span-2 footer__col"><h3>Soluções</h3><ul>{sol}</ul></div>
        <div class="span-2 footer__col"><h3>Segmentos</h3><ul>{seg}</ul></div>
        <div class="span-2 footer__col"><h3>Empresa</h3><ul>{emp}</ul></div>
        <div class="span-2 footer__col"><h3>Contato</h3><ul>
          <li><a href="{zap}" target="_blank" rel="noopener">WhatsApp</a></li>
          <li><a href="tel:{tel_link}">{tel}</a></li>{email}{social}
          <li>{horario}</li></ul></div>
      </div>
      <div class="footer__legal">
        <span>&copy; <span data-ano>2026</span> {nome}{cnpj} &nbsp; <a href="/politica-de-privacidade/">Privacidade</a> &nbsp; <a href="/termos-de-uso/">Termos de uso</a></span>
      </div>
    </div>
  </div>
</footer>""".format(lead=E(lead), btn=btn_primario(), nome=E(SITE["nome_completo"]),
                    posic=E(SITE["posicionamento"]), sol=sol, seg=seg, emp=emp,
                    zap=whatsapp_link(ZAP_PADRAO), tel_link=c["telefone_link"], tel=E(c["telefone"]),
                    email=email, social=social, horario=E(c["horario"]), cnpj=E(cnpj))


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
        "address": {"@type": "PostalAddress", "streetAddress": c["endereco_rua"],
                    "addressLocality": c["endereco_cidade"], "addressRegion": c["endereco_uf"],
                    "postalCode": c["endereco_cep"], "addressCountry": "BR"},
        "openingHours": c["horario_schema"],
        "sameAs": [u for u in REDES.values() if u],
        "areaServed": COMERCIAL.get("regiao_atendimento") or "Brasil",
    }
    if c.get("email"):
        dados["email"] = c["email"]
    return '<script type="application/ld+json">{}</script>'.format(json.dumps(dados, ensure_ascii=False))


def schema_faq(itens):
    dados = {"@context": "https://schema.org", "@type": "FAQPage",
             "mainEntity": [{"@type": "Question", "name": f["pergunta"],
                             "acceptedAnswer": {"@type": "Answer",
                                                "text": " ".join(html.unescape(p) for p in f["resposta"])}}
                            for f in itens]}
    return '<script type="application/ld+json">{}</script>'.format(json.dumps(dados, ensure_ascii=False))


def schema_migalhas(trilha):
    if not trilha:
        return ""
    ld = [{"@type": "ListItem", "position": i + 1, "name": nome, "item": SITE["url"] + (href or "")}
          for i, (nome, href) in enumerate(trilha)]
    return '<script type="application/ld+json">{}</script>'.format(
        json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": ld},
                   ensure_ascii=False))


HEAD_ESTILO = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/kit/system.css">
<link rel="stylesheet" href="/kit/ui/cards.css">
<link rel="stylesheet" href="/kit/motion/motion.css">
<link rel="stylesheet" href="/kit/layout/layout.css">
<link rel="stylesheet" href="/kit/icons/icon.css">
<style>
:root {
  --p-bg: #f5ede4; --p-surface: #ebddd0; --p-ink: #2a171d; --p-muted: #6a565b;
  --p-accent: #6e0f2a; --p-accent-ink: #f5ede4; --p-action: #6e0f2a; --p-action-ink: #f5ede4;
  --p-inv-bg: #2a171d; --p-inv-surface: #362329; --p-inv-ink: #f5ede4; --p-inv-muted: #a29491;
  --p-inv-accent: #f5ede4; --p-inv-accent-ink: #2a171d; --p-inv-action: #f5ede4; --p-inv-action-ink: #2a171d;
  --font-display: "Schibsted Grotesk", system-ui, sans-serif;
  --font-text: "Schibsted Grotesk", system-ui, sans-serif;
  --display-weight: 400;
  --display-tracking: -0.035em;
  --display-tracking-xl: -0.042em;
  --ly-scale: 0.98;
}
</style>
<link rel="stylesheet" href="/css/page.css">
<script>document.documentElement.classList.add('m-enter');setTimeout(()=>document.documentElement.classList.add('m-enter-done'),700)</script>"""

HEAD_MOMENTO = """
<script>document.documentElement.classList.add('mo-js');setTimeout(()=>document.documentElement.classList.add('mo-safe'),2500)</script>
<link rel="modulepreload" href="/kit/moments/moments.js">
<link rel="modulepreload" href="/kit/moments/lib.js">
<link rel="modulepreload" href="/kit/moments/word-highlight/moment.js">"""


def documento(pagina, corpo, extras_head="", momento=False):
    url = SITE["url"] + pagina["url"]
    return """<!doctype html>
<html lang="{lang}" data-type="service" data-radius="soft" data-buttons="arrow" data-motion>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="site-kind" content="other">
<meta name="page-type" content="service">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="{nome}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{base}/img/share.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#f5ede4">{noindex}
<link rel="icon" href="/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/img/app-180.png">
<link rel="manifest" href="/site.webmanifest">
{estilo}{momento}
{schema}
{extras}
</head>
<body>
{cabecalho}
<main id="top">
{corpo}
</main>
{rodape}
<script type="module" src="/kit/system.js"></script>
<script type="module" src="/kit/motion/motion.js"></script>
<script type="module" src="/kit/layout/layout.js"></script>
<script src="/js/site.js" defer></script>
</body>
</html>
""".format(lang=SITE["lang"], title=E(pagina["title"]), desc=E(pagina["description"]),
           url=url, base=SITE["url"], nome=E(SITE["nome"]),
           noindex=('\n<meta name="robots" content="noindex, nofollow">'
                    '\n<!-- previa: nao indexar, para nao competir com o site real na busca -->'
                    if SITE.get("preview") else ""),
           estilo=HEAD_ESTILO, momento=HEAD_MOMENTO if momento else "",
           schema=schema_negocio() + schema_migalhas(pagina.get("trilha")), extras=extras_head,
           cabecalho=cabecalho(pagina["url"]), corpo=corpo, rodape=rodape())


def _injetar(html_secao, extra):
    i = html_secao.rfind("</div></section>")
    if i < 0:
        return html_secao + extra
    return html_secao[:i] + extra + html_secao[i:]


def monta(pagina):
    PAGINA_ATUAL["url"] = pagina["url"]
    PAGINA_ATUAL["n"] = 0
    secoes = [dict(s) for s in pagina["secoes"]]
    # uma única faixa escura por página (ritmo "dark-band"), na segunda metade
    for tipo in ("beneficios", "etapas", "numerada", "checklist"):
        alvo = [s for s in secoes if s["tipo"] == tipo]
        if alvo:
            if tipo != "beneficios":
                alvo[0]["_inverso"] = True
            break
    partes, pendente, faq_itens, momento = [], "", None, False
    for s in secoes:
        fn = COMPONENTES.get(s["tipo"])
        if not fn:
            raise ValueError("Componente desconhecido: " + s["tipo"])
        h = fn(s)
        if s["tipo"] == "pills":
            pendente = h
            continue
        if s["tipo"] == "nota":
            if partes:
                partes[-1] = _injetar(partes[-1], h)
            continue
        if pendente and h:
            h = _injetar(h, pendente)
            pendente = ""
        if h:
            partes.append(h)
        if s["tipo"] == "faq":
            faq_itens = s["itens"]
        if s["tipo"] == "declaracao":
            momento = True
    extras = schema_faq(faq_itens) if faq_itens else ""
    return documento(pagina, "\n".join(partes), extras, momento)
