const tableAgua = document.querySelector('.tableAgua')
const tableEnergia = document.querySelector('.tableEnergia')
const tableGas = document.querySelector('.tableGas')

// TROCAR OS DADOS

const btnTrocarDados = document.getElementById('btnTrocarDados')
let contTrocarDados = 1

trocarDados()

function trocarDados() {
    if (contTrocarDados == 3) {
        contTrocarDados = 0
    }

    contTrocarDados += 1

    if(contTrocarDados == 1) {
        btnTrocarDados.src = '/static/icons/light-icon-general.png'
        try {
            tableAgua.style.display = 'none'
            tableGas.style.display = 'none'
            tableEnergia.style.display = 'inline-table'
        } catch (error) {
          console.log(error)  
        }
    } else if (contTrocarDados == 2) {
        btnTrocarDados.src = '/static/icons/water-icon-general.png'
        try {
            tableAgua.style.display = 'inline-table'
            tableGas.style.display = 'none'
            tableEnergia.style.display = 'none'
        } catch (error) {
            console.log(error)
        }
    } else if (contTrocarDados == 3) {
        btnTrocarDados.src = '/static/icons/gas-icon-general.png'
        try {
            tableAgua.style.display = 'none'
            tableGas.style.display = 'inline-table'
            tableEnergia.style.display = 'none' 
        } catch (error) {
            console.log(error)
        }
    }
}

btnTrocarDados.addEventListener('click', trocarDados)