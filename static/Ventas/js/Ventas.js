function GuardarCita(){
    swal({
      title: "Estas seguro?",
      text: "Se modificaran los datos de la cita",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    }).then((willDelete) => {
      if (willDelete) {
        swal("OK! Su cita ha sido modificada con exito", {
          icon: "success",
        }).then(function() {
        window.location.href = "/Ventas/Calendario/";
     });
      } else {
        swal("OK! Ningun dato de su cita se ha modificado");
      }
    });

        }

function CancelarCita(){
    swal({
        title: "Tenga cuidado!",
        text: "Esta opcion no se puede desaser!",
        icon: "warning",
        buttons: true,
      }).then((willDelete) => {
        if (willDelete) {
          swal("OK! Se ha cancelado su cita", {
            icon: "success",
          }).then(function() {
          window.location.href = "/Ventas/Calendario/";
       });
        } else {
          swal("OK! No se cancelo la cita ");
        }
      });
}

function CambioEstadoServicio(){
  swal({
    title: "Hecho",
    text: "Estado del servicio cambiado con exito",
    icon: "success",
  });
}


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


function ConfirmarNoGuardarCita(){
  swal({
    title: "Estas seguro?",
    text: "No se guardaran los cambios que haya hecho",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      swal("OK! Se redigira al listado de las citas", {
        icon: "error",
      }).then(function() {
      window.location.href = "/Ventas/ListadoCitas/";
   });
    } else {
      swal("OK! Puede seguir haciendo lo que estaba haciendo");
    }
  });
}

function GuardarCita(){
  swal({
    title: "Hecho",
    text: "Cita guardada",
    icon: "success",
  }).then(function() {
    window.location.href = "/Ventas/ListadoCitas/";
 });
}

function ConfirmarCita(){
  swal({
    title: "Hecho",
    text: "Cita Confirmada",
    icon: "success",
  });
}

function CancelarCita2(){
  swal({
      title: "Tenga cuidado!",
      text: "Esta opcion no se puede desaser!",
      icon: "warning",
      buttons: true,
    }).then((willDelete) => {
      if (willDelete) {
        swal("OK! Se ha cancelado su cita", {
          icon: "success",
        }).then(function() {
        window.location.href = "/Ventas/ListadoCitas/";
     });
      } else {
        swal("OK! No se cancelo la cita ");
      }
    });
}
// MODALES
// tipo de servicio 
function abrir_modal_editar(url){
   $("#EditarTipoServicio").load(url, function (){ 
      $(this).appendTo("body").modal('show');
    });
}

function abrir_modal_crear(url){
   $("#AgregarTipoServicio").load(url, function (){ 
      $(this).appendTo("body").modal('show');
    });
}

function abrir_modal_eliminar(url){ 
  $("#EliminarTipoServicio").load(url, function (){ 
    $(this).appendTo("body").modal('show');
  });
}

// catalogo

function abrir_modal_detalleServicio(url){
  $("#VerMasServivios").load(url, function (){  
    $(this).appendTo("body").modal("show");
  });
}

// ERRORES

// EDITAR SERVICIO 
function mostrarErroresEditarServicio(errores){
  errorsd=JSON.parse(errores)
  $(document).ready(function(){
      let formulario = $("#EditarServicioForm")
      formulario.find('.bg-danger').text('');
       for(let e in errorsd){
            $("span[data-key='"+e+"']").text(errorsd[e])
       }
  });
}
// AGREGAR SERVICIO 
function mostrarErroresAgregarServicio(errores){
  errorsd=JSON.parse(errores)
  $(document).ready(function(){
      let formulario = $("#AgregarServicioForm")
      formulario.find('.bg-danger').text('');
       for(let e in errorsd){
            $("span[data-key='"+e+"']").text(errorsd[e])
       }
  });
}

// AJAX
 
function registrar(){
  $.ajax({
    data: $("#formCrearTipo_Servicio").serialize(),
    url: $("#formCrearTipo_Servicio").attr('action'),
    type: $("#formCrearTipo_Servicio").attr('method'),
    success: function(response){
      window.location.href="/Ventas/AdminVentas/"
    },
    error: function(error){
      $(document).ready(function(){
        let formulario = $("#formCrearTipo_Servicio")
        formulario.find('.bg-danger').text('');
         for(let e in error.responseJSON.error){
           let txt=error.responseJSON.error[e]
              $("span[data-key='"+e+"']").text(txt)
         }
    });
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





function CambiarEstadoTipoServicio(id){
let ids=id
let token = $("#EstadoTipoServicioForm2").find('input[name=csrfmiddlewaretoken]').val()
console.log(token)
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
      swal("OK! Ningun dato del tipo de servicio ha sido modificado");
      window.location.href="/Ventas/AdminVentas/"
    }
  });
  return false;
}

