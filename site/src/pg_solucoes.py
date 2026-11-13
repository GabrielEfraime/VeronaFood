# -*- coding: utf-8 -*-
"""Hub de Soluções e as seis páginas de solução."""

from layout import SOLUCOES_NAV

TRILHA_BASE = [("Início", "/"), ("Soluções", "/solucoes/")]

# Enquanto a faixa de prazo real não estiver definida, o site não inventa número:
# diz com honestidade que o prazo sai no diagnóstico.
PRAZO_PADRAO = ("A faixa de prazo depende do porte da sua operação e de quanto já existe pronto. "
                "Dou esse número no diagnóstico, antes de qualquer proposta.")


def _pagina(slug, title, description, chapeu, h1, apoio, figura,
            sintomas, entregaveis, entregaveis_sub, etapas,
            precisamos, faq, nota_entregaveis=None, zap=None, btn=None,
            prazo=PRAZO_PADRAO, nao_precisamos=None):
    nome = chapeu.capitalize() if chapeu.isupper() else chapeu
    secoes = [
        {"tipo": "hero", "chapeu": chapeu, "h1": h1, "apoio": apoio,
         "figura": figura, "zap": zap, "btn": btn},
        {"tipo": "sintomas", "h2": "Isso provavelmente é para você se…", "itens": sintomas},
        {"tipo": "checklist", "h2": "O que você recebe", "sub": entregaveis_sub,
         "itens": entregaveis, "nota": nota_entregaveis},
        {"tipo": "etapas", "h2": "Como funciona", "itens": etapas, "fundo": " secao--claro"},
        {"tipo": "numerada", "h2": "Prazo e o que preciso de você",
         "sub": prazo,
         "itens": precisamos,
         "nota": nao_precisamos},
        {"tipo": "faq", "h2": "Perguntas frequentes", "itens": faq,
         "fundo": " secao--claro"},
        {"tipo": "cta_form",
         "h2": "Comece pelo diagnóstico.",
         "texto": ("Uma visita, um relatório por escrito e um plano com prioridade. "
                   "A partir daí você decide o que fazer e em que ritmo."),
         "sufixo": "-" + slug,
         "zap": zap},
    ]
    return {
        "url": "/solucoes/{}/".format(slug),
        "title": title,
        "description": description,
        "trilha": TRILHA_BASE + [(nome, None)],
        "secoes": secoes,
    }


# =========================================================================
def hub():
    situacoes = [
        {"titulo": "Vou abrir meu negócio",
         "texto": "Melhor momento para acertar o processo: fluxo de cozinha, documentação e equipe treinada antes de a porta abrir.",
         "href": "/solucoes/consultoria-completa/", "icone": "completa", "link": "Ver consultoria completa"},
        {"titulo": "Recebi uma notificação da vigilância",
         "texto": "Eu olho o que foi apontado, organiza a documentação e põe a rotina de controle para rodar.",
         "href": "/solucoes/seguranca-dos-alimentos/", "icone": "escudo", "link": "Ver segurança dos alimentos"},
        {"titulo": "Quero organizar custo e padrão",
         "texto": "Ficha técnica, porcionamento e procedimentos escritos: o prato sai igual e você sabe quanto ele custa.",
         "href": "/solucoes/custos-e-ficha-tecnica/", "icone": "custos", "link": "Ver custos e ficha técnica"},
    ]
    cards = [
        {"titulo": t, "texto": d, "href": h,
         "icone": {"Segurança dos alimentos": "seguranca", "Rotulagem": "rotulo",
                   "Custos e ficha técnica": "custos", "Treinamento de equipe": "treino",
                   "Padronização de processos": "processo"}.get(t, "completa"),
         "meio": t in ("Treinamento de equipe", "Padronização de processos")}
        for t, h, d in SOLUCOES_NAV if t != "Consultoria completa"
    ]
    return {
        "url": "/solucoes/",
        "title": "Soluções em consultoria de alimentos, VeronaFood",
        "description": ("Segurança dos alimentos, rotulagem, ficha técnica e custos, treinamento de equipe e "
                        "padronização de processos. Veja o que a Verona Food faz na prática."),
        "trilha": [("Início", "/"), ("Soluções", None)],
        "secoes": [
            {"tipo": "hero_simples", "chapeu": "Soluções", "h1": "O que eu resolvo",
             "apoio": ("Cinco frentes de trabalho que funcionam sozinhas ou combinadas, e uma consultoria "
                       "completa para quem precisa de tudo junto. Se você não sabe por onde começar, "
                       "o diagnóstico resolve isso em uma visita.")},
            {"tipo": "cards", "h2": "Em qual dessas situações você está?",
             "sub": "O nome do serviço importa menos que o problema que você tem agora.",
             "itens": situacoes, "fundo": " secao--claro"},
            {"tipo": "cards", "h2": "As frentes de trabalho", "grade": "grade--solucoes",
             "itens": cards,
             "destaque": {"titulo": "Consultoria completa", "icone": "completa",
                          "href": "/solucoes/consultoria-completa/",
                          "texto": ("Diagnóstico, plano, implantação e acompanhamento contínuo, "
                                    "no ritmo que a sua operação aguenta."),
                          "link": "Ver o que inclui"}},
            {"tipo": "cta",
             "h2": "Não sabe qual você precisa?",
             "texto": ("Normalmente não é uma frente só. Eu começo pelo diagnóstico, vê sua operação de "
                       "perto e aponta o que é urgente, o que é importante e o que pode esperar. "
                       "Você decide o que fazer com isso.")},
        ],
    }


# =========================================================================
def seguranca():
    return _pagina(
        slug="seguranca-dos-alimentos",
        title="Consultoria em segurança dos alimentos, VeronaFood",
        description=("Manual de boas práticas, POPs, checklists e adequação sanitária aplicados à rotina "
                     "da sua cozinha. Agende um diagnóstico."),
        chapeu="Segurança dos alimentos",
        h1="Sua cozinha em ordem, no papel e na prática.",
        apoio=("Manual de boas práticas, procedimentos escritos, checklists de controle e adequação sanitária. "
               "Feitos a partir da sua operação real, não de um modelo pronto que ninguém consegue seguir."),
        figura="foto de conferência de câmara fria",
        zap="Olá! Vim pela página de segurança dos alimentos e queria entender melhor.",
        sintomas=[
            "Você tem manual e POPs guardados numa pasta, mas ninguém da equipe usa no dia a dia.",
            "Recebeu uma notificação da vigilância e não sabe por onde começar a responder.",
            "Vai abrir ou reformar e quer acertar o fluxo e a documentação antes de a operação começar.",
            "Sua equipe muda bastante e, a cada troca, o padrão de higiene e controle se perde.",
            "Você faz o controle “de cabeça”, sabe o que precisa ser feito, mas não tem registro de nada.",
            "Um cliente corporativo, um aplicativo ou uma rede pediu documentação que você não tem.",
        ],
        entregaveis_sub=("Documento que você consegue abrir, entender e usar. Tudo em arquivo editável, "
                         "para a sua equipe atualizar depois que eu sair."),
        entregaveis=[
            "<b>Diagnóstico sanitário da operação</b> <span>,  relatório com o que está em ordem, o que precisa de ajuste e a ordem de prioridade.</span>",
            "<b>Manual de Boas Práticas</b> <span>,  escrito para a sua operação: seus equipamentos, seu fluxo, seus produtos.</span>",
            "<b>POPs</b> <span>,  Procedimentos Operacionais Padronizados: o passo a passo escrito de cada tarefa crítica.</span>",
            "<b>Checklists de controle</b> <span>,  recebimento, temperatura, higienização e conferência diária, prontos para imprimir.</span>",
            "<b>Planilhas de registro</b> <span>,  onde a equipe anota o que mediu, com instrução de preenchimento.</span>",
            "<b>Plano de adequação</b> <span>,  o que precisa mudar na estrutura ou no processo, por prioridade.</span>",
            "<b>Treinamento de implantação</b> <span>,  a equipe aprende a usar o que foi escrito, no próprio ambiente de trabalho.</span>",
        ],
        etapas=[
            {"titulo": "Visita de diagnóstico",
             "texto": "Vou até a sua operação em horário de funcionamento, é assim que dá para ver a rotina de verdade. Olho estrutura, fluxo, armazenamento, higienização, documentação e como a equipe trabalha."},
            {"titulo": "Relatório e plano",
             "texto": "Você recebe o diagnóstico por escrito, com o que é urgente, o que é importante e o que pode esperar. Junto vai o plano de adequação, com prazo e responsável por item."},
            {"titulo": "Elaboração dos documentos",
             "texto": "Escrevo manual, POPs, checklists e planilhas a partir do que vi. Você revisa, pede ajuste, eu fecho."},
            {"titulo": "Implantação e treinamento",
             "texto": "Levo os documentos para dentro da operação: treinamento da equipe, checklists afixados e a rotina de registro começando a rodar."},
        ],
        precisamos=[
            {"titulo": "A documentação que já existir",
             "texto": "Mesmo incompleta ou vencida: manual antigo, POPs, laudos, contratos de controle de pragas e de limpeza de caixa d’água. Alvará e licença sanitária, se já houver."},
            {"titulo": "Acesso à operação funcionando",
             "texto": "Cozinha e áreas de armazenamento em horário de produção. Operação parada não mostra onde o processo falha."},
            {"titulo": "Uma pessoa de referência da sua equipe",
             "texto": "Alguém que acompanhe o diagnóstico e a implantação. Sem alguém de dentro, o processo não para em pé."},
        ],
        nao_precisamos=("<b>O que você não precisa fazer:</b> organizar nada antes. Eu vejo a operação "
                        "como ela está, é esse o ponto."),
        faq=[
            {"pergunta": "Vocês garantem que eu passo na fiscalização?",
             "resposta": ["Não, e desconfie de quem garantir. O resultado de uma fiscalização depende do órgão, do fiscal e de como a sua operação está no dia.",
                          "O que eu entrego é a documentação organizada, os procedimentos escritos e a equipe treinada para sustentar o padrão, que é o que está sob o seu controle."]},
            {"pergunta": "Já tenho um manual. Serve?",
             "resposta": ["Serve como ponto de partida. No diagnóstico eu confiro se ele descreve a sua operação de hoje e se está atualizado.",
                          "Muitas vezes o problema não é o manual: é que ele foi escrito para outra cozinha."]},
            {"pergunta": "Minha cozinha é pequena. Dá para adequar?",
             "resposta": ["Dá. Cozinha pequena não impede adequação, ela muda a solução. O que não cabe em espaço se resolve em fluxo, horário e ordem das tarefas."]},
            {"pergunta": "Vocês atrapalham o serviço durante a visita?",
             "resposta": ["A visita de diagnóstico é em horário de operação porque é a única forma de ver a rotina real, mas eu observo, não interfere. Treinamento e implantação ficam fora do pico."]},
        ],
    )


# =========================================================================
def rotulagem():
    p = _pagina(
        slug="rotulagem",
        title="Rotulagem de alimentos e tabela nutricional, VeronaFood",
        description=("Rótulo e tabela nutricional para produtos de fabricação própria. Para padarias, "
                     "confeitarias, mercados e pequenos fabricantes."),
        chapeu="Rotulagem",
        h1="Seu produto está pronto. O rótulo também precisa estar.",
        apoio=("Tabela nutricional, lista de ingredientes, declaração de alergênicos e as informações "
               "obrigatórias do produto que você embala. Calculado a partir da sua receita real, "
               "não de um produto parecido."),
        figura="foto de produto embalado com rótulo",
        btn="Pedir orçamento de rotulagem",
        zap="Olá! Vim pela página de rotulagem e queria um orçamento.",
        sintomas=[
            "Você produz e embala alimento para vender, na sua loja, em feira, em marketplace ou para outro estabelecimento.",
            "Um cliente, um mercado ou um aplicativo pediu o rótulo do seu produto e você não tem.",
            "Tem rótulo, mas ele foi feito há anos e você não sabe se ainda está certo.",
            "Copiou o rótulo de um produto parecido e desconfia que isso não basta.",
            "Vai lançar um produto novo e quer resolver o rótulo antes de imprimir embalagem.",
            "Trabalha com castanhas, leite, ovo, trigo ou derivados e precisa declarar isso corretamente.",
        ],
        entregaveis_sub=("Tudo calculado a partir da sua receita, com a memória de cálculo junto, para você "
                         "entender de onde veio cada número e conseguir atualizar quando mudar o ingrediente."),
        entregaveis=[
            "<b>Tabela nutricional do seu produto</b> <span>,  calculada a partir da receita, do rendimento e da porção que você vende.</span>",
            "<b>Lista de ingredientes</b> <span>,  em ordem e na forma correta de declaração.</span>",
            "<b>Declaração de alergênicos</b> <span>,  o que precisa ser declarado e como, considerando o que acontece na sua produção.</span>",
            "<b>Conferência das demais informações obrigatórias</b> <span>,  o que se aplica ao seu produto e ao seu canal de venda.</span>",
            "<b>Memória de cálculo</b> <span>,  a planilha com a conta por trás da tabela, para você atualizar quando a receita mudar.</span>",
            "<b>Orientação para a próxima vez</b> <span>,  como proceder com os próximos produtos da sua linha.</span>",
        ],
        etapas=[
            {"titulo": "Você manda a receita",
             "texto": "Ingredientes, quantidades, rendimento e a porção que você vende. Se não tiver isso escrito com precisão, eu levanto junto, e esse levantamento já costuma mostrar coisa útil sobre o seu produto."},
            {"titulo": "Confiro a produção",
             "texto": "Como o produto é feito e com o que ele divide bancada e equipamento. É isso que define a declaração de alergênicos."},
            {"titulo": "Calculo",
             "texto": "Tabela nutricional a partir da receita real, lista de ingredientes na forma correta e declaração de alergênicos."},
            {"titulo": "Você recebe e revisa",
             "texto": "Entrego o conteúdo do rótulo e a memória de cálculo. Você confere, pergunta o que não entendeu, eu ajusto antes de a embalagem ir para a gráfica."},
        ],
        prazo=("Rotulagem é o serviço em que o prazo mais pesa, porque quem procura normalmente tem embalagem "
               "para imprimir. Eu fecho prazo por produto logo na primeira conversa."),
        precisamos=[
            {"titulo": "A receita completa",
             "texto": "Todos os ingredientes com quantidade exata, inclusive sal, açúcar, gordura e aditivos. Mais o rendimento e a porção em que o produto é vendido."},
            {"titulo": "A marca dos ingredientes que você compra",
             "texto": "Se possível, a embalagem ou a ficha do fornecedor: essa informação entra no cálculo."},
            {"titulo": "Como e onde o produto é feito",
             "texto": "Principalmente o que divide bancada e equipamento com ele, e onde o produto é vendido, loja própria, outro estabelecimento, feira ou marketplace."},
        ],
        nao_precisamos=("<b>O que atrasa o trabalho:</b> receita “a olho”. Se a sua está na cabeça do "
                        "confeiteiro, o primeiro passo é pesá-la, e aí vale conversar sobre "
                        "<a href=\"/solucoes/custos-e-ficha-tecnica/\">ficha técnica</a>, que resolve as duas coisas de uma vez."),
        faq=[
            {"pergunta": "Posso usar o rótulo de um produto parecido?",
             "resposta": ["Não. A tabela nutricional sai da sua receita, do seu rendimento e da sua porção.",
                          "Dois bolos de cenoura com a mesma aparência podem ter valores bem diferentes, e a declaração de alergênicos depende da sua produção, não da do outro fabricante."]},
            {"pergunta": "Mudei um ingrediente. Preciso refazer tudo?",
             "resposta": ["Não necessariamente, é para isso que a memória de cálculo vai junto. Mudança pequena você atualiza sozinha na planilha.",
                          "Mudança que altere a composição principal ou a declaração de alergênicos, melhor conferir."]},
            {"pergunta": "Meu cliente é um mercado e ele exigiu documentação. É só o rótulo?",
             "resposta": ["Rótulo costuma ser parte do que é pedido, mas não o todo: normalmente vem junto uma exigência de documentação da sua produção.",
                          "Vale olhar o que foi pedido inteiro antes de resolver só o rótulo. Isso eu vejo na conversa."]},
            {"pergunta": "Por que vocês não publicam aqui a lista do que o rótulo precisa ter?",
             "resposta": ["Porque as regras de rotulagem mudam, têm prazos de transição e não são iguais para todo produto, depende do que você fabrica, do tamanho da produção e de onde você vende.",
                          "Uma lista desatualizada na internet não é informação: é armadilha. Você monta o rótulo por ela, imprime a embalagem e descobre depois. Prefiro olhar o seu produto com a regra que vale hoje para ele."]},
        ],
    )
    # esta página tem CTA próprio: quem procura rotulagem tem demanda fechada
    p["secoes"][-1]["h2"] = "Me mande sua receita e eu te digo o que falta."
    p["secoes"][-1]["texto"] = ("Orçamento por produto, prazo fechado e a memória de cálculo junto, "
                                "para você conseguir atualizar sozinha depois.")
    return p


# =========================================================================
def custos():
    return _pagina(
        slug="custos-e-ficha-tecnica",
        title="Ficha técnica e controle de custos, VeronaFood",
        description=("Saiba quanto cada prato realmente custa. Fichas técnicas, controle de porcionamento "
                     "e de perdas para negócios de alimentação."),
        chapeu="Custos e ficha técnica",
        h1="Você sabe quanto cada prato deixa?",
        apoio=("Ficha técnica item por item, custo real da receita, porcionamento padronizado e controle de "
               "perdas. É o trabalho que mostra onde o dinheiro está indo embora sem ninguém perceber."),
        figura="foto de pesagem de ingredientes na cozinha",
        zap="Olá! Vim pela página de custos e ficha técnica e queria entender melhor.",
        sintomas=[
            "O preço do cardápio foi montado “olhando o concorrente” e nunca foi recalculado.",
            "O mesmo prato sai de tamanhos diferentes dependendo de quem está na praça.",
            "O faturamento é bom, mas a sobra no fim do mês não bate com isso.",
            "Você não sabe quais itens do cardápio dão lucro e quais estão só ocupando espaço.",
            "A cada aumento de fornecedor, você reajusta no escuro ou absorve o prejuízo.",
            "Há desperdício visível, sobra de porção, produto vencendo, aparas que ninguém aproveita.",
        ],
        entregaveis_sub=("Planilhas que a sua equipe consegue manter depois. Se a ficha técnica só funcionar "
                         "comigo por perto, ela não serve."),
        entregaveis=[
            "<b>Ficha técnica por item</b> <span>,  ingredientes, quantidade bruta, fator de correção, rendimento, modo de preparo e foto do prato montado.</span>",
            "<b>Custo real por porção</b> <span>,  já com perda de limpeza e de cocção consideradas.</span>",
            "<b>Análise do cardápio</b> <span>,  quais itens dão margem, quais vendem muito e dão pouco, quais não dão nenhum dos dois.</span>",
            "<b>Padrão de porcionamento</b> <span>,  medida, utensílio e montagem definidos, para o prato sair igual.</span>",
            "<b>Mapa de perdas</b> <span>,  onde o produto se perde: recebimento, armazenamento, pré-preparo, produção ou devolução.</span>",
            "<b>Planilha de acompanhamento</b> <span>,  modelo editável para atualizar o custo quando o fornecedor mudar de preço.</span>",
            "<b>Treinamento da equipe de cozinha</b> <span>,  como usar a ficha técnica no dia a dia, sem travar a operação.</span>",
        ],
        etapas=[
            {"titulo": "Levantamento",
             "texto": "Pego o cardápio, as notas de compra recentes e acompanho a produção. É aqui que aparecem as diferenças entre a receita do papel e a que sai da praça."},
            {"titulo": "Pesagem e teste de rendimento",
             "texto": "Peso ingredientes na entrada e no fim do preparo para descobrir o fator de correção real da sua operação, não o de tabela. É isso que faz a ficha técnica ser verdadeira."},
            {"titulo": "Montagem das fichas",
             "texto": "Cada item vira uma ficha com custo, rendimento e modo de preparo. Você revisa, ajusta o que não representa a sua cozinha, eu fecho."},
            {"titulo": "Análise e implantação",
             "texto": "Com os custos na mão, olho o cardápio inteiro e aponto o que reajustar, reformular ou tirar. Depois: ficha na praça, porcionamento combinado com o time e planilha nas mãos de quem vai mantê-la."},
        ],
        precisamos=[
            {"titulo": "Cardápio e preços praticados",
             "texto": "O cardápio atual com os preços de venda que você cobra hoje."},
            {"titulo": "Notas fiscais ou relatório de compras",
             "texto": "O histórico recente de compras, para o custo partir do que você realmente paga."},
            {"titulo": "Acesso à cozinha durante a produção",
             "texto": "Para acompanhar e pesar. Também é bom ter alguém da cozinha disponível para acompanhar a pesagem."},
        ],
        nao_precisamos=("<b>O que você não precisa ter:</b> ficha técnica de nada. Se já tiver, melhor, "
                        "eu confiro e atualiza em vez de refazer."),
        faq=[
            {"pergunta": "Isso serve para cardápio que muda toda semana?",
             "resposta": ["Serve, e é aí que faz mais diferença. Eu monto ficha dos itens fixos e das bases, e deixa um modelo para você calcular o prato novo sozinho em poucos minutos."]},
            {"pergunta": "Vocês definem o preço de venda dos meus pratos?",
             "resposta": ["Eu entrego o custo real e a análise de margem. O preço final é decisão sua, porque depende do seu público, da sua região e do seu posicionamento, e isso você conhece melhor que ninguém."]},
            {"pergunta": "Minha equipe não vai seguir a ficha técnica.",
             "resposta": ["Vai seguir se a ficha for feita com ela e não contra ela. Por isso a pesagem é acompanhada e o padrão de porcionamento é combinado na praça, não imposto de cima."]},
            {"pergunta": "Isso tem a ver com segurança dos alimentos?",
             "resposta": ["Tem mais do que parece: ficha técnica define temperatura, tempo e modo de preparo, que são os mesmos pontos que o controle sanitário acompanha. Quando as duas frentes são feitas juntas, uma reforça a outra."]},
        ],
    )


# =========================================================================
def treinamentos():
    return _pagina(
        slug="treinamentos",
        title="Treinamento de equipe em manipulação de alimentos, VeronaFood",
        description=("Capacitação por função, com linguagem de cozinha e material que fica com o seu time. "
                     "Presencial, na sua operação."),
        chapeu="Treinamento de equipe",
        h1="Treinamento que a equipe entende e aplica no dia seguinte.",
        apoio=("Capacitação por função, com linguagem de cozinha, exemplo da sua própria operação e material "
               "que fica com o time. Presencial, no seu ambiente de trabalho."),
        figura="foto de treinamento de equipe na cozinha",
        zap="Olá! Vim pela página de treinamentos e queria entender melhor.",
        sintomas=[
            "Sua equipe muda com frequência e cada pessoa nova aprende “olhando o colega”.",
            "Você já explicou a mesma coisa várias vezes e ela continua saindo errada.",
            "Contratou gente sem experiência em cozinha e precisa colocar todo mundo no mesmo nível.",
            "Já fez treinamento antes, mas era genérico demais e ninguém aplicou.",
            "Precisa comprovar capacitação da equipe para um cliente, uma rede ou uma auditoria.",
            "Vai abrir e quer a equipe pronta antes do primeiro dia.",
        ],
        entregaveis_sub=("Treinamento feito a partir do que vi na sua cozinha. "
                         "Exemplo real vale mais que slide bonito."),
        entregaveis=[
            "<b>Programa por função</b> <span>,  cozinha, salão, recebimento, estoque e liderança não precisam do mesmo conteúdo.</span>",
            "<b>Encontro presencial na sua operação</b> <span>,  no horário que menos atrapalha, com turmas por turno quando necessário.</span>",
            "<b>Material de apoio</b> <span>,  resumo ilustrado para a equipe levar e cartazes dos pontos críticos para afixar na cozinha.</span>",
            "<b>Lista de presença e registro</b> <span>,  documento do que foi dado, para quem e quando.</span>",
            "<b>Avaliação prática</b> <span>,  eu verifico na bancada se o que foi ensinado está sendo feito, não só se foi entendido.</span>",
            "<b>Relatório para a gestão</b> <span>,  o que a equipe domina, onde ainda há lacuna e o que reforçar.</span>",
        ],
        etapas=[
            {"titulo": "Entender a operação",
             "texto": "Antes de montar qualquer conteúdo, eu observo a rotina e conversa com a equipe. Treinamento genérico é o que faz as pessoas acharem que treinamento não serve."},
            {"titulo": "Montar o programa",
             "texto": "Defino quais grupos, quais temas e em que horário, normalmente fora do pico, para não parar a operação."},
            {"titulo": "Dar o treinamento",
             "texto": "Presencial, com exemplo da própria cozinha, demonstração prática e espaço para a equipe perguntar. Linguagem direta, sem termo que ninguém usa no dia a dia."},
            {"titulo": "Verificar e reforçar",
             "texto": "Alguns dias depois, volto à bancada para ver o que pegou e o que não pegou. O que não pegou vira reforço, e você recebe o registro do que foi dado."},
        ],
        precisamos=[
            {"titulo": "Lista da equipe por função e por turno",
             "texto": "Para montar as turmas certas. Treinar só o turno da manhã é o erro mais comum, e é a noite que costuma operar com menos supervisão."},
            {"titulo": "Um espaço e uma escala combinada",
             "texto": "Não precisa ser sala: cozinha fora do pico funciona. O importante é a escala combinada com antecedência, para a equipe participar sem correria."},
            {"titulo": "A liderança presente",
             "texto": "Quando a chefia não participa, a equipe entende que não é prioridade, e aí o treinamento não pega."},
        ],
        faq=[
            {"pergunta": "Preciso parar a operação?",
             "resposta": ["Não. Eu combino horário fora do pico ou faz turmas por turno, para a operação seguir rodando."]},
            {"pergunta": "Minha equipe tem gente que lê pouco. Funciona?",
             "resposta": ["Funciona, é por isso que o material é ilustrado, a demonstração é prática e os cartazes ficam na parede. O treinamento é falado e feito, não lido."]},
            {"pergunta": "Já fiz treinamento e não adiantou.",
             "resposta": ["Quase sempre pelo mesmo motivo: o conteúdo era genérico e não falava da cozinha daquela equipe.",
                          "Aqui o treinamento é montado depois de observar a sua operação, com exemplo que a equipe reconhece, e tem uma verificação prática depois."]},
        ],
    )


# =========================================================================
def padronizacao():
    return _pagina(
        slug="padronizacao-de-processos",
        title="Padronização de processos e POPs, VeronaFood",
        description="Procedimentos escritos, checklists e rotinas que mantêm o padrão mesmo com troca de equipe.",
        chapeu="Padronização de processos",
        h1="O padrão não pode depender de quem está na escala.",
        apoio=("Procedimentos escritos, checklists de rotina e divisão clara de responsabilidade. Para o seu "
               "negócio funcionar igual na segunda-feira e no sábado à noite, com você presente ou não."),
        figura="foto de checklist afixado na cozinha",
        zap="Olá! Vim pela página de padronização de processos e queria entender melhor.",
        sintomas=[
            "A operação só roda bem quando você está lá.",
            "Cada pessoa da equipe faz a mesma tarefa de um jeito diferente.",
            "A qualidade cai no fim de semana, no turno da noite ou quando alguém falta.",
            "Você tem mais de uma unidade e elas não se parecem.",
            "Está preparando alguém para assumir a gestão e precisa que o conhecimento saia da sua cabeça.",
            "Perde tempo demais apagando incêndio de coisa que já aconteceu antes.",
        ],
        entregaveis_sub=("Procedimento curto, escrito em linguagem de cozinha e pendurado onde a tarefa "
                         "acontece. Manual de 80 páginas na gaveta não muda nada."),
        entregaveis=[
            "<b>Mapeamento da rotina</b> <span>,  como a operação funciona hoje, do recebimento ao fechamento, por turno e por função.</span>",
            "<b>Procedimentos escritos</b> <span>,  o passo a passo de cada tarefa crítica, em uma página, com foto quando ajuda.</span>",
            "<b>Checklists de abertura, troca de turno e fechamento</b> <span>,  o que conferir, quem confere e onde registra.</span>",
            "<b>Matriz de responsabilidade</b> <span>,  quem faz, quem confere e quem decide. Acaba com o “achei que era você”.</span>",
            "<b>Fluxo de cozinha revisado</b> <span>,  ordem das etapas e circulação de pessoas e produtos, para reduzir cruzamento e retrabalho.</span>",
            "<b>Rotina de conferência da liderança</b> <span>,  o que o gestor olha por dia, por semana e por mês, em uma página.</span>",
            "<b>Treinamento de implantação</b> <span>,  a equipe aprende a rotina nova no próprio posto de trabalho.</span>",
        ],
        etapas=[
            {"titulo": "Observar a rotina",
             "texto": "Acompanho a operação em horário real, em mais de um turno quando for o caso. Escrever procedimento sem ver a cozinha funcionando é o erro mais comum nesse trabalho."},
            {"titulo": "Mapear e apontar",
             "texto": "Desenho o fluxo como ele é hoje e marco onde há retrabalho, gargalo, risco de contaminação cruzada e tarefa sem dono."},
            {"titulo": "Escrever os procedimentos",
             "texto": "Cada tarefa crítica vira um procedimento de uma página. Escritos com quem executa, revisados por quem lidera."},
            {"titulo": "Implantar e ajustar",
             "texto": "Checklists afixados, rotina combinada com cada turno, liderança treinada para conferir. Depois eu volto: procedimento que não cabe na rotina eu reescrevo, a rotina é que manda."},
        ],
        precisamos=[
            {"titulo": "Acesso à operação em funcionamento",
             "texto": "Em mais de um turno, se houver. O turno que você menos vê costuma ser o que mais precisa."},
            {"titulo": "Escala e divisão de funções atual",
             "texto": "Mesmo que seja informal e esteja só na sua cabeça."},
            {"titulo": "A liderança envolvida do começo ao fim",
             "texto": "Padronização sem gestão por perto não se sustenta depois que eu saio."},
        ],
        faq=[
            {"pergunta": "Isso é a mesma coisa que o manual de boas práticas?",
             "resposta": ["Tem sobreposição, mas não é igual. O manual trata da segurança do alimento e atende à exigência sanitária.",
                          "A padronização olha a operação inteira, produção, atendimento, estoque, troca de turno, inclusive o que não é sanitário. Quando as duas são feitas juntas, não há documento duplicado."]},
            {"pergunta": "Minha equipe vai achar que é burocracia.",
             "resposta": ["Vai, se o procedimento for longo e escrito longe da cozinha. Por isso eu escrevo com quem executa, em uma página, e tira tudo que não muda nada na prática."]},
            {"pergunta": "Tenho duas unidades. Dá para padronizar as duas?",
             "resposta": ["Dá, e normalmente é onde o ganho é maior. O procedimento é um só; o que muda por unidade é anexo, não documento novo."]},
            {"pergunta": "E quando a operação mudar?",
             "resposta": ["Os arquivos ficam com você em formato editável, com instrução de como atualizar."]},
        ],
    )


# =========================================================================
def completa():
    return _pagina(
        slug="consultoria-completa",
        title="Consultoria completa para operação de alimentos, VeronaFood",
        description="Diagnóstico, plano de ação, implantação e acompanhamento contínuo para o seu negócio de alimentação.",
        chapeu="Consultoria completa",
        h1="Quando o negócio precisa de tudo junto.",
        apoio=("Segurança dos alimentos, custos, padronização e treinamento numa frente só, com diagnóstico, "
               "plano, implantação e acompanhamento contínuo. No ritmo que a sua operação aguenta."),
        figura="foto de consultoria em reunião com a equipe",
        zap="Olá! Vim pela página de consultoria completa e queria conversar.",
        sintomas=[
            "Vai abrir e quer acertar fluxo, documentação, custo e equipe antes de a porta abrir.",
            "Já tentou resolver por partes e cada frente desandou enquanto você cuidava da outra.",
            "Cresceu rápido e a estrutura de processo não acompanhou.",
            "Vai abrir a segunda unidade e precisa que ela funcione como a primeira.",
            "Está assumindo um negócio que já existe e quer entender o que herdou.",
            "Prefere ter alguém de fora acompanhando de perto, em vez de um projeto que entrega e some.",
        ],
        entregaveis_sub=("Tudo das frentes de trabalho, montado numa ordem que respeita a sua operação, "
                         "e alguém acompanhando enquanto a mudança pega."),
        entregaveis=[
            "<b>Diagnóstico completo</b> <span>,  sanitário, de processo, de custo e de equipe, numa visita só e num relatório só.</span>",
            "<b>Plano de ação priorizado</b> <span>,  o que é urgente, o que é importante e o que pode esperar, com prazo e responsável.</span>",
            "<b>Toda a documentação</b> <span>,  manual, POPs, checklists, planilhas de registro e fichas técnicas.</span>",
            "<b>Padronização da operação</b> <span>,  fluxo revisado, matriz de responsabilidade e rotina de conferência da liderança.</span>",
            "<b>Treinamento da equipe</b> <span>,  por função, presencial, com material e registro.</span>",
            "<b>Acompanhamento periódico</b> <span>,  visitas para conferir, ajustar e destravar o que empacar.</span>",
            "<b>Relatório de evolução</b> <span>,  o que avançou desde o diagnóstico, por escrito.</span>",
        ],
        etapas=[
            {"titulo": "Diagnóstico",
             "texto": "Uma ou mais visitas em horário de operação, olhando tudo: estrutura, fluxo, documentação, custo, equipe e gestão. Você recebe o retrato do negócio por escrito."},
            {"titulo": "Plano de ação",
             "texto": "Monto o plano com você, não para você. Prazo realista, responsável por item e custo de cada frente. Você aprova o que faz sentido agora."},
            {"titulo": "Implantação",
             "texto": "Executo junto com o seu time: documentos escritos, procedimentos combinados, fichas montadas, equipe treinada. Na ordem que menos atrapalha a operação."},
            {"titulo": "Acompanhamento",
             "texto": "Volto periodicamente para conferir o que se manteve, ajustar o que não funcionou e preparar a equipe para seguir sozinha. É a etapa que diferencia a consultoria completa de um projeto avulso."},
        ],
        precisamos=[
            {"titulo": "Acesso à operação funcionando",
             "texto": "E a documentação que já existir, mesmo incompleta."},
            {"titulo": "Cardápio, preços e compras recentes",
             "texto": "Mais a escala e a divisão de funções atual."},
            {"titulo": "A sua participação, ou de quem decide",
             "texto": "Consultoria completa mexe em processo, custo e equipe. Precisa de alguém com poder de decidir acompanhando."},
        ],
        faq=[
            {"pergunta": "Qual a diferença para contratar os serviços separados?",
             "resposta": ["Ordem e continuidade. Separado, cada frente anda sozinha e você faz a costura.",
                          "Completo, eu defino a sequência, reaproveita o que uma frente produz na outra, a ficha técnica já define temperatura e tempo que o controle sanitário usa, e acompanha enquanto a mudança pega."]},
            {"pergunta": "Preciso fazer tudo de uma vez?",
             "resposta": ["Não. O plano de ação é priorizado justamente para você escolher o ritmo. Tem cliente que faz tudo em poucos meses e tem cliente que faz por etapas ao longo do ano."]},
            {"pergunta": "Estou abrindo agora. Quando devo chamar?",
             "resposta": ["Quanto antes melhor, de preferência ainda no projeto da cozinha. Corrigir fluxo e estrutura no papel custa muito menos que corrigir depois de a obra pronta."]},
            {"pergunta": "Como funciona o investimento?",
             "resposta": ["Não trabalho com tabela de preço: duas cozinhas do mesmo tamanho podem precisar de trabalhos completamente diferentes.",
                          "O valor depende do porte da operação, de quanto já existe pronto e por quanto tempo você quer acompanhamento. Por isso a proposta vem depois do diagnóstico."]},
        ],
    )


def paginas():
    return [hub(), seguranca(), rotulagem(), custos(), treinamentos(), padronizacao(), completa()]
