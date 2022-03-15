function abrir_modal_crear(url){
    $("#CreateRol").load(url, function(){
        $(this).appendTo("body").modal('show');
    });
}
function CrearRol(){
    $.ajax({

        data:$('#CrearRoles').serialize(),
        url:$('#CrearRoles').attr('action'),
        type:$('#CrearRoles').attr('method'),
        success: function (response) {
            location.reload()
        },
        error: function(error){
            $('#CrearRoles').find('.text-danger').text('')
            $('#CrearRoles').removeClass('is-invalid')
            for (let item in error.responseJSON["errores"]){
                let input =$("#CrearRoles").find('input[name='+item+']')
                input.addClass("is-invalid")
                $('#'+item).text(error.responseJSON["errores"][item])
                
            for(let item in error.responseJSON["errores"]){
                let textarea=$("#CrearRoles").find('textarea[name='+item+']')
                textarea.addClass("is-invalid")
                $('#'+item).text(error.responseJSON["errores"][item])
            }
        }
        
    }
    });
}

