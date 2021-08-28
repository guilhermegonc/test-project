const createBuyingListener = (token, forms) => {
    document.querySelector('#new-purchase')
    .addEventListener("click", function() {
        addBuyingContent(token, forms)
    })
}

const addBuyingContent = (token, forms) => {
    const modal = addModal()
    createTitle(modal, 'Comprar cotas')
    createForm(token, forms, modal)
}

const createSellingListener = (key, token, forms) => {
    var stockDiv = document.querySelector(`#${key}`)
    stockDiv.addEventListener("click", function() {
        addSellingContent(token, forms, `${key}`)
    })
}

const addSellingContent = (token, forms, code) => {
    const modal = addModal()
    createTitle(modal, `Vender cotas\n${code}`)
    createForm(token, forms, modal, code)
}

const createForm = (token, forms, content, code=null) => {
    const formInput = document.createElement('form')
    formInput.classList.add('form-group')
    formInput.action = '/update-wallet'
    formInput.method = 'post'
    formInput.id = code == null? 'buy-stocks' : 'sell-stocks'

    formInput.innerHTML = token
    formInput.innerHTML += forms

    content.appendChild(formInput)
    code == null ? classifyTransaction('buy') : lockStockCode(code)
    createSubmissionBtn(formInput)
}

const classifyTransaction = method => {
    hiddenInput = document.querySelector('#id_action')
    hiddenInput.value = method
}

const lockStockCode = code => {
    codeInput = document.querySelector('#id_code')
    codeInput.value = code
    codeInput.type = 'hidden'
    classifyTransaction('sell')
}

const createSubmissionBtn = inputElement => {
    const submissionBtn = document.createElement('input')
    submissionBtn.id = 'input-btn'
    submissionBtn.type = 'submit'
    submissionBtn.value = 'Confirmar'
    submissionBtn.classList.add('btn','shadow','btn-full')

    inputElement.appendChild(submissionBtn)
}

const populateStocks = (stocks, token, forms) => {
    for (key in stocks) {
        new StockObject(stocks[key], key)
        createSellingListener(key, token, forms)
    }
    writeSummary(stocks)   
}

const writeSummary = stocks => {
    let walletInvestment = 0
    let walletValue = 0
    const parag = document.querySelector('#info')

    for (s in stocks) {
        walletInvestment += stocks[s].price * stocks[s].quantity
        walletValue += stocks[s].value * stocks[s].quantity
    }
    parag.innerText = `🧾 R$${walletInvestment.toFixed(2)} | R$${walletValue.toFixed(2)} 📊`
}

const highlightStocks = stocks => {
    for (s in stocks) {
        let tag = document.querySelector(`#${s} div`)
        let recommendation = stocks[s].recommended ? 'buy' : 'sell'
        tag.classList.add(recommendation)
    }    
}

const buildRecommendation = (wallet, recommendation) => {
    let inWallet = Object.keys(wallet)
    let inRecommendations = Object.keys(recommendation)
    let toRecommend = inRecommendations.filter(s => inWallet.indexOf(s) === -1)
    toRecommend.length > 0 ? listStocks(toRecommend, recommendation) : returnEmpty()
}

const listStocks = (toAdd, stockData) => {
    let recDiv = document.querySelector('#recommendations')
    for (let s of toAdd) {
        let stockDiv = document.createElement('div')
        stockDiv.id = `rec-${s}`
        stockDiv.classList.add('db-results', 'p-card', 'shadow', 'p-24')
        createStockRecCard(stockDiv, s, stockData[s])
        recDiv.appendChild(stockDiv)
    }
}

const createStockRecCard = (parentDiv, code, stock) => {
    let card = document.createElement('div')
    card.classList.add('card-btn')

    parentDiv.appendChild(card)
    addCardDetails(card, code, stock)
}

const addCardDetails = (parentDiv, code, stock) => {
    let pCode = document.createElement('p')
    pCode.classList.add('s9', 'str', 'blue', 'm-b-0')
    pCode.innerText = `${code}`
    parentDiv.appendChild(pCode)
    
    let price = document.createElement('p')
    price.classList.add('s9', 'light-gray', 'm-0')
    price.innerText = `R$${stock.price.toFixed(2)}`
    parentDiv.appendChild(price)

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
    emptyDiv.classList.add('db-results', 'p-card-empty', 'm-b-24', 'p-24')
    
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