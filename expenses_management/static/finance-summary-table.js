class SavingBalanceTable {
    constructor(div, values) {
        this.summary = new SummaryTable(div, values, 'saving-summary')
        this.summary.populateHeader('details-savings', 'Caixa', 'Saldo')
        this.summary.addTitle('details-savings', 'Economias (acumulado)')
    }
}

class ExpenseTypeTable {
    constructor(div, values) {
        this.summary = new SummaryTable(div, values, 'expense-summary')
        this.summary.populateHeader('details-expenses', 'Categoria', 'Soma (Média)')
        this.summary.addTitle('details-expenses', 'Gastos por categoria')
    }
}

class SummaryTable {
    constructor(div, values, type=null) {
        this.parent = div
        this.html = new Table(type)
        div.appendChild(this.html.table)        

        this.table = this.html.table
        this.header = this.html.header

        this.html.firstRow.remove()
        this.html.btn.remove()
        
        this.populateTable(values)
    }

    populateHeader = (id, name, value) => {
        const h = document.querySelectorAll(`#${id} table th`)
        h[0].innerText = name
        h[3].innerText = value
        h[1].remove()
        h[2].remove()
    }

    populateTable = data => {
        const keys  = Object.keys(data)
        keys.forEach((key, value) => {
            let row = document.createElement('tr')

            row.innerHTML = `
                <td class="s10 str main-column">${key}</td>
                <td id ="table-${key}-value" class="s9 light-gray m-0 t-right">${data[key]}</td>
            `
            this.html.table.appendChild(row)
        })
    }
    
    addTitle = (id, text) => {
        const details = document.querySelector(`#${id}`)

        const h3 = document.createElement('h3')
        h3.classList.add('s8', 'txt-center', 'p-24')
        h3.innerText = text

        details.insertBefore(h3, this.table)
        this.changeStyles(details)
    }

    changeStyles = parent => {
        parent.classList.add('summary-card', 'shadow', 'chart-card')
        this.table.classList.remove('shadow' , 'm-a')
    }
}
