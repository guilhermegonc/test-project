class ExpenseCard{
    constructor(div, sum, limit, balance){
        this.card = this.createCard()
        div.appendChild(this.card)
        this.addSettings()
        this.addLabel()
        this.balance = this.addBalance(balance)
        this.expenses = this.addTotalExpense(sum)
        this.limit = this.addTarget(limit)
        this.recent = this.addRecent()
        this.populateData(balance)
        this.footer = this.addDetails()
    }

    createCard = () => {
        const div = document.createElement('div')
        div.id = 'total-expenses'
        div.classList.add('summary-card', 'shadow-mobile', 'p-24', 'm-b-24')
        return div
    }

    addSettings = () => {
        const i = document.createElement('i')
        i.id = 'settings'
        i.classList.add('fl-r', 'light', 'material-icons', 'p-12', 'action-icon')
        i.innerText = 'add'
        i.addEventListener('click', function(){
            new EditModal('expense')
        })
        this.card.appendChild(i)
    }

    addLabel = () => {
        const p = document.createElement('p')
        p.id = 'card-label'
        p.classList.add('s9', 'str', 'light', 'm-0', 'txt-left')
        p.innerText = 'Disponível'
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
        p.innerText = `Gasto: R$ ${sum}`
        this.card.appendChild(p)
        return p
    }

    addTarget = limit => {        
        const p = document.createElement('p')
        p.classList.add('s9', 'm-0', 'txt-left', 'str', 'light')
        p.innerText = `Limite: R$ ${limit}`
        this.card.appendChild(p)
        return p
    }

    addRecent = async() => {
        const p = document.createElement('p')
        p.classList.add('s9', 'm-0', 'txt-left', 'str', 'light')
        p.innerText = 'Carregando'
        this.card.appendChild(p)

        const uri = 'load-expenses?start=0&end=1'
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
        btn.href = '/expenses'
        btn.innerText = 'Ver mais'

        div.appendChild(btn)
        this.card.appendChild(div)
        return div
    }

    populateData = (reference, limit) => {
        let label
        if (reference < 0) {
            label = 'danger'
        } else if (limit * 0.9 > reference){
            label = 'warning'
        } else {
            label = 'good'
        }
        this.card.classList.add(label)
    }
}
