# Proposta de site — VeronaFood Consultoria de Alimentos

**Documento de direção visual e estrutural para aprovação antes do desenvolvimento.**
Versão 1 · 12/11/2026

---

## Como ler este documento

Ao longo do texto, dois marcadores separam o que é fato do que é sugestão:

- ✅ **Confirmado** — informação que já existe (no site atual ou no pacote de identidade da pasta `VeronaFood_Alimentos`).
- ⚠️ **A confirmar** — campo que precisa de dado real da Verona Food antes da publicação. Nenhum número, resultado, depoimento ou certificação foi inventado neste documento. Onde aparece um texto de exemplo marcado como *placeholder*, ele serve apenas para a equipe de design dimensionar o bloco.

O que foi levantado antes de propor:

- **Site atual** (veronafood.com.br): WordPress/Elementor, menu Home / Sobre nós / Serviços (âncora) / Blog / Contato. Cinco serviços: Controle de qualidade, Manual de Boas Práticas & POPs, Treinamento, Ficha técnica, Rotulagem. Headline atual: "A parceria que transforma negócios". Contato por WhatsApp e telefone. Sem formulário visível na home, sem depoimentos, sem números, sem CNPJ, rodapé com "Copyright © 2023", seção "Localização" vazia, posts sem data, slug numérico em um post, menu "Serviços" apontando para âncora, e a página /contatos respondendo com redirecionamento de verificação antifrau­de que quebra o acesso.
- **Referências**: Certtus (foco em foodservice brasileiro, canal único de WhatsApp, página de serviço com "o que está incluso" + "como funciona", depoimentos com cargo), Arnika (formulário com campo de área de interesse, bloco "o que acontece depois", páginas por cidade), ANFSI (hero com selos de credencial, três pilares, formulário com abas por tipo de demanda, prazo de resposta declarado, FAQ de objeções).

O que foi aproveitado das referências é **lógica de organização e de conversão**. Nenhum texto, layout, componente ou elemento de identidade foi copiado.

---

# 1. Conceito do site

## 1.1 A ideia em poucas linhas

Um site que parece uma **consultoria sênior, não um folder de serviços**. Fundo champagne, vinho usado com economia (reservado para o que importa: títulos-chave, botões, o símbolo), muito espaço em branco e uma linha editorial calma. A elegância vem do ritmo e do espaçamento, não de ornamento.

A experiência é de **leitura curta e decisão rápida**: cada seção responde a uma pergunta que o dono do negócio faz de verdade — "isso é para mim?", "o que exatamente eu recebo?", "como começa?", "quem me atende?", "quanto tempo leva?" — e termina com um caminho de contato à mão.

A curva do símbolo (a folha dupla) vira o **elemento gráfico condutor** do site: aparece como separador entre blocos, como traço decorativo no topo de seções e na animação de entrada do hero. É o que dá assinatura visual sem precisar de imagens genéricas.

## 1.2 Posicionamento

> **A Verona Food organiza a operação de quem trabalha com alimento — da segurança sanitária ao custo do prato — e deixa o processo rodando com a equipe do cliente.**

Três ideias que o site precisa sustentar em todo lugar:

1. **Amplitude real** — a Verona Food não é só "consultoria de restaurante". Atende restaurantes, bares, hotéis, padarias, confeitarias, cozinhas industriais, buffets, eventos, mercados e outros negócios de alimentação.
2. **Escopo além do sanitário** — segurança dos alimentos é a porta de entrada, mas custo, padronização e treinamento são parte do trabalho. Isso diferencia da maioria dos concorrentes, que param na adequação à vigilância.
3. **Aplicável à rotina** — a entrega não é um documento guardado na gaveta: é procedimento que a equipe consegue seguir no dia a dia.

## 1.3 Mensagem principal do site

A frase que organiza tudo, usada no hero e repetida em variações ao longo das páginas:

> **Processo claro, equipe treinada, operação sob controle.**

## 1.4 Primeira tela da página inicial

**Chapéu (eyebrow, acima do título):**

> CONSULTORIA PARA NEGÓCIOS DE ALIMENTAÇÃO

**Frase principal (H1):**

> ## Sua operação de alimentos organizada do começo ao fim.

**Chamada complementar (subtítulo):**

> Segurança dos alimentos, controle de custos, padronização de processos e treinamento de equipe — com um plano feito para a realidade do seu negócio, não para o papel.

**Botões de ação:**

| | Texto | Ação | Estilo |
|---|---|---|---|
| Primário | **Agendar diagnóstico** | Rola até o formulário curto (`#diagnostico`) na home, ou abre a página `/contato` nas internas | Fundo vinho, texto champagne |
| Secundário | **Falar no WhatsApp** | `wa.me` com mensagem pré-preenchida | Contorno vinho, fundo transparente, ícone do WhatsApp |

**Linha de reforço abaixo dos botões** (texto pequeno, cinza-vinho):

> Resposta em até 1 dia útil. Sem compromisso. ⚠️ *A confirmar: só publicar o prazo se a Verona Food conseguir cumpri-lo sempre.*

**Por que "Agendar diagnóstico" e não "Solicitar orçamento":** "orçamento" pressupõe que o visitante já sabe o que quer comprar — e ele normalmente não sabe. "Diagnóstico" é uma oferta de entrada concreta, de baixo compromisso, que também serve de triagem comercial. O site atual usa "Solicitar orçamento" num popup; a troca é uma das mudanças de maior impacto na conversão.

---

# 2. Direção de arte

## 2.1 Paleta

### Cores da marca (já definidas no pacote de identidade)

| Nome | HEX | Função no site |
|---|---|---|
| **Vinho** | `#6E0F2A` | Cor principal. Botões primários, títulos de seção em fundos claros, rodapé, faixas de destaque, ícone da marca. Usar com economia: se tudo é vinho, nada é. |
| **Borgonha** | `#8B1E3F` | Estado *hover* do vinho, links em texto corrido, gradiente sutil em faixas grandes, segundo tom em gráficos e ilustrações. |
| **Rosé** | `#B86A7A` | Decorativo apenas: curva do símbolo, separadores, numeração de etapas, estados selecionados leves, ícone de aspas em depoimentos. **Nunca** para texto corrido sobre fundo claro (contraste insuficiente). |
| **Champagne** | `#F5EDE4` | Fundo padrão de páginas e seções. É a cor que dá o ar premium e acolhedor ao site. |
| **Taupe** | `#B59B8A` | Neutro quente. Bordas, divisórias, legendas, texto de apoio sobre fundo vinho, molduras de imagem. |

### Cores funcionais a acrescentar (necessárias para um site; precisam de aprovação)

| Nome | HEX | Função |
|---|---|---|
| **Tinta** | `#2A1B1E` | Cor de texto corrido. Um quase-preto puxado para o vinho, não um preto neutro — é o que faz a página parecer "desenhada" em vez de padrão. Contraste sobre champagne: 14,9:1. |
| **Tinta suave** | `#6B585C` | Texto secundário, legendas, metadados de artigo. Contraste sobre champagne: 5,4:1 ✅ AA. |
| **Champagne claro** | `#FBF7F2` | Fundo de cards sobre o champagne, campos de formulário, zebra de tabela. Cria camada sem precisar de sombra. |
| **Linha** | `#E3D7CA` | Bordas de card, divisórias finas, contorno de campo em repouso. |
| **Âmbar** | `#C2762F` | ⚠️ **Acento quente proposto.** Uso pontual e pequeno: ícone de destaque em "Benefícios", marcador de item em listas de entregáveis, tag "Novo" em conteúdos, sublinhado de palavra-chave no hero. Evita que o site vire monocromático vinho-bege. Sobre champagne o contraste é 3,6:1 — portanto **só para elementos gráficos e texto grande (≥24px bold)**, nunca para texto corrido. Se a marca preferir não ampliar a paleta, o rosé assume essa função com perda de contraste. |
| **Verde confirmação** | `#2F6B4F` | Mensagem de sucesso do formulário, checkmarks em listas de "o que está incluso". |
| **Vermelho erro** | `#A4231F` | Validação de formulário. Distinto o bastante do vinho para não confundir. |

### Como a paleta se distribui (regra prática para o designer)

- **60%** champagne `#F5EDE4` e champagne claro `#FBF7F2` — fundos.
- **25%** tinta `#2A1B1E` e taupe `#B59B8A` — texto e estrutura.
- **12%** vinho `#6E0F2A` e borgonha `#8B1E3F` — ações e âncoras visuais.
- **3%** rosé `#B86A7A` e âmbar `#C2762F` — detalhe.

Seções de respiro em vinho sólido (faixa de CTA, rodapé, bloco "quem te atende") quebram o ritmo claro e dão o contraste premium. Regra: **no máximo três faixas escuras na home**, e nunca duas seguidas.

### Tema escuro

Opcional, mas se for feito: fundo `#1A1012`, texto `#F0E6DC`, superfícies `#241518`, vinho clareado para `#C4536E` (botões e links precisam de contraste no escuro — o vinho original fica ilegível sobre fundo escuro). O logotipo usa a versão `horizontal_cream.svg` da pasta `01_Logos`.

## 2.2 Tipografia

**Recomendação (A):**

| Papel | Fonte | Pesos | Observação |
|---|---|---|---|
| Títulos (H1–H3) | **Fraunces** | 400 / 600, eixo `SOFT` em 40, `opsz` automático | Serifada moderna com variação óptica. Dá a elegância premium que uma sans geométrica não dá, e os terminais arredondados evitam o ar jurídico/distante. Google Fonts. |
| Texto corrido, H4+, listas, tabelas | **Inter** | 400 / 500 / 600 | Já indicada no guia da marca. Excelente leitura em telas pequenas. Google Fonts. |
| Botões, rótulos, chapéus (eyebrows), navegação | **Inter** | 600, `letter-spacing: 0.06em`, caixa alta nos chapéus | Mantém consistência com o lettering "CONSULTORIA DE ALIMENTOS" do logo. |
| Números grandes (etapas, estatísticas) | **Fraunces** 600, `font-variant-numeric: tabular-nums` | | |

**Alternativa conservadora (B):** títulos em **Montserrat** 600/700 e corpo em **Inter** — exatamente o par indicado no guia de identidade (`07_Guide/style_guide.svg`). É mais seguro e mais parecido com o logotipo, porém mais comum; o site perde um pouco de personalidade. ⚠️ *Decisão da Verona Food. Recomendamos A, com fallback para B se houver preferência por aderência literal ao guia.*

**Escala tipográfica** (base 16px, razão 1,25 no mobile e 1,333 no desktop):

| Elemento | Mobile | Desktop | Entrelinha |
|---|---|---|---|
| H1 | 34px | 58px | 1,08 |
| H2 | 26px | 40px | 1,15 |
| H3 | 21px | 26px | 1,25 |
| Corpo | 17px | 18px | 1,65 |
| Corpo pequeno / legenda | 15px | 15px | 1,55 |
| Chapéu / rótulo | 12px | 13px | 1,2 · `0.08em` |

Largura máxima de texto corrido: **68 caracteres** (~640px). Títulos com `text-wrap: balance`.

> ⚠️ **Licença de fontes:** Fraunces, Inter e Montserrat são todas de licença aberta (SIL Open Font License) e podem ser usadas no site e em materiais editáveis. O guia da marca já registra que as famílias não são redistribuídas no pacote — carregar via Google Fonts ou hospedar localmente com o arquivo de licença junto.

## 2.3 Fotografia e imagens

**Princípio:** nenhuma foto de banco de imagem com chef sorrindo de braços cruzados. O site é de uma consultoria real; as imagens precisam parecer o trabalho dela.

**O que fotografar** (⚠️ sessão de fotos a produzir — é o maior investimento de conteúdo desta proposta):

1. **Consultoria em campo** — a consultora com prancheta/tablet em cozinha real, conferindo câmara fria, termômetro, etiquetagem, estoque.
2. **Treinamento** — equipe em roda, manipuladores de uniforme, consultora explicando. Enquadramentos de três quartos e de costas preservam identidade.
3. **Documentação em uso** — manual de boas práticas aberto na bancada, checklist preso na parede da cozinha, POP plastificado ao lado da pia, planilha de ficha técnica na tela.
4. **Detalhes de operação** — mise en place, etiqueta de validade sendo colada, balança, rotulagem, termômetro na palma da mão. São as fotos que dão textura ao site sem expor ninguém.
5. **Retrato da responsável técnica** — um retrato em contexto (na cozinha de um cliente ou em bancada neutra), luz natural, sem fundo infinito de estúdio.

**Privacidade dos clientes:** rostos de funcionários só com autorização de uso de imagem assinada; marcas e logotipos de estabelecimentos desfocados ou fora de enquadramento, salvo autorização escrita. Preferir enquadramentos de mão, bancada e detalhe — resolvem 70% da necessidade sem nenhum risco.

**Tratamento:** luz natural, temperatura levemente quente, sem filtro pesado, sem preto e branco. Crop em 4:3 (cards) e 3:2 (banners). Moldura: cantos em 12px, sem sombra, com uma linha `#E3D7CA` de 1px. Em faixas vinho, a foto recebe um leve véu vinho (`mix-blend-mode: multiply` a 8%) para integrar.

**Enquanto não houver fotos próprias:** usar composições gráficas — fundo champagne com a curva da folha em rosé/taupe, cartões de documento estilizados, ícones em linha ampliados. **Não** usar banco de imagens genérico: um site com três fotos reais e o resto gráfico é mais confiável do que um site cheio de fotos que ninguém acredita.

**Ilustração/ícone:** família de ícones em **traço de 1,5px, cantos arredondados, sem preenchimento**, na cor vinho ou taupe, derivada do traço do símbolo (`05_Motion/icon_line_drawing.svg` já define o vocabulário de linha). Tamanho padrão 28px nos cards, 20px em listas.

## 2.4 Componentes visuais — tratamento

| Elemento | Tratamento |
|---|---|
| **Cards** | Fundo `#FBF7F2`, borda 1px `#E3D7CA`, raio **12px**, padding 28px (24px no mobile). Sem sombra em repouso. No hover: borda passa a `#B59B8A`, elevação suave `0 6px 20px rgba(110,15,42,.08)`, transição 180ms. Cards clicáveis inteiros, não só o link. |
| **Botão primário** | Fundo vinho, texto champagne, raio **8px**, padding 16px×28px, peso 600. Hover: borgonha. Foco: contorno 3px âmbar com 2px de afastamento. Ativo: escurece 6%. |
| **Botão secundário** | Contorno 1,5px vinho, texto vinho, fundo transparente. Hover: fundo vinho a 8%. |
| **Link em texto** | Vinho, sublinhado com `text-underline-offset: 3px` e espessura 1px; no hover a espessura vai a 2px. Nunca link sem sublinhado dentro de parágrafo. |
| **Bordas e divisórias** | 1px `#E3D7CA`. Entre seções, usar a **curva da folha** em rosé a 25% de opacidade, largura 120px, centralizada — é a assinatura gráfica do site. |
| **Fundos** | Alternância champagne → champagne claro → champagne, com até três faixas vinho na página. Sem gradiente chamativo; se houver, vinho→borgonha a 180° com variação mínima. |
| **Espaçamento** | Escala de 4px: 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96. Espaço vertical entre seções: **96px** no desktop, **56px** no mobile. Esse respiro é o principal responsável pela sensação de "premium". |
| **Cantos** | 12px em cards e imagens, 8px em botões e campos, 999px em tags/pills. Um sistema só, sem exceções. |
| **Sombra** | Praticamente ausente. Só em elementos flutuantes (menu mobile aberto, botão fixo de WhatsApp, modal). Profundidade vem de cor de fundo, não de sombra. |

## 2.5 Como ficar elegante sem parecer distante

Cinco decisões concretas que resolvem isso:

1. **Serifa só nos títulos, sans no corpo.** O texto que a pessoa realmente lê é Inter — moderno e direto. A elegância fica na camada de cima.
2. **Linguagem de cozinha, não de consultoria.** "Vamos até sua cozinha" em vez de "realizamos visita técnica in loco". "O que você recebe" em vez de "entregáveis do escopo". Primeira pessoa do plural, frases curtas.
3. **Rosto e nome na home.** A seção "Quem vai te atender" com foto e nome real da responsável técnica, logo depois das etapas — a proximidade vem de ver uma pessoa, não uma marca.
4. **Vinho com parcimônia.** Vinho em bloco inteiro intimida; vinho pontual sobre champagne é sofisticado. Por isso a regra dos 12%.
5. **Nada de superlativo.** Sem "excelência", "soluções inovadoras", "100% de conformidade". Afirmação específica e verificável sempre bate afirmação grandiosa — e evita problema legal.

---

# 3. Mapa do site

```
/                        Início
/solucoes                Soluções (hub)
  /solucoes/seguranca-dos-alimentos
  /solucoes/custos-e-ficha-tecnica
  /solucoes/treinamentos
  /solucoes/padronizacao-de-processos
  /solucoes/consultoria-completa
/segmentos               Segmentos atendidos (hub)
  /segmentos/restaurantes-e-bares
  /segmentos/padarias-e-confeitarias
  /segmentos/hoteis-e-buffets
  /segmentos/cozinhas-industriais
  /segmentos/mercados-e-varejo
  /segmentos/eventos
/como-funciona           Como funciona
/sobre                   Sobre a Verona Food
/conteudos               Conteúdos (listagem)
  /conteudos/[slug]      Artigo
/contato                 Contato
/politica-de-privacidade
/termos-de-uso
```

## Decisões de agrupamento e por quê

**"Como funciona" fica junto de "Sobre"? Não — fica separada, mas pequena.**
Não é uma página institucional: é a página que responde "o que vai acontecer comigo se eu contratar". É curta (uma tela e meia), tem as quatro etapas detalhadas, o que o cliente precisa fornecer, prazos típicos e o FAQ de objeções. Vale como página própria porque é o link que a consultora manda por WhatsApp para um lead em dúvida. ⚠️ *Alternativa, se a Verona Food preferir um site mais enxuto: virar uma seção longa dentro de `/sobre`. Recomendamos manter separada.*

**"Segmentos" ficam em páginas próprias? Sim, mas na segunda fase.**
No lançamento (fase 1), `/segmentos` pode ser uma página única com todos os segmentos em cards e um parágrafo cada. As páginas individuais (`/segmentos/padarias-e-confeitarias` etc.) entram na fase 2, conforme a Verona Food tiver conteúdo real e casos para cada uma. Elas são o maior ativo de busca do site — alguém pesquisa "consultoria boas práticas padaria", não "consultoria de alimentos" — mas página de segmento vazia é pior que página de segmento inexistente.

**"Soluções" e "Serviços" são a mesma coisa — por que "Soluções"?**
Porque o escopo da Verona Food passa de segurança a custo e gestão, e "serviços" empurra a leitura para uma lista de produtos avulsos. "Soluções" sustenta melhor a venda de consultoria completa. Qualquer um dos dois funciona; o importante é que **o nome do menu seja igual ao título da seção** — no site atual o menu diz "Serviços" e a seção diz "Consultoria de alimentos", o que confunde.

**"Conteúdos" em vez de "Blog".**
"Blog" sugere publicação frequente, e um blog parado envelhece o site. "Conteúdos" comporta artigo, checklist para download, vídeo curto e material de apoio, sem criar expectativa de cadência.

**"Contato" como página e não só como WhatsApp.**
O site atual manda "Contato" para uma página que hoje está quebrada por verificação de robô. A nova `/contato` precisa ser uma página real, leve, com formulário curto, WhatsApp, telefone, e-mail, endereço, horário e mapa.

**O que sai do site atual:**
- Popup "Solicitar orçamento" (substituído pelo formulário de diagnóstico em página).
- Menu "Serviços" como âncora na home (passa a ser página com filhas).
- Seção "Localização" vazia na página Sobre.
- Banner de cookies genérico (substituído por um que realmente respeite a LGPD — ver §6.4).
- Posts sem data e com slug numérico (migrar com slug descritivo e redirecionamento 301).

---

# 4. Página inicial — proposta completa

Ordem de leitura, de cima para baixo. Para cada seção: objetivo, textos sugeridos, conteúdo visual, ação e comportamento no celular.

---

### S0 · Cabeçalho

**Objetivo:** dar orientação e deixar o contato a um toque, sem roubar atenção do conteúdo.

**Conteúdo:** logo `horizontal_dual.svg` à esquerda (altura 36px) · menu central: Soluções · Segmentos · Como funciona · Sobre · Conteúdos · botão **Falar com a Verona Food** à direita (estilo primário compacto).

**Comportamento:** fundo champagne a 92% com `backdrop-filter: blur(8px)`, fixo no topo. Em repouso não tem borda; ao rolar mais de 40px ganha linha inferior `#E3D7CA`. "Soluções" e "Segmentos" abrem um painel simples (não mega-menu) com as páginas filhas e uma frase cada.

**Celular:** logo + ícone de menu (hambúrguer, 44×44px). O menu abre em painel de tela cheia, fundo champagne, itens em 20px com 56px de altura de toque, e os dois botões (WhatsApp e Agendar diagnóstico) fixos no rodapé do painel. **Botão flutuante de WhatsApp** no canto inferior direito a partir da segunda dobra, 56×56px, vinho, com `env(safe-area-inset-bottom)` respeitado.

---

### S1 · Hero

**Objetivo:** em 5 segundos, dizer o que a Verona Food faz, para quem, e dar dois caminhos de contato.

**Chapéu:** `CONSULTORIA PARA NEGÓCIOS DE ALIMENTAÇÃO`

**H1:** **Sua operação de alimentos organizada do começo ao fim.**

**Subtítulo:** Segurança dos alimentos, controle de custos, padronização de processos e treinamento de equipe — com um plano feito para a realidade do seu negócio, não para o papel.

**Botões:** `Agendar diagnóstico` (primário) · `Falar no WhatsApp` (secundário)

**Linha de reforço:** Atendimento de segunda a sexta, das 9h às 18h. ✅ *(horário confirmado no site atual)*

**Conteúdo visual:** layout de duas colunas 55/45. À esquerda o texto; à direita uma foto vertical de consultoria em cozinha real, cantos 12px, com a curva da folha em rosé saindo por trás do canto inferior esquerdo da foto. Fundo champagne. Animação de entrada: o texto sobe 12px com fade em 400ms escalonado; a curva da folha desenha o traço em 900ms (usar `05_Motion/icon_line_drawing.svg` como base), respeitando `prefers-reduced-motion`.

**Celular:** uma coluna. Chapéu → H1 → subtítulo → **botões empilhados em largura total** (primário em cima) → foto abaixo, em 4:3. A foto nunca fica acima do H1: a primeira coisa na tela é a frase.

---

### S2 · Faixa de segmentos (prova de amplitude)

**Objetivo:** responder imediatamente "isso serve para o meu tipo de negócio?" — a objeção número 1 do visitante, e o ponto em que o site atual falha ao parecer focado só em restaurante.

**Texto introdutório (uma linha, centralizada, 15px, tinta suave):**
> Trabalhamos com diferentes tipos de negócio de alimentação:

**Conteúdo:** linha de *pills* com borda `#E3D7CA` e texto tinta — Restaurantes · Bares · Hotéis · Padarias · Confeitarias · Cozinhas industriais · Buffets e eventos · Mercados. Cada pill leva ao segmento correspondente.

**Ação:** link discreto `Ver todos os segmentos →`

**Celular:** rolagem horizontal com *scroll-snap*, sem cortar o último item (padding-right de 16px no container). Alternativa: duas linhas que quebram naturalmente — preferível, porque rolagem horizontal escondida passa despercebida.

> ⚠️ **Não usar aqui logotipos de clientes nem "+X clientes atendidos"** enquanto a Verona Food não tiver lista real e autorização de uso de marca. Se tiver, este é o melhor lugar do site para colocar.

---

### S3 · Soluções

**Objetivo:** mostrar o escopo completo do trabalho, organizado de forma que ninguém precise ler tudo.

**H2:** **O que a gente resolve**
**Apoio:** Cada frente funciona sozinha ou combinada. Na dúvida, o diagnóstico aponta por onde começar.

**Conteúdo:** grade de 5 cards (3 + 2 no desktop, com o quinto card — Consultoria completa — ocupando largura dupla e fundo vinho, para se destacar como a oferta principal).

| Card | Título | Texto (1–2 linhas) | Link |
|---|---|---|---|
| 1 | **Segurança dos alimentos** | Boas práticas, POPs, controle de qualidade e adequação sanitária — organizados para passarem no dia a dia, não só na visita. | Ver detalhes → |
| 2 | **Custos e ficha técnica** | Ficha técnica por prato, custo real da receita, controle de porcionamento e perdas. Você passa a saber quanto cada item deixa. | Ver detalhes → |
| 3 | **Treinamento de equipe** | Capacitação por função, com linguagem de cozinha e material que fica com o time depois que a gente sai. | Ver detalhes → |
| 4 | **Padronização de processos** | Procedimentos escritos, checklists e rotinas que mantêm o padrão mesmo com troca de equipe. | Ver detalhes → |
| 5 (destaque, fundo vinho) | **Consultoria completa** | Quando o negócio precisa de tudo junto: diagnóstico, plano, implantação e acompanhamento contínuo, no ritmo da sua operação. | Falar sobre consultoria completa → |

**Conteúdo visual:** ícone em linha (28px, vinho) no topo de cada card; no card 5, ícone e texto em champagne sobre vinho.

**Celular:** uma coluna, cards em largura total, card 5 por último mantendo o fundo vinho. Ícone passa a ficar em linha com o título para economizar altura.

---

### S4 · Como funciona (etapas)

**Objetivo:** tirar o medo do primeiro contato mostrando que o processo é previsível.

**H2:** **Como o trabalho acontece**
**Apoio:** Quatro etapas. Você sabe onde está em cada uma.

| Etapa | Título | Texto |
|---|---|---|
| 01 | **Diagnóstico** | Visitamos sua operação, olhamos processo, estrutura, documentação e rotina da equipe. Você recebe um relatório com o que está em ordem e o que precisa de ajuste, por prioridade. |
| 02 | **Plano de ação** | Montamos o plano com prazos realistas, responsáveis e custo de cada frente. Você aprova o que faz sentido agora e o que fica para depois. |
| 03 | **Implantação** | Colocamos em prática junto com seu time: documentos, procedimentos, rotinas de controle e treinamento no próprio ambiente de trabalho. |
| 04 | **Acompanhamento** | Voltamos para conferir se o padrão se manteve, ajustamos o que não funcionou na prática e preparamos a equipe para seguir sozinha. |

**Conteúdo visual:** linha do tempo horizontal no desktop, com o número em Fraunces 600 48px em rosé, título em vinho e a curva da folha ligando as quatro etapas. Fundo champagne claro para separar da seção anterior.

**Ação:** `Ver o processo em detalhe →` levando a `/como-funciona`.

**Celular:** vira linha do tempo **vertical**, com um filete rosé de 2px na lateral esquerda ligando os números. Formato muito mais legível que carrossel.

---

### S5 · Benefícios para a operação

**Objetivo:** traduzir serviço em resultado prático, sem prometer o que depende de terceiros.

**H2:** **O que muda na sua rotina**

Quatro itens, ícone + título + uma linha:

1. **Menos retrabalho** — procedimentos escritos acabam com o "cada um faz de um jeito".
2. **Equipe mais segura** — gente treinada erra menos e pergunta menos.
3. **Custo visível** — ficha técnica mostra o que cada prato realmente custa.
4. **Operação pronta para fiscalização** — documentação organizada e rotina de controle em dia, a qualquer momento.

> ⚠️ **Regra de redação obrigatória nesta seção:** nada de "garantia de aprovação", "conformidade total", "zero multas" ou "100% em conformidade". O resultado de uma fiscalização depende do órgão e da operação do cliente. "Pronta para fiscalização" descreve o estado da documentação e da rotina, não promete resultado. Revisar com a Verona Food antes de publicar.

**Conteúdo visual:** fundo vinho sólido, texto champagne, ícones em linha âmbar. É a primeira faixa escura da página e quebra o ritmo claro.

**Celular:** 2×2 no tablet, 1 coluna no celular.

---

### S6 · Quem vai te atender

**Objetivo:** dar rosto e credibilidade técnica. É o antídoto contra "consultoria genérica".

**H2:** **Quem vai te atender**

**Texto:** ⚠️ *A escrever com dados reais.* Estrutura sugerida: nome · formação · registro em conselho de classe (se houver) · quantos anos de atuação · duas linhas sobre a abordagem, em primeira pessoa.

> ✅ **Confirmado no site atual:** Bárbara Camargo Pontes, Consultora em Alimentos. A empresa nasceu do objetivo da idealizadora de unir gastronomia e nutrição.
> ⚠️ **A confirmar antes de publicar:** formação completa, registro profissional (CRN, CRMV ou equivalente, se aplicável), ano de início da atuação, cursos e certificações que possam ser citados nominalmente, e se há mais profissionais na equipe.

**Conteúdo visual:** foto da responsável em contexto, retrato 4:5, à esquerda; texto à direita; abaixo do nome, uma linha de credenciais em pills de borda taupe. Fundo champagne claro.

**Ação:** `Conhecer a Verona Food →` para `/sobre`.

**Celular:** foto no topo (4:3), texto embaixo. Pills de credencial quebram em duas linhas.

---

### S7 · Depoimentos ou resultados

**Objetivo:** prova social.

> ⚠️ **Esta seção só entra no ar com material real e autorizado por escrito.** Se não houver, **a seção não existe** — não se coloca depoimento genérico nem "case fictício". A ausência de prova social é menos danosa que a prova inventada.

**Se houver depoimentos**, formato recomendado (foi o melhor padrão observado nas referências): aspas em texto corrido 20px Fraunces, e abaixo **nome · cargo · tipo de estabelecimento · cidade**. Três depoimentos no desktop, carrossel com snap no celular. Sem estrelas, sem foto de stock; foto real do cliente só com autorização.

**Se houver resultados numéricos** (ex.: número de clientes atendidos, horas de treinamento ministradas, estabelecimentos adequados), apresentar como três números grandes em Fraunces sobre champagne, com nota de rodapé dizendo o período de apuração. Cada número precisa ter origem documentada internamente.

**Alternativa, se não houver nada disso agora:** substituir por um bloco **"O que você recebe"** — lista visual dos entregáveis concretos (manual de boas práticas, POPs, checklists de controle, fichas técnicas, material de treinamento, relatório de diagnóstico). É prova de substância sem precisar de terceiros, e é honesta. **Recomendamos essa alternativa para o lançamento.**

---

### S8 · Conteúdo educativo

**Objetivo:** mostrar domínio do assunto e capturar quem ainda não vai contratar hoje.

**H2:** **Para ler antes de contratar qualquer consultoria**
**Apoio:** Conteúdo prático sobre segurança, custos e gestão na operação de alimentos.

**Conteúdo:** três cards de artigo — imagem 3:2, categoria em chapéu âmbar, título em Fraunces 21px, data e tempo de leitura em tinta suave.

> ✅ Já existe material aproveitável no site atual: ISO 22000, segurança em eventos gastronômicos, importância do treinamento, manual de boas práticas. Migrar com revisão de texto, data de publicação visível e slug descritivo.

**Ação:** `Ver todos os conteúdos →`

**Celular:** um card por linha; mostrar só dois e o link para a listagem, para não alongar a página.

---

### S9 · Perguntas frequentes

**Objetivo:** derrubar objeções que travam o contato.

**H2:** **Perguntas que a gente ouve sempre**

Seis perguntas em acordeão (a primeira aberta por padrão):

1. **Meu negócio é pequeno. Vale a pena contratar consultoria?** — ⚠️ *resposta a escrever com a Verona Food.*
2. **Quanto tempo leva para adequar minha operação?** — resposta honesta por faixa, dependendo do porte e do estado atual.
3. **O trabalho é presencial ou a distância?** — ⚠️ *confirmar se há atendimento remoto e quais regiões são atendidas presencialmente.*
4. **Quanto custa?** — explicar a lógica de precificação (porte, escopo, frequência) e dizer que o valor sai depois do diagnóstico. Não é preciso publicar tabela.
5. **Vocês atendem fora de São Paulo?** — ⚠️ *confirmar raio de atendimento.*
6. **O que eu preciso ter em mãos para começar?** — lista curta: alvará, documentação existente, rotina atual, acesso à cozinha.

**Técnico:** `<details>/<summary>` nativo com estilização — acessível por teclado sem JavaScript. Marcar com `FAQPage` schema (ver §8).

**Celular:** idêntico, com área de toque de 56px por pergunta.

---

### S10 · Chamada final

**Objetivo:** última conversão, com formulário visível e não atrás de um clique.

**Fundo:** vinho sólido. **Layout:** duas colunas — texto à esquerda, formulário em card champagne claro à direita.

**H2 (champagne):** **Vamos começar pelo diagnóstico.**
**Texto:** Conte em duas linhas como está sua operação hoje. A gente responde com o próximo passo — sem compromisso e sem proposta genérica.

**Formulário curto** (campos em §6.2). Botão primário em âmbar sobre o vinho (para destacar) ou champagne com texto vinho — testar; **champagne com texto vinho** é a recomendação por contraste.

**Abaixo do formulário:** `Prefere conversar agora? Chamar no WhatsApp →` e o telefone ✅ (11) 2362-6207 como texto selecionável.

**Celular:** texto primeiro, formulário embaixo, campos em largura total com 52px de altura. O botão de envio não pode ficar escondido atrás do botão flutuante do WhatsApp — dar `padding-bottom: 96px` ao card nesta largura.

---

### S11 · Rodapé

**Objetivo:** fechar com informação institucional completa e ser o lugar onde ninguém se perde.

Quatro colunas no desktop, acordeão no celular:

1. **Marca** — logo `horizontal_cream.svg`, uma linha de posicionamento, Instagram ✅ `@veronafood.consultoria` e demais redes ⚠️ *a confirmar.*
2. **Soluções** — as cinco páginas.
3. **Institucional** — Sobre, Como funciona, Segmentos, Conteúdos, Contato.
4. **Contato** — ✅ WhatsApp (11) 99495-5987 · ✅ Telefone (11) 2362-6207 · ⚠️ e-mail *a confirmar* · ✅ R. Antônio de Couros, 270 — Vila Palmeiras, São Paulo/SP, CEP 02726-000 · ✅ Seg a sex, 9h às 18h.

**Barra inferior:** © 2026 VeronaFood Consultoria de Alimentos · ⚠️ **CNPJ a confirmar e publicar** (dá credibilidade e é esperado de prestador de serviço B2B) · Política de Privacidade · Termos de Uso.

> ⚠️ O rodapé atual exibe "Copyright © 2023". O novo deve usar ano dinâmico.

**Fundo:** vinho. Texto champagne, links com hover em taupe.

---

# 5. Páginas internas

---

## 5.1 `/solucoes` — Soluções (hub)

**Objetivo:** apresentar as cinco frentes e encaminhar para a página certa.

**Seções:** hero curto (H1 "O que a gente resolve" + uma linha) → bloco "Por onde começar?" com três situações clicáveis — *"Vou abrir meu negócio"*, *"Recebi uma notificação da vigilância"*, *"Quero organizar custo e padrão"* — cada uma levando à solução correspondente (organizar por **momento do cliente**, não só por disciplina, é o que mais aumenta a taxa de clique) → os cinco cards de solução em grade → bloco "Não sabe qual precisa?" com CTA de diagnóstico.

**CTA:** `Agendar diagnóstico` fixo no final.

---

## 5.2 `/solucoes/[slug]` — Página de solução (template reutilizável)

Vale para as cinco. Estrutura fixa, conteúdo variável:

1. **Hero** — chapéu com o nome da frente, H1, duas linhas de contexto, botão `Agendar diagnóstico`.
2. **Para quem é** — 3 a 5 bullets de situação ("você tem POP escrito mas ninguém segue", "sua equipe muda muito e o padrão se perde").
3. **O que você recebe** — lista de entregáveis concretos com checkmark verde. É o bloco mais importante da página: substitui adjetivo por substantivo.
4. **Como funciona nesta frente** — as 3 ou 4 etapas específicas, versão resumida de §4/S4.
5. **Prazo e o que precisamos de você** — ⚠️ *a preencher com a Verona Food.* Transparência aqui reduz muito a ansiedade do lead.
6. **Perguntas sobre esta solução** — 3 a 4 itens de FAQ específicos.
7. **Conteúdos relacionados** — dois artigos.
8. **CTA final** — faixa vinho com formulário curto ou botão.

**Conteúdo por página** (⚠️ textos completos a desenvolver com a Verona Food; os cinco títulos e os entregáveis-base vêm dos serviços já descritos no site atual):

| Página | Entregáveis-base a detalhar |
|---|---|
| Segurança dos alimentos | Diagnóstico sanitário, Manual de Boas Práticas, POPs, checklists de controle (temperatura, higienização, recebimento), plano de adequação |
| Custos e ficha técnica | Fichas técnicas por item, custo por porção, controle de perdas e porcionamento, planilha de acompanhamento |
| Treinamentos | Programa por função, material didático, treinamento presencial, lista de presença e registro |
| Padronização de processos | Mapeamento da rotina, procedimentos escritos, checklists operacionais, rotina de conferência |
| Consultoria completa | Combinação das frentes + acompanhamento recorrente, com agenda de visitas definida |

---

## 5.3 `/segmentos` — Segmentos atendidos

**Objetivo:** provar amplitude e capturar busca por tipo de negócio.

**Seções:** hero ("Com que tipo de negócio trabalhamos") → grade de cards por segmento, cada um com foto, nome e duas linhas sobre o que muda naquele contexto (padaria tem desafio de validade e rotulagem; cozinha industrial tem volume e transporte; evento tem operação temporária e cadeia fria fora de casa) → bloco "Seu negócio não está na lista?" com CTA.

**CTA:** `Falar sobre o meu caso`.

**Fase 2:** cada card vira página própria, com o mesmo template da página de solução, trocando "O que você recebe" por "O que costuma aparecer em [segmento]".

---

## 5.4 `/como-funciona` — Como funciona

**Objetivo:** ser o link que resolve a dúvida de quem está quase contratando.

**Seções:** hero curto → as quatro etapas em detalhe (uma tela cada, com o que acontece, quanto tempo costuma levar e o que o cliente precisa disponibilizar) → **"O que acontece depois que você entra em contato"** em três passos (1. a gente responde em até 1 dia útil ⚠️; 2. conversa de 15–20 minutos para entender a operação; 3. agendamento da visita de diagnóstico) → "Como funciona o investimento" explicando a lógica de precificação sem tabela → FAQ completo → CTA.

**CTA:** `Agendar diagnóstico` e WhatsApp.

---

## 5.5 `/sobre` — Sobre a Verona Food

**Objetivo:** credibilidade por pessoa e por história, não por adjetivo.

**Seções:** hero com retrato da responsável e uma frase de posicionamento → **História** (✅ base real: a empresa nasceu do objetivo de unir gastronomia e nutrição — desenvolver com a Verona Food) → **Quem te atende**, com nome, formação, registro e tempo de atuação ⚠️ → **Como trabalhamos**, três ou quatro princípios escritos em primeira pessoa (nada de "missão, visão e valores" em bullets genéricos) → **Onde atendemos**, com o endereço real e a região de cobertura ⚠️ → CTA.

> ⚠️ A página atual tem uma seção "Localização" vazia. Na nova, ou se publica mapa e região de atendimento de verdade, ou a seção não existe.

---

## 5.6 `/conteudos` — Conteúdos

**Objetivo:** atrair busca e nutrir quem ainda não decidiu.

**Seções:** hero com uma linha → filtro por categoria (Segurança dos alimentos · Custos e gestão · Treinamento · Legislação) → grade de artigos com imagem, categoria, título, data e tempo de leitura → paginação numerada (não "carregar mais", que prejudica indexação) → bloco de newsletter ou material rico ⚠️ *opcional, só se houver quem mantenha.*

**Página de artigo:** título, data, autor com foto e link para `/sobre`, sumário em artigos longos, texto em coluna de 68 caracteres, imagens com legenda, **CTA de contato ao final de todo artigo** (hoje o post de ISO 22000 termina sem nenhuma chamada — é desperdício direto), e três artigos relacionados.

---

## 5.7 `/contato` — Contato

**Objetivo:** ser a página mais fácil do site.

**Seções:** H1 "Vamos conversar" + uma linha → duas colunas: à esquerda o formulário curto, à direita os canais diretos (WhatsApp com botão grande, telefone, e-mail ⚠️, endereço, horário) → abaixo, "O que acontece depois" em três passos → mapa incorporado ⚠️ *só se o endereço for ponto de atendimento; se for escritório sem recepção, substituir por "região atendida".*

> ⚠️ **Corrigir o problema atual:** a página `/contatos` responde hoje com redirecionamento para um domínio externo de verificação, o que impede o acesso. Na reconstrução, usar proteção antispam que não bloqueie o visitante (honeypot + rate limit, ou Cloudflare Turnstile embutido, nunca redirecionamento para outro domínio).

---

# 6. Fluxo de conversão

## 6.1 O caminho mais curto

```
Chegada (home, artigo ou página de solução)
        │
        ├── Tem pressa / quer falar agora ──► WhatsApp  (botão no header + flutuante no mobile + rodapé)
        │                                      mensagem pré-preenchida por origem
        │
        ├── Quer entender primeiro ─────────► Soluções → Como funciona → formulário
        │
        └── Quer ser procurado ─────────────► Formulário curto (home S10, /contato, fim de cada página)
                                                      │
                                              Confirmação na tela + e-mail
                                                      │
                                              Resposta em até 1 dia útil ⚠️
```

**Três regras:**

1. **Toda página termina com contato.** Sem exceção, inclusive artigos.
2. **Dois canais, sempre os mesmos.** WhatsApp para quem tem pressa, formulário para quem prefere ser procurado. Não adicionar um terceiro (chat, agendamento online) no lançamento — mais opções reduzem conversão.
3. **Uma mensagem de WhatsApp por origem.** O site atual usa dois textos diferentes sem critério. Padronizar: da home, "Olá! Vim pelo site e gostaria de agendar um diagnóstico."; de uma página de solução, "Olá! Vim pela página de [solução] e queria entender melhor."; de artigo, "Olá! Li o artigo sobre [tema] e tenho uma dúvida." Isso já entrega contexto para a consultora.

## 6.2 Formulário curto

Só o necessário para iniciar a conversa — **cinco campos**:

| Campo | Tipo | Obrigatório | Observação |
|---|---|---|---|
| Nome | texto | sim | `autocomplete="name"` |
| WhatsApp ou telefone | tel | sim | máscara brasileira, `inputmode="tel"` |
| E-mail | email | não | opcional reduz abandono; o WhatsApp já basta para responder |
| Tipo de negócio | seleção | sim | Restaurante · Bar · Hotel · Padaria · Confeitaria · Cozinha industrial · Buffet/Eventos · Mercado · Outro — serve de triagem e já diz muito sobre o lead |
| Como podemos ajudar | texto longo, 3 linhas | não | *placeholder*: "Conte em duas linhas como está sua operação hoje." |

**Nada de:** CNPJ, cargo, faturamento, número de funcionários, "como nos conheceu", orçamento disponível. Cada campo a mais derruba a conversão, e tudo isso se pergunta na conversa.

**Comportamento:** validação ao sair do campo (não a cada tecla); erro em texto abaixo do campo, nunca só cor; botão com estado de carregamento; sucesso em bloco verde na própria página — "Recebemos. Respondemos em até 1 dia útil ⚠️. Se preferir, chame no WhatsApp." — nunca redirecionar para uma página de obrigado vazia.

## 6.3 Opções sem pressionar

- Nenhum popup de saída, nenhum popup de entrada, nenhum cronômetro.
- O número de telefone e o e-mail aparecem como **texto selecionável**, para quem prefere ligar sozinho.
- "Ainda não quer falar? [Baixe o checklist de boas práticas]" ⚠️ *material a produzir* — alternativa para quem está pesquisando.
- Nenhum campo obrigatório que o visitante possa não querer dar agora.

## 6.4 Privacidade e LGPD

**Abaixo do botão de envio**, texto de 13px em tinta suave:

> Usamos seus dados apenas para responder a este contato. Não enviamos newsletter sem autorização e não compartilhamos suas informações com terceiros. Veja nossa [Política de Privacidade](/politica-de-privacidade).

**Checkbox de consentimento:** não é obrigatório para responder a um contato solicitado pelo próprio titular (Art. 7º, V da LGPD — execução de procedimentos preliminares a pedido do titular). Mas **é obrigatório** se a Verona Food quiser usar o contato depois para marketing. Recomendação: um checkbox **opcional e não pré-marcado**:

> ☐ Quero receber conteúdos sobre segurança dos alimentos e gestão por e-mail.

**Banner de cookies:** só aparece se o site realmente usar cookies não essenciais (Google Analytics, pixel de anúncio). Precisa ter **"Aceitar" e "Recusar" com o mesmo peso visual** — banner com só "Aceitar" não atende à LGPD. Nenhum script de rastreamento dispara antes da escolha.

**Política de Privacidade** precisa conter: quais dados são coletados, finalidade, base legal, prazo de guarda, com quem são compartilhados (incluindo o provedor de hospedagem e a ferramenta de e-mail), direitos do titular e **canal de contato do encarregado** ⚠️ *a definir — pode ser o próprio e-mail da empresa.*

> ⚠️ Este texto é orientação de estrutura, não parecer jurídico. A política final deve ser revisada por quem tem responsabilidade jurídica pela empresa.

---

# 7. Responsividade e acessibilidade

## 7.1 Pontos de quebra

| Faixa | Comportamento |
|---|---|
| **até 599px** (celular) | Uma coluna. Menu em painel de tela cheia. Botões em largura total. Linha do tempo vertical. Botão flutuante de WhatsApp. Espaço entre seções: 56px. |
| **600–899px** (tablet retrato) | Duas colunas em grades de card. Menu ainda em hambúrguer. Hero ainda empilhado. Espaço: 72px. |
| **900–1199px** (tablet paisagem / notebook pequeno) | Menu horizontal completo. Hero em duas colunas. Grade de 3 cards. Espaço: 88px. |
| **1200px+** (desktop) | Layout completo. Container de 1200px com gutter de 24px. Espaço: 96px. |
| **1600px+** | Container não cresce além de 1200px; só aumenta a margem lateral. Texto não deve esticar. |

**Teste obrigatório em:** iPhone SE (375px, a largura mais apertada que ainda importa), iPhone 15 (393px), iPad (768px) e notebook 1366px.

## 7.2 Navegação em telas pequenas

- Hambúrguer de 44×44px com rótulo acessível (`aria-label="Abrir menu"`, `aria-expanded`).
- Painel de menu abre com foco movido para o primeiro item e **armadilha de foco** enquanto aberto; `Esc` fecha e devolve o foco ao botão.
- Itens com 56px de altura, separados por linha `#E3D7CA`.
- Submenus ("Soluções", "Segmentos") como acordeão dentro do painel, nunca como segunda camada deslizante.
- Botão de WhatsApp flutuante com 56×56px, afastado 16px das bordas + `env(safe-area-inset-bottom)`, e `aria-label="Falar no WhatsApp"`. Some quando o formulário final está visível, para não cobrir o botão de envio.

## 7.3 Legibilidade e contraste

- Corpo nunca abaixo de **17px** no celular.
- Entrelinha 1,65 no corpo, 1,08–1,25 em títulos.
- **Contrastes verificados** (WCAG 2.2 AA exige 4,5:1 para texto normal, 3:1 para texto grande e componentes):

| Combinação | Razão | Situação |
|---|---|---|
| Tinta `#2A1B1E` sobre champagne `#F5EDE4` | 14,9:1 | ✅ AAA |
| Tinta suave `#6B585C` sobre champagne | 5,4:1 | ✅ AA |
| Vinho `#6E0F2A` sobre champagne | 10,9:1 | ✅ AAA |
| Champagne sobre vinho | 10,9:1 | ✅ AAA |
| Taupe `#B59B8A` sobre champagne | 1,9:1 | ❌ só decorativo |
| Rosé `#B86A7A` sobre champagne | 3,0:1 | ⚠️ só gráfico e texto ≥24px bold |
| Âmbar `#C2762F` sobre champagne | 3,6:1 | ⚠️ só gráfico e texto grande |
| Taupe sobre vinho | 5,6:1 | ✅ AA (texto de apoio no rodapé) |

- Nenhuma informação transmitida **só por cor**: erro de formulário tem ícone e texto; item ativo do menu tem sublinhado além da cor.
- Página legível com zoom de 200% sem rolagem horizontal, e com `text-spacing` aumentado.

## 7.4 Toque e formulário

- Alvo mínimo de toque **44×44px**, com 8px de separação entre alvos adjacentes.
- Campo de formulário com 52px de altura no celular e `font-size: 16px` no mínimo (abaixo disso o iOS dá zoom automático ao focar).
- **Toda etiqueta visível e acima do campo** — nunca *placeholder* como rótulo, que some ao digitar.
- `autocomplete` correto em nome, telefone e e-mail; `inputmode="tel"` no telefone.
- Erros anunciados por leitor de tela: `aria-live="polite"` no resumo de erros e `aria-describedby` ligando o campo à sua mensagem.
- `<fieldset>`/`<legend>` em grupos, `<label for>` em todos os campos.

## 7.5 Teclado, foco e leitores de tela

- **Anel de foco visível em tudo:** contorno 3px âmbar `#C2762F` com `outline-offset: 2px`. Nunca `outline: none` sem substituto.
- Link "Pular para o conteúdo" como primeiro elemento focável, visível ao receber foco.
- Ordem de tabulação igual à ordem visual; nada de `tabindex` positivo.
- Estrutura semântica: um `<h1>` por página, hierarquia de títulos sem pular nível, `<nav>`, `<main>`, `<footer>`, landmarks nomeados.
- Acordeão do FAQ em `<details>/<summary>` nativo — funciona por teclado sem JavaScript.
- Carrossel (se houver) com botões de anterior/próximo reais, pausa automática e navegação por teclado. **Preferível: evitar carrossel.**

## 7.6 Imagens e movimento

- **Texto alternativo descritivo** em toda imagem com conteúdo: "Consultora conferindo temperatura de câmara fria com termômetro digital" — não "foto1" nem "consultoria".
- Imagem puramente decorativa recebe `alt=""` para o leitor pular.
- Logo com `alt="VeronaFood Consultoria de Alimentos"`.
- Ícones decorativos com `aria-hidden="true"`; ícone que carrega significado sozinho recebe texto alternativo.
- `prefers-reduced-motion: reduce` desliga a animação da curva no hero, as transições de entrada e qualquer *parallax*; a página fica completa e estática.
- Formatos: WebP com fallback JPEG, `loading="lazy"` fora da primeira dobra, `width`/`height` declarados para não haver salto de layout.

---

# 8. SEO e conteúdo

## 8.1 Títulos e descrições

| Página | `<title>` (≤60 car.) | `meta description` (≤155 car.) |
|---|---|---|
| Início | VeronaFood — Consultoria para negócios de alimentação | Consultoria em segurança dos alimentos, custos, padronização e treinamento para restaurantes, padarias, hotéis, cozinhas industriais e eventos. |
| Soluções | Soluções em consultoria de alimentos — VeronaFood | Segurança dos alimentos, ficha técnica e custos, treinamento de equipe e padronização de processos. Veja o que a Verona Food faz na prática. |
| Segurança dos alimentos | Consultoria em segurança dos alimentos — VeronaFood | Manual de boas práticas, POPs, checklists e adequação sanitária aplicados à rotina da sua cozinha. Agende um diagnóstico. |
| Custos e ficha técnica | Ficha técnica e controle de custos — VeronaFood | Saiba quanto cada prato realmente custa. Fichas técnicas, controle de porcionamento e de perdas para negócios de alimentação. |
| Treinamentos | Treinamento de equipe em manipulação de alimentos — VeronaFood | Capacitação por função, com linguagem de cozinha e material que fica com o seu time. Presencial, na sua operação. |
| Padronização | Padronização de processos e POPs — VeronaFood | Procedimentos escritos, checklists e rotinas que mantêm o padrão mesmo com troca de equipe. |
| Consultoria completa | Consultoria completa para operação de alimentos — VeronaFood | Diagnóstico, plano de ação, implantação e acompanhamento contínuo para o seu negócio de alimentação. |
| Segmentos | Segmentos atendidos — VeronaFood Consultoria | Restaurantes, bares, hotéis, padarias, confeitarias, cozinhas industriais, buffets, eventos e mercados. |
| Como funciona | Como funciona a consultoria — VeronaFood | Diagnóstico, plano de ação, implantação e acompanhamento. Veja o que acontece em cada etapa e o que esperar do primeiro contato. |
| Sobre | Sobre a VeronaFood Consultoria de Alimentos | Quem somos, como trabalhamos e quem vai te atender. Consultoria para negócios de alimentação em São Paulo. ⚠️ *ajustar região* |
| Conteúdos | Conteúdos sobre segurança e gestão de alimentos — VeronaFood | Artigos práticos sobre boas práticas, legislação, custos e treinamento para quem trabalha com alimento. |
| Contato | Fale com a VeronaFood — Consultoria de Alimentos | Agende um diagnóstico ou chame no WhatsApp. Atendimento de segunda a sexta, das 9h às 18h. |

**Regras:** um `<title>` único por página, nunca "Home | Verona Food". `canonical` em todas. Open Graph e Twitter Card com imagem 1200×630 em vinho com o logo em champagne.

## 8.2 Dados estruturados (schema.org)

- `ProfessionalService` ou `LocalBusiness` no rodapé de todas as páginas: nome, endereço ✅, telefone ✅, horário ✅, URL, logo, `sameAs` para o Instagram ✅. ⚠️ Não incluir `aggregateRating` sem avaliações reais.
- `Service` em cada página de solução.
- `FAQPage` nas páginas com FAQ (gera resultado expandido no Google — é um dos ganhos mais baratos de visibilidade).
- `Article` com `datePublished` e `author` em cada conteúdo.
- `BreadcrumbList` nas internas.

## 8.3 Temas de conteúdo úteis

Organizados por intenção de busca, do mais comercial ao mais informativo:

**Alta intenção (quem já tem problema):**
- Como se preparar para uma visita da vigilância sanitária
- O que a vigilância costuma pedir em restaurante / em padaria
- Manual de boas práticas: o que precisa ter e quem pode elaborar
- O que é POP e quais a sua cozinha precisa ter

**Intenção média (quem quer melhorar):**
- Ficha técnica de prato: como montar e por que muda seu lucro
- Controle de temperatura: o que registrar e com que frequência
- Rotulagem de alimentos: o que mudou e o que se aplica ao seu negócio
- Como treinar manipuladores sem parar a operação
- Checklist de recebimento de mercadoria

**Por segmento (captura busca específica, alto valor):**
- Boas práticas em padaria e confeitaria: os pontos mais críticos
- Segurança dos alimentos em buffets e eventos
- Cozinha industrial: controle de cadeia fria no transporte
- Hotel: café da manhã e serviço de quarto, o que observar

**Institucional:**
- Quanto custa uma consultoria de alimentos e o que entra no preço
- O que esperar do primeiro diagnóstico

⚠️ Todo conteúdo que cite legislação, prazo ou exigência deve ser revisado tecnicamente pela Verona Food antes da publicação, e marcado com data de última revisão.

## 8.4 Linguagem clara e encontrável

- Escrever como o cliente pesquisa, não como o setor fala. Ele busca "consultoria vigilância sanitária restaurante", não "adequação às RDCs vigentes".
- Termo técnico sempre na primeira vez acompanhado de explicação curta: "POP (Procedimento Operacional Padronizado — o passo a passo escrito de cada tarefa)".
- H2 e H3 escritos como pergunta ou como frase completa, não como rótulo. "Como montar uma ficha técnica" indexa melhor que "Ficha técnica".
- Um assunto por página. Não empilhar cinco serviços num texto só.

## 8.5 Estrutura para publicar sem refazer o site

O site deve nascer com **CMS**, não como HTML estático editado por desenvolvedor. Duas opções razoáveis:

- **WordPress com tema próprio** (sem construtor visual pesado) — a Verona Food já está em WordPress, a migração de conteúdo é direta e a consultora publica sozinha. É a recomendação para este caso.
- **Site estático com CMS headless** (Astro/Next + Sanity ou similar) — mais rápido e mais seguro, exige mais do desenvolvimento inicial.

Em qualquer um, o conteúdo precisa estar modelado em **tipos**: Solução, Segmento, Conteúdo, Depoimento, FAQ. Assim, publicar um artigo novo, acrescentar um segmento ou cadastrar um depoimento é preencher um formulário, não mexer em layout.

**Migração do site atual:** mapear todas as URLs existentes e aplicar **redirecionamento 301** para as novas — principalmente `/empresa/` → `/sobre`, `/noticias/` → `/conteudos`, `/contatos/` → `/contato` e cada post para seu novo slug. Sem isso, o site perde o posicionamento que já tem. Enviar o novo sitemap no Google Search Console no dia da virada.

---

# 9. Componentes e sistema visual

Lista do que precisa ser desenhado uma vez e reutilizado. Cada item precisa de versão **desktop** e **celular**, e dos estados **repouso / hover / foco / ativo / desabilitado** quando for interativo.

### Estrutura
1. **Cabeçalho** — desktop com menu horizontal; celular com hambúrguer; variantes: topo da página (sem borda) e rolado (com borda).
2. **Painel de menu mobile** — tela cheia, com acordeões e botões fixos no rodapé.
3. **Painel de submenu desktop** — para Soluções e Segmentos.
4. **Rodapé** — quatro colunas no desktop, acordeão no celular; variante compacta para páginas de conversão.
5. **Botão flutuante de WhatsApp** — só mobile.
6. **Container e grade** — 12 colunas, 1200px, gutter 24px (16px no mobile).

### Ação
7. **Botão** — primário, secundário, terciário (link com seta), tamanhos M e G, com e sem ícone, largura total no mobile.
8. **Link de texto** — em parágrafo, em lista, com seta.
9. **Tag / pill** — segmento, categoria de artigo, credencial. Variantes clicável e estática.

### Conteúdo
10. **Card de solução** — ícone, título, texto, link; variante destaque (fundo vinho).
11. **Card de segmento** — foto, nome, duas linhas.
12. **Card de artigo** — imagem, categoria, título, data, tempo de leitura; variantes grande (destaque) e lista.
13. **Item de etapa** — número, título, texto; variantes horizontal (desktop) e vertical (mobile).
14. **Item de benefício** — ícone + título + linha; versão sobre fundo claro e sobre vinho.
15. **Bloco de depoimento** — aspas, texto, nome, cargo, estabelecimento, cidade; carrossel no mobile.
16. **Bloco de estatística** — número grande + rótulo + nota de origem.
17. **Lista de entregáveis** — checkmark verde + texto, duas colunas no desktop.
18. **Bloco de pessoa** — foto, nome, cargo, credenciais em pills, texto.
19. **Acordeão de FAQ** — `<details>` estilizado, ícone que gira, primeiro item aberto.
20. **Bloco de conteúdo de artigo** — títulos, parágrafos, listas, citação, imagem com legenda, caixa de destaque, tabela.

### Conversão
21. **Formulário curto** — cinco campos, com estados de erro, carregamento e sucesso; versão em card claro e versão sobre vinho.
22. **Campo de formulário** — texto, telefone com máscara, e-mail, seleção, área de texto, checkbox; estados repouso / foco / erro / preenchido / desabilitado.
23. **Faixa de CTA** — fundo vinho, com e sem formulário, com e sem imagem.
24. **Mensagem de sucesso e de erro** — em bloco, com ícone e texto.

### Avisos e informação técnica
25. **Caixa de nota técnica** — fundo champagne claro, filete âmbar de 3px à esquerda, ícone de informação. Para avisos do tipo "o resultado de fiscalização depende do órgão e da operação" dentro de artigos e páginas de solução. É o componente que mantém o site honesto sem quebrar o ritmo visual.
26. **Banner de cookies** — com Aceitar e Recusar de mesmo peso.
27. **Aviso de privacidade** — texto curto abaixo de formulário.
28. **Breadcrumb** — nas páginas internas.

### Gráficos
29. **Separador de folha** — a curva do símbolo como divisória entre seções, em três larguras.
30. **Família de ícones em linha** — mínimo 16 ícones (segurança, custo, treinamento, processo, consultoria, restaurante, bar, hotel, padaria, confeitaria, cozinha industrial, buffet, mercado, evento, documento, checklist).
31. **Moldura de imagem** — com cantos 12px e linha taupe; variantes retrato, paisagem e com véu vinho.

**Entrega recomendada:** biblioteca no Figma com tokens de cor, tipografia e espaçamento ligados a variáveis, e os componentes acima com *auto layout* e variantes. Isso permite que o desenvolvimento gere CSS a partir de tokens em vez de valores soltos.

---

# 10. Wireframe textual — página inicial

```
┌──────────────────────────────────────────────────────────────────────────┐
│ [logo VeronaFood]   Soluções ▾  Segmentos ▾  Como funciona  Sobre        │
│                     Conteúdos            [ Falar com a Verona Food ]     │
└──────────────────────────────────────────────────────────────────────────┘
   fixo · fundo champagne com blur · borda inferior ao rolar

┌──────────────────────────────────────────────────────────────────────────┐
│  CONSULTORIA PARA NEGÓCIOS DE ALIMENTAÇÃO                 ╭────────────╮  │
│                                                           │            │  │
│  Sua operação de alimentos                                │   FOTO     │  │
│  organizada do começo ao fim.                             │ consultoria│  │
│                                                           │  em cozinha│  │
│  Segurança dos alimentos, controle de custos,             │   real     │  │
│  padronização de processos e treinamento de equipe        │  (3:4)     │  │
│  — com um plano feito para a realidade do seu             │            │  │
│  negócio, não para o papel.                               ╰────────────╯  │
│                                                          ╱ curva folha    │
│  [ Agendar diagnóstico ]  [ ⌞ Falar no WhatsApp ]                        │
│  Atendimento de segunda a sexta, das 9h às 18h.                          │
└──────────────────────────────────────────────────────────────────────────┘
   S1 · fundo champagne · 55/45 · altura ~ 620px desktop

┌──────────────────────────────────────────────────────────────────────────┐
│          Trabalhamos com diferentes tipos de negócio de alimentação:     │
│   (Restaurantes)(Bares)(Hotéis)(Padarias)(Confeitarias)                  │
│   (Cozinhas industriais)(Buffets e eventos)(Mercados)                    │
│                      Ver todos os segmentos →                            │
└──────────────────────────────────────────────────────────────────────────┘
   S2 · fundo champagne claro · pills · centralizado

                         ╰───── separador folha ─────╯

┌──────────────────────────────────────────────────────────────────────────┐
│  O que a gente resolve                                                   │
│  Cada frente funciona sozinha ou combinada. Na dúvida, o diagnóstico     │
│  aponta por onde começar.                                                │
│                                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                    │
│  │ ◇ ícone      │  │ ◇ ícone      │  │ ◇ ícone      │                    │
│  │ Segurança    │  │ Custos e     │  │ Treinamento  │                    │
│  │ dos alimentos│  │ ficha técnica│  │ de equipe    │                    │
│  │ texto 2 lin. │  │ texto 2 lin. │  │ texto 2 lin. │                    │
│  │ Ver detalhes→│  │ Ver detalhes→│  │ Ver detalhes→│                    │
│  └──────────────┘  └──────────────┘  └──────────────┘                    │
│  ┌──────────────┐  ┌───────────────────────────────┐                     │
│  │ ◇ ícone      │  │ ◆ CONSULTORIA COMPLETA        │ ← fundo VINHO       │
│  │ Padronização │  │ Quando o negócio precisa de   │                     │
│  │ de processos │  │ tudo junto: diagnóstico,      │                     │
│  │ texto 2 lin. │  │ plano, implantação e          │                     │
│  │ Ver detalhes→│  │ acompanhamento.               │                     │
│  └──────────────┘  │ Falar sobre consultoria →     │                     │
│                    └───────────────────────────────┘                     │
└──────────────────────────────────────────────────────────────────────────┘
   S3 · fundo champagne · grade 3+2

┌──────────────────────────────────────────────────────────────────────────┐
│  Como o trabalho acontece                                                │
│  Quatro etapas. Você sabe onde está em cada uma.                         │
│                                                                          │
│   01 ───────── 02 ───────── 03 ───────── 04        ← linha curva rosé    │
│   Diagnóstico  Plano de     Implantação  Acompanha-                      │
│                ação                      mento                           │
│   texto 3 lin. texto 3 lin. texto 3 lin. texto 3 lin.                    │
│                                                                          │
│                     Ver o processo em detalhe →                          │
└──────────────────────────────────────────────────────────────────────────┘
   S4 · fundo champagne claro · timeline horizontal

┌──────────────────────────────────────────────────────────────────────────┐
│ ████████████████████  FUNDO VINHO  ██████████████████████████████████████ │
│  O que muda na sua rotina                                                │
│   ◇ Menos retrabalho      ◇ Equipe mais segura                           │
│   ◇ Custo visível         ◇ Operação pronta para fiscalização            │
└──────────────────────────────────────────────────────────────────────────┘
   S5 · fundo vinho · 2×2 · ícones âmbar

┌──────────────────────────────────────────────────────────────────────────┐
│  ╭────────────╮    Quem vai te atender                                   │
│  │   RETRATO  │    [Nome] ⚠️                                             │
│  │ responsável│    [Formação · registro · anos de atuação] ⚠️            │
│  │   (4:5)    │    (pill)(pill)(pill)                                    │
│  │            │    Texto em 1ª pessoa, 3 a 4 linhas. ⚠️                  │
│  ╰────────────╯    Conhecer a Verona Food →                              │
└──────────────────────────────────────────────────────────────────────────┘
   S6 · fundo champagne claro

┌──────────────────────────────────────────────────────────────────────────┐
│  O que você recebe                       ⚠️ substitui depoimentos        │
│   ✓ Relatório de diagnóstico    ✓ Checklists de controle                 │
│   ✓ Manual de Boas Práticas     ✓ Fichas técnicas                        │
│   ✓ POPs da sua operação        ✓ Material de treinamento                │
│                                                                          │
│   (quando houver depoimento real e autorizado, esta seção é trocada      │
│    por 3 blocos: aspas + nome + cargo + estabelecimento + cidade)        │
└──────────────────────────────────────────────────────────────────────────┘
   S7 · fundo champagne

                         ╰───── separador folha ─────╯

┌──────────────────────────────────────────────────────────────────────────┐
│  Para ler antes de contratar qualquer consultoria                        │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐                               │
│  │  imagem   │ │  imagem   │ │  imagem   │                               │
│  │ CATEGORIA │ │ CATEGORIA │ │ CATEGORIA │                               │
│  │ Título do │ │ Título do │ │ Título do │                               │
│  │ artigo    │ │ artigo    │ │ artigo    │                               │
│  │ data·5min │ │ data·4min │ │ data·6min │                               │
│  └───────────┘ └───────────┘ └───────────┘                               │
│                   Ver todos os conteúdos →                               │
└──────────────────────────────────────────────────────────────────────────┘
   S8 · fundo champagne claro

┌──────────────────────────────────────────────────────────────────────────┐
│  Perguntas que a gente ouve sempre                                       │
│  ▾ Meu negócio é pequeno. Vale a pena contratar consultoria?             │
│     resposta aberta por padrão...                                        │
│  ▸ Quanto tempo leva para adequar minha operação?                        │
│  ▸ O trabalho é presencial ou a distância?                               │
│  ▸ Quanto custa?                                                         │
│  ▸ Vocês atendem fora de São Paulo?                                      │
│  ▸ O que eu preciso ter em mãos para começar?                            │
└──────────────────────────────────────────────────────────────────────────┘
   S9 · fundo champagne · coluna única de 760px centralizada

┌──────────────────────────────────────────────────────────────────────────┐
│ ████████████████████  FUNDO VINHO  ██████████████████████████████████████ │
│  Vamos começar pelo           ┌────────────────────────────┐             │
│  diagnóstico.                 │ Nome*                      │             │
│                               │ [___________________]      │             │
│  Conte em duas linhas como    │ WhatsApp ou telefone*      │             │
│  está sua operação hoje.      │ [___________________]      │             │
│  A gente responde com o       │ E-mail                     │             │
│  próximo passo — sem          │ [___________________]      │             │
│  compromisso e sem proposta   │ Tipo de negócio*           │             │
│  genérica.                    │ [ selecionar          ▾]   │             │
│                               │ Como podemos ajudar        │             │
│  Prefere conversar agora?     │ [___________________]      │             │
│  Chamar no WhatsApp →         │ ☐ Quero receber conteúdos  │             │
│  (11) 2362-6207               │ [   Enviar mensagem    ]   │             │
│                               │ aviso de privacidade·LGPD  │             │
│                               └────────────────────────────┘             │
└──────────────────────────────────────────────────────────────────────────┘
   S10 · fundo vinho · card champagne claro

┌──────────────────────────────────────────────────────────────────────────┐
│ ███ FUNDO VINHO ████████████████████████████████████████████████████████ │
│  [logo cream]        SOLUÇÕES        INSTITUCIONAL      CONTATO          │
│  Processo claro,     Segurança       Sobre              WhatsApp         │
│  equipe treinada,    Custos          Como funciona      Telefone         │
│  operação sob        Treinamento     Segmentos          E-mail ⚠️        │
│  controle.           Padronização    Conteúdos          Endereço         │
│  [Instagram]         Completa        Contato            Seg–sex 9h–18h   │
│ ───────────────────────────────────────────────────────────────────────  │
│  © 2026 VeronaFood Consultoria de Alimentos · CNPJ ⚠️ ·                  │
│  Política de Privacidade · Termos de Uso                                 │
└──────────────────────────────────────────────────────────────────────────┘
   S11 · fundo vinho · 4 colunas → acordeão no mobile

[ botão flutuante WhatsApp — só mobile, canto inferior direito ]
```

### Ordem no celular (mesma sequência, uma coluna)

```
Cabeçalho (logo + ☰)
S1  chapéu · H1 · subtítulo · [Agendar diagnóstico] · [WhatsApp] · foto 4:3
S2  pills em 2–3 linhas · link
S3  5 cards empilhados (completa por último, fundo vinho)
S4  timeline vertical com filete rosé
S5  benefícios 1 coluna sobre vinho
S6  foto 4:3 · nome · pills · texto
S7  entregáveis em 1 coluna
S8  2 cards de artigo + link
S9  FAQ em acordeão
S10 texto · formulário em largura total · padding-bottom 96px
S11 rodapé em acordeão
    botão flutuante de WhatsApp
```

---

# 11. Critérios de avaliação — como esta proposta responde

| Critério | Como é atendido | Onde |
|---|---|---|
| **Explicar rápido o que faz e para quem** | H1 nomeia a atividade ("operação de alimentos organizada"), subtítulo lista as quatro frentes, e a faixa de pills logo abaixo nomeia oito tipos de negócio. Tudo visível na primeira rolagem. | §4 S1, S2 |
| **Organizar os serviços sem confundir** | Cinco cards com uma linha cada, e a consultoria completa destacada como oferta principal. Detalhe fica nas páginas de solução, com template fixo "para quem é / o que você recebe / como funciona". | §4 S3, §5.2 |
| **Credibilidade sem afirmação vaga** | Substitui adjetivo por entregável concreto ("o que você recebe"), coloca rosto e credenciais na home, explica o processo em quatro etapas e declara o que acontece depois do contato. Nenhum número, selo, depoimento ou certificação inventado. | §4 S6, S7, §5.4 |
| **Contato fácil em todas as páginas** | Botão no cabeçalho em todo lugar, WhatsApp flutuante no celular, formulário de cinco campos na home e em `/contato`, e CTA no fim de toda página, inclusive artigos. Dois canais apenas. | §6 |
| **Funcionar bem no celular** | Mobile-first em cada seção: ordem definida, botões em largura total, timeline vertical, alvos de 44px, campos de 52px e 16px, safe-area respeitada e navegação em painel com armadilha de foco. | §4 (cada seção), §7 |
| **Premium e acolhedor ao mesmo tempo** | Serifa só nos títulos, vinho em 12% da superfície, espaço vertical generoso, linguagem de cozinha em primeira pessoa e rosto na home. Sem superlativo, sem banco de imagens genérico. | §2.5 |
| **Separar fato de sugestão** | Todo item marcado ✅ ou ⚠️ ao longo do documento; a lista consolidada do que falta confirmar está logo abaixo. | este documento inteiro |

## O que precisa ser confirmado antes de publicar

| # | Item | Por quê |
|---|---|---|
| 1 | Nome completo, formação, registro profissional e anos de atuação da responsável técnica | A seção "Quem vai te atender" é o principal elemento de credibilidade da home e não pode ir ao ar com texto genérico |
| 2 | Existe mais alguém na equipe? | Define se o site fala em "eu" ou "nós" e se há página de equipe |
| 3 | **CNPJ** | Esperado de prestador B2B; hoje não aparece no site |
| 4 | **E-mail institucional** | Hoje não existe e-mail visível no site; é necessário para o formulário e para o rodapé |
| 5 | Região de atendimento (só São Paulo capital? Grande SP? interior? outros estados?) | Define as páginas de segmento, o texto do FAQ e o SEO local |
| 6 | Há atendimento remoto? | Pergunta frequente que muda o alcance comercial do site |
| 7 | Prazo real de resposta a um contato | Só publicar "1 dia útil" se for sempre cumprido |
| 8 | Depoimentos com autorização escrita de uso (nome, cargo, estabelecimento) | Sem autorização, a seção não vai ao ar |
| 9 | Números verificáveis (clientes atendidos, treinamentos realizados, período de apuração) | Sem origem documentada, não entram no site |
| 10 | Logotipos de clientes com autorização de uso de marca | Idem |
| 11 | Certificações, cursos e credenciais citáveis nominalmente | Prova técnica real vale mais que qualquer texto |
| 12 | Redes sociais além do Instagram | Rodapé |
| 13 | Produção de fotografia própria (consultoria, treinamento, documentação, detalhes, retrato) | É o maior investimento de conteúdo e o que mais afasta o site do visual de banco de imagens |
| 14 | Aprovação da paleta ampliada — tinta, âmbar e neutros funcionais | A paleta da marca tem cinco cores; um site precisa de texto, bordas, erro e sucesso |
| 15 | Escolha tipográfica: Fraunces (recomendada) ou Montserrat (aderente ao guia) | Define a personalidade do site |
| 16 | Revisão jurídica da Política de Privacidade e dos Termos | Responsabilidade da empresa |
| 17 | Revisão técnica de todo texto que cite legislação ou exigência sanitária | Risco de informação desatualizada |
| 18 | Lista completa das URLs atuais para mapa de redirecionamento 301 | Sem isso, perde-se o posicionamento já conquistado |

---

# Resumo — a direção para aprovar

**Visual.** Fundo champagne com vinho usado em pontos (12% da superfície), títulos em serifa de terminais suaves, corpo em Inter, cards de borda fina sem sombra, cantos de 12px, 96px de respiro entre seções e a curva da folha do símbolo como assinatura gráfica recorrente. Fotografia real de operação, treinamento e documentação — nunca banco de imagens. Elegância pelo espaço e pelo ritmo, proximidade pela linguagem e pelo rosto na home.

**Estrutura.** Sete páginas principais — Início, Soluções (com cinco filhas), Segmentos, Como funciona, Sobre, Conteúdos e Contato. Home em onze seções, do hero ao rodapé, cada uma respondendo a uma pergunta real do visitante e levando ao mesmo par de ações: **Agendar diagnóstico** e **Falar no WhatsApp**. Páginas de solução em template fixo, para que uma frente nova entre no site sem redesenho.

**Conversão.** Dois canais, sempre os mesmos. Formulário de cinco campos, aviso de LGPD, consentimento de marketing separado e opcional, e um bloco de "o que acontece depois" que tira o medo do primeiro contato.

**Honestidade.** Nenhum número, depoimento, selo ou garantia entra no ar sem origem verificável. Onde falta material real, a proposta oferece substituto honesto — "o que você recebe" no lugar de depoimentos, entregáveis concretos no lugar de adjetivos.

**Próximo passo após a aprovação:** fechar os 18 itens da lista acima, produzir a sessão de fotos, escrever os textos finais das cinco páginas de solução e montar a biblioteca de componentes no Figma. Só então começa o desenvolvimento.
