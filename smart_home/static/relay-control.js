const token = '1wSjC7iMMcKzvku4g-mGpOLPQzpQgLu0'
const pin = 'D2'
let lampOn = getLampStatus();

async function getLampStatus() {
    let url = `http://blynk-cloud.com/${token}/get/${pin}`
    let status = await fetch(url)
    status = await status.json() == "1"
    changeText()
}

const setRelay = () => {
    let lampObj = document.querySelector('#lamp')
    lampObj.onclick = () => changeStatus()
}

const changeStatus = () => {
    lampOn = !lampOn
    changePin(lampOn)
}

const changePin = (status) => {
    let newVal = status == true ? '1' : '0'
    let url = `http://blynk-cloud.com/${token}/update/${pin}?value=${newVal}`
    fetch(url)
    changeText()
}

const changeText = () => {
    let lampObj = document.querySelector('#lamp')
    newVal = lampOn == true ? '💡' : '🔌'    
    lampObj.innerText = newVal
}
