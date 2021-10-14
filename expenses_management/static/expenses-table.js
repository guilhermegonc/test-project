class ExpensesTable {
    constructor(div) {
        this.html = new Table('expense')
        div.appendChild(this.html.table)        

        this.table = this.html.table
        this.header = this.html.header
        this.firstRow = this.html.firstRow
        this.btn = this.html.btn
        
        this.populateHeader()
        this.detailFirstRow()
        this.populateTable(expenses)
        this.setupBtn()
    }

    populateHeader = () => {
        const h = document.querySelectorAll('th')
        h[0].innerText = 'Despesa'
        h[1].innerText = 'Nome'
        h[2].innerText = 'Data'
        h[3].innerText = 'Valor'        
    }

    detailFirstRow = () => {
        const r = document.querySelectorAll('td')
        r[0].innerText = 'Adicionar despesa'
        r[3].innerText = 'R$ 00,00'        
    }

    populateTable = data => {
        for (let i = 0; i < data.length; i++) {
            let row = document.createElement('tr')
            let recurringDecoration = data[i].recurring === true ? '⏱' : ' '
            let valueDecoration = data[i].value > 0 ? 'red' : 'green'
            
            row.innerHTML = `
                <td class="s10 str main-column ${valueDecoration}">${data[i].type}</td>
                <td class="s9 light-gray m-0 hide-mobile">${data[i].name}</td>
                <td class="s9 light-gray m-0 hide-mobile">${data[i].date}</td>
                <td class="s9 light-gray m-0 ${valueDecoration} t-right">R$ ${data[i].value} ${recurringDecoration}</td>
            `
            this.table.insertBefore(row, this.btn)            
            row.addEventListener('click', function(){
                new EditModal('expense', forms, data[i])
            })
        }
    }

    setupBtn = () => {
        this.btn.addEventListener('click', this.requestData)
    }

    requestData = async() => {
        const start = counter * 20
        const end = start + 20
        const uri = `load-expenses?start=${start}&end=${end}`
        let response = await fetch(uri)
        response = await response.json()
        expenses = expenses.concat(response.data)
        counter +=1
        this.populateTable(response.data)
    }
}
