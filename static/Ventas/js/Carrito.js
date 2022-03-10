var UpdateBoton = document.getElementsByClassName('addToCar')

for(var i=0 ; i<UpdateBoton.length; i++){
    UpdateBoton[i].addEventListener('click', function(){
        var servicioID = this.dataset.servicio
        var accion = this.dataset.action
        console.log('servicioID ',servicioID, 'accion ',accion)
        console.log("usuario: ", user)

        if(user === "AnonymousUser"){
            console.log("User is not logged in")
        }else{
            ActualizarPedidoDeUsuario(servicioID,accion)
            console.log("Usuario logueado, enviando datos")
        }
    })
}

function ActualizarPedidoDeUsuario(servicioId, accion){ 
    var url = "/Ventas/AddtoCarrito/"
    $.ajax({
        data: {"csrfmiddlewaretoken":csrftoken, "servicioId":servicioId, "accion":accion},
        url: url,
        type: "POST",
        success: function(datas){
            location.href="/Ventas/Carrito/"
        },
        error: function(error){
          return error.json()
        }
      }); 
    
 }