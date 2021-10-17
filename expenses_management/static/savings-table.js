class SavingsTable {
    constructor(div) {
        this.parent = div
        this.html = new Table('saving')
        div.appendChild(this.html.table)        

        this.table = this.html.table
        this.header = this.html.header
        this.firstRow = this.html.firstRow
        this.btn = this.html.btn
        
        this.populateHeader()
        this.detailFirstRow()
        this.populateTable(savings)
        this.setupBtn()
    }

    populateHeader = () => {
        const h = document.querySelectorAll('th')
        h[0].innerText = 'Fundo'
        h[1].innerText = 'Objetivo'
        h[2].innerText = 'Data'
        h[3].innerText = 'Valor'        
    }

    detailFirstRow = () => {
        const r = document.querySelectorAll('td')
        r[0].innerText = 'Adicionar economia'
        r[3].innerText = 'R$ 00,00'        
    }

    populateTable = data => {
        for (let i = 0; i < data.length; i++) {
            let row = document.createElement('tr')
            let valueDecoration = data[i].value > 0 ? 'green' : 'red'
            
            row.innerHTML = `
                <td class="s10 str main-column ${valueDecoration}">${data[i].name}</td>
                <td class="s9 light-gray m-0 hide-mobile">${data[i].objective}</td>
                <td class="s9 light-gray m-0 hide-mobile">${data[i].date}</td>
                <td class="s9 light-gray m-0 ${valueDecoration} t-right">R$ ${data[i].value}</td>
            `
            this.table.insertBefore(row, this.btn)            
            row.addEventListener('click', function(){
                new SavingModal(forms, data[i])
            })
        }
    }

    setupBtn = () => {
        this.btn.addEventListener('click', this.requestData)
    }

    requestData = async() => {
        const start = counter * 20
        const end = start + 20
        const uri = `load-savings?start=${start}&end=${end}`
        let response = await fetch(uri)
        response = await response.json()
        savings = savings.concat(response.data)
        counter +=1
        this.populateTable(response.data)
    }
}
