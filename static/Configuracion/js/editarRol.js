// $(document).ready(function(){
//   $("#editaroles").click(function(){
//     var pk = $(this).data('pid')
//     $("#EditarRol").modal("show");
//   });
//   $("#EditarRol").on('show.bs.modal', function(event){
//     var modal = $(this)
//     var pk = $(this).data('pid')
//     $.ajax({
//         data: {'pk': pk},
//         url: "{% url 'EditarRoles' %}",
//         context: document.body,
//         error: function(response, error) {
//             alert(error);
//         }
//     }).done(function(response) {
//         modal.html(response);
//     });
//   });
// });