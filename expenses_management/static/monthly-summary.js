class ExpenseCard{
    constructor(div, sum, limit, balance){
        this.card = this.createCard()
        div.appendChild(this.card)
        this.addLabel()
        this.balance = this.addBalance(balance)
        this.footer = this.addDetails()
        this.expenses = this.addTotalExpense(sum)
        this.limit = this.addTarget(limit)
        this.populateData(balance)
    }

    createCard = () => {
        const div = document.createElement('div')
        div.id = 'total-expenses'
        div.classList.add('summary-card', 'p-card', 'shadow', 'p-24', 'm-b-24')
        return div
    }

    addLabel = () => {
        const p = document.createElement('p')
        p.id = 'card-label'
        p.classList.add('s10', 'str', 'light', 'm-0', 'txt-left')
        p.innerText = 'GASTOS'
        this.card.appendChild(p)
    }

    addBalance = balance => {
        const h1 = document.createElement('h1')
        h1.id = 'expense-sum'
        h1.classList.add('s4', 'light', 'fl-l')
        h1.innerText = `R$ ${balance.toFixed(2)}`
        this.card.appendChild(h1)
        return h1
    }

    addDetails = () => {
        const span = document.createElement('span')
        span.classList.add('card-footer')
        this.card.appendChild(span)
        return span
    }

    addTotalExpense = sum => {
        const p = document.createElement('p')
        p.classList.add('s8', 'm-0', 'fl-l')
        p.innerText = `💸 R$ ${sum}`
        this.footer.appendChild(p)
        return p
    }

    addTarget = limit => {
        const p = document.createElement('p')
        p.classList.add('s8', 'm-0', 'fl-r')
        p.innerText = `R$ ${limit} 💰`
        this.footer.appendChild(p)
        return p
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
