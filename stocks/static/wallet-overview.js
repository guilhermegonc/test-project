const consolidateWalletResults = () => {
    sumWalletValue()
    sumWalletPrice()
}

const sumWalletValue = () => {
    const div = document.querySelector('#value h3')
    let value = 0
    for (s in stocks) {
        value += stocks[s].value * stocks[s].quantity
    }
    div.innerText = `R$${value.toFixed(2)}`
}

const sumWalletPrice = () => {
    const div = document.querySelector('#price h3')
    let price = 0
    for (s in stocks) {
        price += stocks[s].price * stocks[s].quantity
    }
    div.innerText = `R$${price.toFixed(2)}`
}
