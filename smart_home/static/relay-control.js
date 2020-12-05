class BlynkObject {
    constructor (token, pin, htmlId) {
        this.token = token
        this.pin = pin
        this.status = this.getStatus()
        this.htmlCard = document.querySelector(`#${htmlId} div.status`)
        this.htmlCard.onclick = () => this.changeStatus()
    }
    
    getStatus = async() => {
        let uri = `http://blynk-cloud.com/${this.token}/get/${this.pin}`
        this.status = await fetch(uri)
        this.status = await this.status.json() == "1"
        this.changeText()
    }

    changeStatus = async () => {
        this.status = !this.status
        let uri = `http://blynk-cloud.com/${this.token}/update/${this.pin}?value=${this.status*1}`
        await fetch(uri)
        this.changeText()
    }

    changeText = () => {
        this.htmlCard.innerText = this.status == true ? '💡' : '🔌'
    }
}