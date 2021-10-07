class Table {
    constructor() {
        this.table = this.createTable()
        this.header = this.createHeader()
        this.firstRow = this.addFirstRow()
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

    addFirstRow = () => {
        const row = document.createElement('tr')
        row.innerHTML = `
            <td id="row-empty-state" class="s10 str main-column gray"></td>
            <td class="s9 light-gray m-0 hide-mobile"></td>
            <td class="s9 light-gray m-0 hide-mobile"></td>
            <td class="s9 light-gray m-0 t-right"></td>
            `
        this.table.appendChild(row)
        row.addEventListener('click', function(){
            new ExpenseModal()
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

    loadRows = async(uri) => {
        let response = await fetch(uri)
        response = await response.json()
        return response.data
    }
}

class ExpensesTable {
    constructor(div) {
        this.parent = div
        this.html = new Table()
        div.appendChild(this.html.table)        

        this.table = this.html.table
        this.header = this.html.header
        this.firstRow = this.html.firstRow
        this.btn = this.html.btn
        
        this.populateHeader()
        this.detailFirstRow()
        this.requestData()
        this.setupBtn()
    }

    populateHeader = () => {
        const h = document.querySelectorAll('th')
        h[0].innerText = 'Serviço'
        h[1].innerText = 'Tipo'
        h[2].innerText = 'Data'
        h[3].innerText = 'Valor'        
    }

    detailFirstRow = () => {
        const r = document.querySelectorAll('td')
        r[0].innerText = 'Adicionar despesa'
        r[3].innerText = 'R$ 00,00'        
    }

    requestData = async() => {
        const start = counter * 20
        const end = start + 20
        const uri = `load-expenses?start=${start}&end=${end}`
        
        const data = await this.html.loadRows(uri)
        expenses = expenses.concat(data)
        counter +=1
        this.populateTable(data)
    }
    
    populateTable = data => {
        for (let i = 0; i < data.length; i++) {
            let row = document.createElement('tr')
            let recurringDecoration = data[i].recurring === true ? '⏱' : ' '
            let valueDecoration = data[i].value > 0 ? 'red' : 'green'
            
            row.innerHTML = `
                <td class="s10 str main-column ${valueDecoration}">${data[i].name}</td>
                <td class="s9 light-gray m-0 hide-mobile">${data[i].type}</td>
                <td class="s9 light-gray m-0 hide-mobile">${data[i].date}</td>
                <td class="s9 light-gray m-0 ${valueDecoration} t-right">R$ ${data[i].value.toFixed(2)} ${recurringDecoration}</td>
            `
            this.table.insertBefore(row, this.btn)            
            row.addEventListener('click', function(){
                new ExpenseModal(expenses[i])
            })
        }
    }

    setupBtn = () => {
        this.btn.addEventListener('click', this.requestData)
    }
}

class RecurringTable {
    constructor(div) {
        this.html = new Table()
        div.appendChild(this.html.table)        
        
        this.table = this.html.table
        this.header = this.html.header
        this.firstRow = this.html.firstRow
        
        this.html.btn.remove()
        this.populateHeader()
        this.detailFirstRow()
        this.requestData()
    }

    populateHeader = () => {
        const h = document.querySelectorAll('th')
        h[0].innerText = 'Serviço'
        h[1].innerText = 'Tipo'
        h[2].remove()
        h[3].innerText = 'Valor'        
    }

    detailFirstRow = () => {
        const r = document.querySelectorAll('td')
        r[0].innerText = 'Registrar depesa'
        r[2].remove()
        r[3].innerText = 'R$ 00,00'        
    }

    requestData = async() => {
        const uri = 'load-recurring'    
        const data = await this.html.loadRows(uri)
        this.populateTable(data)
    }
    
    populateTable = data => {
        for (let i = 0; i < data.length; i++) {
            let row = document.createElement('tr')            
            let isActive = data[i].active === true ? '✅' : '❌'
            let valueDecoration = data[i].value > 0 ? 'red' : 'green'
            
            row.innerHTML = `
                <td class="s10 str main-column ${valueDecoration}">${data[i].name}</td>
                <td class="s9 light-gray m-0 hide-mobile">${data[i].type}</td>
                <td class="s9 light-gray m-0 ${valueDecoration} t-right">R$ ${data[i].value.toFixed(2)} ${isActive}</td>
            `
            this.table.appendChild(row)
            row.addEventListener('click', function(){
                new ExpenseModal(data[i])
            })
        }
    }
}

class GoalsTable {
    constructor(div) {
        this.parent = div
        this.html = new Table()
        div.appendChild(this.html.table)

        this.table = this.html.table
        this.header = this.html.header
        this.firstRow = this.html.firstRow
        
        this.html.btn.remove()
        this.populateHeader()
        this.detailFirstRow()
        this.requestData()
    }

    populateHeader = () => {
        const h = document.querySelectorAll('th')
        h[0].innerText = 'Mês'
        h[1].innerText = 'Despesas'
        h[1].classList.remove('hide-mobile')
        h[2].innerText = 'Economias'
        h[2].classList.remove('hide-mobile')
        h[3].remove()        
    }

    detailFirstRow = () => {
        const r = document.querySelectorAll('td')
        r[0].innerText = 'Adicionar meta'
        r[2].remove()
    }

    requestData = async() => {
        const uri = 'load-goals'    
        const data = await this.html.loadRows(uri)
        console.log(data)
        this.populateTable(data)
    }

    populateTable = data => {
        for (let i = 0; i < data.length; i++) {
            let row = document.createElement('tr')            
            
            row.innerHTML = `
                <td class="s10 str main-column">${data[i].date}</td>
                <td class="s9 light-gray m-0 red">R$ ${data[i].expense.toFixed(2)}</td>
                <td class="s9 light-gray m-0 green">R$ ${data[i].saving.toFixed(2)}</td>
            `
            this.table.appendChild(row)
            row.addEventListener('click', function(){
                new ExpenseModal(data[i])
            })
        }
    }
}