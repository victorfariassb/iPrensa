let bttn_sobre = document.querySelector('.bttn-sobre');
let bttn_voltar = document.querySelector('.bttn-voltar');
let main = document.querySelectorAll('.home > div:not(.logo)');
let home = document.querySelector('.home')
let intro = document.querySelector('.intro')
let logo = document.querySelector('.logo');
let sobre = document.querySelector('.sobre')

// página se transforma de modo a apagar dados das outras editorias e mostrar apenas o sobre
bttn_sobre.onclick = function () {
    for (let item of main) {
        item.style.display = 'none';
    }
    home.style.display = 'inline-block';
    logo.style.display = 'flex';

    intro.style.borderRight = '2px solid #000326'
    bttn_sobre.style.display = 'none';
    bttn_voltar.style.display = 'inline-block';
    sobre.style.display = 'block';
    logo.style.flexDirection = 'row';
}

// aqui criamos o mecanismo para voltar à página inicial
bttn_voltar.onclick = function () {
    window.location.reload();
}