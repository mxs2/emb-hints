function parOuImpar() {
  const numero = document.getElementById("numero").value;
  const mensagem = document.getElementById("mensagem");

  mensagem.style.color = "blue"

  if (numero % 2 === 0) {
    mensagem.innerText = `O número ${numero} é par!`;
  } else {
    mensagem.innerText = `O número ${numero} é ímpar!`;
  }
}
