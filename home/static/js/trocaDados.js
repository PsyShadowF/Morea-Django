// TROCAR OS DADOS

const btnTrocarDados = document.getElementById('btnTrocarDados')
let contTrocarDados = 1

function trocarDados() {
    if (contTrocarDados == 3) {
        contTrocarDados = 0
    }

    contTrocarDados += 1

    if(contTrocarDados == 1) {
        btnTrocarDados.src = '/static/icons/light-icon-general.png'
    } else if (contTrocarDados == 2) {
        btnTrocarDados.src = '/static/icons/water-icon-general.png'
    } else if (contTrocarDados == 3) {
        btnTrocarDados.src = '/static/icons/gas-icon-general.png'
    }
}

btnTrocarDados.addEventListener('click', trocarDados)