class EditModal {
    constructor(type){
        this.type = type
        this.modal = this.addInputModal()
        this.form = this.createForm()
        this.addID()
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

    addID = () => {
        const id = document.querySelector('#id_id')
        id.value = 0
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
