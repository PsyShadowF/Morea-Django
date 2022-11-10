//VARIAVEIS PARA FAZER ANIMAÇÃO DA SIDE BAR HOVER

const sideBar = document.getElementById('sideBar')
const sideBarHomeText = document.getElementById('sideBar__textHome')
const sideBarDashboardText = document.getElementById('sideBar__textDashboard')
const sideBarDivHome = document.getElementById('sideBarDivHome')
const sideBarDivDashboard = document.getElementById('sideBarDivDashboard')
const sideBarImageCordenador = document.getElementById('sideBar__imageCordenador')
const sideBarTextCordenador = document.getElementById('sideBar__textCordenador')
const sideBarMudarTemaText = document.getElementById('sideBar__mudarTemaText')
const sideBarDivDadosBrutosLink = document.getElementById('sideBarDivDadosBrutos') 
const sideBarTextDadosBrutos = document.getElementById('sideBar__textDadosBrutos')

//Aumento da div Sidebar, quando o mouse entra nela 

sideBar.addEventListener('mouseenter', () => {
    sideBar.style.width = '200px'
    sideBarDivHome.style.width = '200px'
    sideBarDivDashboard.style.width = '200px'
    sideBarDivDadosBrutosLink.style.width = '200px'
    sideBarHomeText.textContent = 'Home' //Home
    sideBarDashboardText.textContent = 'Dashboard' //Dashboard
    sideBarTextDadosBrutos.textContent = 'Dados Brutos' // Dados Brutos
    sideBarMudarTemaText.textContent = 'Mudar Tema' // Texto do btn para mudar tema


    //Config para ajustar foto do cordenador

    sideBarImageCordenador.style.cssText = `
        display: flex;
        justify-content: flex-start;
        align-items: center;
    `
    sideBarTextCordenador.style.cssText = `
        font-size: 15px;
        margin-left: 5px;
    `
    sideBarTextCordenador.textContent = 'Rubens Matos'
}) 

//Diminuição da div Sidebar, quando o mouse sai nela 

sideBar.addEventListener('mouseleave', () => {
    sideBar.style.width = '70px'
    sideBarDivHome.style.width = '70px'
    sideBarDivDashboard.style.width = '70px'
    sideBarDivDadosBrutosLink.style.width = '70px'
    sideBarHomeText.textContent = '' //home
    sideBarDashboardText.textContent = '' //Dashboard
    sideBarTextDadosBrutos.textContent = '' // Dados brutos

    //Config para ajustar foto do cordenador

    sideBarImageCordenador.style.cssText = `
        display: grid;
        justify-content: start;
    `
    sideBarTextCordenador.style.cssText = `
        font-size: 9px;
        margin-left: 0;
    `
    sideBarTextCordenador.textContent = 'Rubens M.'
    sideBarMudarTemaText.textContent = '' // Texto do btn para mudar tema
})