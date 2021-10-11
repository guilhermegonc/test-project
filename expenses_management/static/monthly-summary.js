class ExpenseCard{
    constructor(type, form, div, sum, limit, balance){
        this.type = type
        this.card = this.createCard()
        div.appendChild(this.card)
        this.addSettings(form)
        this.addLabel()
        this.balance = this.addBalance(balance)
        this.expenses = this.addTotalExpense(sum)
        this.limit = this.addTarget(limit)
        this.recent = this.addRecent()
        this.footer = this.addDetails()
        this.populateData(sum, limit)
    }

    createCard = () => {
        const div = document.createElement('div')
        div.id = 'total-expenses'
        div.classList.add('summary-card', 'shadow', 'p-24', 'm-b-24')
        return div
    }

    addSettings = form => {
        const i = document.createElement('i')
        i.id = 'settings'
        i.classList.add('fl-r', 'light', 'material-icons', 'p-12', 'action-icon')
        i.innerText = 'add'
        i.addEventListener('click', function(){
            new EditModal(this.type, form)
        })
        this.card.appendChild(i)
    }

    addLabel = () => {
        const p = document.createElement('p')
        p.id = 'card-label'
        p.classList.add('s9', 'str', 'light', 'm-0', 'txt-left')
        p.innerText = this.type === 'expense' ? 'Disponível' : 'A investir'
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

    addTotalExpense = sum => {
        const p = document.createElement('p')
        p.classList.add('s9', 'm-0', 'txt-left', 'str', 'light')
        p.innerText = `No mês: R$ ${sum}`
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

    addRecent = async() => {
        const p = document.createElement('p')
        p.classList.add('s9', 'm-0', 'txt-left', 'str', 'light')
        p.innerText = 'Carregando'
        this.card.appendChild(p)


        const uri = `load-${this.type}s?start=0&end=1`
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
        btn.href = `/${this.type}`
        btn.innerText = 'Ver mais'

        div.appendChild(btn)
        this.card.appendChild(div)
        return div
    }

    populateData = (sum, limit) => {
        let label
        if (this.type != 'expense') {
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
