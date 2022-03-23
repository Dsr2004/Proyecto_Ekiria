// MODALES PARA TIPO DE SERVICIOS
//CREAR TIPO DE SERVICIO
 function abrir_modal_crear(url){
    $("#AgregarTipoServicio").load(url, function (){ 
       $(this).appendTo("body").modal('show');
     });
 }

//EDITAR TIPO DE SERVICIO
 function abrir_modal_editar(url){
    $("#EditarTipoServicio").load(url, function (){ 
       $(this).appendTo("body").modal('show');
     });
 }

 //ELIMINAR TIPO DE SERVICIO
 function abrir_modal_eliminar(url){ 
   $("#EliminarTipoServicio").load(url, function (){ 
     $(this).appendTo("body").modal('show');
   });
 }
 //CATALOGO
 //AGREGAR SERVICIO AL CATALOGO

 function abrir_modal_AgregarServicioCatalogo(url){
   $("#AgregarServicioCatalogo").load(url, function (){ 
     $(this).modal('show');
   });
 }

 //FUNCIONALIDADES CON AJAX
 //REGISTRAR TIPO DE SERVICIO
 function registrar(){
    $.ajax({
      data: $("#formCrearTipo_Servicio").serialize(),
      url: $("#formCrearTipo_Servicio").attr('action'),
      type: $("#formCrearTipo_Servicio").attr('method'),
      success: function(response){
        window.location.href="/Ventas/AdminVentas/"
      },
      error: function(error){
          $("#formCrearTipo_Servicio").find('.text-danger').text('');
          for (let i in error.responseJSON["errors"]){
            let x=$("#formCrearTipo_Servicio").find('input[name='+i+']')
            x.addClass("is-invalid")
            $("#"+i).text(error.responseJSON["errors"][i])
        }
      }
    });
  }
  
  // EDITAR TIPO DE SERVICIO 
  function editar(){
    $.ajax({
      data: $("#formEditarTipo_Servicio").serialize(),
      url: $("#formEditarTipo_Servicio").attr('action'),
      type: $("#formEditarTipo_Servicio").attr('method'),
      success: function(response){
        $("#EditarTipoServicio").modal('hide');
        location.reload();
      },
      error: function(error){
        $("#formEditarTipo_Servicio").find('.text-danger').text('');
        for (let i in error.responseJSON["errors"]){
          let x=$("#formEditarTipo_Servicio").find('input[name='+i+']')
          x.addClass("is-invalid")
          $("#"+i).text( error.responseJSON["errors"][i])
        }
      }
        
    });
  }
 
  //CAMBIAR ESTADO DE TIPO DE SERVICIO
  function CambiarEstadoTipoServicio(id){
    let ids=id
    let token = $("#EstadoTipoServicioForm2").find('input[name=csrfmiddlewaretoken]').val()
      swal({
        title: "Estas seguro?",
        text: "Se modificara el estado de el Tipo de Servicio",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      }).then((willDelete) => {
        if (willDelete) {
          swal("OK! Se ha modificado el tipo de servicio", {
            icon: "success",
          }).then(function() {
              $.ajax({
                data: {"csrfmiddlewaretoken":token, "estado":ids},
                url: $("#EstadoTipoServicioForm2").attr('action'),
                type: $("#EstadoTipoServicioForm2").attr('method'),
                success: function(data){
                  window.location.href="/Ventas/AdminVentas/"
                },
                error: function(error){
                  console.log("no")
                  alert("Error:"+error.responseJSON)
                }
              }); 
           
       });
        } else {
          swal("OK! Ningun dato del tipo de servicio ha sido modificado").then(function(){
            location.reload()
          });
          
        }
      });
      return false;
    }
  
    //CAMBIAR ESTADO DE  DE SERVICIO PARA EL CATALOGO
  function CambiarEstadoServicioCatalogo(id){
    let ids=id
    let token = $("#EstadoTipoServicioCatalogoForm").find('input[name=csrfmiddlewaretoken]').val()
      swal({
        title: "¿Estas seguro?",
        text: "Se modificará el estado, Esto significa que el servicio no se mostrará en el catalogo",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      }).then((willDelete) => {
        if (willDelete) {
          swal("OK! Se ha modificado el estado", {
            icon: "success",
          }).then(function() {
              $.ajax({
                data: {"csrfmiddlewaretoken":token, "estado":ids},
                url: $("#EstadoTipoServicioCatalogoForm").attr('action'),
                type: $("#EstadoTipoServicioCatalogoForm").attr('method'),
                success: function(data){
                  window.location.href="/Ventas/AdminVentas/"
                },
                error: function(error){
                  console.log("no")
                  alert("Error:"+error.vi)
                }
              }); 
           
       });
        } else {
          swal("OK! Ningun dato del servicio ha sido modificado").then(function(){
            location.reload()
          });
          
        }
      });
      return false;
    }
  