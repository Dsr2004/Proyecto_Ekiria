/*          Selector de lista           */
let list = document.querySelectorAll('.list');
for (let i = 0; i < list.length; i++) {
    list[i].onclick = function() {
        let j = 0;
        while (j < list.length) {
            list[j++].className = 'list';
        }
        list[i].className = 'list activar';
    }
}
/* Caja tipo togger encargada de desplegar el menú lateral */
let menuToggle = document.querySelector('.toggle');
let content = document.querySelector('.content');
var nav = document.querySelector('.nav');
var img = document.querySelector('.Logo');
var menu = document.querySelector('.menu');
menuToggle.onclick = function() {
        menuToggle.classList.toggle('activar');
        nav.classList.toggle('activar');
        content.classList.toggle('activar');
        img.classList.toggle('activar');
        menu.classList.toggle('activar');
    }
    /**  Transformador scrollbar por tamaño de lista */
window.onload = function() {
    let listas = document.getElementsByClassName("list");
    if (listas.length < 11) {
        nav.classList.add('notscrollbar')
    }
};