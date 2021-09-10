const setupWallet = () => {
    consolidateWalletResults()
    populateStocks()
    populateRecommendations()
    createTransactionControl()
    createBalanceControl()    
}

const populateStocks = () => {
    for (s in stocks) {
        new StockObject(stocks[s], s)
    }
}

const populateRecommendations = () => {
    let rec, tag
    let stockCodes = Object.keys(stocks)
    for (r in recommendations) {
        rec = new RecommendedObject(recommendations[r], r)
        tag = stockCodes.indexOf(rec.code) === -1 ? 'new-stock' : 'old-stock'
        rec.fullfillTag(tag)    }
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
