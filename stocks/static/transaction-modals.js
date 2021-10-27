class TransactionModal {
    constructor (title, type) {
        this.title = title
        this.type = type
        this.addTransactionContent()
        this.addIncrementControl()
    }

    addTransactionContent = () => {
        const modal = addModal()
        createTitle(modal, this.title)
        this.createForm(modal)
    }

    createForm = modal => {
        const formInput = document.createElement('form')
        formInput.classList.add('form-group')
        formInput.action = '/update-wallet'
        formInput.method = 'post'
        formInput.id = 'buy-stocks'
    
        formInput.innerHTML = token
        formInput.innerHTML += forms
    
        modal.appendChild(formInput)
        this.createSubmissionBtn(formInput)
        this.setMethod()
    }

    createSubmissionBtn = inputElement => {
        const submissionBtn = document.createElement('input')
        const btnLabel = 'Salvar'
        submissionBtn.id = 'input-btn'
        submissionBtn.type = 'submit'
        submissionBtn.value = btnLabel
        submissionBtn.classList.add('btn','shadow','btn-full')
    
        inputElement.appendChild(submissionBtn) 
    }

    setMethod = () => {
        const hiddenInput = document.querySelector('#id_action')
        const quantity = document.querySelector('#id_quantity').value
        hiddenInput.value = quantity > 0 ? 'buy' : 'sell'
    }

    addIncrementControl = () => {
        const input = document.querySelector('#id_quantity')
        
        const inc = document.createElement('span')
        const method = '+'
        inc.innerText = method        
        inc.classList.add('increment', 'fl-l')
        input.parentElement.insertBefore(inc, input)

        inc.addEventListener('click', method => this.setQuantity(method, '+'))
        this.addDecrementControl(input)
    }

    addDecrementControl = input => {
        const dec = document.createElement('span')
        const method = '-'
        dec.innerText = method
        dec.classList.add('increment', 'fl-l')
        input.after(dec)

        dec.addEventListener('click', method => this.setQuantity(method, '-'))
    }

    setQuantity = (method, action) => {
        const input = document.querySelector('#id_quantity')
        action === '+' ? input.value++ : input.value--
        this.setMethod()
    }
}