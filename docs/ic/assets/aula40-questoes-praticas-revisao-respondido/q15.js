const input = document.getElementById("texto");

//Resultado da execução será exibido no console do navegador
function validarInput() {
  if (input.value === "") {
    throw new Error("O campo está vazio");
  }
  console.log("Não está vazio");
}
