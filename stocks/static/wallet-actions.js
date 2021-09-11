const setupWallet = () => {
    consolidateWalletResults()
    populateStocks()
    populateRecommendations()
    createTransactionControl()
    createBalanceControl()    
}

const populateStocks = () => {
    let card
    for (s in stocks) {
        card = new StockObject(stocks[s], s, 'stocks')
        card.addValue()
        card.comparePrice()
        card.addRecommendedTransaction()
        card.addTransactionListener('sell')
    }
}

const populateRecommendations = () => {
    let card
    let stockCodes = Object.keys(stocks)
    for (r in recommendations) {
        card = new StockObject(recommendations[r], r, 'recommendations')
        card.compareGrowth()
        card.highlightNotInWallet(stockCodes)
        card.addTransactionListener('buy')

    }
}

const createTransactionControl = () => {
    const btn = document.querySelector('#buy-btn')
    btn.addEventListener("click", function () {
        new TransactionModal('Comprar cotas', 'buy')
    })
}

const createBalanceControl = () => {
    const balance = document.querySelector('#balance-btn')
    balance.addEventListener("click", addBalanceContent)
}
