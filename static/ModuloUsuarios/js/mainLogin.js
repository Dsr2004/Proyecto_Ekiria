$(document).ready(function() {
    $("#FormularioInfo").submit(function() {
        let campo1 = $("#campoInfo1").val();
        let campo2 = $("#campoInfo2").val();
        if (campo1 == "Usuario" && campo2 == "1234") {
            window.location.replace("../Inicio/");
        }
        return false
    })
})