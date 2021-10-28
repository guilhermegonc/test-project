class TransactionModal {
    constructor (title) {
        this.title = title
        this.modal = this.addTransactionContent()
        this.form = this.createForm()
        this.btn = this.createSubmissionBtn()
        this.addIncrementControl()
    }

    addTransactionContent = () => {
        const modal = addModal()
        createTitle(modal, this.title)
        return modal
    }

    createForm = () => {
        const formInput = document.createElement('form')
        formInput.classList.add('form-group')
        formInput.action = '/update-wallet'
        formInput.method = 'post'
        formInput.id = 'buy-stocks'
    
        formInput.innerHTML = token
        formInput.innerHTML += forms
    
        this.modal.appendChild(formInput)
        return formInput
    }

    createSubmissionBtn = () => {
        const submissionBtn = document.createElement('input')
        const btnLabel = 'Salvar'
        submissionBtn.id = 'input-btn'
        submissionBtn.type = 'submit'
        submissionBtn.value = btnLabel
        submissionBtn.classList.add('btn','shadow','btn-full')
    
        this.form.appendChild(submissionBtn)
        return submissionBtn
    }

    setMethod = () => {
        const hiddenInput = document.querySelector('#id_action')
        const quantity = document.querySelector('#id_quantity').value
        hiddenInput.value = quantity > 0 ? 'buy' : 'sell'
        this.btn.value = quantity > 0 ? 'Comprar' : 'Vender'
    }

    addIncrementControl = () => {
        const input = document.querySelector('#id_quantity')
        const inc = document.createElement('span')
        const method = '+'
        inc.innerText = method        
        inc.classList.add('increment', 'fl-l')
        input.after(inc)

        inc.addEventListener('click', method => this.setQuantity(method, '+'))
        this.addDecrementControl(input)
    }

    addDecrementControl = input => {
        const dec = document.createElement('span')
        const method = '-'
        dec.innerText = method
        dec.classList.add('increment', 'fl-l')
        input.parentElement.insertBefore(dec, input)

        dec.addEventListener('click', method => this.setQuantity(method, '-'))
    }

    setQuantity = (method, action) => {
        const input = document.querySelector('#id_quantity')
        action === '+' ? input.value++ : input.value--
        this.setMethod()
    }
}