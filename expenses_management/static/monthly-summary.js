const setupPage = () => {
    writeTitle()
    const truncDate = truncCurrentDate()

    let consolidated = expenses[truncDate].toFixed(2)
    let limit = goals[truncDate][0].toFixed(2)
    let balance = limit - consolidated
    new ExpenseCard('expense', formExpense, div, consolidated, limit, balance)
    
    consolidated = savings[truncDate].toFixed(2)
    limit = goals[truncDate][1].toFixed(2)
    balance = limit - consolidated
    new ExpenseCard('saving', formSaving, div, consolidated, limit, balance)
}

const truncCurrentDate = () => {
    let yyyy = String(date.getFullYear())
    let mm = String(date.getMonth() + 1).padStart(2, '0')
    return `${yyyy}-${mm}-01`
}

const writeTitle = () => {
    const months = {
        0: 'Janeiro',
        1: 'Favereiro',
        2: 'Março',
        3: 'Abril',
        4: 'Maio',
        5: 'Junho',
        6: 'Julho',
        7: 'Agosto',
        8: 'Setembro',
        9: 'Outubro',
        10: 'Novembro',
        11: 'Dezembro'
    }
    const title = document.querySelector('#title')
    const month = months[new Date().getMonth()]
    title.innerText = month
}

class ExpenseCard{
    constructor(type, form, div, sum, limit, balance){
        this.type = type
        this.card = this.createCard()
        this.addShortcut(form)
        this.addLabel()
        this.balance = this.addBalance(balance)
        this.expenses = this.addConsolidated(sum)
        this.limit = this.addTarget(limit)
        this.recent = this.addRecent(type)
        this.footer = this.addDetails()
        this.populateData(type, sum, limit)
        div.appendChild(this.card)
    }

    createCard = () => {
        const div = document.createElement('div')
        div.id = 'total-expenses'
        div.classList.add('summary-card', 'shadow', 'p-24', 'm-b-24')
        return div
    }

    addShortcut = (form, type) => {
        const i = document.createElement('i')
        i.classList.add('fl-r', 'light', 'material-icons', 'p-12', 'action-icon')
        i.innerText = 'add'
        i.addEventListener('click', function(){
            new EditModal(type, form)
        })
        this.card.appendChild(i)
    }

    addLabel = type => {
        const p = document.createElement('p')
        p.id = 'card-label'
        p.classList.add('s9', 'str', 'light', 'm-0', 'txt-left')
        p.innerText = type === 'expense' ? 'Disponível' : 'A investir'
        this.card.appendChild(p)
    }

    addBalance = balance => {
        const h1 = document.createElement('h1')
        h1.id = 'expense-sum'
        h1.classList.add('s3', 'light', 'txt-left', 'm-b-12')
        h1.innerText = `R$ ${balance.toFixed(2)}`
        this.card.appendChild(h1)
        return h1
    }

    addConsolidated = val => {
        const p = document.createElement('p')
        p.classList.add('s9', 'm-0', 'txt-left', 'str', 'light')
        p.innerText = `No mês: R$ ${val}`
        this.card.appendChild(p)
        return p
    }

    addTarget = limit => {        
        const p = document.createElement('p')
        p.classList.add('s9', 'm-0', 'txt-left', 'str', 'light')
        p.innerText = `Planejado: R$ ${limit}`
        this.card.appendChild(p)
        return p
    }

    addRecent = async(type) => {
        const p = document.createElement('p')
        const uri = `load-${type}s?start=0&end=1`
        p.classList.add('s9', 'm-0', 'txt-left', 'str', 'light')
        p.innerText = 'Carregando'
        this.card.appendChild(p)
        const obj = await fetch(uri)
        let name = await obj.json()
        p.innerText = `Recente: ${name['data'][0].name}`
        return p
    }

    addDetails = () => {
        const div = document.createElement('div')
        div.classList.add('fl-l', 'btn-full')

        const btn = document.createElement('a')
        btn.classList.add('btn', 'light', 'card-footer')
        btn.href = `/${this.type}s`
        btn.innerText = 'Ver mais'
        div.appendChild(btn)

        this.card.appendChild(div)
        return div
    }

    populateData = (type, sum, limit) => {
        let label
        if (type != 'expense') {
            label = 'generic'
        } else if (sum > limit) {
            label = 'danger'
        } else if (sum > limit * 0.9) {
            label = 'warning'
        } else {
            label = 'good'
        }
        this.card.classList.add(label)
    }
}
