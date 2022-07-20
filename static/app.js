let main = document.querySelectorAll('.home > div:not(.logo)');
let home = document.querySelector('.home');
let intro = document.querySelector('.intro');


let esporte = document.querySelector('.esporte');
let explicacao_esporte = document.querySelector('.esporte p:first-of-type')
let titulo_esportes = document.querySelector('.esporte .titulo')

let logo = document.querySelector('.logo');
let sobre = document.querySelector('.sobre');
let palavra_dia = document.querySelector('.palavra_dia')
let explicacao_palavra_dia= document.querySelector('.palavra_dia p:first-of-type')
let candidatos = document.querySelector('.candidatos')
let explicacao_candidatos = document.querySelector('.candidatos p:first-of-type')
let numero_materias = document.querySelector('.numero_materias')
let explicacao_numero_materias = document.querySelector('.numero_materias p:first-of-type')

// funções para mudar o texto e o fundo quando mouseover nas boxes

logo.onmouseover = function() {
    intro.style.display = 'none'
    logo.style.backgroundColor = '#000326';
    sobre.style.display = 'inline-block';
}

logo.onmouseout = function() {
    intro.style.display = 'flex'
    logo.style.backgroundColor = '#F29F80';
    sobre.style.display = 'none';
}


esporte.onmouseover = function() {
    let lista_esportes = document.querySelectorAll('.esporte li')
    let ol = document.querySelector('.esporte ol')
    for (let item of lista_esportes) {
        item.style.display = 'none';
    }
    ol.style.display = 'none';
    explicacao_esporte.style.display = 'inline-block';
}

esporte.onmouseout = function() {
    let lista_esportes = document.querySelectorAll('.esporte li')
    let ol = document.querySelector('.esporte ol')
    for (let item of lista_esportes) {
        item.style.display = 'list-item';
    }
    ol.style.display = 'block'
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
    let lista_candidatos = document.querySelectorAll('.candidatos li')
    let chart = document.querySelector('#bar-chart')
    for (let item of lista_candidatos) {
        item.style.display = 'none';
    }
    chart.style.display = 'none'
    candidatos.style.backgroundColor = '#000326';
    explicacao_candidatos.style.display = 'inline-block';
}

candidatos.onmouseout = function() {
    let lista_candidatos = document.querySelectorAll('.candidatos li')
    let chart = document.querySelector('#bar-chart')
    for (let item of lista_candidatos) {
        item.style.display = 'list-item';
    }
    chart.style.display = 'block'
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
