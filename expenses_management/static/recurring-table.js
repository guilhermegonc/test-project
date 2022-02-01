const addRecurringTable = () => {
    const container = document.querySelector('#table-list')
    const info = document.querySelector('#info')
    const html = new RecurringTable(container)
    const text = `No dia 01 de cada mês, as despesas recorrentes "ativas" são adicionadas às suas "despesas" com o ícone ⏱. É possível EDITAR e REMOVÊ-LAS normalmente.\nPara evitar que esses custos sejam adicionados novamente no próximo mês, basta inativá-los por aqui.`

    info.addEventListener('click', function(){
        const modal = addModal()
        createTitle(modal, 'Recorrentes')
        createParagraph(modal, text)
    })
}

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
        this.summaryTable()
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
                new RecurringModal(forms, data[i])
            })
        }
    }

    summaryTable = () => {
        let value = recurring.filter(rec => rec.active == true)
        value = value.reduce((previous, val) => previous + val.value, 0)

        const container = document.querySelector('#summary')
        
        const headingText = document.createElement('p')
        headingText.classList.add('s9', 'str', 'm-0')
        headingText.innerText = 'Custo recorrente:'
        container.appendChild(headingText)

        const mainValue = document.createElement('h1')
        mainValue.classList.add('s3', 'm-b-12')
        mainValue.innerText = `R$${value.toFixed(2)}`
        container.appendChild(mainValue)

        const caption = document.createElement('p')
        caption.classList.add('s9', 'm-0')
        caption.innerText = 'Somente valores ativos.'
        container.appendChild(caption)
    }
}
