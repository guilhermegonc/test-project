let lampOn = true;

const setRelay = () => {
    let lampObj = document.querySelector('#lamp')
    lampObj.onclick = () => changeText(lampObj)
}

const changeText = (appliance) => {
    newVal = lampOn === true ? '💡' : '🔌'
    appliance.innerText = newVal
    changeStatus()
}

const changeStatus = () => lampOn = !lampOn