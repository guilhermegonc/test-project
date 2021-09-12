const distributeBalance = () => {
    const val = getBalance()
    const walletLength = Object.keys(stocks).length
    const target = val / walletLength
    let walletPrice = 0
    
    for (s in stocks) {
        let result = findClosest(stocks[s].price, target)
        walletPrice += result * stocks[s].price
        showBalance(s, stocks[s].price, result)
    }

    writeSummary(walletPrice)
}

const getBalance = () => {
    let balance = document.querySelector('#balance input')
    return parseInt(balance.value)
}

const findClosest = (price, target) => Math.round(target / price)

const showBalance = (code, price, quantity) => {
    const span = document.createElement('span')
    const cost = (quantity * price).toFixed(2)
    const card = document.querySelector(`#stocks #balance-${code}`)
    card.classList.remove('blue', 'str')
    card.classList.add('light-gray')
    span.classList.add('green', 'str')
    span.innerText = `\nR$${cost} (${quantity})`
    card.appendChild(span)
}

const writeSummary = total => {
    const title = document.querySelector('#balance-btn')
    title.innerText = `R$${total.toFixed(2)} - Clique para simular novamente`
}