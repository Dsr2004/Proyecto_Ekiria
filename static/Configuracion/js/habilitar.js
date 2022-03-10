// var btn = 0; //Definimos la Variable
// $(".Habilitar").click(function() { //Function del Click
//   if (btn === 0) { //Condicion de la Variable = 0
//     btn = 1; //Cambiamos a 1
//     $(".btn").text("Ocultar"); //Modificamos el Texto del Boton
//     $(".panel").stop().fadeIn("slow"); //Mostramos el Panel
//   }else{ //Al darle Click de Nuevo
//     btn = 0; //Cambiamos a 0
//     $(".btn").text("Mostrar"); //Modificamos el Texto del Boton
//     $(".panel").stop().fadeOut("slow"); //Ocultamos el Panel
//   }
// });

function ds(id){
    let cosa = id
    let token = $('#estadoRol').find('input[name=csrfmiddlewaretoken]').val()
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
          confirmButton: 'btn btn-success sweetAlertB',
          cancelButton: 'btn btn-danger sweetAlertB',
        },
        buttonsStyling: false
      })
      
      swalWithBootstrapButtons.fire({
        title: '¿Estas seguro?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Aceptar',
        cancelButtonText: 'Cancelar',
        reverseButtons: true
      }).then((result) => {
        if (result.isConfirmed) {
            $(document).ready(function(){
                $.ajax({
                    data:{'csrfmiddlewaretoken':token, 'estado':cosa},
                    url:$('#estadoRol').attr('action'),
                    type:$('#estadoRol').attr('method'),
                    success: function (data) {
                        swalWithBootstrapButtons.fire(
                            'Modificado Correctamente',
                            'Cambiaste el estado',
                            'success'
                        ).then(function(){
                            location.reload()
                        });
                    },error:function (data) {
                        alert("Error: "+error.responseJSON)
                    }
                });
                    
            })
          
        } else if (
          /* Read more about handling dismissals below */
          result.dismiss === Swal.DismissReason.cancel
        ) {
          swalWithBootstrapButtons.fire(
            'Cancelado',
            'Ningun Cambio',
            'error'
          ).then(function(){
              location.reload()
          });
        }
      });
}

// $(document).ready(function() {
//     $('#checkbox').change(function() {
//         $.post("/EstadoRol/", {
//             id: '{{Rol.id_rol}}', 
//             id_rol: this.checked, 
//             csrfmiddlewaretoken: '{{ csrf_token }}' 
//         });
//     });
