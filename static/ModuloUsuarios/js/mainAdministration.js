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