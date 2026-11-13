# -*- coding: utf-8 -*-
"""Hub de Segmentos e as seis páginas por tipo de operação."""

TRILHA_BASE = [("Início", "/"), ("Segmentos", "/segmentos/")]

SOL = {
    "seguranca": ("Segurança dos alimentos", "/solucoes/seguranca-dos-alimentos/", "seguranca"),
    "rotulagem": ("Rotulagem", "/solucoes/rotulagem/", "rotulo"),
    "custos": ("Custos e ficha técnica", "/solucoes/custos-e-ficha-tecnica/", "custos"),
    "treino": ("Treinamento de equipe", "/solucoes/treinamentos/", "treino"),
    "padrao": ("Padronização de processos", "/solucoes/padronizacao-de-processos/", "processo"),
}


def _por_onde(itens):
    """itens: lista de (chave_da_solucao, texto)"""
    cards = []
    for chave, texto in itens:
        titulo, href, ic = SOL[chave]
        cards.append({"titulo": titulo, "texto": texto, "href": href, "icone": ic,
                      "link": "Ver detalhes"})
    return {"tipo": "cards", "h2": "Por onde o trabalho costuma começar",
            "sub": "Depende do diagnóstico, mas neste segmento a ordem mais comum é esta.",
            "grade": "grade--2", "itens": cards, "fundo": " secao--claro"}


def _pagina(slug, title, description, chapeu, h1, apoio, figura, nome_trilha,
            encontramos, por_onde, atencao, faq, zap):
    return {
        "url": "/segmentos/{}/".format(slug),
        "title": title,
        "description": description,
        "trilha": TRILHA_BASE + [(nome_trilha, None)],
        "secoes": [
            {"tipo": "hero", "chapeu": chapeu, "h1": h1, "apoio": apoio, "figura": figura, "zap": zap},
            {"tipo": "sintomas", "h2": "O que costumo encontrar", "itens": encontramos,
             "fundo": ""},
            _por_onde(por_onde),
            {"tipo": "checklist", "h2": "O que pede atenção específica aqui",
             "sub": ("Os pontos de controle deste segmento. Os parâmetros de cada um, tempo, temperatura, "
                     "validade, são definidos no trabalho técnico, porque variam por produto e por processo."),
             "itens": atencao},
            {"tipo": "faq", "h2": "Perguntas de quem atende neste segmento", "itens": faq,
             "fundo": " secao--claro"},
            {"tipo": "cta_form",
             "h2": "Agende a visita à sua operação.",
             "texto": ("A visita de diagnóstico acontece em horário de funcionamento, porque é assim que dá "
                       "para ver onde o padrão se perde."),
             "sufixo": "-" + slug, "zap": zap},
        ],
    }


# =========================================================================
def hub():
    cards = [
        {"titulo": "Restaurantes e bares", "icone": "restaurante", "href": "/segmentos/restaurantes-e-bares/",
         "texto": "Pico de movimento, equipe que muda e cardápio que varia. O padrão tem que aguentar o sábado à noite."},
        {"titulo": "Padarias e confeitarias", "icone": "pao", "href": "/segmentos/padarias-e-confeitarias/",
         "texto": "Produção de madrugada, validade curta e produto embalado na loja. Aqui rotulagem e validade são o centro de tudo."},
        {"titulo": "Hotéis e buffets", "icone": "hotel", "href": "/segmentos/hoteis-e-buffets/",
         "texto": "Comida exposta por horas e volume que muda com a ocupação. O controle está no tempo e na reposição."},
        {"titulo": "Cozinhas industriais", "icone": "industria", "href": "/segmentos/cozinhas-industriais/",
         "texto": "Volume alto, resfriamento e transporte. O alimento sai da sua cozinha e é consumido longe dela."},
        {"titulo": "Mercados e varejo", "icone": "mercado", "href": "/segmentos/mercados-e-varejo/",
         "texto": "Manipulação dentro da loja: açougue, rotisseria, padaria e fatiados. Quem embala assume a responsabilidade do rótulo."},
        {"titulo": "Eventos", "icone": "evento", "href": "/segmentos/eventos/",
         "texto": "Operação montada do zero, em local sem estrutura, com equipe temporária. Tudo precisa estar resolvido antes de sair da base."},
    ]
    return {
        "url": "/segmentos/",
        "title": "Segmentos atendidos, VeronaFood Consultoria",
        "description": ("Restaurantes, bares, hotéis, padarias, confeitarias, cozinhas industriais, buffets, "
                        "eventos e mercados. Consultoria para cada tipo de operação."),
        "trilha": [("Início", "/"), ("Segmentos", None)],
        "secoes": [
            {"tipo": "hero_simples", "chapeu": "Segmentos atendidos",
             "h1": "Cada operação tem o seu ponto crítico.",
             "apoio": ("Uma padaria perde produto por validade; uma cozinha industrial, no resfriamento e no "
                       "transporte; um buffet, no tempo que a comida fica exposta. O trabalho é o mesmo em "
                       "essência, mas começa em lugares diferentes. Veja onde começa no seu.")},
            {"tipo": "cards", "h2": "Com que tipo de negócio trabalho", "itens": cards,
             "fundo": " secao--claro"},
            {"tipo": "cta",
             "h2": "Seu negócio não está na lista?",
             "texto": ("A lista cobre o que mais aparece, não o limite do que dá para atender. Se você "
                       "trabalha com alimento e tem uma operação para organizar, vale a conversa."),
             "btn": "Falar sobre o meu caso"},
        ],
    }


# =========================================================================
def restaurantes():
    return _pagina(
        slug="restaurantes-e-bares", nome_trilha="Restaurantes e bares",
        title="Consultoria para restaurantes e bares, VeronaFood",
        description=("Boas práticas, ficha técnica, padronização e treinamento para restaurantes e bares. "
                     "Padrão que aguenta o pico e a troca de equipe."),
        chapeu="Restaurantes e bares",
        h1="O padrão precisa aguentar o sábado à noite.",
        apoio=("Em restaurante e bar, quase todo problema aparece no pico: a praça atropela, o prato sai "
               "diferente, o controle de temperatura fica para depois. O trabalho é montar um processo que "
               "funcione no movimento, não só na segunda de manhã."),
        figura="foto de cozinha de restaurante em operação",
        zap="Olá! Tenho um restaurante/bar e vim pelo site.",
        encontramos=[
            "<b>Mise en place sem controle de validade</b>, produto pré-preparado sem identificação de data, ou com etiqueta que ninguém confere.",
            "<b>Prato de tamanho variável</b>, cada cozinheiro monta de um jeito; o custo e a percepção do cliente mudam junto.",
            "<b>Cadeia fria interrompida no recebimento</b>, mercadoria parada na área de descarga enquanto a equipe termina outra coisa.",
            "<b>Contaminação cruzada no pré-preparo</b>, mesma bancada, mesma tábua, mesmo pano para tudo, principalmente no aperto.",
            "<b>Bar fora do escopo de controle</b>, gelo, polpa, frutas cortadas e guarnições costumam ficar de fora do manual, e são ponto crítico.",
            "<b>Delivery sem padrão de embalagem e transporte</b>, o prato sai certo da cozinha e chega diferente.",
            "<b>Rotatividade alta</b>, treinamento feito uma vez e nunca repetido, enquanto metade da equipe já é outra.",
            "<b>Preço de cardápio desatualizado</b>, montado na abertura e nunca recalculado, mesmo com fornecedor reajustando.",
        ],
        por_onde=[
            ("seguranca", "Manual, POPs e checklists que caibam na rotina do pico, não um documento que só funciona com a casa vazia."),
            ("padrao", "Abertura, troca de turno e fechamento definidos, com responsável por tarefa."),
            ("treino", "Por função e por turno, com reforço sempre que entra gente nova."),
            ("custos", "Depois que o processo está em pé, a ficha técnica passa a ser confiável."),
        ],
        atencao=[
            "Bar e cozinha tratados como uma operação só na documentação.",
            "Controle de temperatura em equipamento de alto uso, que abre e fecha o tempo todo no pico.",
            "Identificação e validade de produto pré-preparado e de produto aberto.",
            "Fluxo de louça suja e de resíduo em cozinha apertada.",
            "Manipulação de alimentos crus e de alimentos prontos na mesma estrutura.",
            "Delivery: embalagem, tempo e temperatura até a entrega.",
        ],
        faq=[
            {"pergunta": "Minha cozinha é pequena. Dá para adequar?",
             "resposta": ["Dá. Cozinha pequena não impede adequação, ela muda a solução. O que não cabe em espaço se resolve em fluxo, horário e ordem das tarefas. No diagnóstico eu trabalho com o espaço que existe."]},
            {"pergunta": "Vocês atrapalham o serviço durante a visita?",
             "resposta": ["A visita de diagnóstico é justamente em horário de operação, porque é a única forma de ver a rotina real, mas eu observo, não interfere. Treinamento e implantação ficam fora do pico."]},
            {"pergunta": "Meu cardápio muda toda semana. A ficha técnica serve?",
             "resposta": ["Serve. Eu monto ficha das bases e dos itens fixos e deixa um modelo para você calcular o prato novo em poucos minutos."]},
        ],
    )


# =========================================================================
def padarias():
    return _pagina(
        slug="padarias-e-confeitarias", nome_trilha="Padarias e confeitarias",
        title="Consultoria para padarias e confeitarias, VeronaFood",
        description=("Boas práticas, rotulagem, validade e padronização para padarias e confeitarias. "
                     "Para o produto embalado na loja sair certo."),
        chapeu="Padarias e confeitarias",
        h1="Quem embala assume a responsabilidade do rótulo.",
        apoio=("Padaria e confeitaria produzem, embalam e vendem no mesmo lugar, e isso traz uma camada que "
               "restaurante não tem: rotulagem, prazo de validade definido pela própria loja e produtos com "
               "recheio e cobertura que não perdoam erro de temperatura."),
        figura="foto de produção de padaria",
        zap="Olá! Tenho uma padaria/confeitaria e vim pelo site.",
        encontramos=[
            "<b>Rótulo incompleto ou genérico</b>, produto embalado na loja sem todas as informações obrigatórias, ou com rótulo copiado de outro item.",
            "<b>Validade definida no chute</b>, prazo atribuído por hábito, sem base no produto e sem nada que sustente.",
            "<b>Alergênicos sem controle</b>, leite, ovo, trigo, castanhas e derivados circulando na mesma bancada, sem separação nem declaração.",
            "<b>Recheio e cobertura fora de controle de temperatura</b>, preparo de madrugada, montagem de manhã, exposição o dia todo.",
            "<b>Vitrine sem monitoramento</b>, produto exposto em equipamento refrigerado que ninguém mede.",
            "<b>Produção em dois turnos sem passagem de informação</b>, quem entra de manhã não sabe o que a madrugada deixou pronto, nem quando.",
            "<b>Reaproveitamento sem critério</b>, sobra do dia anterior virando ingrediente do dia seguinte, sem registro nem regra.",
            "<b>Receita na cabeça do padeiro</b>, e o produto muda quando essa pessoa falta ou sai.",
        ],
        por_onde=[
            ("seguranca", "Com foco em validade, identificação de produto em processo e controle de alergênicos."),
            ("rotulagem", "Tabela nutricional, ingredientes e alergênicos do produto que você embala na loja."),
            ("custos", "Padaria é onde a ficha técnica dá o retorno mais rápido: receita padronizada reduz perda e estabiliza o produto."),
            ("padrao", "Passagem de turno, controle de produção e regra escrita de reaproveitamento."),
        ],
        atencao=[
            "Informação obrigatória no rótulo de produto embalado na ausência do consumidor.",
            "Declaração de alergênicos e separação de linha de produção.",
            "Critério para definir prazo de validade dos produtos de fabricação própria.",
            "Controle de temperatura em vitrine refrigerada e em câmara de recheios.",
            "Identificação de produto em processo: massa em fermentação, base pronta, recheio montado.",
            "Regra escrita para sobra e para reaproveitamento.",
            "Controle de pragas em ambiente com farinha e açúcar.",
        ],
        faq=[
            {"pergunta": "Minha produção é de madrugada e eu não estou lá.",
             "resposta": ["É justamente por isso que procedimento escrito e registro valem mais aqui que em qualquer outro segmento. O turno que você não vê precisa deixar rastro do que fez e quando."]},
            {"pergunta": "Faço bolo com castanha e pão sem nada. Preciso separar?",
             "resposta": ["O tema é controle de alergênicos e envolve separação de produção, de utensílios e declaração no rótulo. O que se aplica ao seu caso depende do que você produz e de como a sua cozinha é organizada, isso eu vejo na visita."]},
            {"pergunta": "Como eu defino a validade dos meus produtos?",
             "resposta": ["Não é por hábito nem por comparação com o concorrente. O critério precisa estar escrito e sustentado, e varia conforme o produto e o processo. É um dos pontos que o diagnóstico define para a sua operação."]},
        ],
    )


# =========================================================================
def hoteis():
    return _pagina(
        slug="hoteis-e-buffets", nome_trilha="Hotéis e buffets",
        title="Consultoria para hotéis e buffets, VeronaFood",
        description=("Boas práticas e padronização para café da manhã, buffet, room service e eventos em "
                     "hotéis. Controle de exposição e de reposição."),
        chapeu="Hotéis e buffets",
        h1="Comida exposta por horas exige controle de hora em hora.",
        apoio=("Em hotel e em buffet, o alimento fica à mostra, é reposto várias vezes e passa por muita "
               "gente. O ponto crítico não é o preparo: é o tempo que o produto passa na mesa e o que "
               "acontece com o que sobra."),
        figura="foto de serviço de buffet",
        zap="Olá! Trabalho com hotel/buffet e vim pelo site.",
        encontramos=[
            "<b>Tempo de exposição sem registro</b>, ninguém anota a que horas a cuba entrou no balcão.",
            "<b>Reposição que mistura lote novo com lote antigo</b>, cuba completada por cima em vez de trocada.",
            "<b>Mesa quente e mesa fria sem monitoramento</b>, equipamento ligado, mas sem medição durante o serviço.",
            "<b>Volume que muda com a ocupação</b>, produção dimensionada para a média, gerando sobra num dia e falta no outro.",
            "<b>Sobra de buffet sem destino definido</b>, o que volta da mesa e o que ficou pronto mas não foi exposto são coisas diferentes, e raramente há regra escrita para cada um.",
            "<b>Room service com transporte sem controle</b>, o prato sai correto da cozinha e percorre corredor e elevador antes de chegar.",
            "<b>Café da manhã com manipulação na frente do hóspede</b>, frios, frutas, sucos e pães expostos com acesso aberto.",
            "<b>Equipe de eventos contratada por demanda</b>, gente que entra na operação sem ter passado por nenhum treinamento da casa.",
        ],
        por_onde=[
            ("seguranca", "Com foco no controle de exposição, na reposição e no destino de sobra."),
            ("padrao", "Montagem e reposição do buffet, passagem de turno e rotina de conferência durante o serviço."),
            ("treino", "Incluindo quem entra por demanda, que costuma ser a maior lacuna do segmento."),
            ("custos", "Dimensionamento por ocupação, que é onde hotel mais perde dinheiro."),
        ],
        atencao=[
            "Registro de horário de exposição e critério de retirada.",
            "Controle de temperatura em mesa quente, mesa fria e refrigeração de apoio durante o serviço.",
            "Regra escrita para sobra exposta e para sobra não exposta, são situações diferentes.",
            "Transporte interno de alimento pronto: room service e eventos em outro andar.",
            "Higienização de utensílios de serviço e troca durante o buffet.",
            "Treinamento de equipe temporária antes de entrar em operação.",
            "Café da manhã: proteção do alimento exposto e fluxo do hóspede.",
        ],
        faq=[
            {"pergunta": "Quanto tempo a comida pode ficar no balcão?",
             "resposta": ["O parâmetro depende da temperatura mantida e do tipo de alimento, e é definido no trabalho técnico, por isso não publico um número aqui que valeria para qualquer operação.",
                          "É um dos primeiros pontos que o diagnóstico define para a sua casa, junto com o registro de horário e o critério de retirada."]},
            {"pergunta": "O que eu faço com o que sobra do buffet?",
             "resposta": ["A distinção importante é entre o que foi exposto ao público e o que ficou pronto na cozinha sem ser exposto: o tratamento dos dois é diferente.",
                          "Quase nenhuma operação tem isso escrito, e é um dos primeiros documentos que eu monto."]},
            {"pergunta": "Minha equipe de eventos muda a cada evento. Como treino?",
             "resposta": ["Com um treinamento curto de entrada, padronizado, que todo mundo faz antes do primeiro serviço, e com procedimento afixado no posto, para quem não tem tempo de decorar nada."]},
            {"pergunta": "Tenho restaurante, café da manhã e eventos no mesmo hotel. É um trabalho só?",
             "resposta": ["É um trabalho só com três frentes. A documentação de base é comum; o que muda é o procedimento de cada serviço e o controle durante a exposição."]},
        ],
    )


# =========================================================================
def industriais():
    return _pagina(
        slug="cozinhas-industriais", nome_trilha="Cozinhas industriais",
        title="Consultoria para cozinhas industriais, VeronaFood",
        description=("Boas práticas, resfriamento, transporte e padronização para cozinhas industriais e "
                     "refeições coletivas. Volume alto com controle."),
        chapeu="Cozinhas industriais",
        h1="O alimento sai da sua cozinha e é consumido longe dela.",
        apoio=("Em refeição coletiva, o risco não termina quando a panela sai do fogo. Resfriamento, "
               "armazenamento, transporte e distribuição são a parte do processo que menos se vê e mais pesa "
               ",  ainda mais quando o cliente é uma empresa que audita você."),
        figura="foto de cozinha industrial em produção",
        zap="Olá! Trabalho com cozinha industrial e vim pelo site.",
        encontramos=[
            "<b>Resfriamento pós-cocção sem controle</b>, produção grande esfriando em temperatura ambiente, sem registro de tempo nem de temperatura.",
            "<b>Transporte sem monitoramento</b>, caixa térmica sem medição na saída e na chegada.",
            "<b>Distribuição em ponto remoto sem procedimento</b>, quem serve no cliente não faz parte da rotina de controle da cozinha.",
            "<b>Amostra de refeição mal coletada ou mal guardada</b>, quando existe.",
            "<b>Volume que esconde falha</b>, o erro de um lote vira o erro de centenas de refeições.",
            "<b>Equipe grande em escala</b>, treinamento de um turno que nunca chega aos outros.",
            "<b>Cliente corporativo com auditoria própria</b>, exigência documental que a cozinha descobre no dia da visita.",
            "<b>Cardápio fixo com custo não revisado</b>, contrato fechado por refeição e custo de insumo subindo por dentro.",
        ],
        por_onde=[
            ("seguranca", "Com atenção ao que acontece depois da cocção: resfriamento, armazenamento, transporte e distribuição."),
            ("padrao", "Procedimento por posto, por turno e por ponto de distribuição."),
            ("treino", "Por função, com turmas por turno: em escala grande, treinar um turno só não cobre a operação."),
            ("custos", "Custo por refeição, que é a unidade com que o negócio é contratado."),
        ],
        atencao=[
            "Resfriamento e reaquecimento de grandes volumes: tempo, temperatura e registro.",
            "Transporte: equipamento, tempo de percurso e controle na saída e na chegada.",
            "Distribuição fora da base: responsabilidade, procedimento e registro.",
            "Coleta e guarda de amostras.",
            "Rastreabilidade de lote: saber qual produção foi para qual ponto.",
            "Documentação exigida por cliente corporativo, que costuma ir além da exigência sanitária.",
            "Dimensionamento de equipe e de equipamento para o volume real.",
        ],
        faq=[
            {"pergunta": "Meu cliente faz auditoria própria. Vocês preparam para isso?",
             "resposta": ["Eu organizo a documentação, os procedimentos e os registros que sustentam uma auditoria.",
                          "O resultado da auditoria depende do auditor e da operação no dia, isso nenhuma consultoria controla."]},
            {"pergunta": "Transporto refeição por mais de uma hora. Isso é um problema?",
             "resposta": ["É um ponto de controle, não necessariamente um problema. O que importa é o equipamento, a temperatura de saída e o registro na chegada.",
                          "O parâmetro aceitável para o seu caso é definido no trabalho técnico."]},
            {"pergunta": "Tenho equipe em três turnos. O treinamento cobre todos?",
             "resposta": ["Cobre, com turmas por turno. Treinar só o turno da manhã é o erro mais comum do segmento, e é o turno da noite que costuma operar com menos supervisão."]},
        ],
    )


# =========================================================================
def mercados():
    return _pagina(
        slug="mercados-e-varejo", nome_trilha="Mercados e varejo",
        title="Consultoria para mercados e varejo de alimentos, VeronaFood",
        description=("Boas práticas e rotulagem para açougue, rotisseria, padaria e fatiados dentro da loja. "
                     "Quem manipula no varejo assume responsabilidade."),
        chapeu="Mercados e varejo",
        h1="Mercado que manipula vira produtor de alimento.",
        apoio=("Açougue, rotisseria, padaria interna, hortifrúti e fatiados transformam a loja em operação de "
               "produção, com as mesmas exigências de quem fabrica, mais a camada de rotulagem e validade do "
               "produto embalado no próprio ponto de venda."),
        figura="foto de setor de rotisseria em mercado",
        zap="Olá! Tenho um mercado e vim pelo site.",
        encontramos=[
            "<b>Setores tratados como ilhas</b>, açougue, padaria e rotisseria cada um com uma prática, sem documentação comum.",
            "<b>Rótulo de produto embalado na loja incompleto</b>, peso, data, composição ou identificação faltando.",
            "<b>Validade atribuída pela loja sem critério</b>, produto fatiado ou porcionado recebendo prazo por hábito.",
            "<b>Exposição em ilha e balcão sem monitoramento</b>, equipamento aberto, fluxo de cliente constante, medição esporádica.",
            "<b>Fatiados e frios manipulados no balcão</b>, utensílio e superfície compartilhados entre produtos diferentes.",
            "<b>Hortifrúti sem controle de seleção e descarte</b>, produto no limite sendo aproveitado em outro setor sem registro.",
            "<b>Recebimento em volume alto sem conferência completa</b>, caminhão chega, mercadoria entra, conferência fica para depois.",
            "<b>Equipe de reposição sem treinamento de manipulação</b>, gente que mexe em alimento sem ter sido treinada para isso.",
        ],
        por_onde=[
            ("seguranca", "Documentação única para a loja, com procedimento específico por setor de manipulação."),
            ("rotulagem", "Do produto embalado e porcionado na própria loja."),
            ("padrao", "Recebimento, reposição, controle de exposição e descarte, com responsável por setor."),
            ("treino", "Por setor, incluindo quem repõe e quem atende no balcão."),
        ],
        atencao=[
            "Informação obrigatória no rótulo de produto embalado ou porcionado na loja.",
            "Critério para definir validade de fatiados, porcionados e preparados no ponto.",
            "Controle de temperatura em ilha, balcão e câmara, durante o horário de funcionamento.",
            "Separação entre produtos crus e prontos para consumo na exposição e no fatiamento.",
            "Regra de aproveitamento entre setores, hortifrúti para rotisseria, por exemplo, e seu registro.",
            "Conferência de recebimento com volume alto.",
            "Controle de pragas em área de estoque e de recebimento.",
        ],
        faq=[
            {"pergunta": "Cada setor tem um encarregado diferente. Como padronizar?",
             "resposta": ["Com documentação comum para a loja e procedimento específico por setor, mais uma matriz de responsabilidade que diga quem faz, quem confere e quem decide em cada ponto."]},
            {"pergunta": "Tenho várias lojas. Dá para fazer uma vez só?",
             "resposta": ["Dá, e é onde o ganho é maior: o procedimento é um só, e o que muda por loja vira anexo. A implantação e o treinamento é que acontecem loja a loja."]},
            {"pergunta": "Quem define a validade do frango assado da rotisseria?",
             "resposta": ["A loja, e é por isso que o critério precisa estar escrito e sustentado, em vez de vir do hábito.",
                          "Definir esse critério é parte do trabalho, e depende do produto e do processo de cada setor."]},
        ],
    )


# =========================================================================
def eventos():
    return _pagina(
        slug="eventos", nome_trilha="Eventos",
        title="Consultoria para eventos gastronômicos, VeronaFood",
        description=("Segurança dos alimentos em eventos: transporte, montagem em local sem estrutura, "
                     "equipe temporária e serviço fora da base."),
        chapeu="Eventos",
        h1="Operação montada do zero, em um lugar que não é seu.",
        apoio=("Evento é a operação mais difícil de controlar: estrutura improvisada, equipe que você conheceu "
               "naquela manhã, alimento que viajou e nenhuma chance de corrigir no meio do caminho. "
               "Tudo precisa estar resolvido antes de sair da base."),
        figura="foto de montagem de operação em evento",
        zap="Olá! Trabalho com eventos e vim pelo site.",
        encontramos=[
            "<b>Local sem estrutura avaliada antes</b>, água, energia, ponto de lavagem e espaço de apoio descobertos no dia da montagem.",
            "<b>Transporte sem controle</b>, alimento pronto viajando sem medição na saída e na chegada.",
            "<b>Equipe temporária sem treinamento</b>, freelancers contratados por evento entrando direto na operação.",
            "<b>Preparo antecipado sem registro</b>, produção feita dois dias antes, armazenada e transportada, sem rastro de quando e como.",
            "<b>Tempo de serviço longo</b>, comida exposta durante horas de recepção, em equipamento improvisado.",
            "<b>Sem procedimento para imprevisto</b>, o que fazer se o equipamento falhar, se o evento atrasar, se a comida chegar fora de temperatura.",
            "<b>Responsabilidade difusa</b>, buffet, local, decoração e cliente final com fronteiras pouco claras sobre quem responde pelo quê.",
            "<b>Sem registro do evento</b>, terminou, desmontou, não ficou documentação de nada.",
        ],
        por_onde=[
            ("seguranca", "Com procedimento específico de operação fora da base: transporte, montagem, serviço e desmontagem."),
            ("padrao", "Checklist de pré-evento, de montagem e de encerramento, mais a avaliação prévia do local."),
            ("treino", "Um treinamento de entrada, curto e padronizado, que todo freelancer faz antes do primeiro serviço."),
            ("custos", "Custo por convidado, que é como o evento é vendido."),
        ],
        atencao=[
            "Avaliação prévia do local: água potável, energia, ponto de higienização, área de apoio e descarte.",
            "Transporte de alimento pronto: equipamento, tempo e registro.",
            "Preparo antecipado: o que pode ser feito com antecedência e como armazenar.",
            "Controle durante o serviço em equipamento provisório.",
            "Higiene da equipe em local sem vestiário nem lavatório adequado.",
            "Treinamento mínimo de equipe temporária antes de entrar em operação.",
            "Registro do evento: o que foi produzido, transportado, servido e descartado.",
            "Definição escrita de responsabilidade entre buffet, local e cliente.",
        ],
        faq=[
            {"pergunta": "Cada evento é em um lugar diferente. Dá para padronizar?",
             "resposta": ["Dá, e é o que mais funciona aqui. O que se padroniza não é o local: é o checklist de avaliação prévia, o procedimento de transporte e o roteiro de montagem.",
                          "O lugar muda; a rotina não."]},
            {"pergunta": "Minha equipe é toda freelancer.",
             "resposta": ["Então o treinamento tem que ser curto, padronizado e obrigatório antes do primeiro serviço, e o procedimento afixado no posto, porque ninguém decora nada em um dia."]},
            {"pergunta": "O local não tem pia nem vestiário. O que faço?",
             "resposta": ["É um dos pontos que a avaliação prévia do local existe para resolver, com estrutura provisória quando necessário. O que não dá é descobrir isso no dia da montagem."]},
        ],
    )


def paginas():
    return [hub(), restaurantes(), padarias(), hoteis(), industriais(), mercados(), eventos()]
