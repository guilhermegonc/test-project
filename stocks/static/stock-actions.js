const createSellingListener = (key, token, forms) => {
    var stockDiv = document.querySelector(`#${key}`)
    stockDiv.addEventListener("click", function() {
        addSellingContent(token, forms, `${key}`)
    })
}

const addSellingContent = (token, forms, code) => {
    const modal = addModal()
    createTitle(modal, `Vender cotas\n${code}`)
    createForm(token, forms, modal, code)
}

const createForm = (token=null, forms, content, code=null) => {
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

const classifyTransaction = method => {
    hiddenInput = document.querySelector('#id_action')
    hiddenInput.value = method
}

const lockStockCode = code => {
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

const createBuyingListener = (token, forms) => {
    let btn = document.querySelector('#buy-btn')
    
    btn.addEventListener("click", function() {
        addBuyingContent(token, forms)
    })
}

const addBuyingContent = (token, forms) => {
    const modal = addModal()
    createTitle(modal, 'Comprar cotas')
    createForm(token, forms, modal)
}
