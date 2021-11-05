class SavingBalanceTable {
    constructor(div, values) {
        this.summary = new SummaryTable(div, values, 'saving-summary')
        this.summary.populateHeader('details-savings', 'Caixa', 'Saldo')
        this.summary.addTitle('details-savings', 'Economias (acumulado)')
        this.addCurrency()
    }

    addCurrency = () => {
        this.summary.values.forEach(key => {
            key.children[1].innerText = `R$ ${key.children[1].innerText}`
            key.children[1].classList.add('light-grey')
        })
    }
}

class ExpenseTypeTable {
    constructor(div, values) {
        this.summary = new SummaryTable(div, values, 'expense-summary')
        this.summary.populateHeader('details-expenses', 'Categoria', 'Soma (Média)')
        this.summary.addTitle('details-expenses', 'Gastos por categoria')
        this.addCurrency()
    }
    
    addCurrency = () => {
        let values
        this.summary.values.forEach(key => {
            values = key.children[1].innerText.split(',')
            key.children[1].innerText = `R$ ${values[0]}\n(R$ ${values[1]})`
            this.colorCell(key, values[0], values[1])
        })
    }

    colorCell = (cell, value, average) => {
        value = parseFloat(value)
        average = parseFloat(average)
        const color = value < average || value <= 0 ? 'green' : 'red'
        cell.classList.add(color)
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
        
        this.values = this.populateTable(values)
    }

    populateHeader = (id, name, value) => {
        const h = document.querySelectorAll(`#${id} table th`)
        h[0].innerText = name
        h[3].innerText = value
        h[1].remove()
        h[2].remove()
    }

    populateTable = data => {
        const values = []
        const keys  = Object.keys(data)
        keys.forEach((key) => {
            let row = document.createElement('tr')
            
            let tdName = document.createElement('td')
            tdName.classList.add('s10', 'str', 'main-column')
            tdName.innerText = key
            row.appendChild(tdName)

            let tdValue =  document.createElement('td')
            tdValue.classList.add('s9', 'm-0', 't-right')
            tdValue.innerText = data[key]
            row.appendChild(tdValue)

            values.push(row)
            this.html.table.appendChild(row)
        })
        return values
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
