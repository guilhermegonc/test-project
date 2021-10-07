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
