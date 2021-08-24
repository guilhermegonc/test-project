class StockObject {
    constructor (code) {
        this.code = code
        this.htmlCard = document.querySelector(`#${code}`)
        this.value = this.getValue()
    }

    getValue = async() => {
        let apiKey = ''
        let func = 'TIME_SERIES_DAILY'
        let size = 'full'
        // let uri = `https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=BIDI11.SA&apikey=${apiKey}`
        // this.value = await fetch(uri)
        // this.value = await this.value.json()
        // console.log(this.value)
        this.parseValue(this.value)
    }

    parseValue = () => {
        // this.value = this.value['Time Series (Daily)'] 
        // let mostRecent = Object.keys(this.value).sort().pop()
        // this.value = this.value[mostRecent]['4. close']
        this.addValue()
    }

    addValue = () => {
        let lastClose = document.createElement('p')
        lastClose.classList.add('s9','light-gray','m-0')
        lastClose.innerText = 'Atualizar Função'
        this.htmlCard.appendChild(lastClose)
    }
}