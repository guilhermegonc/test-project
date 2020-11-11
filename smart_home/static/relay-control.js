let status
let lampObj

const startApp = (tkn, pin) => {
    lampObj = document.querySelector('#lamp')
    status = getLampStatus(tkn, pin)
    listenRelay(tkn, pin)
}

const getLampStatus = async (tkn, pin) => {
    let url = `http://blynk-cloud.com/${tkn}/get/${pin}`
    status = await fetch(url)
    status = await status.json() == "1"
    changeText()
}

const changeText = () => lampObj.innerText = status == true ? '💡' : '🔌'

const listenRelay = (tkn, pin) => lampObj.onclick = () => changePin(tkn, pin)

const changePin = async (tkn, pin) => {
    status = !status
    let newVal = status == true ? '1' : '0'
    let url = `http://blynk-cloud.com/${tkn}/update/${pin}?value=${newVal}`
    await fetch(url)
    changeText()
}
