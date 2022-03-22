
//EDITAR SERVICIO
function ConfirmacionEditarServicio(){
    event.preventDefault();
    swal({
        title: "Estas seguro?",
        text: "Se modificaran los datos del servicio",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then((willDelete) => {
        if (willDelete) {
        swal("OK! Se ha modificado el servicio", {
            icon: "success",
        }).then(function() {
        window.location.href = "/Ventas/ListadoServicios/";
        document.forms['EditarServicioForm'].submit();
        });
        } else {
        swal("OK! Ningun dato del servicio ha sido modificado");
        }
    });
    return false;
}
      
//CAMBIAR ESTADO DE SERVICIO
function CambiarEstadoServicio(id){
    let ids=id
    let token = $("#EstadoServicioForm").find('input[name=csrfmiddlewaretoken]').val()
    swal({
      title: "Estas seguro?",
      text: "Se modificara el estado del Servicio",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    }).then((changeStatus) => {
      if (changeStatus) {
        $(document).ready(function(){
        $.ajax({
          data: {"csrfmiddlewaretoken":token, "estado":ids},
          url: $("#EstadoServicioForm").attr('action'),
          type: $("#EstadoServicioForm").attr('method'),
          success: function(datas){
            swal("OK! Se ha modificado el Servicio", {
                icon: "success",
              }).then(function(){
                location.reload()
              });
          },
          error: function(error){
            console.log("no")
            alert("Error:"+error.responseJSON)
          }
        }); 
        })
      } else {
        swal("OK! Ningun dato del servicio ha sido modificado").then(function(){
          location.reload()
        });
        
      }
    });
}
