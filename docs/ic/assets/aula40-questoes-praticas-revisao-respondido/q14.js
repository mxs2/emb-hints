let h1 = document.getElementById("titulo")
let cor = "blue"

function alterarCor(cor){
    h1.style.color = cor
}

/*
  Também pode ser feito assim:
  
  index.html:
  <button onclick="alterarCor()">Clique aqui</button>
  
  q14.js
  let h1 = document.getElementById("titulo")

  function alterarCor(){
    h1.style.color = 'blue'
  }
 */

