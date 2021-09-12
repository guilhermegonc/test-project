const distributeBalance = () => {
    const stockCodes = Object.keys(stocks)
    const val = getBalance()
    const toBalace = stocksToBalance()
    const walletLength = toBalace.length
    const target = val / walletLength
    let walletPrice = 0
    let code, stockObj 
    for (let i = 0; i < walletLength; i++) {
        code = toBalace[i]
        stockObj = stockCodes.indexOf(code) != -1 ? stocks[code] : recommendations[code]
        let result = findClosest(stockObj.price, target)
        walletPrice += result * stockObj.price
        showBalance(code, stockObj.price, result)
    }
    writeSummary(walletPrice)
}

const getBalance = () => {
    let balance = document.querySelector('#balance input')
    return parseInt(balance.value)
}

const stocksToBalance = () => {
    const stockCodes = Object.keys(stocks)
    const walletToBalance = stockCodes.filter(onlyRecommended)
    const recommendedCodes = Object.keys(recommendations)
    const recommendationsToBalance = recommendedCodes.filter(onlyOutWallet)
    return walletToBalance.concat(recommendationsToBalance)
}

const onlyRecommended = value => {
    return stocks[value].recommended && value != 'IVVB11'
}

const onlyOutWallet = value => {
    const stockCodes = Object.keys(stocks)
    return stockCodes.indexOf(value) === -1
}

const findClosest = (price, target) => Math.round(target / price)

const showBalance = (code, price, quantity) => {
    const cost = (quantity * price).toFixed(2)
    const text = `R$${cost} (${quantity})`
    const span = document.querySelector(`#balance-${code} #balance-simulation`)
    span  === null ? createSpan(code, text) : modifySpan(span, text)
}

const createSpan = (code, text) => {
    const card = document.querySelector(`#balance-${code}`)
    card.classList.remove('blue', 'str')
    card.classList.add('light-gray')

    const span = document.createElement('span')
    span.id = 'balance-simulation'
    span.classList.add('green', 'str')
    card.appendChild(span)
    modifySpan(span, text)
}

const modifySpan = (span, text) => {
    span.innerText = text
}

const writeSummary = total => {
    const title = document.querySelector('#balance-btn')
    title.innerText = `R$${total.toFixed(2)} - Clique para simular novamente`
}