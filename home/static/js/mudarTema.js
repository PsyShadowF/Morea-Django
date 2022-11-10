// Mudar de tema

const body = document.body;
let cont = 1; //CONTADOR PARA FAZER A TROCA DE TEMA
const sideBarMudarTema = document.getElementById("sideBar__mudarTemaImage");

let getStotage = localStorage.getItem("contTheme");
cont = Number(getStotage); // PEGA O VALOR DO CONT DO STORAGE, CONVERTE EM NUMBER É ATRIBUI A let cont

if (cont == 1) {
  // TROCA DO ICONE DO BTN DE TROCAR TEMA
  sideBarMudarTema.src = "/static/icons/sun-icon-general.png";
  
  body.classList.toggle("container--black");
}

function sideBarTemaTogle() {
  if (cont >= 2) {
    cont = 0;
  }
  cont += 1;

  if (cont == 1) {
    sideBarMudarTema.src = "/static/icons/sun-icon-general.png";
  } else {
    sideBarMudarTema.src = "/static/icons/moon-icon-general.png";
  }

  body.classList.toggle("container--black");
  localStorage.setItem("contTheme", cont);
}

sideBarMudarTema.addEventListener("click", sideBarTemaTogle); //CLICK NO BUTTON DE TROCAR TEMA
