const addBuyingContent = (token, forms) => {
    const modal = addModal()
    createTitle(modal, 'Comprar cotas')
    createForm(token, forms, modal)
}

const createForm = (token, forms, content, code=null) => {
    const formInput = document.createElement('form')
    formInput.classList.add('form-group')
    formInput.action = '/update-wallet'
    formInput.method = 'post'
    formInput.id = code == null? 'buy-stocks' : 'sell-stocks'

    formInput.innerHTML = token
    formInput.innerHTML += forms

    content.appendChild(formInput)
    code == null ? classifyTransaction('buy') : lockStockCode(code)
    createSubmissionBtn(formInput)
}

const classifyTransaction = (method) => {
    hiddenInput = document.querySelector('#id_action')
    hiddenInput.value = method
}

const lockStockCode = (code) => {
    codeInput = document.querySelector('#id_code')
    codeInput.value = code
    codeInput.type = 'hidden'
    classifyTransaction('sell')
}

const createSubmissionBtn = inputElement => {
    const submissionBtn = document.createElement('input')
    submissionBtn.id = 'input-btn'
    submissionBtn.type = 'submit'
    submissionBtn.value = 'Confirmar'
    submissionBtn.classList.add('btn','shadow','btn-full')

    inputElement.appendChild(submissionBtn)
}

const addSellingContent = (token, forms, code) => {
    const modal = addModal()
    createTitle(modal, `Vender cotas\n${code}`)
    createForm(token, forms, modal, code)
}
