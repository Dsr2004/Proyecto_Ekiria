function añadirUsuario() {
    window.location.href = "../CrearUsuario/";
}

function cancelCreate() {
    window.location.href = "../Administracion/";
}
const getValueInput = () => {
    let inputValue = document.getElementById("Idate").value;
    document.getElementById("valueInput").innerHTML = inputValue;
}

function CambiarEstadoUsuario(id){
    let ids=id
    let token = $("#EstadoUsuarioForm").find('input[name=csrfmiddlewaretoken]').val()
    console.log(token)
    swal({
        title: "Estas seguro?",
        text: "Se modificara el estado de el Tipo de Servicio",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
      }).then((willDelete) => {
        if (willDelete) {
          swal("OK! Se ha modificado el tipo de servicio", {
            icon: "success",
          }).then(function() {
              $.ajax({
                data: {"csrfmiddlewaretoken":token, "estado":ids},
                url: $("#EstadoUsuarioForm").attr('action'),
                type: $("#EstadoUsuarioForm").attr('metho  d'),
                success: function(data){
                  window.location.href="/InformacionUsuario/Administracion/"
                },
                error: function(error){
                  console.log("no")
                  alert("Error:"+error.responseJSON)
                }
              }); 
           
       });
        } else {
          swal("OK! Ningun dato del tipo de servicio ha sido modificado");
          window.location.href="/InformacionUsuario/Administracion/"
        }
      });
      return false;
    
    }