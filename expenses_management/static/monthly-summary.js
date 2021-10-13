const setupPage = () => {
    writePageTitle()
    const truncDate = truncCurrentDate()
    
    let modalTitle = 'Disponível:'
    let objectName = 'expense'
    let paginationUri = '/load-expenses'
    let requestUri = '/expenses'
    let realized = expenses[truncDate].toFixed(2)
    let planned = goals[truncDate][0].toFixed(2)
    let balance = planned - realized
    let fontColor = 'light'
    let cardColor = planned * 0.9 > realized ? 'good' : 'danger'
    new ExpenseCard(div, formExpense, modalTitle, objectName, paginationUri, 
        requestUri, realized, planned, balance, fontColor, cardColor)
    
    modalTitle = 'A investir:'
    objectName = 'saving'
    paginationUri = '/load-savings'
    requestUri = '/savings'
    realized = savings[truncDate].toFixed(2)
    planned = goals[truncDate][1].toFixed(2)
    balance = planned - realized
    fontColor = 'black'
    cardColor = 'generic'
    new ExpenseCard(div, formSaving, modalTitle, objectName, paginationUri, 
        requestUri, realized, planned, balance, fontColor, cardColor)
}

const truncCurrentDate = () => {
    let yyyy = String(date.getFullYear())
    let mm = String(date.getMonth() + 1).padStart(2, '0')
    return `${yyyy}-${mm}-01`
}

const writePageTitle = () => {
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
    constructor(div, form, cardTitle, modalType, requestURI, 
        viewMoreURI, realized, planned, balance, fontColor, cardColor) {
        
        this.realized = realized
        this.planned = planned
        this.balance = balance
        this.card = this.createCard(fontColor, cardColor)
        
        this.addShortcut(modalType, form)
        this.addLabel(cardTitle)
        this.addTitle(balance)
        this.addSubtext('No mês: R$', realized)
        this.addSubtext('Planejado: R$', planned)
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
            new EditModal(modalType, form)
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
        h1.innerText = `R$ ${value.toFixed(2)}`
        this.card.appendChild(h1)
    }

    addSubtext = (text, value) => {
        const p = document.createElement('p')
        p.classList.add('s9', 'm-0', 'str')
        p.innerText = `${text} ${value}`
        this.card.appendChild(p)
    }

    addRecent = async(requestURI) => {
        const p = document.createElement('p')
        const uri = `${requestURI}?start=0&end=1`
        p.classList.add('s9', 'm-0', 'str')
        p.innerText = 'Carregando'
        this.card.appendChild(p)
        const obj = await fetch(uri)
        let name = await obj.json()
        p.innerText = `Recente: ${name['data'][0].name}`
    }

    addLoadBtn = uri => {
        const div = document.createElement('div')
        div.classList.add('fl-l', 'btn-full')
        const btn = document.createElement('a')
        btn.classList.add('btn', 'light', 'card-footer', 'primary')
        btn.href = `${uri}`
        btn.innerText = 'Ver mais'
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
