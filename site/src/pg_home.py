# -*- coding: utf-8 -*-
"""Página inicial."""

from config import CONTATO
from layout import SEGMENTOS_NAV

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
    {"titulo": "Segurança dos alimentos", "icone": "seguranca",
     "href": "/solucoes/seguranca-dos-alimentos/",
     "texto": "Boas práticas, POPs, controle de qualidade e adequação sanitária — organizados para passarem no dia a dia, não só na visita."},
    {"titulo": "Rotulagem", "icone": "rotulo",
     "href": "/solucoes/rotulagem/",
     "texto": "Tabela nutricional, lista de ingredientes e alergênicos do produto que você embala, calculados a partir da sua receita."},
    {"titulo": "Custos e ficha técnica", "icone": "custos",
     "href": "/solucoes/custos-e-ficha-tecnica/",
     "texto": "Custo real da receita, porcionamento e controle de perdas. Você passa a saber quanto cada item deixa."},
    {"titulo": "Treinamento de equipe", "icone": "treino", "meio": True,
     "href": "/solucoes/treinamentos/",
     "texto": "Capacitação por função, com linguagem de cozinha e material que fica com o time depois que a gente sai."},
    {"titulo": "Padronização de processos", "icone": "processo", "meio": True,
     "href": "/solucoes/padronizacao-de-processos/",
     "texto": "Procedimentos escritos, checklists e rotinas que mantêm o padrão mesmo com troca de equipe."},
]

ETAPAS = [
    {"titulo": "Diagnóstico",
     "texto": "Visitamos sua operação em horário de funcionamento e olhamos processo, estrutura, documentação e rotina da equipe. Você recebe um relatório com o que está em ordem e o que precisa de ajuste, por prioridade."},
    {"titulo": "Plano de ação",
     "texto": "Montamos o plano com prazos realistas, responsáveis e custo de cada frente. Você aprova o que faz sentido agora e o que fica para depois."},
    {"titulo": "Implantação",
     "texto": "Colocamos em prática junto com seu time: documentos, procedimentos, rotinas de controle e treinamento no próprio ambiente de trabalho."},
    {"titulo": "Acompanhamento",
     "texto": "Voltamos para conferir se o padrão se manteve, ajustamos o que não funcionou na prática e preparamos a equipe para seguir sozinha."},
]

FAQ_HOME = [
    {"pergunta": "Meu negócio é pequeno. Vale a pena contratar consultoria?",
     "resposta": ["Vale, e costuma custar menos do que as pessoas imaginam. Operação pequena tem menos documentação para escrever e menos gente para treinar, então o trabalho é menor.",
                  "O que não muda com o tamanho é a exigência."]},
    {"pergunta": "Quanto tempo leva para adequar minha operação?",
     "resposta": ["Depende do porte do negócio e de quanta documentação já existe. No diagnóstico a gente dá a faixa de prazo antes de qualquer proposta, para você já saber com o que está lidando."]},
    {"pergunta": "Vocês garantem aprovação na fiscalização?",
     "resposta": ["Não, e desconfie de quem garantir. O resultado de uma fiscalização depende do órgão, do fiscal e de como a sua operação está no dia.",
                  "O que a gente entrega é a documentação organizada, os procedimentos escritos e a equipe treinada para sustentar o padrão — que é o que está sob o seu controle."]},
    {"pergunta": "O trabalho é presencial ou a distância?",
     "resposta": ["O diagnóstico é presencial: não dá para avaliar uma cozinha por foto. A implantação e o treinamento também acontecem dentro da sua operação, porque é lá que o processo precisa funcionar."]},
    {"pergunta": "Quanto custa?",
     "resposta": ["Não trabalhamos com tabela de preço. O valor depende do porte da operação, de quanto já existe pronto e por quanto tempo você quer acompanhamento.",
                  "Por isso a proposta vem depois do diagnóstico: assim você recebe um número baseado no seu negócio, e não uma faixa genérica. Veja a lógica completa em <a href=\"/como-funciona/\">Como funciona</a>."]},
    {"pergunta": "O que eu preciso ter em mãos para começar?",
     "resposta": ["Para a conversa inicial, nada. Para o diagnóstico: a documentação que já existir, mesmo incompleta ou vencida, e acesso à operação funcionando. Não precisa organizar nada antes — a gente precisa ver como é."]},
]

ENTREGAVEIS = [
    "<b>Relatório de diagnóstico</b> <span>— o retrato da sua operação, com prioridade por item.</span>",
    "<b>Manual de Boas Práticas</b> <span>— escrito para a sua cozinha, não um modelo pronto.</span>",
    "<b>POPs da sua operação</b> <span>— o passo a passo escrito de cada tarefa crítica.</span>",
    "<b>Checklists de controle</b> <span>— prontos para imprimir e pendurar na parede.</span>",
    "<b>Fichas técnicas</b> <span>— custo, rendimento e modo de preparo por item.</span>",
    "<b>Material de treinamento</b> <span>— que fica com a equipe depois que a gente sai.</span>",
]

ARTIGOS = [
    {"categoria": "Segurança dos alimentos", "titulo": "ISO 22000: segurança dos alimentos com padrão internacional",
     "meta": "Leitura de 5 min", "figura": "imagem do artigo", "href": "/conteudos/"},
    {"categoria": "Eventos", "titulo": "Garanta a segurança do seu evento gastronômico",
     "meta": "Leitura de 4 min", "figura": "imagem do artigo", "href": "/conteudos/"},
    {"categoria": "Treinamento", "titulo": "Capacite sua equipe, surpreenda seus clientes",
     "meta": "Leitura de 4 min", "figura": "imagem do artigo", "href": "/conteudos/"},
]


def pagina():
    prazo = CONTATO.get("prazo_resposta")
    fine = CONTATO["horario"] + "."
    if prazo:
        fine = "Resposta {}. Sem compromisso.".format(prazo)

    return {
        "url": "/",
        "arquivo": "index.html",
        "title": "VeronaFood — Consultoria para negócios de alimentação",
        "description": ("Consultoria em segurança dos alimentos, custos, padronização e treinamento para "
                        "restaurantes, padarias, hotéis, cozinhas industriais, buffets, eventos e mercados."),
        "secoes": [
            {"tipo": "hero",
             "chapeu": "Consultoria para negócios de alimentação",
             "h1": "Sua operação de alimentos organizada do começo ao fim.",
             "apoio": ("Segurança dos alimentos, controle de custos, padronização de processos e treinamento "
                       "de equipe — com um plano feito para a realidade do seu negócio, não para o papel."),
             "fine": fine,
             "figura": "foto real de consultoria em cozinha"},

            {"tipo": "pills",
             "intro": "Trabalhamos com diferentes tipos de negócio de alimentação:",
             "itens": PILLS_SEGMENTOS,
             "link": ("Ver todos os segmentos", "/segmentos/")},

            {"tipo": "cards",
             "h2": "O que a gente resolve",
             "sub": "Cada frente funciona sozinha ou combinada. Na dúvida, o diagnóstico aponta por onde começar.",
             "grade": "grade--solucoes",
             "itens": CARDS_SOLUCOES,
             "destaque": {
                 "titulo": "Consultoria completa", "icone": "completa",
                 "href": "/solucoes/consultoria-completa/",
                 "texto": ("Quando o negócio precisa de tudo junto: diagnóstico, plano, implantação e "
                           "acompanhamento contínuo, no ritmo da sua operação."),
                 "link": "Ver o que inclui"}},

            {"tipo": "etapas",
             "h2": "Como o trabalho acontece",
             "sub": "Quatro etapas. Você sabe onde está em cada uma.",
             "itens": ETAPAS,
             "link": ("Ver o processo em detalhe", "/como-funciona/")},

            {"tipo": "beneficios",
             "h2": "O que muda na sua rotina",
             "itens": [
                 {"titulo": "Menos retrabalho", "icone": "processo",
                  "texto": "Procedimentos escritos acabam com o “cada um faz de um jeito”."},
                 {"titulo": "Equipe mais segura", "icone": "equipe",
                  "texto": "Gente treinada erra menos e pergunta menos."},
                 {"titulo": "Custo visível", "icone": "moeda",
                  "texto": "Ficha técnica mostra o que cada prato realmente custa."},
                 {"titulo": "Pronta para fiscalização", "icone": "escudo",
                  "texto": "Documentação organizada e rotina de controle em dia, a qualquer momento."},
             ],
             "nota": ("“Pronta para fiscalização” descreve o estado da sua documentação e da sua rotina. "
                      "O resultado de uma fiscalização depende do órgão e da operação no dia — "
                      "isso nenhuma consultoria controla.")},

            {"tipo": "pessoa", "chapeu": "Quem vai te atender"},

            {"tipo": "provas",
             "h2_entregaveis": "O que você recebe",
             "h2_depoimentos": "O que dizem os clientes",
             "sub": "Documento que você consegue abrir, entender e usar — em arquivo editável, para a sua equipe atualizar depois.",
             "entregaveis": ENTREGAVEIS},

            {"tipo": "folha"},

            {"tipo": "artigos",
             "h2": "Para ler antes de contratar qualquer consultoria",
             "sub": "Conteúdo prático sobre segurança, custos e gestão na operação de alimentos.",
             "itens": ARTIGOS,
             "link": ("Ver todos os conteúdos", "/conteudos/")},

            {"tipo": "faq", "h2": "Perguntas que a gente ouve sempre", "itens": FAQ_HOME},

            {"tipo": "cta_form",
             "h2": "Vamos começar pelo diagnóstico.",
             "texto": ("Conte em duas linhas como está sua operação hoje. A gente responde com o próximo passo "
                       "— sem compromisso e sem proposta genérica."),
             "sufixo": "-home"},
        ],
    }
