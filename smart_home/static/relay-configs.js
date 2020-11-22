const prepopulateFields = (pin, name, status) => {
    let p = document.querySelector('#id_pin:not(.populated)')
    p.value = pin
    p.disabled = true
    p.classList.add('populated')

    let n = document.querySelector('#id_name:not(.populated)')
    n.value = name != 'None' ? name : null
    n.classList.add('populated')

    let s = document.querySelector('#id_active:not(.populated)')
    s.checked = status === 'True'
    s.classList.add('populated')
}
