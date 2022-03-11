function CambioLetra() {
    $(document).ready(function() {
        let TipoLetra = document.querySelector("#TipoLetra").value;
        let body = document.querySelectorAll("#text");
        body.forEach(texto => {
            if (texto.style.fontFamily = TipoLetra) {
                texto.style.fontFamily = TipoLetra
                texto = texto.style.fontFamily = TipoLetra
                console.log(texto)
            }
        });
    })
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