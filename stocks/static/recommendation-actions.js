const createBalanceListener = recommended => {
    let bal = document.querySelector('#balance-btn')
    bal.addEventListener("click", function () {
        addBalanceContent(recommended)
    })
}

const addBalanceContent = (stocks) => {
    const modal = addModal()
    createTitle(modal, `Valor para distribuir`)
    createCustomInput(modal)
    addBalanceInputListener(stocks)
}

const createCustomInput = (parentDiv) => {
    let div = document.createElement('div')
    
    let form = document.createElement('form')
    form.id = 'balance'
    form.classList.add('m-b-24', 'db-results')
    div.appendChild(form)


    let inp = document.createElement('input')
    inp.type = 'number'
    inp.name = 'total'
    form.appendChild(inp)

    let btn = document.createElement('div')
    btn.id = 'balance-form-btn'
    btn.classList.add('shadow', 'btn', 'light')
    btn.innerText = 'Distribuir valores'
    form.appendChild(btn)

    parentDiv.appendChild(div)
}

const addBalanceInputListener = (recommended) => {
    let btn = document.querySelector('#balance-form-btn')
    btn.addEventListener("click", function() {
        distributeBalance(recommended)
    })
}