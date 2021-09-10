const setupRecommendations = () => {
    populateRecommendations() 
}

const populateRecommendations = () => {
    let rec, tag
    for (r in recommendations) {
        rec = new RecommendedObject(recommendations[r], r)
        tag = rec.stockObj.active ? 'active-stock' : 'inactive-stock'
        rec.fullfillTag(tag)
        rec.addStatusControl()
    }
}
