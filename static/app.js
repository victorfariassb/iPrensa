let bttn_sobre = document.querySelector('.bttn-sobre');
let bttn_voltar = document.querySelector('.bttn-voltar');
let main = document.querySelectorAll('.home > div:not(.logo)');
let home = document.querySelector('.home');
let intro = document.querySelector('.intro');
let logo = document.querySelector('.logo');
let sobre = document.querySelector('.sobre');


let esporte = document.querySelector('.esporte');
let explicacao_esporte = document.querySelector('.esporte p:first-of-type')
let palavra_dia = document.querySelector('.palavra_dia')
let explicacao_palavra_dia= document.querySelector('.palavra_dia p:first-of-type')
let candidatos = document.querySelector('.candidatos')
let explicacao_candidatos = document.querySelector('.candidatos p:first-of-type')
let numero_materias = document.querySelector('.numero_materias')
let explicacao_numero_materias = document.querySelector('.numero_materias p:first-of-type')

// página se transforma de modo a apagar dados das outras editorias e mostrar apenas o sobre
bttn_sobre.onclick = function () {
    for (let item of main) {
        item.style.display = 'none';
    }
    home.style.display = 'inline-block';
    home.style.padding = '0'
    intro.style.height = '100%';

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

esporte.onmouseover = function() {
    let filhos = document.querySelectorAll('.esporte *')
    for (let filho of filhos) {
        filho.style.display = 'none'}
    esporte.style.backgroundColor = '#D93B18';
    explicacao_esporte.style.display = 'inline-block';
}

esporte.onmouseout = function() {
    let filhos = document.querySelectorAll('.esporte *')
    for (let filho of filhos) {
        filho.style.display = 'inline-block'}
    esporte.style.backgroundColor = '#000326';
    explicacao_esporte.style.display = 'none';
}


palavra_dia.onmouseover = function() {
    let filhos = document.querySelectorAll('.palavra_dia *')
    for (let filho of filhos) {
        filho.style.display = 'none'}
    palavra_dia.style.backgroundColor = '#000326';
    explicacao_palavra_dia.style.display = 'inline-block';
}

palavra_dia.onmouseout = function() {
    let filhos = document.querySelectorAll('.palavra_dia *')
    for (let filho of filhos) {
        filho.style.display = 'inline-block'}
    palavra_dia.style.backgroundColor = '#D93B18';
    explicacao_palavra_dia.style.display = 'none';
}

candidatos.onmouseover = function() {
    let filhos = document.querySelectorAll('.candidatos *')
    for (let filho of filhos) {
        filho.style.display = 'none'}
    candidatos.style.backgroundColor = '#000326';
    explicacao_candidatos.style.display = 'inline-block';
}

candidatos.onmouseout = function() {
    let filhos = document.querySelectorAll('.candidatos *')
    for (let filho of filhos) {
        filho.style.display = 'inline-block'}
    candidatos.style.backgroundColor = '#D93B18';
    explicacao_candidatos.style.display = 'none';
}

numero_materias.onmouseover = function() {
    let filhos = document.querySelectorAll('.numero_materias *')
    for (let filho of filhos) {
        filho.style.display = 'none'}
    numero_materias.style.backgroundColor = '#000326';
    explicacao_numero_materias.style.display = 'inline-block';
}

numero_materias.onmouseout = function() {
    let filhos = document.querySelectorAll('.numero_materias *')
    for (let filho of filhos) {
        filho.style.display = 'inline-block'}
    numero_materias.style.backgroundColor = '#D93B18';
    explicacao_numero_materias.style.display = 'none';
}
