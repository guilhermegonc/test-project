class RecurringTable {
    constructor(div) {
        this.html = new Table('recurring')
        div.appendChild(this.html.table)        
        
        this.table = this.html.table
        this.header = this.html.header
        this.firstRow = this.html.firstRow
        
        this.html.btn.remove()
        this.populateHeader()
        this.detailFirstRow()
        this.populateTable(recurring)
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
    
    populateTable = data => {
        for (let i = 0; i < data.length; i++) {
            let row = document.createElement('tr')            
            let isActive = data[i].active === true ? '✅' : '❌'
            let valueDecoration = data[i].value > 0 ? 'red' : 'green'
            
            row.innerHTML = `
                <td class="s10 str main-column ${valueDecoration}">${data[i].name}</td>
                <td class="s9 light-gray m-0 hide-mobile">${data[i].type}</td>
                <td class="s9 light-gray m-0 ${valueDecoration} t-right">R$ ${data[i].value} ${isActive}</td>
            `
            this.table.appendChild(row)
            row.addEventListener('click', function(){
                new EditModal('recurring', forms, data[i])
            })
        }
    }
}
