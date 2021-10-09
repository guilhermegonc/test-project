class Table {
    constructor(type) {
        this.table = this.createTable()
        this.header = this.createHeader()
        this.firstRow = this.addFirstRow(type)
        this.btn = this.addPaginationBtn()
    }

    createTable = () => {
        const table = document.createElement('table')
        table.classList.add('shadow', 'm-a')
        return table
    }

    createHeader = () => {
        const header = document.createElement('tr')
        header.innerHTML = `
            <th class="s10 main-column"></th>
            <th class="s10 hide-mobile"></th>
            <th class="s10 hide-mobile"></th>
            <th class="s10 t-right"></th>
            `
        this.table.appendChild(header)
        return header
    }

    addFirstRow = type => {
        const row = document.createElement('tr')
        row.innerHTML = `
            <td id="row-empty-state" class="s10 str gray"></td>
            <td class="s9 light-gray m-0 hide-mobile"></td>
            <td class="s9 light-gray m-0 hide-mobile"></td>
            <td class="s9 light-gray m-0 t-right"></td>
        `
        this.table.appendChild(row)
        row.addEventListener('click', function(){
            if (type === 'expense') {
                new ExpenseModal()
            }
            if (type === 'recurring') {
                new RecurringModal()
            }
            if (type === 'goal') {
                new GoalModal()
            }
            if (type === 'saving') {
                new SavingModal()
            }
        })
    }

    addPaginationBtn = () => {
        const td = document.createElement('td')
        const link = document.createElement('a')
        
        link.classList.add('btn', 'light')
        link.innerText = 'Carregar mais'
        
        td.colSpan = 4
        td.appendChild(link)        
        this.table.appendChild(td)
        return td
    }
}
