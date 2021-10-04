const addInputModal = () => {
    const modal = addModal()
    createTitle(modal, `Nova despesa`)
    // createCustomForm(modal)
    // addBalanceInputListener()
}

const createCustomForm = parentDiv => {
    const div = document.createElement('div')
    const form = document.createElement('form')    
    form.id = 'balance'
    form.classList.add('m-b-24', 'db-results')
    div.appendChild(form)
    addCustomInput(form)
    parentDiv.appendChild(div)
}

const addCustomInput = parentDiv => {
    const inp = document.createElement('input')
    inp.type = 'number'
    inp.name = 'total'
    parentDiv.appendChild(inp)
    addFormBtn(parentDiv)
}

const addFormBtn = parentDiv => {
    const btn = document.createElement('div')
    btn.id = 'balance-form-btn'
    btn.classList.add('shadow', 'btn')
    btn.innerText = 'Distribuir valores'
    parentDiv.appendChild(btn)
}

const addBalanceInputListener = () => {
    let btn = document.querySelector('#balance-form-btn')
    btn.addEventListener("click", function() {
        distributeBalance()
        close()
    })
}
