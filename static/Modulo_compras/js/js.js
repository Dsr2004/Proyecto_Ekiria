// class TextoAnimado {
// 	constructor(id, objetivo){
// 		this.texto = document.getElementById(id);
// 		this.objetivo = document.getElementById(objetivo);
// 		this.letras = this.texto.innerText.split("");
		
// 		this.texto.innerText = '';

// 		this.letras.forEach((letra) => {
// 			let caracter = letra === ' ' ? '&nbsp;' : letra;

// 			this.texto.innerHTML = this.texto.innerHTML + `
// 				<div>
// 					<span>${caracter}</span>
// 					<span class="segunda-linea">${caracter}</span>
// 				</div>
// 			`;
// 		});

// 		this.objetivo.addEventListener('mouseenter', () => {
// 			let cuenta = 0;

// 			const intervalo = setInterval(() => {
// 				if(cuenta < this.texto.children.length){
// 					this.texto.children[cuenta].classList.add('animacion');
// 					cuenta += 1;
// 				} else {
// 					clearInterval(intervalo);
// 				}
// 			}, 30);
// 		});

// 		this.objetivo.addEventListener('mouseleave', () => {
// 			let cuenta = 0;

// 			const intervalo = setInterval(() => {
// 				if(cuenta < this.texto.children.length){
// 					this.texto.children[cuenta].classList.remove('animacion');
// 					cuenta += 1;
// 				} else {
// 					clearInterval(intervalo);
// 				}
// 			}, 30);
// 		});
		
// 	}
// }

// new TextoAnimado('logo', 'logotipo');

// function buscador_interno(){

// 	filter = inputSearch.value.toUpperCase();
// }

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
}