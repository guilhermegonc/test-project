class pinObject {
    constructor(id, pin, name, status) {
        this.id = id
        this.pin = pin
        this.name = name
        this.status = status
    }
}

const populateFields2 = (pinObj) => {
    let d = document.querySelector('#device_id')
    d.value = pinObj['id']

    let p = document.querySelector('#id_pin')
    p.value = pinObj['pin']

    let n = document.querySelector('#id_name')
    n.value = pinObj['name'] == '' ? writePlaceholder(n) : pinObj['name']

    let s = document.querySelector('#id_active')
    s.checked = pinObj['status'] === 'True'
}

const writePlaceholder = (form) => {
    form.placeholder = 'Dê um nome para diferenciar os aparelhos.'
    return ''
}

const startListener = (pins) => {
    populateFields2(pins['D0'])    
    let pin = document.querySelector('#id_pin')
    pin.onchange = () => {
        let pinVal = pins[pin.value]
        populateFields2(pinVal)
    }
}