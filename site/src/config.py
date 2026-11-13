# -*- coding: utf-8 -*-
"""
Configuração do site da VeronaFood.

Tudo o que muda sem mexer em código está aqui.

Os campos com valor None são PENDÊNCIAS: o site é construído sem eles,
sem inventar nada e sem deixar texto de mentira no ar. Ao preencher,
rode `python build.py` de novo e o conteúdo aparece sozinho.
O build imprime a lista do que ainda falta.
"""

SITE = {
    "nome": "VeronaFood",
    "nome_completo": "VeronaFood Consultoria de Alimentos",
    "url": "https://veronafood.com.br",
    "lang": "pt-BR",
    "posicionamento": "Processo claro, equipe treinada, operação sob controle.",

    # Prefixo de caminho. Vazio quando o site está na raiz de um domínio.
    # Preenchido por `build.py --base /VeronaFood` para a prévia no GitHub Pages,
    # que serve o site dentro de um subdiretório.
    "base_path": "",
    # Prévia não deve competir com o site real na busca: entra noindex.
    "preview": False,
    "descricao_curta": (
        "Consultoria em segurança dos alimentos, custos, padronização e treinamento "
        "para restaurantes, bares, hotéis, padarias, cozinhas industriais, buffets, "
        "eventos e mercados."
    ),
}

# --- contato -------------------------------------------------------------
# ✅ confirmados no site atual
CONTATO = {
    "telefone": "(11) 2362-6207",
    "telefone_link": "+551123626207",
    "whatsapp": "(11) 99495-5987",
    "whatsapp_numero": "5511994955987",
    "endereco_rua": "R. Antônio de Couros, 270",
    "endereco_bairro": "Vila Palmeiras",
    "endereco_cidade": "São Paulo",
    "endereco_uf": "SP",
    "endereco_cep": "02726-000",
    "horario": "Segunda a sexta, das 9h às 18h",
    "horario_schema": "Mo-Fr 09:00-18:00",

    # ⚠️ PENDENTE — não existe no site atual
    "email": "consultoriadealimentos.vfood@gmail.com",
    "cnpj": "40.864.832/0001-70",
    "prazo_resposta": "em até 1 dia útil",  # confirmado pela responsável em 12/11/2026
}

REDES = {
    "instagram": "https://www.instagram.com/veronafood.consultoria/",
    # ⚠️ PENDENTE — confirmar se existem
    "linkedin": None,
    "facebook": None,
}

# --- responsável técnica --------------------------------------------------
# ✅ nome e cargo constam no site atual. O resto vem da entrevista.
EQUIPE = [
    {
        "nome": "Bárbara Pontes",
        "cargo": "Consultora em Alimentos",
        "foto": None,            # ⚠️ ex.: "img/barbara.jpg"
        "credenciais": ["Nutricionista", "Gastrônoma", "10 anos de atuação"],  # ⚠️ falta o número do CRN
        "bio": None,             # ⚠️ 3 a 4 linhas em primeira pessoa
    },
]

# --- operação comercial ---------------------------------------------------
COMERCIAL = {
    # ⚠️ PENDENTE — define o texto do botão principal em todo o site
    # Valores aceitos: "gratuito", "abatido", "cobrado", None
    "diagnostico": None,
    "regiao_atendimento": "São Paulo",
    "atendimento_remoto": None,  # ⚠️ True / False
}

# --- formulário -----------------------------------------------------------
FORMULARIO = {
    # ⚠️ PENDENTE — endereço que recebe o envio.
    # Enquanto for None, o formulário valida e mostra a confirmação,
    # mas NÃO envia nada: o build avisa e o console do navegador também.
    # Opções sem servidor: Formspree, Basin, Web3Forms, Netlify Forms.
    "endpoint": None,
    "tipos_negocio": [
        "Restaurante", "Bar", "Hotel", "Padaria", "Confeitaria",
        "Cozinha industrial", "Buffet ou eventos", "Mercado", "Outro",
    ],
}

# --- provas ---------------------------------------------------------------
# Regra do projeto: nada entra no ar sem origem verificável.
# Enquanto estas listas estiverem vazias, as seções não são geradas
# e a home mostra "O que você recebe" no lugar dos depoimentos.
DEPOIMENTOS = []   # {"texto","nome","cargo","estabelecimento","cidade"}
NUMEROS = []       # {"valor","rotulo","apuracao"}
CLIENTES = []      # {"nome","logo"}

# --- analytics ------------------------------------------------------------
# Só dispara depois do aceite no aviso de cookies.
ANALYTICS_ID = None


# =========================================================================
# Derivados — não precisa editar daqui para baixo
# =========================================================================

def endereco_linha():
    c = CONTATO
    return "{}, {} — {}/{}, CEP {}".format(
        c["endereco_rua"], c["endereco_bairro"],
        c["endereco_cidade"], c["endereco_uf"], c["endereco_cep"],
    )


def whatsapp_link(mensagem):
    from urllib.parse import quote
    return "https://wa.me/{}?text={}".format(
        CONTATO["whatsapp_numero"], quote(mensagem)
    )


# Mensagem de WhatsApp por origem, para a consultora já receber contexto.
ZAP_PADRAO = "Olá! Vim pelo site e gostaria de agendar um diagnóstico."


def pendencias():
    """Lista o que falta preencher. O build mostra isso no terminal."""
    faltando = []
    if not CONTATO["email"]:
        faltando.append("CONTATO['email'] — e-mail institucional (rodapé, contato, schema)")
    if not CONTATO["cnpj"]:
        faltando.append("CONTATO['cnpj'] — exibido no rodapé")
    if not CONTATO["prazo_resposta"]:
        faltando.append("CONTATO['prazo_resposta'] — usado no hero e no formulário")
    if not COMERCIAL["diagnostico"]:
        faltando.append("COMERCIAL['diagnostico'] — gratuito/abatido/cobrado (afeta todos os botões)")
    if not COMERCIAL["regiao_atendimento"]:
        faltando.append("COMERCIAL['regiao_atendimento'] — página Sobre e FAQ")
    if COMERCIAL["atendimento_remoto"] is None:
        faltando.append("COMERCIAL['atendimento_remoto'] — FAQ")
    if not FORMULARIO["endpoint"]:
        faltando.append("FORMULARIO['endpoint'] — SEM ISSO O FORMULÁRIO NÃO ENVIA")
    for p in EQUIPE:
        if not p["credenciais"]:
            faltando.append("EQUIPE: credenciais de {} (formação, registro, anos)".format(p["nome"]))
        if not p["bio"]:
            faltando.append("EQUIPE: bio de {} (3 a 4 linhas em 1ª pessoa)".format(p["nome"]))
        if not p["foto"]:
            faltando.append("EQUIPE: foto de {}".format(p["nome"]))
    if not DEPOIMENTOS:
        faltando.append("DEPOIMENTOS — vazio: a home usa 'O que você recebe' no lugar")
    if not REDES["linkedin"] and not REDES["facebook"]:
        faltando.append("REDES — só Instagram confirmado")
    return faltando
