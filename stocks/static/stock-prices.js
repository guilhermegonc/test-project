class StockObject {
    constructor (stockObj, code) {
        this.code = code
        this.price = stockObj.price
        this.quantity = stockObj.quantity
        this.value = stockObj.value
        this.htmlCard = document.querySelector(`#${this.code}`)
        this.addInfo()
    }

    addInfo = () => {
        let balance = (this.value * this.quantity).toFixed(2)
        let pDiv = document.createElement('p')
        pDiv.classList.add('s9', 'str', 'blue', 'm-b-0')
        pDiv.innerText = `${this.code} - R$${balance}`
        this.htmlCard.appendChild(pDiv)
        this.addPrice()
    }

    addPrice = () => {
        let pDiv = document.createElement('p')
        pDiv.classList.add('s9', 'light-gray', 'm-0')
        pDiv.innerText = `R$${this.price} (${this.quantity} un.)`
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
}
