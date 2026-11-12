# VeronaFood — site e identidade

Projeto do novo site da **VeronaFood Consultoria de Alimentos**: proposta de design, textos de todas as páginas e o site funcional.

---

## Ver o site funcionando

```bash
cd site
python build.py --servir
```

Abre em `http://localhost:8000`. Precisa só de Python 3.9 ou mais novo — não há dependências para instalar.

Para gerar sem servidor: `python build.py`. A saída fica em `site/dist/`, que é uma pasta estática pronta para subir em qualquer hospedagem.

---

## O que tem aqui

| Pasta ou arquivo | O que é |
|---|---|
| **`site/`** | O site. Código, conteúdo e a saída gerada. Comece pelo [`site/LEIA-ME.md`](site/LEIA-ME.md). |
| **`VeronaFood_Alimentos/`** | Pacote de identidade visual: logos, ícones, cartão, papéis de parede, guia de estilo. |
| `proposta-veronafood.html` | **Proposta para a cliente.** Arquivo único, abre em qualquer navegador e imprime em PDF. |
| `proposta-visual.html` | Versão navegável da direção visual, com prévia da home, paleta e tipografia. |
| `PROPOSTA-SITE-VERONAFOOD.md` | Proposta completa: conceito, direção de arte, mapa do site, home seção por seção, SEO, acessibilidade e componentes. |
| `TEXTOS-PAGINAS-SOLUCOES.md` | Textos finais do hub de Soluções e das páginas de solução. |
| `TEXTOS-PAGINA-ROTULAGEM.md` | Textos da página de Rotulagem e os ajustes que ela provoca no site. |
| `TEXTOS-PAGINAS-SEGMENTOS.md` | Textos do hub de Segmentos e das seis páginas por tipo de operação. |
| `TEXTOS-SOBRE-E-COMO-FUNCIONA.md` | Textos das duas páginas institucionais e o **roteiro de entrevista** que fecha as pendências do projeto. |

---

## Estado do projeto

**Pronto:** as 21 páginas do site, com menu, formulário validado, FAQ, dados estruturados, sitemap, redirecionamentos das URLs antigas e acessibilidade (foco visível, navegação por teclado, contraste conferido, alvos de toque).

**Falta, e o build avisa toda vez:**

1. **O formulário não envia** — falta configurar `FORMULARIO['endpoint']` em `site/src/config.py`. Qualquer serviço de formulário sem servidor resolve.
2. **As fotos** — todas as imagens são molduras com a descrição do que entra ali.
3. **Os artigos** — listados como "em revisão técnica", sem link, porque tocam em legislação.
4. **Os campos do `config.py`** — credenciais da responsável técnica, região de atendimento, política do diagnóstico, CNPJ e e-mail.

O caminho mais curto para fechar quase tudo isso é o roteiro de 22 perguntas no fim de `TEXTOS-SOBRE-E-COMO-FUNCIONA.md`.

---

## Um princípio do projeto

Nada no site é inventado. Onde falta informação real, a seção não existe ou o texto se adapta — em vez de entrar com número, depoimento ou garantia sem origem verificável.

Isso vale especialmente para parâmetros sanitários. As páginas nomeiam o ponto de controle — *o tempo que a cuba fica no balcão*, *a temperatura de saída no transporte* — e deixam o número para o trabalho técnico, porque ele é regulado, varia por produto e muda com o tempo.
