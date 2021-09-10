class StockObject {
    constructor (stockObj, code) {
        this.htmlCard = document.querySelector(`#${code}`)
        this.code = code
        this.stockObj = stockObj
        this.addInfo()
        this.addListener(code)
    }

    addInfo = () => {
        this.addBalance()
        this.addCode()
        this.addPrice()
        this.highlightRecommendation()
    }

    addListener = code => this.htmlCard.addEventListener("click", function () {
        const title = `Vender cotas ${code}`
        new TransactionModal(title, 'sell')
    })

    addBalance = () => {
        let balance = (this.stockObj.value * this.stockObj.quantity).toFixed(2)
        let pBalance = document.createElement('p')
        pBalance.classList.add('s9', 'str', 'blue', 'm-0', 'fl-r')
        pBalance.innerText = `R$${balance} (${this.stockObj.quantity}) `
        
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
        pDiv.innerText = `R$${this.stockObj.price} un.`
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
        let growth = ((this.stockObj.value - this.stockObj.price) / this.stockObj.value * 100).toFixed(2)
        let color = growth >= 0 ? 'green' : 'red'
        paragraph.innerText = `R$${this.stockObj.value} (${growth}%)`
        paragraph.classList.add(color, 'str')
    }

    highlightRecommendation = () => {
        let recClass = this.stockObj.recommended === true ? 'buy' : 'sell'
        let recDiv = document.querySelector(`#${this.code} div`)
        recDiv.classList.add(recClass)
    }
}
