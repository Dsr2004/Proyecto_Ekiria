function CambioLetra() {
    $(document).ready(function() {
        let TipoLetra = document.querySelector("#TipoLetra").value;
        let body = document.querySelectorAll(".tipo");
        body.forEach(texto => {
            if (texto.style.fontFamily = TipoLetra) {
                texto.style.fontFamily = TipoLetra
                texto = texto.style.fontFamily = TipoLetra
                console.log(texto)
            }
        });
    })
}
function ColorLetra(event) {
    const codigo = event.which || event.keyCode;
    if(codigo === 13){
        $(document).ready(function(){
            let ColorLetra = document.querySelector("#ColorLetra").value;
            let texto = document.querySelectorAll(".tipo");
            texto.forEach(textos =>{
                if (textos.style.color = ColorLetra) {
                    textos.style.color = ColorLetra
                    textos = textos.style.color = ColorLetra 
                }
            });
            
        });
    }  
}



function ColorFondo(event) {
    const codigo = event.which || event.keyCode;
    if(codigo === 13){
        let ColorFondo = document.getElementById("ColorFondo").value;
        let body = document.getElementById("texto");
        body.style.backgroundColor = ColorFondo;
    }
    
}

function CambiarTamano(event) {
    const codigo = event.which || event.keyCode;
    if(codigo === 13){
        $(document).ready(function(){
            let TamanoLetra = document.querySelector("#TamanoLetra").value;
            let tamano = document.querySelectorAll("#text");
            tamano.forEach(tamanos =>{
                if (tamanos.style.fontSize = TamanoLetra) {
                    tamanos.style.fontSize = TamanoLetra+("px")
                    tamanos = tamanos.style.fontSize = TamanoLetra+("px") 
                }
            });
            
        });
    }  
}
function CambiarTamano2(event) {
    const codigo = event.which || event.keyCode;
    if(codigo === 13){
        $(document).ready(function(){
            let TamanoLetra2 = document.querySelector("#TamanoLetra2").value;
            let tamano2 = document.querySelectorAll("#text2");
            tamano2.forEach(tamanos2 =>{
                if (tamanos2.style.fontSize = TamanoLetra2) {
                    tamanos2.style.fontSize = TamanoLetra2+("px")
                    tamanos2 = tamanos2.style.fontSize = TamanoLetra2+("px") 
                }
            });
            
        });
    }  
}
