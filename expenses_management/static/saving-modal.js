class SavingModal {
    constructor(obj=null) {
        this.html = new EditModal('saving')
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
