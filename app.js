let bttn_sobre = document.querySelector('.sobre');
let sobre = document.querySelectorAll('.home > div:not(.logo)');
let logo = document.querySelector('.logo');


bttn_sobre.onclick = function() {
    for (let item of sobre) {
    item.style.display = 'none';
    }
    logo.style.gridColumnEnd = 7;
    logo.style.gridRowEnd = 7;
}