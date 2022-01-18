/*El evento «DOMContentLoaded» que hemos asociado al objeto document: sirve para detectar cuando el navegador ya ha procesado todos los 
elementos de la página, momento en el cual ya somos capaces de acceder al formulario con seguridad.
El evento «submit» que hemos asociado al formulario, que se dispara en el momento que el usuario envíe el formulario. Como manejador del 
evento submit hemos indicado el nombre de una función llamada «manejadorValidacion», cuyo código nos servirá para realizar las 
correspondientes validaciones.*/

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("formulario").addEventListener('submit', validarFormulario);
});

const expresiones = {
    texto: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
    nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/
}

function validarFormulario(e) {
    /*En el objeto evento disponemos del método preventDefault() que realiza la parada del comportamiento predeterminado 
    del evento correspondiente, en este caso el envío del formulario.*/
    e.preventDefault();

    var nombre = document.getElementById('nombre').value;
    if (expresiones.nombre.test(nombre)) {
    } else {
        alert("Datos no válidos");
        document.getElementById('nombre').focus();
        return;
    }
    var apellido = document.getElementById('apellido').value;
    if (expresiones.nombre.test(apellido)) {
    } else {
        alert("Datos no válidos");
        document.getElementById('apellido').focus();
        return;
    }

    var edad = document.getElementById('edad').value;
    if (edad < 15 || edad > 70) {
        alert('Ingrese una edad válida entre 15 y 70 años');
        document.getElementById('edad').focus();
        return;
    }

    var dni = document.getElementById('dni').value;
    if (dni.length != 8) {
        alert('El DNI tiene que tener una longitus de 8. Ejemplo: 48752103');
        document.getElementById('dni').focus();
        return;
    }

    var cuil = document.getElementById('cuil').value;
    if (cuil.length != 11) {
        alert('El cuil tiene que tener una longitus de 11. Ejemplo: 27487521030');
        document.getElementById('cuil').focus();
        return;
    }

    var celular = document.getElementById('celular').value;
    if (celular.length != 10) {
        alert('El número de celular tiene que tener una longitud de 10. Ejemplo 1187432541');
        document.getElementById('celular').focus();
        return;
    }

    document.getElementById('formulario').submit();
}
