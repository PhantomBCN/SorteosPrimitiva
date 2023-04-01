// Función para generar números aleatorios no repetidos entre 1 y 49
function generarNumerosAleatorios() {
    let numeros = [];
    while (numeros.length < 6) {
      let numero = Math.floor(Math.random() * 49) + 1;
      if (numeros.indexOf(numero) === -1) {
        numeros.push(numero);
      }
    }
    return numeros.sort(function(a, b) {
      return a - b;
    });
  }
  
  // Función para asignar los números aleatorios generados a los inputs correspondientes
  function asignarNumerosAleatorios() {
    let numerosAleatorios = generarNumerosAleatorios();
    let inputs = document.querySelectorAll('input[type="number"]');
    for (let i = 0; i < inputs.length - 2; i++) {
      inputs[i].value = numerosAleatorios[i];
    }
  }
  
  // Event listener para el botón "Generar números aleatorios"
  document.getElementById('generar-numeros').addEventListener('click', function(event) {
    event.preventDefault();
    asignarNumerosAleatorios();
  });
  