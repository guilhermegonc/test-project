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
