# -*- coding: utf-8 -*-
"""Converte o texto das páginas internas para a primeira pessoa do singular."""
import re
import sys

ARQS = ["src/pg_solucoes.py", "src/pg_segmentos.py", "src/pg_institucional.py"]

VERBOS = {
    "olhamos": "olho", "escrevemos": "escrevo", "montamos": "monto", "entregamos": "entrego",
    "pegamos": "pego", "conferimos": "confiro", "levamos": "levo", "transformamos": "transformo",
    "separamos": "separo", "colocamos": "coloco", "visitamos": "visito", "voltamos": "volto",
    "definimos": "defino", "desenhamos": "desenho", "acompanhamos": "acompanho", "pesamos": "peso",
    "treinamos": "treino", "executamos": "executo", "conversamos": "converso",
    "identificamos": "identifico", "ajustamos": "ajusto", "calculamos": "calculo",
    "marcamos": "marco", "organizamos": "organizo", "observamos": "observo", "fechamos": "fecho",
    "preparamos": "preparo", "deixamos": "deixo", "mostramos": "mostro", "respondemos": "respondo",
    "vamos": "vou", "temos": "tenho", "fazemos": "faço", "damos": "dou", "vemos": "vejo",
    "trabalhamos": "trabalho", "publicamos": "publico", "usamos": "uso", "apontamos": "aponto",
    "levantamos": "levanto", "reescrevemos": "reescrevo", "resolvemos": "resolvo",
    "recebemos": "recebo", "oferecemos": "ofereço", "montamos": "monto", "cobramos": "cobro",
    "indicamos": "indico", "sugerimos": "sugiro", "atendemos": "atendo", "partimos": "parto",
}

GENTE = {
    "vai": "vou", "dá": "dou", "monta": "monto", "olha": "olho", "confere": "confiro", "vê": "vejo",
    "define": "defino", "entrega": "entrego", "escreve": "escrevo", "volta": "volto", "pesa": "peso",
    "observa": "observo", "fecha": "fecho", "reescreve": "reescrevo", "levanta": "levanto",
    "prepara": "preparo", "organiza": "organizo", "faz": "faço", "tem": "tenho", "treina": "treino",
    "trabalha": "trabalho", "pega": "pego", "leva": "levo", "responde": "respondo", "mostra": "mostro",
    "ajusta": "ajusto", "calcula": "calculo", "marca": "marco", "visita": "visito", "monta": "monto",
    "resolve": "resolvo", "apoia": "apoio", "acompanha": "acompanho", "começa": "começo",
    "junta": "junto", "sabe": "sei", "pode": "posso", "precisa": "preciso", "quer": "quero",
    "conhece": "conheço", "analisa": "analiso", "separa": "separo", "aponta": "aponto",
    "identifica": "identifico", "executa": "executo", "desenha": "desenho", "transforma": "transformo",
    "coloca": "coloco", "deixa": "deixo", "recebe": "recebo", "avalia": "avalio",
}

FRASES = [
    ("Perguntas que a gente ouve sempre", "Perguntas frequentes"),
    ("Perguntas de quem trabalha neste segmento", "Perguntas de quem atende neste segmento"),
    ("O que a gente faz", "O que eu faço"),
    ("O que precisamos de você", "O que preciso de você"),
    ("Prazo e o que precisamos de você", "Prazo e o que preciso de você"),
    ("A gente responde", "Eu respondo"),
    ("A gente dá esse número", "Dou esse número"),
    ("a gente dá esse número", "dou esse número"),
    ("A gente vai até a sua operação", "Eu vou até a sua operação"),
    ("a gente monta o plano com você", "eu monto o plano com você"),
    ("Vamos começar pelo diagnóstico.", "Comece pelo diagnóstico."),
    ("Vamos ver a sua operação de perto.", "Agende a visita à sua operação."),
    ("Vamos até a sua operação", "Vou até a sua operação"),
    ("Vamos conversar sobre a sua operação.", "Vamos conversar sobre a sua operação."),
    ("quem precisamos", "quem preciso"),
    ("Para ver o que a gente", "Para ver o que eu"),
    ("nosso", "meu"), ("nossa", "minha"),
]


def converte(s):
    for a, b in FRASES:
        s = s.replace(a, b)
    # "a gente <verbo>" -> "eu <verbo 1ª pessoa>"
    def gente(m):
        ini, v = m.group(1), m.group(2)
        novo = GENTE.get(v)
        if not novo:
            return m.group(0)
        pre = "Eu" if ini == "A" else "eu"
        return "{} {}".format(pre, novo)
    s = re.sub(r"\b([Aa]) gente (\w+)", gente, s)
    for k, v in VERBOS.items():
        s = re.sub(r"\b{}\b".format(k), v, s)
        s = re.sub(r"\b{}\b".format(k.capitalize()), v.capitalize(), s)
    # travessões no meio de frases
    s = s.replace(" — ", ", ")
    s = s.replace("—", ", ")
    return s


def main():
    for arq in ARQS:
        txt = open(arq, encoding="utf-8").read()
        novo = converte(txt)
        open(arq, "w", encoding="utf-8").write(novo)
    restos = []
    for arq in ARQS:
        for i, l in enumerate(open(arq, encoding="utf-8").read().split("\n"), 1):
            if re.search(r"\b(a gente|A gente|nós|conosco)\b|\b\w+(amos|emos|imos)\b", l) and "def " not in l:
                restos.append("{}:{}: {}".format(arq, i, l.strip()[:200]))
    print("\n".join(restos))


if __name__ == "__main__":
    main()
