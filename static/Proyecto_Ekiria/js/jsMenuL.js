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
list.forEach(listElement => {
        listElement.addEventListener('click', () => {
            listElement.className = "list activar"
            let height = 0;
            let menu = listElement.nextElementSibling;
            if (menu.clientHeight == "0") {
                height = menu.scrollHeight;
                listElement.classList.toggle('arrow');
                let list = document.querySelectorAll(".list_show")
                for (let i = 0; i < list.length; i++) {
                    list[i].style.height = 0;
                }
            }
            menu.style.height = height + "px";
        })
    })
    /* Caja tipo togger encargada de desplegar el menú lateral */
let menuToggle = document.querySelector('.toggle');
let content = document.querySelector('.content');
var nav = document.querySelector('.nav');
var grid = document.querySelector('.grid');
var img = document.querySelector('.Logo');
var menu = document.querySelector('.menus');
menuToggle.onclick = function() {
        menuToggle.classList.toggle('activar');
        nav.classList.toggle('activar');
        content.classList.toggle('activar');
        grid.classList.toggle('activar');
        menu.classList.toggle('activar');
        img.classList.toggle('activar');
    }
    /**  Transformador scrollbar por tamaño de lista */

/** Submenu */