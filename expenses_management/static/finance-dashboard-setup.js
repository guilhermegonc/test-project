const setupPage = () => {
    const date = new Date()
    const mm = String(date.getMonth()+1)
    const yyyy = date.getFullYear()
    
    adjustSideScroll()
    addControls()
    writePageTitle(mm, yyyy)
    setupCards(mm, yyyy)
    updateChart(mm, yyyy)
    updateExpenseTable(mm, yyyy)
    updateSavingTable()

    document.addEventListener('scroll', function() {
        window.scrollY > 172 ? fixTitle() : releaseTitle()
    })
}

const addControls = () => {
    const previous = document.querySelector('#previous')
    previous.addEventListener('click', function(){
        let monthValue = document.querySelector('#title-month-value').innerText
        monthValue = parseInt(monthValue)
        subtractMonth(monthValue)
    })

    const next = document.querySelector('#next')
    next.addEventListener('click', function(){
        let monthValue = document.querySelector('#title-month-value').innerText
        monthValue = parseInt(monthValue)
        addMonth(monthValue)
    })
}

const addMonth = month => {
    const newMonth = month + 1  
    month = newMonth > 0 && newMonth <= 12 ? newMonth : month
    changeMonth(month)
}

const subtractMonth = month => {
    const newMonth = month - 1   
    month = newMonth > 0 && newMonth <= 12 ? newMonth : month
    changeMonth(month)
}

const changeMonth = month => {
    const yearHTML = document.querySelector('#title-year-value')
    const year = yearHTML.innerText
    writePageTitle(month, year)
    deleteCards()
    setupCards(month, year)
    updateExpenseTable(month, year)
    updateChart(month, year)
}

const writePageTitle = (month, year) => {
    const monthDict = {
        1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
        5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
        9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
    }
    const title = document.querySelector('#title-text')
    const auxTitle = document.querySelector('#aux-title')
    const mm = monthDict[month]
    title.innerText = `${mm}\n${year}`
    auxTitle.innerText = `${mm} - ${year}`

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
    const div = document.querySelector('#summary')
    const truncDate = `${year}-${String(month).padStart(2, '0')}-01`
    new ExpenseCard(div, truncDate, userFinances.months)
    new SavingCard(div, truncDate, userFinances.months)
}

const updateChart = (mm, yyyy) => {
    mm = parseInt(mm) - 1
    const chartCanvas = document.querySelector('#expense-chart')
    chartCanvas.innerHTML = ''
    let barColors = [
        'rgba(221, 221, 221)',
        'rgba(221, 221, 221)',
        'rgba(221, 221, 221)',
        'rgba(221, 221, 221)',
        'rgba(221, 221, 221)',
        'rgba(221, 221, 221)',
        'rgba(221, 221, 221)',
        'rgba(221, 221, 221)',
        'rgba(221, 221, 221)',
        'rgba(221, 221, 221)',
        'rgba(221, 221, 221)',
        'rgba(221, 221, 221)',
    ]
    barColors[mm] = 'rgba(0,0,0)'
    let budgetValues = loadYearBudget(yyyy)
    let realizedValues = loadYearRealized(yyyy)

    startChart(chartCanvas, barColors, budgetValues, realizedValues)
}

const loadYearBudget = year => {
    const budget = []
    let truncDate, val
    for (let i = 1; i < 13; i++) {
        truncDate = `${year}-${String(i).padStart(2,'0')}-01`
        val = userFinances.months[truncDate].expenses.goal
        budget.push(val)
    }
    return budget
}

const loadYearRealized = year => {
    const realized = []
    let truncDate, val
    for (let i = 1; i < 13; i++) {
        truncDate = `${year}-${String(i).padStart(2,'0')}-01`
        val = userFinances.months[truncDate].expenses.total
        realized.push(val)
    }
    return realized
}

const updateExpenseTable = (month, year) => {
    const expDetails = document.querySelector('#details-expenses')
    expDetails.innerHTML = ''

    const truncDate = `${year}-${String(month).padStart(2, '0')}-01`
    const values = getExpenseCategories(truncDate) 
    const expTable = new ExpenseTypeTable(expDetails, values)
}

const getExpenseCategories = date => {
    const expenses = {}
    const categories = Object.keys(userFinances.averages)
    for (c in categories) {
        avg = userFinances.averages[categories[c]].toFixed(2)
        val = userFinances.months[date].expenses.categories[categories[c]]
        val = val === undefined ? '0.00' : val.toFixed(2)
        expenses[categories[c]] = `R$ ${val}<br>(R$ ${avg})`   
    }
    return expenses
}

const updateSavingTable = () => {
    const savDetails = document.querySelector('#details-savings')
    const values = userFinances.savingsSum 
    const savTable = new SavingBalanceTable(savDetails, values)
}


const fixTitle = () => {
    const title = document.querySelector('#aux-title')
    title.classList.remove('hide')
}

const releaseTitle = () => {
    const title = document.querySelector('#aux-title')
    title.classList.add('hide')
}
