class RecommendedObject {
    constructor(stockObj, code) {
        this.code = code
        this.stockObj = stockObj
        this.createCard()
    }

    createCard = () => {
        const recDiv = document.querySelector('#recommendations')
        const stockDiv = document.createElement('div')        
        stockDiv.id = `rec-${this.code}`
        stockDiv.classList.add('db-results', 'p-card', 'shadow', 'p-24', 'm-l-a', 'm-r-a', 'm-b-12')
        recDiv.appendChild(stockDiv)
        this.createContainer(stockDiv)
    }

    createContainer = parentDiv => {
        const card = document.createElement('div')
        card.classList.add('card-btn')
        this.labelCard(card)
        this.addCardDetails(card)
        parentDiv.appendChild(card)
    }

    labelCard = parentDiv => {
        const tag = document.createElement('div')
        tag.id = `tag-${this.code}`
        tag.classList.add('recommendation-tag')
        parentDiv.appendChild(tag)
    }

    addCardDetails = (parentDiv) => {
        this.addRecommendationBalance(parentDiv)
        this.addCardCode(parentDiv)
        this.addCardPrice(parentDiv)
    }

    addRecommendationBalance = parentDiv => {
        const balance = document.createElement('a')
        balance.id = `balance-${this.code}`
        balance.classList.add('s9', 'str', 'blue', 'fl-r', 'clean-a')
        parentDiv.appendChild(balance)
    }

    addCardCode = parentDiv => {
        const aCode = document.createElement('a')
        aCode.id = `search-${this.code}`
        aCode.classList.add('s9', 'str', 'blue', 'm-0', 'clean-a')
        aCode.innerText = `${this.code}`
        parentDiv.appendChild(aCode)
    }

    addCardPrice = parentDiv => {
        const price = document.createElement('p')
        price.classList.add('s9', 'light-gray', 'm-0')
        price.innerText = `R$${this.stockObj.price.toFixed(2)}`
        parentDiv.appendChild(price)
        this.addGrowthData(parentDiv)
    }

    addGrowthData = parentDiv => {
        const growth = document.createElement ('p')
        const growthValue = (this.stockObj.growth * 100).toFixed(2)
        const color = growthValue > 0 ? 'green' : 'red'
        growth.classList.add('s9', 'light-gray', 'm-0', 'str', color)
        growth.innerText = `${growthValue}% (6 meses)`
        parentDiv.appendChild(growth)
    }

    fullfillTag = hClass => {
        const div = document.querySelector(`#tag-${this.code}`)
        div.classList.add(hClass)
    }

    addStatusControl = () => {
        const icon = document.querySelector(`#balance-${this.code}`)
        const status = !this.stockObj.active
        const uri = `change-recommendation-status?code=${this.code}&status=${status}`
        icon.innerText = status ? '🔌' : '💡'
        icon.classList.add('s6')
        icon.classList.remove('s9')
        icon.href = uri
        this.addSearchLink()
    }

    addSearchLink = () => {
        const a = document.querySelector(`#search-${this.code}`)
        a.innerText += ' 📈'
        a.href = `https://www.google.com/search?q=${this.code}`
        a.target = 'blank'
    }
}