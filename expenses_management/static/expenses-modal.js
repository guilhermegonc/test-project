class ExpenseModal {
    constructor(expenseObj=null) {
        this.expenseObj = expenseObj
        this.addInputModal()
    }

    addInputModal = () => {
        const modal = addModal()
        const title = this.expenseObj === null ? 'Nova despesa' : 'Editar'
        createTitle(modal, title)
        this.createForm(modal)
    }

    createForm = modal => {
        const formInput = document.createElement('form')
        formInput.classList.add('form-group')
        formInput.action = '/update-expense'
        formInput.method = 'post'
        formInput.id = 'register-expense'
    
        formInput.innerHTML = token
        formInput.innerHTML += forms
    
        modal.appendChild(formInput)
        this.addFormBtn(formInput)

        this.expenseObj === null ? this.addEmptyExpense() : this.addExpenseData()
    }

    addEmptyExpense = () => {
        const date = new Date()
        const dd = String(date.getDate()).padStart(2, '0')
        const mm = String(date.getMonth() + 1).padStart(2, '0')
        const yyyy = String(date.getFullYear())

        const idInput = document.querySelector('#id_id')
        idInput.value = 0

        const dateInput = document.querySelector('#id_date')
        dateInput.value = `${yyyy}-${mm}-${dd}`
    }

    addExpenseData = () => {
        const id = document.querySelector('#id_id')
        id.value = this.expenseObj.id
        
        const name = document.querySelector('#id_name')
        name.value = this.expenseObj.name

        const type = document.querySelector('#id_type')
        type.value = this.expenseObj.type

        const date = document.querySelector('#id_date')
        date.value = this.expenseObj.date

        const value = document.querySelector('#id_value')
        value.value = this.expenseObj.value

        const recurring = document.querySelector('#id_recurring')
        recurring.checked = this.expenseObj.recurring

    }

    addFormBtn = div => {
        const btn = document.createElement('input')
        btn.id = 'expense-form-btn'
        btn.type = 'submit'
        btn.value = 'Adicionar despesa'
        btn.classList.add('shadow', 'btn')

        div.appendChild(btn)
    }
}
