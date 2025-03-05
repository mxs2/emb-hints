let button = document.getElementById("btn-validar")
let mensagem = document.getElementById("mensagem")

  mensagem.style.color = "red"

function mostrarMensagem(){
    mensagem.innerText = "O mouse está sobre a área do botão"
}

function ocultarMensagem(){
    mensagem.innerText = "O mouse está fora da área do botão"
}