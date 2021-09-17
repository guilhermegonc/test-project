const consolidateWalletResults = () => {
    price = sumWalletPrice()
    value = sumWalletValue()
}

const sumWalletPrice = () => {
    const div = document.querySelector('#wallet-cost')
    div.innerText = `R$${invested.toFixed(2)}`
}

const sumWalletValue = () => {
    const div = document.querySelector('#wallet-value')
    let value = 0
    for (s in stocks) {
        value += stocks[s].value * stocks[s].quantity
    }
    div.innerText = `R$${value.toFixed(2)}`
    const color = value >= invested ? 'green' : 'red'
    div.classList.add(color)
}

