function CambioLetra() {
   $(document).ready(function(){
    let TipoLetra = document.querySelector("#TipoLetra").value;
    let body = document.querySelectorAll("#text")[0];
    if (body.style.fontFamily = TipoLetra){
        body.style.fontFamily = TipoLetra
        body = body.style.fontFamily = TipoLetra 
        console.log(body)
    }
   })
}   
