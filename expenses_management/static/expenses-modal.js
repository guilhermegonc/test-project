class ExpenseModal {
    constructor(apiObj=null) {
        this.apiObj = apiObj
        this.type = this.apiObj != null ? this.classifyObj() : null
        this.modal = this.addInputModal()
        this.form = this.createForm()
        this.apiObj != null ? this.addObjData() : this.addEmptyData()
    }

    classifyObj = () => {
        return this.apiObj.hasOwnProperty('recurring') ? 'expense' : 'recurring'
    }

    addInputModal = () => {
        const modal = addModal()
        const title = this.apiObj === null ? 'Nova despesa' : 'Editar'
        createTitle(modal, title)
        return modal
    }

    createForm = () => {
        const form = document.createElement('form')
        form.classList.add('form-group')
        form.action = this.type === 'expense' ? '/update-expense' : '/update-recurring'
        form.method = 'post'
        form.id = 'register'
    
        form.innerHTML = token
        form.innerHTML += forms
    
        this.modal.appendChild(form)
        this.addFormBtn(form)
        return form
    }

    addFormBtn = form => {
        const btn = document.createElement('input')
        const btnText = this.apiObj === null ? 'Registrar' : 'Atualizar'
        btn.id = 'form-btn'
        btn.type = 'submit'
        btn.value = btnText
        btn.classList.add('shadow', 'btn')
        form.appendChild(btn)
    }

    addEmptyData = () => {
        const idInput = document.querySelector('#id_id')
        idInput.value = 0

        const date = document.querySelector('#id_date')
        date != null ? date.value = this.addCurrentDate() : null
    }

    addCurrentDate = () => {
        const date = new Date()
        const day = String(date.getDate()).padStart(2, '0')
        const month = String(date.getMonth() + 1).padStart(2, '0')
        const year = String(date.getFullYear())
        return `${year}-${month}-${day}`
    }

    addObjData = () => {
        const id = document.querySelector('#id_id')
        id.value = this.apiObj.id
        
        const name = document.querySelector('#id_name')
        name.value = this.apiObj.name

        const type = document.querySelector('#id_type')
        type.value = this.apiObj.type

        const value = document.querySelector('#id_value')
        value.value = this.apiObj.value

        const date = document.querySelector('#id_date')
        date != null ? date.value = this.apiObj.date : null

        const active = document.querySelector('#id_active')
        active != null ? this.apiObj.active : null

        const recurring = document.querySelector('#id_active')
        recurring != null ? this.apiObj.recurring : null

        this.addDestroyBtn()
    }

    addDestroyBtn = () => {
        const btn = document.createElement('a')
        const uri = this.type === 'expense' ? 'destroy-expense' : 'destroy-recurring'
        btn.id = 'destroy-btn'
        btn.href = `/${uri}?id=${this.apiObj.id}`
        btn.innerText = 'Remover'
        btn.classList.add('shadow', 'btn', 'clean-a', 'danger')
        this.form.appendChild(btn)
    }
}
