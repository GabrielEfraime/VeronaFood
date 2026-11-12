# Site da VeronaFood

Site estático, 21 páginas, sem framework e sem `npm install`. Só Python 3.9 ou mais novo.

```bash
cd site
python build.py             # gera tudo em site/dist/
python build.py --servir    # gera e abre em http://localhost:8000
```

O build imprime, no fim, **o que ainda falta preencher** e um aviso se algum link interno estiver quebrado.

---

## O que mexer

Quase tudo o que muda no dia a dia está em **`src/config.py`**: contato, endereço, horário, dados da responsável técnica, depoimentos, endpoint do formulário. Nenhum desses valores está escrito dentro do HTML.

```
site/
├── build.py              roda o gerador
├── src/
│   ├── config.py         ← contato, equipe, provas, formulário  (comece aqui)
│   ├── layout.py         cabeçalho, rodapé, componentes, SEO
│   ├── pg_home.py        página inicial
│   ├── pg_solucoes.py    hub + 6 páginas de solução
│   ├── pg_segmentos.py   hub + 6 páginas de segmento
│   └── pg_institucional.py  como funciona, sobre, conteúdos, contato, legais
├── assets/
│   ├── css/site.css      o sistema visual inteiro
│   ├── js/site.js        menu, FAQ, formulário, WhatsApp
│   └── img/              coloque aqui as fotos (ver abaixo)
└── dist/                 SAÍDA — é esta pasta que vai para o ar
```

`dist/` é apagada e recriada a cada build. Nunca edite nada lá dentro.

---

## Os campos que ainda faltam

O site foi construído para funcionar **sem inventar nada**. Os campos em branco no `config.py` não geram texto de mentira: a seção some, ou o texto se adapta.

| Campo | O que muda quando preencher |
|---|---|
| `FORMULARIO['endpoint']` | **O formulário passa a enviar de verdade.** Hoje ele valida e mostra a confirmação, mas não manda nada para lugar nenhum. |
| `COMERCIAL['diagnostico']` | Com `"gratuito"`, o botão principal de todo o site vira "Agendar diagnóstico gratuito". |
| `CONTATO['prazo_resposta']` | Aparece no hero, no formulário e em "o que acontece depois". Só preencha se for sempre cumprido. |
| `CONTATO['email']` | Entra no rodapé, na página de contato e nos dados estruturados. |
| `CONTATO['cnpj']` | Entra no rodapé. |
| `COMERCIAL['regiao_atendimento']` | **Cria a seção "Onde eu atendo"** na página Sobre. Sem isso ela não existe — melhor que a seção vazia do site atual. |
| `EQUIPE[0]['credenciais']`, `['bio']`, `['foto']` | Preenchem o bloco "Quem vai te atender", na home e na página Sobre. |
| `DEPOIMENTOS` | **Trocam a seção "O que você recebe" por depoimentos** na home. Enquanto estiver vazia, a home usa os entregáveis — que é a alternativa honesta. |

### Formulário: como ligar o envio

Qualquer serviço que aceite `POST` de formulário serve, sem precisar de servidor próprio. Formspree, Basin, Web3Forms e Netlify Forms funcionam. Pegue a URL que o serviço fornecer e cole:

```python
FORMULARIO = {"endpoint": "https://formspree.io/f/xxxxxxxx", ...}
```

Rode `python build.py` de novo e pronto. Enquanto estiver `None`, o navegador avisa no console e o build avisa no terminal.

---

## Fotos

Coloque os arquivos em `assets/img/` e aponte no conteúdo. Onde ainda não há foto, o site mostra uma moldura com a descrição do que deve entrar ali — nada quebra, e fica visível o que falta produzir.

Formato: JPG ou WebP, 1600px no maior lado, até 300 KB. As proporções usadas são 3:4 (hero), 3:2 (etapas e artigos) e 4:5 (retrato).

Para o retrato da responsável, basta `EQUIPE[0]["foto"] = "img/barbara.jpg"`.

---

## Publicar

A pasta `dist/` é um site estático comum. Funciona em qualquer lugar:

- **Netlify ou Vercel** — arraste a pasta `dist/`. O arquivo `_redirects` já vai junto e cuida das URLs antigas.
- **Cloudflare Pages** — mesma coisa.
- **Hospedagem atual** — suba o conteúdo de `dist/` na raiz. Aí os redirecionamentos precisam ser recriados em `.htaccess` ou no painel, porque `_redirects` é específico de Netlify.

### Antes de virar a chave

1. Confira o `_redirects`: ele leva `/empresa/` para `/sobre/`, `/noticias/` para `/conteudos/`, `/contatos/` para `/contato/` e os posts antigos para `/conteudos/`. **Sem isso o site perde o posicionamento que já tem no Google.**
2. Envie `sitemap.xml` no Google Search Console.
3. Confirme que o formulário chega onde deve — mande um teste.
4. Troque `SITE['url']` se o domínio for diferente.

---

## O que já está pronto

- 21 páginas: home, 7 de soluções, 7 de segmentos, como funciona, sobre, conteúdos, contato, privacidade e termos.
- Menu com painéis no desktop e painel de tela cheia no celular, com foco preso e `Esc` para fechar.
- Botão de WhatsApp flutuante que some quando o formulário final aparece, para não cobrir o envio.
- Mensagem de WhatsApp diferente por página, para a consultora já receber o contexto.
- Formulário de cinco campos com validação em português, máscara de telefone e confirmação na própria página.
- FAQ em `<details>` nativo — funciona por teclado mesmo sem JavaScript.
- Dados estruturados: `ProfessionalService` em todas as páginas, `BreadcrumbList` nas internas e `FAQPage` onde há perguntas.
- `sitemap.xml`, `robots.txt`, `site.webmanifest`, favicon e ícones do pacote de identidade.
- Acessibilidade: foco visível, link para pular ao conteúdo, hierarquia de títulos, `alt` em tudo, alvos de toque de 44px e respeito a `prefers-reduced-motion`.
- Impressão: as páginas saem limpas em PDF.

## O que não está pronto

- **Os artigos.** `/conteudos/` lista os quatro textos do site atual como "em revisão técnica", sem link. Eles precisam ser revisados antes de voltar ao ar — e aí ganham página própria.
- **As fotos.** Todas as imagens são molduras com a descrição do que entra ali.
- **O envio do formulário.** Depende do endpoint.
- **As pendências do `config.py`**, listadas pelo build.

---

## Se o site for para WordPress

A proposta recomendava WordPress, porque a Verona Food já está nele e assim a consultora publica sozinha. Este site estático não impede isso: o `site.css` e o `site.js` vão inteiros para o tema, e os componentes do `layout.py` viram os templates. O conteúdo dos arquivos `pg_*.py` vira o conteúdo das páginas no painel.

Vale decidir isso antes de produzir as fotos, porque o corte das imagens é o mesmo nos dois caminhos.
