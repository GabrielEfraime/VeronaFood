# -*- coding: utf-8 -*-
"""Página inicial."""

from config import CONTATO, COMERCIAL

PILLS_SEGMENTOS = [
    ("Restaurantes", "/segmentos/restaurantes-e-bares/"),
    ("Bares", "/segmentos/restaurantes-e-bares/"),
    ("Hotéis", "/segmentos/hoteis-e-buffets/"),
    ("Padarias", "/segmentos/padarias-e-confeitarias/"),
    ("Confeitarias", "/segmentos/padarias-e-confeitarias/"),
    ("Cozinhas industriais", "/segmentos/cozinhas-industriais/"),
    ("Buffets e eventos", "/segmentos/eventos/"),
    ("Mercados", "/segmentos/mercados-e-varejo/"),
]

CARDS_SOLUCOES = [
    {"titulo": "Segurança dos alimentos",
     "href": "/solucoes/seguranca-dos-alimentos/",
     "texto": "Boas práticas, POPs, controle de qualidade e adequação sanitária. Para funcionar todo dia, não só no dia da visita."},
    {"titulo": "Rotulagem",
     "href": "/solucoes/rotulagem/",
     "texto": "Tabela nutricional, ingredientes e alergênicos do produto que você embala, calculados a partir da sua receita."},
    {"titulo": "Custos e ficha técnica",
     "href": "/solucoes/custos-e-ficha-tecnica/",
     "texto": "Quanto custa cada receita, cada porção e cada perda. E quanto cada prato deixa no fim do mês."},
    {"titulo": "Treinamento de equipe",
     "href": "/solucoes/treinamentos/",
     "texto": "Treino por função, em linguagem de cozinha, com material que fica com o time."},
    {"titulo": "Padronização de processos",
     "href": "/solucoes/padronizacao-de-processos/",
     "texto": "Procedimentos escritos e checklists para o padrão se manter quando a equipe troca."},
]

ETAPAS = [
    {"titulo": "Diagnóstico",
     "texto": "Visito a operação funcionando e olho processo, estrutura, documentos e rotina da equipe. Você recebe um relatório do que está em ordem e do que precisa de ajuste, por prioridade."},
    {"titulo": "Plano de ação",
     "texto": "Monto o plano com prazo, responsável e custo de cada frente. Você aprova o que faz sentido agora e deixa o resto para depois."},
    {"titulo": "Implantação",
     "texto": "Faço junto com o seu time: documentos, procedimentos, rotina de controle e treinamento no próprio local de trabalho."},
    {"titulo": "Acompanhamento",
     "texto": "Volto para ver se o padrão ficou, ajusto o que não funcionou e deixo a equipe pronta para seguir sozinha."},
]

FAQ_HOME = [
    {"pergunta": "Meu negócio é pequeno. Compensa contratar consultoria?",
     "resposta": ["Costuma custar menos do que se imagina. Operação pequena tem menos documento para escrever e menos gente para treinar.",
                  "A exigência da fiscalização é a mesma, qualquer que seja o tamanho."]},
    {"pergunta": "Quanto tempo leva para adequar a operação?",
     "resposta": ["Depende do porte e de quanta documentação já existe. Digo a faixa de prazo no diagnóstico, antes de qualquer proposta."]},
    {"pergunta": "Você garante a aprovação na fiscalização?",
     "resposta": ["Não, e desconfie de quem garante. O resultado depende do órgão, do fiscal e de como a operação está naquele dia.",
                  "O que eu entrego é a documentação em ordem, os procedimentos escritos e a equipe treinada. Isso está nas suas mãos."]},
    {"pergunta": "O trabalho é presencial ou a distância?",
     "resposta": ["O diagnóstico é presencial. Não dá para avaliar uma cozinha por foto. A implantação e o treinamento também acontecem na sua operação, que é onde o processo precisa funcionar."]},
    {"pergunta": "Quanto custa?",
     "resposta": ["Não tenho tabela. O valor depende do porte, de quanto já existe pronto e de quanto tempo de acompanhamento você quer.",
                  "A proposta vem depois do diagnóstico, com número baseado no seu negócio. A lógica completa está em <a href=\"/como-funciona/\">Como funciona</a>."]},
    {"pergunta": "O que preciso ter em mãos para começar?",
     "resposta": ["Para a primeira conversa, nada. Para o diagnóstico, a documentação que existir, mesmo incompleta ou vencida, e acesso à operação funcionando."]},
]

ENTREGAVEIS = [
    "<b>Relatório de diagnóstico:</b> <span>o retrato da sua operação, com prioridade por item.</span>",
    "<b>Manual de Boas Práticas:</b> <span>escrito para a sua cozinha, não um modelo pronto.</span>",
    "<b>POPs:</b> <span>o passo a passo de cada tarefa crítica.</span>",
    "<b>Checklists de controle:</b> <span>prontos para imprimir e pendurar na parede.</span>",
    "<b>Fichas técnicas:</b> <span>custo, rendimento e modo de preparo por item.</span>",
    "<b>Material de treinamento:</b> <span>fica com a equipe quando eu saio.</span>",
]

ARTIGOS = [
    {"categoria": "Segurança dos alimentos", "titulo": "ISO 22000: segurança dos alimentos com padrão internacional",
     "meta": "Leitura de 5 min", "href": "/conteudos/"},
    {"categoria": "Eventos", "titulo": "Garanta a segurança do seu evento gastronômico",
     "meta": "Leitura de 4 min", "href": "/conteudos/"},
    {"categoria": "Treinamento", "titulo": "Capacite sua equipe, surpreenda seus clientes",
     "meta": "Leitura de 4 min", "href": "/conteudos/"},
]


def pagina():
    prazo = CONTATO.get("prazo_resposta")
    regiao = COMERCIAL.get("regiao_atendimento") or "Brasil"

    return {
        "url": "/",
        "arquivo": "index.html",
        "title": "VeronaFood — Consultoria para negócios de alimentação",
        "description": ("Consultoria em segurança dos alimentos, custos, padronização e treinamento para "
                        "restaurantes, padarias, hotéis, cozinhas industriais, buffets, eventos e mercados."),
        "secoes": [
            {"tipo": "hero",
             "h1": "Sua cozinha funcionando como está no papel.",
             "apoio": ("Sou nutricionista e gastrônoma. Ajudo quem trabalha com comida a organizar segurança "
                       "dos alimentos, custos, processos e treinamento da equipe, a partir da operação como ela é."),
             "fatos": [("Atendimento", regiao),
                       ("Horário", "Seg a sex, 9h às 18h"),
                       ("Resposta", prazo[0].upper() + prazo[1:] if prazo else "Por WhatsApp ou telefone"),
                       ("Formação", "Nutricionista e gastrônoma")]},

            {"tipo": "pills", "intro": "Atendo:", "itens": PILLS_SEGMENTOS,
             "link": ("Ver os segmentos", "/segmentos/")},

            {"tipo": "cards",
             "h2": "Frentes de trabalho",
             "sub": "Cada frente funciona sozinha ou junto com as outras. O diagnóstico mostra por onde começar.",
             "itens": CARDS_SOLUCOES,
             "destaque": {"titulo": "Consultoria completa",
                          "href": "/solucoes/consultoria-completa/",
                          "texto": "Para quando o negócio precisa de tudo: diagnóstico, plano, implantação e acompanhamento contínuo."}},

            {"tipo": "declaracao", "rotulo": "Como eu trabalho",
             "texto": ("Procedimento escrito longe da cozinha não sobrevive à primeira semana. "
                       "Eu escrevo junto com <strong>quem executa</strong>, em uma página, "
                       "na linguagem de quem usa.")},

            {"tipo": "etapas",
             "h2": "Quatro etapas de trabalho",
             "itens": ETAPAS,
             "link": ("Ver o processo em detalhe", "/como-funciona/")},

            {"tipo": "beneficios",
             "h2": "O que muda na rotina",
             "itens": [
                 {"titulo": "Menos retrabalho",
                  "texto": "Com o procedimento escrito, acaba o “cada um faz de um jeito”."},
                 {"titulo": "Equipe mais segura",
                  "texto": "Gente treinada erra menos e pergunta menos."},
                 {"titulo": "Custo à vista",
                  "texto": "A ficha técnica mostra quanto cada prato custa de verdade."},
                 {"titulo": "Documentação em dia",
                  "texto": "Papel organizado e rotina de controle rodando, para qualquer visita."},
             ],
             "nota": ("Não prometo aprovação em fiscalização: o resultado depende do órgão e do dia. "
                      "Entrego a documentação em ordem e a equipe preparada.")},

            {"tipo": "provas",
             "h2_entregaveis": "O que você recebe",
             "h2_depoimentos": "O que dizem os clientes",
             "sub": "Tudo em arquivo editável, para a sua equipe atualizar depois.",
             "entregaveis": ENTREGAVEIS},

            {"tipo": "artigos",
             "h2": "Conteúdos para ler antes de contratar",
             "sub": "Segurança, custos e gestão na operação de alimentos.",
             "itens": ARTIGOS,
             "link": ("Ver todos os conteúdos", "/conteudos/")},

            {"tipo": "faq", "h2": "Perguntas frequentes", "itens": FAQ_HOME},

            {"tipo": "cta_form",
             "h2": "Conte como está a sua operação",
             "texto": "Duas linhas bastam. Respondo com o próximo passo.",
             "sufixo": "-home", "pessoa": True},
        ],
    }
