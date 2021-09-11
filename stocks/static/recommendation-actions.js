const setupRecommendations = () => {
    populateRecommendations() 
}

const populateRecommendations = () => {
    let card
    for (r in recommendations) {
        card = new StockObject(recommendations[r], r, 'recommendations')
        card.compareGrowth()
        card.addStatusLabel()
        card.addStatusControl()
        card.addSearchLink()
    }
}
