class StockObject {
    constructor (stockObj, code) {
        this.code = code
        this.price = stockObj.price
        this.quantity = stockObj.quantity
        this.value = stockObj.value
        this.recommended = stockObj.recommended
        this.htmlCard = document.querySelector(`#${this.code}`)
        this.addInfo()
        this.highlightRecommendation()
    }

    addInfo = () => {
        this.addBalance()
        this.addCode()
        this.addPrice()
    }

    addBalance = () => {
        let balance = (this.value * this.quantity).toFixed(2)
        let pBalance = document.createElement('p')
        pBalance.classList.add('s9', 'str', 'blue', 'm-0', 'fl-r')
        pBalance.innerText = `R$${balance} (${this.quantity}) `
        
        let icon = this.addEditIcon()
        pBalance.appendChild(icon)
        
        this.htmlCard.appendChild(pBalance)
    }

    addEditIcon = () => {
        let icon = document.createElement('i')
        icon.classList.add('material-icons', 'menu-icon')
        icon.innerText = 'edit'
        return icon
    }

    addCode = () => {
        let pCode = document.createElement('p')
        pCode.classList.add('s9', 'str', 'blue', 'm-0')
        pCode.innerText = `${this.code}`
        this.htmlCard.appendChild(pCode)
    }

    addPrice = () => {
        let pDiv = document.createElement('p')
        pDiv.classList.add('s9', 'light-gray', 'm-0')
        pDiv.innerText = `R$${this.price} un.`
        this.htmlCard.appendChild(pDiv)
        this.addValue()        
    }

    addValue = () => {
        let pDiv = document.createElement('p')
        pDiv.classList.add('s9','light-gray','m-0')
        this.htmlCard.appendChild(pDiv)
        let growth = this.compareResult(pDiv)

    }

    compareResult = (paragraph) => {
        let growth = ((this.value - this.price) / this.value * 100).toFixed(2)
        let color = growth >= 0 ? 'green' : 'red'
        paragraph.innerText = `R$${this.value} (${growth}%)`
        paragraph.classList.add(color, 'str')
    }

    highlightRecommendation = () => {
        let recClass = this.recommended === true ? 'buy' : 'sell'
        let recDiv = document.querySelector(`#${this.code} div`)
        recDiv.classList.add(recClass)
    }
}
