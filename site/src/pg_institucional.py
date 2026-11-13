# -*- coding: utf-8 -*-
"""Como funciona, Sobre, Conteúdos, Contato e páginas legais."""

import html as _html

from config import CONTATO, COMERCIAL, EQUIPE, SITE, REDES, endereco_linha, whatsapp_link
from layout import formulario, ZAP_PADRAO, SVG_WHATSAPP

E = _html.escape


# =========================================================================
def como_funciona():
    prazo = CONTATO.get("prazo_resposta")
    resposta_1 = ("{}{}.".format(prazo[0].upper(), prazo[1:]) if prazo
                  else "A gente responde pessoalmente — não há atendimento automático nem central de chamadas.")

    faq = [
        {"pergunta": "Meu negócio é pequeno. Vale a pena?",
         "resposta": ["Vale, e costuma custar menos do que as pessoas imaginam. Operação pequena tem menos documentação para escrever e menos gente para treinar, então o trabalho é menor.",
                      "O que não muda com o tamanho é a exigência."]},
        {"pergunta": "Quanto tempo leva para adequar minha operação?",
         "resposta": ["Depende do porte e de quanta documentação já existe. No diagnóstico a gente dá a faixa de prazo antes de qualquer proposta, para você já saber com o que está lidando."]},
        {"pergunta": "O trabalho é presencial ou a distância?",
         "resposta": ["O diagnóstico é presencial: não dá para avaliar uma cozinha por foto. A implantação e o treinamento também acontecem dentro da operação, porque é lá que o processo precisa funcionar."]},
        {"pergunta": "Quanto custa?",
         "resposta": ["Não trabalhamos com tabela de preço. O valor depende do porte da operação, de quanto já existe pronto e por quanto tempo você quer acompanhamento.",
                      "Por isso a proposta vem depois do diagnóstico: assim você recebe um número baseado no seu negócio, e não uma faixa genérica."]},
        {"pergunta": "Vocês garantem aprovação na fiscalização?",
         "resposta": ["Não, e desconfie de quem garantir. O resultado de uma fiscalização depende do órgão, do fiscal e de como a operação está no dia.",
                      "O que a gente entrega é a documentação organizada, os procedimentos escritos e a equipe treinada — que é o que está sob o seu controle."]},
        {"pergunta": "Já contratei consultoria antes e não funcionou.",
         "resposta": ["Isso é mais comum do que parece, e quase sempre pelo mesmo motivo: o documento foi escrito longe da cozinha e a equipe nunca conseguiu seguir.",
                      "É por isso que aqui o procedimento é escrito com quem executa, e a gente volta para conferir se pegou."]},
        {"pergunta": "O que eu preciso ter em mãos para começar?",
         "resposta": ["Para a conversa inicial, nada. Para o diagnóstico: a documentação que já existir, mesmo incompleta, e acesso à operação funcionando. O resto a gente levanta na visita."]},
    ]

    etapas = [
        {"titulo": "Diagnóstico", "figura": "foto de visita de diagnóstico em cozinha",
         "texto": ("A gente vai até a sua operação em horário de funcionamento. Não é visita protocolar: é "
                   "passar algumas horas olhando como as coisas realmente acontecem quando a casa está rodando."),
         "campos": [
             ("O que a gente faz", "Olhamos estrutura, fluxo de trabalho, armazenamento, higienização, controle de temperatura, documentação e como a equipe executa cada tarefa. Conversamos com quem está na operação, não só com quem gerencia — é de quem põe a mão que vêm as respostas mais úteis."),
             ("O que você recebe", "Um relatório por escrito com o retrato da sua operação: o que já está em ordem, o que precisa de ajuste e o que é risco. Tudo classificado por prioridade — urgente, importante, pode esperar."),
             ("O que precisamos de você", "Acesso à operação funcionando, a documentação que já existir e uma pessoa da sua equipe acompanhando. Não precisa organizar nada antes: a gente precisa ver como é, não como ficaria se você arrumasse."),
         ]},
        {"titulo": "Plano de ação", "figura": "foto de reunião de plano de ação",
         "texto": ("Com o diagnóstico na mão, a gente monta o plano com você — não para você. Você conhece seu "
                   "caixa, sua equipe e seu calendário; a gente conhece o que precisa ser feito."),
         "campos": [
             ("O que a gente faz", "Transformamos cada ponto do diagnóstico em ação, com prazo, responsável e custo. Separamos o que depende de obra ou investimento do que depende só de mudança de rotina — e esse segundo grupo costuma ser maior do que as pessoas imaginam."),
             ("O que você recebe", "O plano de ação por escrito, em ordem de prioridade, e a proposta de trabalho com escopo e valor. Você aprova o que faz sentido agora e deixa o resto para depois."),
             ("O que precisamos de você", "Uma conversa com quem decide. Plano aprovado por alguém que não pode decidir não sai do papel."),
         ]},
        {"titulo": "Implantação", "figura": "foto de treinamento no posto de trabalho",
         "texto": ("É aqui que o trabalho vira rotina. Documento escrito, procedimento combinado, equipe "
                   "treinada e checklist pendurado na parede — dentro da sua operação, no horário que menos atrapalha."),
         "campos": [
             ("O que a gente faz", "Escrevemos os documentos a partir do que vimos, combinamos cada procedimento com quem executa, treinamos a equipe no próprio posto de trabalho e colocamos a rotina de registro para rodar. Você revisa tudo antes de valer."),
             ("O que você recebe", "Toda a documentação em arquivo editável, o material de treinamento, os checklists prontos para imprimir e a sua equipe sabendo usar tudo isso."),
             ("O que precisamos de você", "Tempo da equipe, combinado com antecedência e fora do pico, e a liderança presente. Quando a chefia não participa, a equipe entende que não é prioridade."),
         ]},
        {"titulo": "Acompanhamento", "figura": "foto de conferência de rotina com a equipe",
         "texto": "Consultoria que entrega e some deixa uma pasta bonita e uma operação igual. A gente volta para ver se pegou.",
         "campos": [
             ("O que a gente faz", "Conferimos se o padrão se manteve depois que a novidade passou, identificamos o que a equipe não conseguiu seguir e ajustamos. Procedimento que não cabe na rotina está errado — quem manda é a rotina, e a gente reescreve."),
             ("O que você recebe", "Relatório do que avançou e do que travou, documentos ajustados e sua equipe preparada para seguir sem a gente."),
             ("O que precisamos de você", "Que a rotina de registro continue entre as visitas. É o registro que mostra o que aconteceu quando ninguém estava olhando."),
         ]},
    ]

    return {
        "url": "/como-funciona/",
        "title": "Como funciona a consultoria — VeronaFood",
        "description": ("Diagnóstico, plano de ação, implantação e acompanhamento. Veja o que acontece em cada "
                        "etapa e o que esperar do primeiro contato."),
        "trilha": [("Início", "/"), ("Como funciona", None)],
        "secoes": [
            {"tipo": "hero_simples", "chapeu": "Como funciona",
             "h1": "Antes de contratar, saiba exatamente o que vai acontecer.",
             "apoio": ("Quatro etapas, nessa ordem, com você sabendo onde está em cada uma. Nenhuma proposta "
                       "sai antes de a gente conhecer sua operação — porque proposta feita sem ver a cozinha é chute.")},

            {"tipo": "etapas_detalhe", "h2": "As quatro etapas", "itens": etapas, "fundo": " secao--claro"},

            {"tipo": "numerada", "h2": "O que acontece depois que você entra em contato",
             "sub": "O primeiro contato não compromete você a nada. Veja o caminho inteiro antes de mandar a mensagem.",
             "itens": [
                 {"titulo": "Eu respondo", "texto": resposta_1},
                 {"titulo": "Conversa rápida",
                  "texto": "De 15 a 20 minutos, para entender que tipo de operação você tem, o que está pegando e se faz sentido marcar uma visita."},
                 {"titulo": "Visita de diagnóstico",
                  "texto": "Agendada no horário em que a sua operação roda de verdade — inclusive de madrugada ou em fim de semana, se for o caso."},
             ],
             "nota": "Só depois disso vem proposta. Antes disso, não há nada para você decidir."},

            {"tipo": "prosa", "fundo": " secao--claro", "html": """
      <h2>Como funciona o investimento</h2>
      <p class="texto" style="margin-top:16px">Não trabalhamos com tabela de preço, e o motivo é simples: duas
        cozinhas do mesmo tamanho podem precisar de trabalhos completamente diferentes. Uma já tem metade da
        documentação pronta e precisa de ajuste; a outra começa do zero.</p>
      <p class="texto" style="margin-top:16px">O valor depende de três coisas: <b>o porte da operação</b>,
        <b>quanto já existe pronto</b> e <b>por quanto tempo você quer acompanhamento</b>. Por isso a proposta
        vem depois do diagnóstico — assim você recebe um número baseado no seu negócio, e não uma faixa
        genérica que não quer dizer nada.</p>
      <p class="texto" style="margin-top:16px">O que dá para adiantar: você aprova o que faz sentido agora e
        deixa o resto para depois. Ninguém é obrigado a comprar tudo de uma vez.</p>"""},

            {"tipo": "faq", "h2": "Perguntas que a gente ouve sempre", "itens": faq},

            {"tipo": "cta_form",
             "h2": "O primeiro passo é uma conversa de 20 minutos.",
             "texto": ("Sem proposta, sem compromisso e sem apresentação de slides. Só para entender o que "
                       "está pegando e se faz sentido marcar a visita."),
             "sufixo": "-cf"},
        ],
    }


# =========================================================================
def sobre():
    p = EQUIPE[0]

    historia = """
      <h2>Como a Verona Food começou</h2>
      <p class="texto" style="margin-top:16px">A Verona Food nasceu do objetivo de unir duas áreas que quase
        nunca conversam: a gastronomia, que pensa no prato, e a nutrição, que pensa no que o prato faz.</p>
      <p class="texto" style="margin-top:16px">Dessa junção vem o jeito de trabalhar: entender a cozinha por
        dentro para escrever procedimento que a equipe consegue seguir, e entender o lado técnico para que esse
        procedimento tenha sentido. É o que separa um manual que fica na gaveta de uma rotina que roda.</p>"""

    principios = [
        {"titulo": "Vou até a cozinha em horário de movimento",
         "texto": "Operação parada não mostra nada. O que preciso ver acontece no pico, quando a equipe está correndo e o processo é testado de verdade."},
        {"titulo": "Escrevo com quem executa",
         "texto": "Procedimento feito na mesa do escritório não sobrevive à primeira semana. Eu escrevo junto com quem vai fazer, em uma página, na linguagem que a pessoa usa."},
        {"titulo": "Volto para ver se funcionou",
         "texto": "Entregar a pasta é a parte fácil. O trabalho só está feito quando a rotina continua rodando depois que eu saio."},
        {"titulo": "Não prometo o que não depende de mim",
         "texto": "O resultado de uma fiscalização depende do órgão e do dia. O que depende de mim é a documentação em ordem, o procedimento executável e a equipe treinada — e disso eu respondo."},
    ]

    secoes = [
        {"tipo": "hero", "chapeu": "Sobre a Verona Food",
         "h1": "Quem vai até a sua cozinha sou eu.",
         "apoio": ("Consultoria para negócios de alimentação conduzida de perto, operação por operação. "
                   "Sem equipe terceirizada, sem material genérico e sem promessa que dependa de terceiros."),
         "figura": "retrato da responsável técnica em contexto"},
        {"tipo": "prosa", "html": historia, "fundo": " secao--claro"},
        {"tipo": "pessoa", "chapeu": "Quem vai te atender"},
        {"tipo": "numerada", "h2": "Como eu trabalho", "itens": principios},
    ]

    # "Onde atendo" só existe se houver conteúdo real — o site atual tem essa
    # seção vazia, e repetir isso seria pior do que não ter.
    regiao = COMERCIAL.get("regiao_atendimento")
    if regiao:
        remoto = COMERCIAL.get("atendimento_remoto")
        extra = (" Além disso, parte do trabalho — revisão de documento e reuniões de plano — pode ser feita a distância."
                 if remoto else "")
        secoes.append({"tipo": "prosa", "fundo": " secao--claro", "html": """
      <h2>Onde eu atendo</h2>
      <p class="texto" style="margin-top:16px">{regiao}.{extra}</p>
      <p class="texto" style="margin-top:16px">Escritório em {end}</p>""".format(
            regiao=E(regiao), extra=extra, end=E(endereco_linha()))})

    secoes.append({
        "tipo": "cta_form",
        "h2": "Vamos conversar sobre a sua operação.",
        "texto": "Vinte minutos para entender o que está pegando. Sem proposta e sem compromisso.",
        "sufixo": "-sobre"})

    return {
        "url": "/sobre/",
        "title": "Sobre a VeronaFood Consultoria de Alimentos",
        "description": ("Quem somos, como trabalhamos e quem vai te atender. Consultoria para negócios de "
                        "alimentação."),
        "trilha": [("Início", "/"), ("Sobre", None)],
        "secoes": secoes,
    }


# =========================================================================
# Conteúdos
# Os artigos do site atual serão revisados e migrados com data e slug próprio.
# Enquanto isso não acontece, a listagem mostra os temas sem link quebrado.
ARTIGOS = [
    {"categoria": "Segurança dos alimentos", "titulo": "ISO 22000: segurança dos alimentos com padrão internacional",
     "resumo": "O que a norma exige, para quem faz sentido e como é o caminho de implementação."},
    {"categoria": "Eventos", "titulo": "Garanta a segurança do seu evento gastronômico",
     "resumo": "O que avaliar no local, como transportar e o que combinar com a equipe antes da montagem."},
    {"categoria": "Treinamento", "titulo": "Capacite sua equipe, surpreenda seus clientes",
     "resumo": "Por que treinamento genérico não pega e o que muda quando ele parte da sua própria cozinha."},
    {"categoria": "Segurança dos alimentos", "titulo": "Manual de Boas Práticas: garantia de segurança e qualidade",
     "resumo": "O que o documento precisa descrever e por que um modelo pronto raramente serve."},
]

TEMAS = [
    "Como se preparar para uma visita da vigilância sanitária",
    "O que é POP e quais a sua cozinha precisa ter",
    "Ficha técnica de prato: como montar e por que muda seu lucro",
    "Rotulagem: o que precisa estar no rótulo do produto que você embala",
    "Contaminação cruzada: os cinco pontos onde ela mais acontece",
    "Checklist de recebimento de mercadoria",
    "Boas práticas em padaria e confeitaria: os pontos mais críticos",
    "Quanto custa uma consultoria de alimentos e o que entra no preço",
]


def conteudos():
    cards = [{"titulo": a["titulo"], "texto": a["resumo"] + ' <span style="display:block;margin-top:8px;font-size:13.5px;color:var(--taupe)">Em revisão técnica</span>'}
             for a in ARTIGOS]
    temas = ["<span>{}</span>".format(E(t)) for t in TEMAS]
    return {
        "url": "/conteudos/",
        "title": "Conteúdos sobre segurança e gestão de alimentos — VeronaFood",
        "description": ("Artigos práticos sobre boas práticas, legislação, custos e treinamento para quem "
                        "trabalha com alimento."),
        "trilha": [("Início", "/"), ("Conteúdos", None)],
        "secoes": [
            {"tipo": "hero_simples", "chapeu": "Conteúdos",
             "h1": "Para ler antes de contratar qualquer consultoria",
             "apoio": ("Conteúdo prático sobre segurança dos alimentos, custos e gestão na operação. "
                       "Escrito para quem trabalha na cozinha, não para quem escreve norma.")},
            {"tipo": "rows", "h2": "Em preparação", "grade": "grade--2", "itens": cards,
             "sub": ("Estes textos já existiam e estão sendo revisados tecnicamente antes de voltar ao ar, "
                     "com data de publicação e data da última revisão visíveis."),
             "fundo": " secao--claro"},
            {"tipo": "checklist", "h2": "Próximos temas", "itens": temas,
             "sub": "O que vem pela frente, escolhido pelo que mais aparece nas visitas."},
            {"tipo": "cta_form",
             "h2": "Tem uma dúvida que não está aqui?",
             "texto": "Mande a pergunta. Se for útil para mais gente, ela vira conteúdo — e você recebe a resposta antes.",
             "sufixo": "-cont"},
        ],
    }


# =========================================================================
def contato():
    c = CONTATO
    email = ('<p><a href="mailto:{0}">{0}</a></p>'.format(c["email"])) if c["email"] else ""
    prazo = c.get("prazo_resposta")
    linha_prazo = ("<p class=\"miudo\">Respondemos {}.</p>".format(E(prazo))) if prazo else ""

    canais = """
<section class="secao">
  <div class="container">
    <div class="cta-final">
      <div>
        <h1 style="color:var(--vinho);font-size:clamp(30px,4.4vw,44px)">Vamos conversar</h1>
        <p class="apoio" style="margin-top:16px">Conte em duas linhas como está sua operação hoje.
          A gente responde com o próximo passo — sem compromisso e sem proposta genérica.</p>
        {prazo}

        <div class="grade grade--2" style="margin-top:32px">
          <div class="card">
            <h3 style="font-size:18px">WhatsApp</h3>
            <p>O jeito mais rápido de falar com a gente.</p>
            <p style="margin-top:14px"><a class="btn btn--primario btn--compacto" href="{zap}" target="_blank" rel="noopener">{svg}{wpp}</a></p>
          </div>
          <div class="card">
            <h3 style="font-size:18px">Telefone</h3>
            <p>{horario}.</p>
            <p style="margin-top:14px"><a class="btn btn--secundario btn--compacto" href="tel:{tel_link}">{tel}</a></p>
          </div>
        </div>

        <div class="card" style="margin-top:18px">
          <h3 style="font-size:18px">Onde estamos</h3>
          <p>{endereco}</p>
          {email}
          <p style="margin-top:10px"><a class="link-seta" href="{instagram}" target="_blank" rel="noopener">Instagram</a></p>
        </div>
      </div>
      {form}
    </div>
  </div>
</section>""".format(
        prazo=linha_prazo, zap=whatsapp_link(ZAP_PADRAO), svg=SVG_WHATSAPP,
        wpp=E(c["whatsapp"]), horario=E(c["horario"]), tel_link=c["telefone_link"],
        tel=E(c["telefone"]), endereco=E(endereco_linha()), email=email,
        instagram=REDES["instagram"], form=formulario("-contato"))

    return {
        "url": "/contato/",
        "title": "Fale com a VeronaFood — Consultoria de Alimentos",
        "description": ("Agende um diagnóstico ou chame no WhatsApp. Atendimento de segunda a sexta, "
                        "das 9h às 18h."),
        "trilha": [("Início", "/"), ("Contato", None)],
        "secoes": [
            {"tipo": "hero_simples", "h1": "Fale com a Bárbara.",
             "apoio": "Conte em duas linhas como está a sua operação. Respondo com o próximo passo.",
             "sem_botoes": True},
            {"tipo": "contato", "h2": "Conte como está a sua operação",
             "texto": "Sem compromisso e sem proposta genérica.", "sufixo": "-contato"},
            {"tipo": "numerada", "h2": "O que acontece depois", "fundo": " secao--claro",
             "itens": [
                 {"titulo": "Eu respondo",
                  "texto": "Pessoalmente. Não há atendimento automático nem central de chamadas." if not prazo
                           else "{}{}. Pessoalmente, sem atendimento automático.".format(E(prazo[0].upper()), E(prazo[1:]))},
                 {"titulo": "Conversa rápida",
                  "texto": "De 15 a 20 minutos, para entender o tipo de operação, o que está pegando e se faz sentido marcar uma visita."},
                 {"titulo": "Visita de diagnóstico",
                  "texto": "No horário em que a sua operação roda de verdade. Só depois dela vem proposta."},
             ]},
        ],
    }


# =========================================================================
def privacidade():
    email = CONTATO["email"] or "o canal de contato indicado no site"
    corpo = """
      <h1>Política de Privacidade</h1>
      <p class="texto" style="margin-top:18px">Esta política explica quais dados a {nome} coleta, para que
        usa e quais são os seus direitos, conforme a Lei Geral de Proteção de Dados (Lei 13.709/2018).</p>

      <h2>Quais dados coletamos</h2>
      <p>Coletamos apenas o que você informa no formulário de contato: nome, telefone ou WhatsApp, e-mail
        (opcional), tipo de negócio e a mensagem que você escrever. Não coletamos dados sensíveis e não pedimos
        CPF, CNPJ ou dados financeiros para iniciar uma conversa.</p>

      <h2>Para que usamos</h2>
      <p>Para responder ao seu contato e, se houver interesse, conduzir a conversa comercial. Se você marcar a
        caixa de consentimento, também para enviar conteúdos por e-mail — e só nesse caso.</p>

      <h2>Base legal</h2>
      <p>O tratamento para responder ao seu contato se apoia no artigo 7º, inciso V da LGPD: execução de
        procedimentos preliminares a pedido do titular. O envio de conteúdos se apoia no seu consentimento,
        que você pode retirar a qualquer momento.</p>

      <h2>Com quem compartilhamos</h2>
      <p>Não vendemos nem cedemos seus dados. Eles podem transitar por prestadores de serviço necessários ao
        funcionamento do site, como a hospedagem e a ferramenta que recebe o formulário, sempre limitados a
        essa finalidade.</p>

      <h2>Por quanto tempo guardamos</h2>
      <p>Mantemos os dados enquanto durar a conversa comercial e pelo prazo necessário ao cumprimento de
        obrigações legais. Depois disso, são eliminados.</p>

      <h2>Cookies</h2>
      <p>Este site não usa cookies de rastreamento ou de publicidade. Se isso mudar, você verá um aviso com as
        opções de aceitar e recusar com o mesmo destaque, e nenhum script de medição será carregado antes da
        sua escolha.</p>

      <h2>Seus direitos</h2>
      <p>Você pode pedir confirmação de tratamento, acesso, correção, anonimização, portabilidade ou eliminação
        dos seus dados, além de revogar o consentimento. Para exercer qualquer um desses direitos, fale com a
        gente por {email}.</p>

      <h2>Alterações</h2>
      <p>Podemos atualizar esta política. A data da última atualização fica sempre indicada abaixo.</p>
      <p class="miudo" style="margin-top:28px">Última atualização: novembro de 2026.</p>""".format(
        nome=E(SITE["nome_completo"]), email=E(email))

    return {
        "url": "/politica-de-privacidade/",
        "title": "Política de Privacidade — VeronaFood",
        "description": "Como a VeronaFood coleta, usa e protege os seus dados, conforme a LGPD.",
        "trilha": [("Início", "/"), ("Política de Privacidade", None)],
        "secoes": [{"tipo": "prosa", "html": corpo}],
    }


def termos():
    corpo = """
      <h1>Termos de Uso</h1>
      <p class="texto" style="margin-top:18px">Ao usar este site, você concorda com as condições abaixo.</p>

      <h2>Sobre o conteúdo</h2>
      <p>O conteúdo publicado aqui tem finalidade informativa e não substitui a avaliação técnica da sua
        operação. Assuntos ligados a legislação sanitária mudam com o tempo e variam conforme o tipo de
        estabelecimento, o produto e a localidade. Antes de tomar qualquer decisão com base em um texto deste
        site, confirme o que se aplica ao seu caso.</p>

      <h2>Sobre os serviços</h2>
      <p>As descrições de serviço apresentam o escopo típico do trabalho. O escopo real, os prazos e o
        investimento são definidos por proposta, depois do diagnóstico da operação.</p>
      <p>A {nome} não garante resultado que dependa de terceiros, como a aprovação em fiscalização, auditoria
        ou certificação. O que é entregue é a documentação, o procedimento e a capacitação acordados.</p>

      <h2>Propriedade do conteúdo</h2>
      <p>Textos, imagens, marca e identidade visual deste site pertencem à {nome}. A reprodução depende de
        autorização.</p>

      <h2>Links para outros sites</h2>
      <p>Links para sites de terceiros são oferecidos por conveniência. Não respondemos pelo conteúdo nem pelas
        práticas de privacidade deles.</p>

      <h2>Contato</h2>
      <p>Dúvidas sobre estes termos podem ser enviadas pelos canais da página de
        <a href="/contato/">contato</a>.</p>
      <p class="miudo" style="margin-top:28px">Última atualização: novembro de 2026.</p>""".format(
        nome=E(SITE["nome_completo"]))

    return {
        "url": "/termos-de-uso/",
        "title": "Termos de Uso — VeronaFood",
        "description": "Condições de uso do site da VeronaFood Consultoria de Alimentos.",
        "trilha": [("Início", "/"), ("Termos de Uso", None)],
        "secoes": [{"tipo": "prosa", "html": corpo}],
    }


FOTOS = [
    ("Cozinha de restaurante com dois cozinheiros", "MarkBuckawicki", "CC0",
     "https://creativecommons.org/publicdomain/zero/1.0/",
     "https://commons.wikimedia.org/wiki/File:Restaurant_Kitchen_expo_station.jpg"),
    ("Mãos cortando pimentão vermelho", "Shixart1985", "CC BY 2.0",
     "https://creativecommons.org/licenses/by/2.0/",
     "https://commons.wikimedia.org/wiki/File:Chef_prepares_fresh_ingredients_by_chopping_red_vegetables.jpg"),
    ("Tábuas de corte com legumes", "Robert Loescher", "CC BY-SA 4.0",
     "https://creativecommons.org/licenses/by-sa/4.0",
     "https://commons.wikimedia.org/wiki/File:Chopped_Veggies_on_Cutting_Board.jpg"),
    ("Buffet de café da manhã em hotel", "Kim", "CC BY-SA 2.0",
     "https://creativecommons.org/licenses/by-sa/2.0",
     "https://commons.wikimedia.org/wiki/File:Breakfast_buffet_Marriott_Hotel_Lima_05.jpg"),
]


def creditos():
    itens = "".join(
        '<h2>{}</h2><p>Autor: {}. Licença <a href="{}">{}</a>. <a href="{}">Arquivo original</a>.</p>'
        .format(E(t), E(a), l, E(lic), o) for t, a, lic, l, o in FOTOS)
    corpo = ('<h1>Créditos das fotografias</h1><p class="texto">Fotografias provisórias de bancos livres '
             '(Wikimedia Commons), usadas até a Verona Food ter as suas.</p>' + itens)
    return {
        "url": "/creditos/",
        "title": "Créditos das fotografias — VeronaFood",
        "description": "Autores e licenças das fotografias usadas no site da VeronaFood.",
        "trilha": [("Início", "/"), ("Créditos das fotografias", None)],
        "secoes": [{"tipo": "prosa", "html": corpo}],
    }


def paginas():
    return [como_funciona(), sobre(), conteudos(), contato(), privacidade(), termos(), creditos()]
