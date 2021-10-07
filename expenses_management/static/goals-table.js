class GoalsTable {
    constructor(div) {
        this.parent = div
        this.html = new Table('goal')
        div.appendChild(this.html.table)

        this.table = this.html.table
        this.header = this.html.header
        this.firstRow = this.html.firstRow
        
        this.html.btn.remove()
        this.populateHeader()
        this.detailFirstRow()
        this.populateTable(goals)
    }

    populateHeader = () => {
        const h = document.querySelectorAll('th')
        h[0].innerText = 'Mês'

        h[1].innerText = 'Despesas'
        h[1].classList.remove('hide-mobile')
        h[1].classList.add('t-right')

        h[2].innerText = 'Economias'
        h[2].classList.remove('hide-mobile')
        h[2].classList.add('t-right')

        h[3].remove()        
    }

    detailFirstRow = () => {
        const r = document.querySelectorAll('td')
        r[0].innerText = 'Adicionar meta'
        r[2].remove()
    }

    populateTable = data => {
        for (let i = 0; i < data.length; i++) {
            let row = document.createElement('tr')            
            
            row.innerHTML = `
                <td class="s9 str main-column">${data[i].date}</td>
                <td class="s9 light-gray m-0 red t-right">R$ ${data[i].expense}</td>
                <td class="s9 light-gray m-0 green t-right">R$ ${data[i].saving}</td>
            `
            this.table.appendChild(row)
            row.addEventListener('click', function(){
                new GoalModal(data[i])
            })
        }
    }
}