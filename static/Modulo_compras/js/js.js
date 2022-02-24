function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // ¿Esta cadena de cookies comienza con el nombre que queremos?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');


function eliminarprov(id_proveedor) {
  let path = "/compras/eliminarprov/"
  var ruta = path+id_proveedor
  console.log(ruta)
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
          confirmButton: 'btn btn-success',
          cancelButton: 'btn btn-danger'
        },
        buttonsStyling: false
      })
      
      swalWithBootstrapButtons.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Yes, delete it!',
        cancelButtonText: 'No, cancel!',
        reverseButtons: true
      }).then((result) => {
        if (result.isConfirmed) {
          swalWithBootstrapButtons.fire(
            'Deleted!',
            'Your file has been deleted.',
            'success',
            window.location.href=ruta
            
          )
        } else if (
          /* Read more about handling dismissals below */
          result.dismiss === Swal.DismissReason.cancel
        ) {
          swalWithBootstrapButtons.fire(
            'Cancelled',
            'Your imaginary file is safe 🙂',
            'error'
          )
        }
      })
};

function agregarprov(url){
 $("#agregar_prov").load(url,function() {
   $(this).modal('show')
 })

};

function mostrarerrores(errors){
  $('#errores').html("");
  let error = "";
  for (let item in errors.responseJSON.errors){
    error += '<div class = "alert alert-danger"<strong>'+ errors.responseJSON.errors[item] + '</strong></div>'; 
  }

  $('#errores').append(error)

}


function registrar(){
 
  $.ajax({
    data: $("#agregarprov").serialize(),
    url: $("#agregarprov").attr('action'),
    type: $("#agregarprov").attr('method'),
    success: function(response){
      console.log(response)
    },
    error: function(errors){
      // $('.form-control').addClass('is-valid')
   
      console.log(errors)
      //  console.log(errors.responseJSON["errors"])
      // let gerrores = errors.responseJSON["errors"]
        mostrarerrores(errors)
         }
  });
}






// function pasarPost(id_proveedor) {
//     $.ajax({
//       data: id_proveedor,
//       url: '/compras/listarprov/',
//       type: "POST",
//       success: function(data) {
//     }
//     })
// }