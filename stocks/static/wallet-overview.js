const consolidateWalletResults = stocks => {
    const wPrice = document.querySelector('#price h3')
    const wValue = document.querySelector('#value h3')

    let walletInvestment = 0
    let walletValue = 0
    for (s in stocks) {
        walletInvestment += stocks[s].price * stocks[s].quantity
        walletValue += stocks[s].value * stocks[s].quantity
    }

    wPrice.innerText = `R$${walletInvestment.toFixed(2)}`
    wValue.innerText = `R$${walletValue.toFixed(2)}`
}

const buildRecommendation = (wallet, recommendation) => {
    let inWallet = Object.keys(wallet)
    listRecommendationStocks(inWallet, recommendation)
}