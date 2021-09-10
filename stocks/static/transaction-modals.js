class TransactionModal {
    constructor (title, type) {
        this.title = title
        this.type = type
        this.addTransactionContent()
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
        this.addMethod()
    }

    createSubmissionBtn = inputElement => {
        const submissionBtn = document.createElement('input')
        submissionBtn.id = 'input-btn'
        submissionBtn.type = 'submit'
        submissionBtn.value = 'Confirmar'
        submissionBtn.classList.add('btn','shadow','btn-full')
    
        inputElement.appendChild(submissionBtn) 
    }

    addMethod = () => {
        const hiddenInput = document.querySelector('#id_action')
        hiddenInput.value = this.type
    }
}