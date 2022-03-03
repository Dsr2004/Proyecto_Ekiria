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
    swal.fire({
        title: "Estas seguro?",
        text: "Se modificara el estado de el Usuario",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then((willDelete) => {
        if (willDelete) {
            swal.fire("OK! Se ha modificado el Usuario", {
                icon: "success",
            }).then(function() {
                $.ajax({
                    data: {"csrfmiddlewaretoken":token, "estado":ids},
                    url: $("#EstadoUsuarioForm").attr('action'),
                    type: $("#EstadoUsuarioForm").attr('method'),
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
            swal.fire("OK! Ningun dato del tipo de servicio ha sido modificado");
            window.location.href="/Ventas/AdminVentas/"
        }
        });
        return false;
    
    }