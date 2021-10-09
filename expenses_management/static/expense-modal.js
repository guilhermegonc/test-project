class ExpenseModal {
    constructor(obj=null) {
        this.html = new EditModal('expense')
        this.obj = obj
        this.obj != null ? this.fullfillForm() : null
        this.addTypeHelper()
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

        const recurring = document.querySelector('#id_recurring')
        recurring.value = this.obj.recurring

        this.html.addDestroyBtn(this.obj.id)
    }

    addTypeHelper = () => {
        const name = document.querySelector('#id_name')
        name.addEventListener('blur', function () {
            console.log('type')
        })
    }
}
