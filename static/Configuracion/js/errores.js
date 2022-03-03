function abrir_modal_crear(url){
    $("#CreateRol").load(url, function(){
        $(this).modal("show")
    });
}
function CrearUsuario(){
    $.ajax({

        data:$('#CrearRoles').serialize(),
        url:$('#CrearRoles').attr('action'),
        type:$('#CrearRoles').attr('method'),
        success: function (response) {
            location.reload()
        },
        error: function(error){
            for (let item in error.responseJSON["errores"]){
                let input =$("#CrearRoles").find('input[name='+item+']')
                input.addClass("is-invalid")
               
        }
    }
    });
}

