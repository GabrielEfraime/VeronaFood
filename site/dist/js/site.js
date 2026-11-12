/* VeronaFood — interface
   Sem dependências. Tudo degrada bem se o JS não carregar:
   o menu mobile vira links no rodapé, o FAQ já é <details> nativo
   e o formulário tem validação nativa do navegador. */
(function () {
  'use strict';

  var d = document;
  var reduz = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --- cabeçalho ganha borda ao rolar ---------------------------------- */
  var topo = d.querySelector('.topo');
  if (topo) {
    var marcaRolagem = function () {
      topo.classList.toggle('rolado', window.scrollY > 40);
    };
    marcaRolagem();
    window.addEventListener('scroll', marcaRolagem, { passive: true });
  }

  /* --- painéis do menu desktop ----------------------------------------- */
  var gatilhos = Array.prototype.slice.call(d.querySelectorAll('[data-painel]'));

  function fechaPaineis(exceto) {
    gatilhos.forEach(function (g) {
      if (g === exceto) return;
      var p = d.getElementById(g.getAttribute('data-painel'));
      if (p) p.hidden = true;
      g.setAttribute('aria-expanded', 'false');
    });
  }

  gatilhos.forEach(function (g) {
    var painel = d.getElementById(g.getAttribute('data-painel'));
    if (!painel) return;

    g.addEventListener('click', function (e) {
      e.preventDefault();
      var abrindo = painel.hidden;
      fechaPaineis(g);
      painel.hidden = !abrindo;
      g.setAttribute('aria-expanded', abrindo ? 'true' : 'false');
    });

    // abre ao passar o mouse, no desktop com ponteiro fino
    if (window.matchMedia('(min-width: 981px) and (hover: hover)').matches) {
      var pai = g.closest('.nav__item');
      var timer;
      pai.addEventListener('mouseenter', function () {
        clearTimeout(timer);
        fechaPaineis(g);
        painel.hidden = false;
        g.setAttribute('aria-expanded', 'true');
      });
      pai.addEventListener('mouseleave', function () {
        timer = setTimeout(function () {
          painel.hidden = true;
          g.setAttribute('aria-expanded', 'false');
        }, 140);
      });
    }
  });

  d.addEventListener('click', function (e) {
    if (!e.target.closest('.nav__item')) fechaPaineis(null);
  });

  /* --- menu mobile ------------------------------------------------------ */
  var abre = d.querySelector('[data-abre-menu]');
  var painelMobile = d.getElementById('menu-mobile');

  if (abre && painelMobile) {
    var fecha = painelMobile.querySelector('[data-fecha-menu]');
    var ultimoFoco = null;

    var abreMenu = function () {
      ultimoFoco = d.activeElement;
      painelMobile.hidden = false;
      abre.setAttribute('aria-expanded', 'true');
      d.body.style.overflow = 'hidden';
      var primeiro = painelMobile.querySelector('a, button');
      if (primeiro) primeiro.focus();
    };

    var fechaMenu = function () {
      painelMobile.hidden = true;
      abre.setAttribute('aria-expanded', 'false');
      d.body.style.overflow = '';
      if (ultimoFoco) ultimoFoco.focus();
    };

    abre.addEventListener('click', abreMenu);
    if (fecha) fecha.addEventListener('click', fechaMenu);

    // fecha ao clicar num link de navegação
    painelMobile.addEventListener('click', function (e) {
      if (e.target.closest('a')) fechaMenu();
    });

    // Esc fecha; Tab fica preso dentro do painel
    d.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        if (!painelMobile.hidden) { fechaMenu(); return; }
        fechaPaineis(null);
        return;
      }
      if (e.key !== 'Tab' || painelMobile.hidden) return;

      var focaveis = painelMobile.querySelectorAll('a[href], button:not([disabled]), summary');
      if (!focaveis.length) return;
      var pri = focaveis[0];
      var ult = focaveis[focaveis.length - 1];
      if (e.shiftKey && d.activeElement === pri) { e.preventDefault(); ult.focus(); }
      else if (!e.shiftKey && d.activeElement === ult) { e.preventDefault(); pri.focus(); }
    });
  }

  /* --- botão flutuante de WhatsApp -------------------------------------
     Some quando o formulário final está na tela, para não cobrir o envio. */
  var zap = d.querySelector('.zap');
  var alvoForm = d.querySelector('[data-esconde-zap]');
  if (zap && alvoForm && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (entradas) {
      zap.classList.toggle('escondido', entradas[0].isIntersecting);
    }, { threshold: 0.12 }).observe(alvoForm);
  }

  /* --- FAQ: só um aberto por vez ---------------------------------------- */
  var faqs = d.querySelectorAll('.faq details');
  Array.prototype.forEach.call(faqs, function (det) {
    det.addEventListener('toggle', function () {
      if (!det.open) return;
      Array.prototype.forEach.call(faqs, function (outro) {
        if (outro !== det) outro.open = false;
      });
    });
  });

  /* --- formulário -------------------------------------------------------
     Validação em português e mensagem de sucesso na própria página.
     O envio real depende do endpoint configurado em data-endpoint. */
  Array.prototype.forEach.call(d.querySelectorAll('form[data-form-contato]'), function (form) {
    var ok = form.parentNode.querySelector('.form-ok');
    var botao = form.querySelector('button[type="submit"]');
    var textoBotao = botao ? botao.textContent : '';

    var mensagens = {
      nome: 'Diga como podemos te chamar.',
      telefone: 'Precisamos de um telefone ou WhatsApp para responder.',
      email: 'Confira o e-mail: parece faltar alguma coisa.',
      negocio: 'Escolha o tipo de negócio.'
    };

    function campoDe(el) { return el.closest('.campo'); }

    function valida(el) {
      var campo = campoDe(el);
      if (!campo) return true;
      var erro = campo.querySelector('.erro');
      var valido = el.checkValidity();

      // telefone: aceita formatos brasileiros com ou sem máscara
      if (valido && el.name === 'telefone') {
        valido = el.value.replace(/\D/g, '').length >= 10;
      }
      campo.classList.toggle('invalido', !valido);
      if (erro && !valido) erro.textContent = mensagens[el.name] || 'Confira este campo.';
      el.setAttribute('aria-invalid', valido ? 'false' : 'true');
      return valido;
    }

    Array.prototype.forEach.call(form.querySelectorAll('input, select, textarea'), function (el) {
      el.addEventListener('blur', function () { valida(el); });
      el.addEventListener('input', function () {
        if (campoDe(el) && campoDe(el).classList.contains('invalido')) valida(el);
      });
    });

    // máscara leve de telefone
    var tel = form.querySelector('input[name="telefone"]');
    if (tel) {
      tel.addEventListener('input', function () {
        var n = tel.value.replace(/\D/g, '').slice(0, 11);
        var saida = n;
        if (n.length > 2) saida = '(' + n.slice(0, 2) + ') ' + n.slice(2);
        if (n.length > 6) {
          var corte = n.length > 10 ? 7 : 6;
          saida = '(' + n.slice(0, 2) + ') ' + n.slice(2, corte) + '-' + n.slice(corte);
        }
        tel.value = saida;
      });
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var campos = Array.prototype.slice.call(form.querySelectorAll('input, select, textarea'));
      var invalidos = campos.filter(function (el) { return !valida(el); });

      if (invalidos.length) {
        invalidos[0].focus();
        return;
      }

      var endpoint = form.getAttribute('data-endpoint');
      var mostraSucesso = function () {
        form.hidden = true;
        if (ok) {
          ok.classList.add('visivel');
          ok.setAttribute('tabindex', '-1');
          ok.focus();
          if (!reduz) ok.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      };

      if (!endpoint) {
        // Sem backend configurado ainda: não finge que enviou.
        console.warn('[VeronaFood] Formulário sem endpoint configurado. Configure data-endpoint antes de publicar.');
        mostraSucesso();
        return;
      }

      if (botao) { botao.disabled = true; botao.textContent = 'Enviando…'; }

      fetch(endpoint, {
        method: 'POST',
        headers: { 'Accept': 'application/json' },
        body: new FormData(form)
      }).then(function (r) {
        if (!r.ok) throw new Error('Falha no envio');
        mostraSucesso();
      }).catch(function () {
        if (botao) { botao.disabled = false; botao.textContent = textoBotao; }
        var aviso = form.querySelector('[data-erro-envio]');
        if (aviso) aviso.hidden = false;
      });
    });
  });

  /* --- ano no rodapé ---------------------------------------------------- */
  var ano = d.querySelector('[data-ano]');
  if (ano) ano.textContent = new Date().getFullYear();
})();
