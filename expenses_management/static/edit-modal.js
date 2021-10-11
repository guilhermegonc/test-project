class EditModal {
    constructor(type, obj=null){
        this.type = type
        this.obj = obj
        this.modal = this.addInputModal()
        this.form = this.createForm()
        this.addFormBtn()
        this.prefillForm()
        this.obj != null ? this.fullfillForm() : null
        this.addTypeHelper()
    }

    addInputModal = () => {
        const modal = addModal()
        const title = this.obj != null ? 'Editar' : 'Adicionar'
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
    
    addFormBtn = () => {
        const btn = document.createElement('input')
        btn.type = 'submit'
        btn.value = 'Salvar'
        btn.classList.add('shadow', 'btn')
        this.form.appendChild(btn)
    }

    prefillForm = () => {
        const id = document.querySelector('#id_id')
        id.value = 0

        this.addCurrentDate()
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

    fullfillForm = () => {
        const fields = {
            'id': this.obj.id,
            'name': this.obj.name,
            'type': this.obj.type,
            'value': this.obj.value,
            'date': this.obj.date,
            'recurring': this.obj.recurring,
            'active': this.obj.active,
            'expenses': this.obj.expenses,
            'savings': this.obj.savings,
            'objective': this.obj.objective,
        }

        for (const [key, value] of Object.entries(fields)) {
            this.fullfillInput(key, value)
        }
        this.addDestroyBtn()
    }

    fullfillInput = (identifier, objectValue) => {
        const input = document.querySelector(`#id_${identifier}`)
        if (input != null) {
            input.value = objectValue
        }
    }

    addDestroyBtn = () => {
        const btn = document.createElement('a')
        btn.href = `/destroy-${this.type}?id=${this.obj.id}`
        btn.innerText = 'Remover'
        btn.classList.add('shadow', 'btn', 'clean-a', 'danger')
        this.form.appendChild(btn)
    }

    addTypeHelper = () => {
        const name = document.querySelector('#id_name')
        name.addEventListener('blur', function () {
            searchTypeMatch(name.value.toLowerCase())
        })
    }
}