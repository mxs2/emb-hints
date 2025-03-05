const piada = document.getElementById("piada");

function obterPiada() {
  fetch("https://api.chucknorris.io/jokes/random")
    .then((response) => response.json())
    .then((data) => {
      piada.innerText = data.value
      piada.style.backgroundColor = "yellow"
    })
    .catch((error) => {
      console.error("Erro ao obter piada: " + error);
      piada.innerText = "Piada não encontrada";
    
    });
}
