class ExpenseCard {
    constructor(month, transactions) {
        this.realized = transactions[month].toFixed(2)
        this.planned = goals[month][0].toFixed(2)
        this.balance = (this.planned - this.realized).toFixed(2)
        this.color = this.planned * 0.95 > this.realized ? 'good' : 'danger'
        
        this.card = new SummaryCard(div, 'light', this.color)
        this.card.label.innerText = 'Disponível:'
        this.card.title.innerText = `R$ ${this.balance}`
        this.card.addSubtext(`Planejado: R$ ${this.planned}`)
        this.card.addSubtext(`Realizado: R$ ${this.realized}`)
        this.card.footerBtn.firstChild.href = 'expenses'
        this.card.addSettingsBtn()

        this.card.shortcut.addEventListener('click', function() {
            new ExpenseModal(formExpense)
        })

        this.card.loadRecent('load-transactions/expenses')
    }
}

class SavingCard {
    constructor(month, transactions) {
        this.realized = transactions[month].toFixed(2)
        this.planned = goals[month][1].toFixed(2)
        this.balance = (this.planned - this.realized).toFixed(2)
        this.color = 'generic'
        
        this.card = new SummaryCard(div, 'black', this.color)
        this.card.label.innerText = 'A investir:'
        this.card.title.innerText = `R$ ${this.balance}`
        this.card.addSubtext(`Planejado: R$ ${this.planned}`)
        this.card.addSubtext(`.`)
        this.card.footerBtn.firstChild.href = 'savings'
        this.card.addSettingsBtn()

        this.card.shortcut.addEventListener('click', function() {
            new SavingModal(formSaving)
        })

        this.card.loadRecent('load-transactions/savings')
    }
}

class SummaryCard{
    constructor(div, fontColor, cardColor) {
        this.card = this.createCard(fontColor, cardColor)
        this.shortcut = this.addShortcut()
        this.label = this.addLabel()
        this.title = this.addTitle()
        this.footerBtn = this.addFooterBtn()
        div.appendChild(this.card)
    }

    createCard = (font, color) => {
        const div = document.createElement('div')
        div.classList.add('summary-card', 'shadow', 'p-24',
            'm-b-24', 'txt-left', font, color)
        return div
    }

    addShortcut = () => {
        const i = document.createElement('i')
        i.classList.add('fl-r', 'material-icons', 'p-12', 'action-icon')
        i.innerText = 'add'
        this.card.appendChild(i)
        return i
    }

    addLabel = () => {
        const p = document.createElement('p')
        p.classList.add('s9', 'str', 'm-0')
        p.innerText = 'Card:'
        this.card.appendChild(p)
        return p
    }

    addTitle = value => {
        const h1 = document.createElement('h1')
        h1.classList.add('s3', 'm-b-12')
        h1.innerText = `Título`
        this.card.appendChild(h1)
        return h1
    }

    addSubtext = (text) => {
        const p = document.createElement('p')
        p.classList.add('s9', 'm-0')
        p.innerHTML = text
        this.card.insertBefore(p, this.footerBtn)
        return p
    }

    addFooterBtn = uri => {
        const div = document.createElement('div')
        div.classList.add('fl-l', 'btn-full')
        const btn = document.createElement('a')
        btn.classList.add('btn', 'light', 'card-footer')
        btn.href = `${uri}`
        btn.innerText = 'Ver todos'
        div.appendChild(btn)
        this.card.appendChild(div)
        return div
    }

    addSettingsBtn = () => {
        this.footerBtn.firstElementChild.classList.add('primary')

        const div = document.createElement('div')
        div.classList.add('btn-full')
        const btn = document.createElement('a')
        btn.classList.add('btn', 'light', 'card-footer', 'fl-r', 'secondary')
        btn.href = `/goals`
        
        const i = document.createElement('i')
        i.classList.add('material-icons', 'icon-adjust')
        i.innerText = 'settings'

        btn.appendChild(i)
        div.appendChild(btn)
        this.card.appendChild(div)
    }

    loadRecent = async(requestURI) => {
        const recent = this.addSubtext(`Recente: Carregando`)
        const uri = `${requestURI}?start=0&end=1`
        const data = await fetch(uri)
        let obj = await data.json()
        let text = obj['data'][0]['type'] === undefined ? obj['data'][0]['objective'] : obj['data'][0]['type']
        recent.innerText = `Recente: ${text}`
    }

}
