// Trocar de pagina

const sideBarDivHomeLink = document.getElementById("sideBarDivHome");
const btnDash = document.getElementById("container__dashboard");
const btnDashSideBar = document.getElementById("sideBarDivDashboard");
const btnDadosBrutosLink = document.getElementById("container__dadosBrutos");

// IR ATÉ A HOME

function toHome() {
  window.location.href = "/home/";
}
sideBarDivHomeLink.addEventListener("click", toHome);

// IR ATÉ O DASHBOARD

function toDash() {
  window.location.href = "/dashboard/";
}

if (btnDash) {
  btnDash.addEventListener("click", toDash);
}

btnDashSideBar.addEventListener("click", toDash);

// IR ATÉ OS DADOS BRUTOS

function toDadosBrutos() {
  window.location.href = "/dados/";
}

if (btnDadosBrutosLink) {
  btnDadosBrutosLink.addEventListener("click", toDadosBrutos);
}

sideBarDivDadosBrutosLink.addEventListener("click", toDadosBrutos);
