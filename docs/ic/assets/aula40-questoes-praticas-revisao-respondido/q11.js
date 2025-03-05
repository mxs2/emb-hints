let variavelGlobal = "exemplo de variável global";

function exemploEscopoDeFuncao() {
  let variavelLocal = "exemplo de variável local";

  console.log("Dentro da função: " + variavelGlobal); // Funciona
  console.log("Dentro da função: " +variavelLocal); // Funciona
}

exemploEscopoDeFuncao();

console.log("Fora da função: " + variavelGlobal); // Funciona
console.log("Fora da função: " + variavelLocal); // Não nunciona
