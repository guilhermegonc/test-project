const listRecommendationStocks = (walletStocks=null, stockData, addControl=false) => {
    let stk = Object.keys(stockData)
    let recDiv = document.querySelector('#recommendations')
    
    for (let s of stk) {
        let stockDiv = document.createElement('div')
        let inWallet = walletStocks.indexOf(s) != -1
        
        stockDiv.id = `rec-${s}`
        stockDiv.classList.add('db-results', 'p-card', 'shadow', 'p-24', 'm-l-a', 'm-r-a', 'm-b-12')

        createStockCard(stockDiv, s, stockData[s], inWallet, addControl)
        recDiv.appendChild(stockDiv)
    }
}

const createStockCard = (parentDiv, code, stock, inWallet, addControl) => {
    let card = document.createElement('div')
    card.classList.add('card-btn')
    
    tag = labelCard(card, inWallet)
    addControl ? deactivateBtn(card, code, tag, stock.active) : null
    parentDiv.appendChild(card)
    addCardDetails(card, code, stock)
}

const deactivateBtn = (card, code, tag, status) => {
    let icon  = document.createElement('i')
    let iconColor = status ? 'active-icon' : 'inactive-icon'

    icon.classList.add('material-icons', 'fl-r', iconColor)
    icon.innerText = status ? 'toggle_on' : 'toggle_off'
    card.appendChild(icon)

    let activeClass = status ? 'active-stock' : 'inactive-stock'
    tag.classList.remove('new-stock')
    tag.classList.add(activeClass)

    icon.addEventListener('click', function() {
        status = !status
        let uri = `change-recommendation-status?code=${code}&status=${status}`
        window.location.href = uri
    })
}

const labelCard = (parentDiv, inWallet) => {
    let tag = document.createElement('div')
    tag.classList.add('recommendation-tag', 'new-stock')
    inWallet ? tag.classList.add('new-stock') : tag.classList.add('old-stock')
    parentDiv.appendChild(tag)
    return tag
}

const addCardDetails = (parentDiv, code, stock) => {
    addRecommendationBalance(parentDiv)
    addCardCode(parentDiv, code)
    addCardPrice(parentDiv, stock)
}

const addRecommendationBalance = (parentDiv) => {
    let balance = document.createElement('p')
    balance.classList.add('s9', 'str', 'blue', 'fl-r')
    parentDiv.appendChild(balance)
}

const addCardCode = (parentDiv, code) => {
    let aCode = document.createElement('a')
    
    aCode.classList.add('s9', 'str', 'blue', 'm-0', 'clean-a')
    aCode.innerText = `🔍 ${code}`
    aCode.href = `https://www.google.com/search?q=${code}`
    aCode.target = 'blank'


    parentDiv.appendChild(aCode)
}

const addCardPrice = (parentDiv, stock) => {
    let price = document.createElement('p')
    
    price.classList.add('s9', 'light-gray', 'm-0')
    price.innerText = `R$${stock.price.toFixed(2)}`
    parentDiv.appendChild(price)
    addGrowthData(parentDiv, stock)
}

const addGrowthData = (parentDiv, stock) => {
    let growth = document.createElement ('p')
    let growthValue = (stock.growth * 100).toFixed(2)
    let color = growthValue > 0 ? 'green' : 'red'
    
    growth.classList.add('s9', 'light-gray', 'm-0', 'str', color)
    growth.innerText = `${growthValue}% (6 meses)`
    parentDiv.appendChild(growth)
}

const returnEmpty = () => {
    let toAppend = document.querySelector('#recommendations')
    let emptyDiv = document.createElement('div')
    emptyDiv.classList.add('db-results', 'p-card-empty', 'p-24', 'm-l-a', 'm-r-a', 'm-b-12')
    
    toAppend.appendChild(emptyDiv)
    createEmptyCard(emptyDiv)
}

const createEmptyCard = parentDiv => {
    let emptyCard = document.createElement('div')
    emptyCard.classList.add('card-btn')

    parentDiv.appendChild(emptyCard)
    addCardEmptyDetails(emptyCard)
}

const addCardEmptyDetails = cardDiv => {
    let pText = document.createElement('p')
    pText.classList.add('s9', 'str', 'light', 'm-b-0')
    pText.innerText = 'Sem novas recomendações'
    cardDiv.appendChild(pText)

    let pSub = document.createElement('p')
    pSub.classList.add('s9', 'light', 'm-0')
    pSub.innerText = 'Lista atualizada no dia 10 de cada mês'
    cardDiv.appendChild(pSub)
}