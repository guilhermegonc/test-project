const consolidateWalletResults = () => {
    price = sumWalletPrice()
    value = sumWalletValue(price)
}

const sumWalletPrice = () => {
    const div = document.querySelector('#wallet-cost')
    let price = 0
    for (s in stocks) {
        price += stocks[s].price * stocks[s].quantity
    }
    div.innerText = `R$${price.toFixed(2)}`
    return price
}

const sumWalletValue = price => {
    const div = document.querySelector('#wallet-value')
    let value = 0
    for (s in stocks) {
        value += stocks[s].value * stocks[s].quantity
    }
    div.innerText = `R$${value.toFixed(2)}`
    const color = value >= price ? 'green' : 'red'
    div.classList.add(color)
    return value
}

