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

function fg(){
    if (value == True)
    var i=document.getElementById("Habilitar").value = inabilitado;
    else{
        var i=document.getElementById("Habilitar").value = Habilitado;
    }
}