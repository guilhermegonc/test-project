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
    const recommendationCodes  = Object.keys(recommendations)
    const newRecommended = recommendationCodes.filter(inWallet)
    newRecommended.length === 0 ? new EmptyCard() : loopRecommended(newRecommended)
}

const loopRecommended = recommended => {
    let card, index
    for (let i = 0; i < recommended.length; i++) {
        index = recommended[i]
        card = new StockObject(recommendations[index], index, 'recommendations')
        card.compareGrowth()
        card.addTransactionListener('buy')
    }
}

const inWallet = value => {
    let stockCodes = Object.keys(stocks)
    return stockCodes.indexOf(value) === -1
}

const createTransactionControl = () => {
    const btn = document.querySelector('#buy-btn')
    btn.addEventListener("click", function () {
        new TransactionModal('Comprar cotas', 'buy')
    })
}

const createBalanceControl = () => {
    const balance = document.querySelector('#wallet')
    balance.addEventListener("click", addBalanceContent)
}
