const addInputModal = () => {
    const modal = addModal()
    createTitle(modal, `Nova despesa`)
    createCustomForm(modal)
    addListener()
}

const createCustomForm = div => {
    div.innerHTML += `
    <div>
        <form id="expenses" class="m-b-24 db-results">${forms}</form>
    </div>
    `
    addFormBtn(div)
}

const addFormBtn = div => {
    const btn = document.createElement('div')
    btn.id = 'expense-form-btn'
    btn.classList.add('shadow', 'btn')
    btn.innerText = 'Adicionar despesa'
    div.appendChild(btn)
}

const addListener = () => {
    const btn = document.querySelector('#expense-form-btn')
    btn.addEventListener("click", function() {
        close()
    })
}
