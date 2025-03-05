const mensagem = document.getElementById("mensagem");
const entrada = document.getElementById("entrada");

function validarEntrada() {
  let tamanhoEntrada = entrada.value.length;
  console.log(tamanhoEntrada)
  if (tamanhoEntrada < 5) {
    mensagem.innerText = "Entrada deve ter no mínimo 5 caracteres";
    mensagem.style.color = "purple"
  }

}
