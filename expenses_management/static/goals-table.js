const addGoalsTable = () => {
    const container = document.querySelector('#table-list')
    const html = new GoalsTable(container)
}

class GoalsTable {
    constructor(div) {
        this.parent = div
        this.html = new Table('goal')
        div.appendChild(this.html.table)

        this.html.btn.remove()
        this.populateHeader()
        this.detailFirstRow()
        this.populateTable(goals)
    }

    populateHeader = () => {
        const h = document.querySelectorAll('th')
        h[0].innerText = 'Mês'
        h[0].classList.remove('main-column')

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
        r[0].innerText = 'Adicionar planejamento'
        r[1].classList.remove('hide-mobile')
        r[2].remove()
    }

    populateTable = data => {
        const months = {
            0: 'Janeiro', 1: 'Fevereiro', 2: 'Março',
            3: 'Abril', 4: 'Maio', 5: 'Junho',
            6: 'Julho', 7: 'Agosto', 8: 'Setembro',
            9: 'Outubro', 10: 'Novembro', 11: 'Dezembro', 
        }

        for (let i = 0; i < data.length; i++) {
            let row = document.createElement('tr')            
            
            row.innerHTML = `
                <td class="s10 str">${months[i]} ${data[i].date.split('-')[0]}</td>
                <td class="s9 light-gray m-0 red t-right">R$ ${data[i].expenses}</td>
                <td class="s9 light-gray m-0 green t-right">R$ ${data[i].savings}</td>
            `
            this.html.table.appendChild(row)
            row.addEventListener('click', function(){
                new GoalModal(forms, data[i])
            })
        }
    }
}