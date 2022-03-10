function CambioLetra() {
   $(document).ready(function(){
    let TipoLetra = document.getElementById("TipoLetra").value;
    let body = document.getElementById("texto")
    if (body.style.fontFamily = TipoLetra){
        body.style.fontFamily = TipoLetra
        body = body.style.fontFamily = TipoLetra 
        console.log(body)
    }
   })
}
