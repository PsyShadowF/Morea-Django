let vh = window.innerHeight * 0.01
 
// Configura o valor em --vh na raiz do documento
document.documentElement.style.setProperty('--vh', `${vh}px`)

// Escuta o evento resize
window.addEventListener('resize', () => {
    // Executa o mesmo script de antes
    let vh = window.innerHeight * 0.01
    document.documentElement.style.setProperty('--vh', `${vh}px`)
})

// Config caso o  height seja menor que 420px

let valorCorrecty =  window.innerHeight * 1.5
if (window.innerHeight <= 300) {
    // CASO O TAMANHO DA TELA SEJA MENOR OU IGUAL A 300PX -> MUDA O TAMANHO PARA FICAR FIXO EM 500PX
    valorCorrecty = 500
}
document.documentElement.style.setProperty('--heightTabela', `${valorCorrecty}px`)


window.addEventListener('resize', () => {
    let valorCorrecty =  window.innerHeight * 1.5
    console.log(window.innerHeight);
    if (window.innerHeight <= 300) { 
        // CASO O TAMANHO DA TELA SEJA MENOR OU IGUAL A 300PX -> MUDA O TAMANHO PARA FICAR FIXO EM 500PX
        valorCorrecty = 500
    }
    document.documentElement.style.setProperty('--heightTabela', `${valorCorrecty}px`)
})