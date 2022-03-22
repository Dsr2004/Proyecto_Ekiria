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

function presionaEnter(event) {

    const key = event.key; 
    console.log("Presionada: " + key);
    
}