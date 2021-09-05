const setStocks = (stocks, token, forms, recommendation) => {
    populateStocks(stocks, token, forms)
    createBuyingListener(token, forms)
    createBalanceListener(recommendation)
    consolidateWalletResults(stocks)
    buildRecommendation(stocks, recommendation)
}

const populateStocks = (stocks, token, forms) => {
    for (s in stocks) {
        new StockObject(stocks[s], s)
        createSellingListener(s, token, forms)
    }
}
