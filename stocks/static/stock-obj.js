class StockObject {
    constructor (stockObj, code, divID) {
        this.code = code
        this.stockObj = stockObj
        this.card = this.createCard(divID)
        this.dataDiv = this.createDataDiv()
        this.cardCode = this.addCardCode()
        this.cardPrice = this.addCardPrice()
        this.relativeData = this.addRelativeData()
        this.extraData = this.addExtraData()
        this.label = this.addLabel()
    }

    createCard = divID => {
        const stockList = document.querySelector(`#${divID}`)
        const card = document.createElement('div')        
        card.id = `rec-${this.code}`
        card.classList.add('db-results', 'p-card', 'shadow', 'p-24', 'm-l-a', 'm-r-a', 'm-b-12')
        stockList.appendChild(card)
        return card
    }

    createDataDiv = () => {
        const cardBtn = document.createElement('div')
        cardBtn.classList.add('card-btn')
        this.card.appendChild(cardBtn)
        return cardBtn
    }

    addCardCode = () => {
        const a = document.createElement('a')
        a.id = `search-${this.code}`
        a.classList.add('s9', 'str', 'blue', 'm-0', 'clean-a')
        a.innerText = `${this.code}`
        this.card.appendChild(a)
        return a
    }

    addCardPrice = () => {
        const price = document.createElement('p')
        price.classList.add('s9', 'light-gray', 'm-0')
        price.innerText = `R$${this.stockObj.price.toFixed(2)}`
        this.card.appendChild(price)
        return price
    }

    addRelativeData = () => {
        const p = document.createElement('p')
        this.card.appendChild(p)
        return p
    }

    addExtraData = () => {
        const balance = document.createElement('a')
        balance.id = `balance-${this.code}`
        balance.classList.add('s9', 'str', 'blue', 'fl-r', 'clean-a')
        this.card.insertBefore(balance, this.card.firstChild)
        return balance
    }

    comparePrice = () => {
        const growth = this.stockObj.value === 0 ? 0 : ((this.stockObj.value - this.stockObj.price) / this.stockObj.value * 100).toFixed(2)
        const color = growth >= 0 ? 'green' : 'red'
        this.relativeData.innerText = `R$${this.stockObj.value} (${growth}%)`
        this.relativeData.classList.add(color, 's9', 'm-0', 'str')
    }

    addLabel = () => {
        const tag = document.createElement('div')
        tag.id = `tag-${this.code}`
        tag.classList.add('recommendation-tag')
        this.card.insertBefore(tag, this.card.firstChild)
        return tag
    }

    addValue = () => {
        const balanceStock = (this.stockObj.quantity * this.stockObj.value).toFixed(2)
        this.extraData.innerText = `R$${balanceStock} (${this.stockObj.quantity})`
    }

    addRecommendedTransaction = () => {
        const colorClass = this.stockObj.recommended ? 'buy' : 'sell'
        this.label.classList.add(colorClass)
    }

    addTransactionListener = method => {
        const action = method === 'buy' ? 'Comprar' : 'Vender'
        const title = `${action} cotas ${this.code}`
        const code = this.code
        this.card.addEventListener('click', function () {
            new TransactionModal(title, method)
            const inp = document.querySelector('#id_code')
            inp.value = code
            inp.type = 'hidden'
        })
    }

    compareGrowth = () => {
        const growthValue = (this.stockObj.growth * 100).toFixed(2)
        console.log(growthValue)
        const color = growthValue > 0 ? 'green' : 'red'
        console.log(color)
        this.relativeData.classList.add('s9', 'light-gray', 'm-0', 'str', color)
        this.relativeData.innerText = `${growthValue}% (6 meses)`
    }

    highlightNotInWallet = stockCodes => {
        const inWallet = stockCodes.indexOf(this.code) != -1
        const colorClass = inWallet ? 'old-stock' : 'new-stock'
        this.label.classList.add(colorClass)
    }

    addStatusLabel = () => {
        const colorClass = this.stockObj.active ? 'active-stock' : 'inactive-stock'
        this.label.classList.add(colorClass)
    }

    addStatusControl = () => {
        const text = this.stockObj.active ? '💡': '🔌'
        const status = !this.stockObj.active
        const uri = `change-recommendation-status?code=${this.code}&status=${status}`
        this.extraData.innerText = text
        this.extraData.classList.add('s6')
        this.extraData.classList.remove('s9')
        this.extraData.href = uri
    }

    addSearchLink = () => {
        this.cardCode.innerText += ' 📈'
        this.cardCode.href = `https://www.google.com/search?q=${this.code}`
        this.cardCode.target = 'blank'
    }
}