class EditModal {
    constructor(type){
        this.type = type
        this.modal = this.addInputModal()
        this.form = this.createForm()
        this.addCurrentDate()
        this.addFormBtn()
    }

    addInputModal = () => {
        const modal = addModal()
        const title = 'Editar'
        createTitle(modal, title)
        return modal
    }

    createForm = () => {
        const form = document.createElement('form')
        form.classList.add('form-group')
        form.action = `/update-${this.type}`
        form.method = 'post'
    
        form.innerHTML = token
        form.innerHTML += forms
    
        this.modal.appendChild(form)
        return form
    }

    addCurrentDate = () => {
        const date = document.querySelector('#id_date')
        date != undefined ? this.stringDate(date) : null
        
    }

    stringDate = input => {
        const date = new Date()
        const yyyy = String(date.getFullYear())
        const mm = String(date.getMonth() + 1).padStart(2, '0')
        const dd = String(date.getDate()).padStart(2, '0')
        input.value =  `${yyyy}-${mm}-${dd}`
    }

    addFormBtn = () => {
        const btn = document.createElement('input')
        btn.type = 'submit'
        btn.value = 'Salvar'
        btn.classList.add('shadow', 'btn')
        this.form.appendChild(btn)
    }

    addDestroyBtn = (id) => {
        const btn = document.createElement('a')
        btn.href = `/destroy-${this.type}?id=${id}`
        btn.innerText = 'Remover'
        btn.classList.add('shadow', 'btn', 'clean-a', 'danger')
        this.form.appendChild(btn)
    }
}

class ExpenseModal {
    constructor(obj=null) {
        this.html = new EditModal('expense')
        this.obj = obj
        this.fullfillForm()
    }

    fullfillForm = () => {
        const id = document.querySelector('#id_id')
        id.value = this.obj.id
        
        const name = document.querySelector('#id_name')
        name.value = this.obj.name

        const type = document.querySelector('#id_type')
        type.value = this.obj.type

        const value = document.querySelector('#id_value')
        value.value = this.obj.value

        const date = document.querySelector('#id_date')
        date.value = this.obj.date

        this.html.addDestroyBtn(this.obj.id)
    }
}

class RecurringModal {
    constructor(obj=null) {
        this.html = new EditModal('expense')
        this.obj = obj
        this.fullfillForm()
    }

    fullfillForm = () => {
        const id = document.querySelector('#id_id')
        id.value = this.obj.id
        
        const name = document.querySelector('#id_name')
        name.value = this.obj.name

        const type = document.querySelector('#id_type')
        type.value = this.obj.type

        const value = document.querySelector('#id_value')
        value.value = this.obj.value

        const date = document.querySelector('#id_active')
        date.checked = this.obj.active

        this.html.addDestroyBtn(this.obj.id)
    }
}

class GoalModal {
    constructor(obj=null) {
        this.html = new EditModal('expense')
        this.obj = obj
        this.form = this.html.form
        this.fullfillForm()
    }

    fullfillForm = () => {
        const id = document.querySelector('#id_id')
        id.value = this.obj.id
        
        const name = document.querySelector('#id_date')
        name.value = this.obj.date

        const type = document.querySelector('#id_savings')
        type.value = this.obj.saving

        const value = document.querySelector('#id_expenses')
        value.value = this.obj.expense

        this.html.addDestroyBtn(this.obj.id)
    }
}

class SavingModal {
    constructor(obj=null) {
        this.html = new EditModal('expense')
        this.obj = obj
        this.form = this.html.form
        this.fullfillForm()
    }

    fullfillForm = () => {
        const id = document.querySelector('#id_id')
        id.value = this.obj.id
        
        const name = document.querySelector('#id_name')
        name.value = this.obj.name

        const type = document.querySelector('#id_objective')
        type.value = this.obj.objective

        const value = document.querySelector('#id_value')
        value.value = this.obj.value

        const date = document.querySelector('#id_date')
        date.value = this.obj.date

        this.html.addDestroyBtn(this.obj.id)
    }
}
