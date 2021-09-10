const distributeBalance = () => {
    const val = getBalance()
    const walletLength = Object.keys(stocks).length
    const target = val / walletLength
    let walletPrice = 0
    
    for (r in recommendations) {
        let result = findClosest(recommendations[r].price, target)
        walletPrice += result * recommendations[r].price
        showBalance(r, recommendations[r].price, result)
    }

    writeSummary(walletPrice)
}

const getBalance = () => {
    let balance = document.querySelector('#balance input')
    return parseInt(balance.value)
}

const findClosest = (price, target) => Math.round(target / price)

const showBalance = (code, price, quantity) => {
    let cost = (quantity * price).toFixed(2)
    let card = document.querySelector(`#balance-${code}`)
    card.innerText = `R$${cost} (${quantity})`
}

const writeSummary = total => {
    const card = document.querySelector('#balance-btn div p')
    card.innerText = `Total: R$${total.toFixed(2)}`
}