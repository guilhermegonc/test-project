const balanceWallet = stocks => {
    let btn = document.querySelector('#balance div')
    btn.addEventListener("click", function() {
        distributeBalance(stocks)
    })
}

const distributeBalance = stocks => {
    let val = getBalance()
    let walletLength = Object.keys(stocks).length
    let target = val / walletLength
    let walletPrice = 0
    for (s in stocks) {
        let result = findClosest(stocks[s].price, target)
        walletPrice += result * stocks[s].price
        showBalance(s, stocks[s].price, result)
    }
    return writeSummary(walletPrice)
}

const getBalance = () => {
    let balance = document.querySelector('#balance input')
    let val = balance.value
    return parseInt(val)
}

const findClosest = (price, target) => Math.round(target / price)

const showBalance = (stockCode, stockPrice, qty) => {
    let cost = (qty * stockPrice).toFixed(2)
    let card = document.querySelector(`#rec-${stockCode} div p`)
    card.innerText = `R$${cost} (${qty})`
}

const writeSummary = total => {
    let card = document.querySelector('#balance-btn div p')
    total = total.toFixed(2)
    card.innerText = `Total: R$${total}`
}