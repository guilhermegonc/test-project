class SavingBalanceTable {
    constructor(div) {
        this.parent = div
        this.html = new Table('saving-summary')
        div.appendChild(this.html.table)        

        this.table = this.html.table
        this.header = this.html.header

        this.html.firstRow.remove()
        this.html.btn.remove()
        
        this.populateHeader()
        this.populateTable(savingBalances)
    }

    populateHeader = () => {
        const h = document.querySelectorAll('th')
        h[0].innerText = 'Reservas'
        h[3].innerText = 'Total'
        h[1].remove()
        h[2].remove()
    }

    populateTable = data => {
        const keys  = Object.keys(data)
        keys.forEach((key, value) => {
            let row = document.createElement('tr')

            row.innerHTML = `
                <td class="s10 str main-column">${key}</td>
                <td class="s9 light-gray m-0 t-right">R$ ${data[key].toFixed(2)}</td>
            `
            this.html.table.appendChild(row)
        })
    }
    
    addTitle = id => {
        const details = document.querySelector(`#${id}`)

        const h3 = document.createElement('h3')
        h3.classList.add('s8', 'txt-center', 'p-12')
        h3.innerText = 'Economias'

        details.insertBefore(h3, this.table)
        this.changeStyles(details)
    }

    changeStyles = parent => {
        parent.classList.add('summary-card', 'shadow', 'chart-card')
        this.table.classList.remove('shadow' , 'm-a')
    }
}