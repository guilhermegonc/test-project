const addControls = () => {
    let date

    const previous = document.querySelector('#previous')
    previous.addEventListener('click', function(){
        date = changeMonth('subtract')
        deleteCards()
        setupCards(date['month'], date['year'])
    })

    const next = document.querySelector('#next')
    next.addEventListener('click', function(){
        date = changeMonth('add')
        deleteCards()
        setupCards(date['month'], date['year'])
    })
}

const changeMonth = method => {
    const monthHTML = document.querySelector('#title-month-value')
    let month = monthHTML.innerText
    let newMonth = method === 'add' ? parseInt(month) + 1 : parseInt(month) - 1   
    month = newMonth > 0 && newMonth <= 12 ? newMonth : month
    
    const yearHTML = document.querySelector('#title-year-value')
    let year = yearHTML.innerText
    
    writePageTitle(month, year)
    return {'month': month, 'year': year}
}

const writePageTitle = (month, year) => {
    const monthDict = {
        1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
        5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
        9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
    }
    const title = document.querySelector('#title-text')
    const mm = monthDict[month]
    title.innerText = `${mm}\n${year}`

    const monthHTML = document.querySelector('#title-month-value')
    monthHTML.innerText = month

    const yearHTML = document.querySelector('#title-year-value')
    yearHTML.innerText = year
}

const deleteCards = () => {
    const cards = document.querySelector('#summary')
    cards.innerHTML = ''
}

const setupCards = (month, year) => {
    const truncDate = `${year}-${String(month).padStart(2, '0')}-01`
    new ExpenseCard(truncDate)
    new SavingCard(truncDate)
}

class ExpenseCard{
    constructor(truncDate){
        this.realized = expenses[truncDate].toFixed(2)
        this.planned = goals[truncDate][0].toFixed(2)
        this.balance = (this.planned - this.realized).toFixed(2)
        this.color = this.planned * 0.95 > this.realized ? 'good' : 'danger'
        new SummaryCard(
            div, 
            formExpense, 
            'Disponível:',
            'expense',
            '/load-expenses', 
            '/expenses', 
            this.realized, 
            this.planned, 
            this.balance, 
            'light', 
            this.color
            )
    }
}

class SavingCard{
    constructor(truncDate){
        this.realized = savings[truncDate].toFixed(2)
        this.planned = goals[truncDate][1].toFixed(2)
        this.balance = (this.planned - this.realized).toFixed(2)
        new SummaryCard(
            div, 
            formSaving, 
            'A Investir:',
            'saving',
            '/load-savings', 
            '/savings', 
            this.realized, 
            this.planned, 
            this.balance,
            'black', 
            'generic',
            )
    }
}

class SummaryCard{
    constructor(div, form, cardTitle, modalType, requestURI, 
        viewMoreURI, realized, planned, balance, fontColor, cardColor) {
        
        this.realized = realized
        this.planned = planned
        this.balance = balance
        this.card = this.createCard(fontColor, cardColor)
        
        this.addShortcut(modalType, form)
        this.addLabel(cardTitle)
        this.addTitle(balance)
        this.addSubtext('Planejado: R$', planned)
        this.addSubtext('Realizado: R$', realized)
        this.addRecent(requestURI)
        this.addLoadBtn(viewMoreURI)
        
        div.appendChild(this.card)
    }

    createCard = (font, color) => {
        const div = document.createElement('div')
        div.classList.add('summary-card', 'shadow', 'p-24', 'm-b-24', 'txt-left', font, color)
        return div
    }

    addShortcut = (modalType, form) => {
        const i = document.createElement('i')
        i.classList.add('fl-r', 'material-icons', 'p-12', 'action-icon')
        i.innerText = 'add'
        i.addEventListener('click', function(){
            switch (modalType) {
                case 'expense':
                    new ExpenseModal(form)
                    break
                case 'saving':
                    new SavingModal(form)
                    break
            }
        })
        this.card.appendChild(i)
    }

    addLabel = text => {
        const p = document.createElement('p')
        p.id = 'card-label'
        p.classList.add('s9', 'str', 'm-0')
        p.innerText = text
        this.card.appendChild(p)
    }

    addTitle = value => {
        const h1 = document.createElement('h1')
        h1.id = 'expense-sum'
        h1.classList.add('s3', 'm-b-12')
        h1.innerText = `R$ ${value}`
        this.card.appendChild(h1)
    }

    addSubtext = (text, value) => {
        const p = document.createElement('p')
        p.classList.add('s9', 'm-0')
        p.innerHTML = `${text} ${value}`
        this.card.appendChild(p)
    }

    addRecent = async(requestURI) => {
        const p = document.createElement('p')
        p.classList.add('s9', 'm-0')
        p.innerText = 'Recente: -'
        this.card.appendChild(p)
        
        const uri = `${requestURI}?start=0&end=1`
        const data = await fetch(uri)
        let obj = await data.json()
        let text = obj['data'][0]['type'] === undefined ? obj['data'][0]['objective'] : obj['data'][0]['type']
        p.innerText = `Recente: ${text}`
    }

    addLoadBtn = uri => {
        const div = document.createElement('div')
        div.classList.add('fl-l', 'btn-full')
        const btn = document.createElement('a')
        btn.classList.add('btn', 'light', 'card-footer', 'primary')
        btn.href = `${uri}`
        btn.innerText = 'Ver todos'
        div.appendChild(btn)
        this.card.appendChild(div)
        this.addSettingsBtn()
    }

    addSettingsBtn = () => {
        const div = document.createElement('div')
        div.classList.add('btn-full')
        const btn = document.createElement('a')
        btn.classList.add('btn', 'light', 'card-footer', 'secondary')
        btn.href = `/goals`
        
        const i = document.createElement('i')
        i.classList.add('material-icons', 'icon-adjust')
        i.innerText = 'settings'

        btn.appendChild(i)
        div.appendChild(btn)
        this.card.appendChild(div)
    }
}
