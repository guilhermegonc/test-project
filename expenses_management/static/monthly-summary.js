const setupPage = () => {
    const mm = String(date.getMonth()+1)
    const yyyy = date.getFullYear()
    adjustSideScroll()
    addControls()
    writePageTitle(mm, yyyy)
    setupCards(mm, yyyy)
    addChart()
    updateExpenseTable(mm, yyyy)
    updateSavingTable()

    document.addEventListener('scroll', function() {
        window.scrollY > 172 ? fixTitle() : releaseTitle()
    })
}

const fixTitle = () => {
    const title = document.querySelector('#aux-title')
    title.classList.remove('hide')
}

const releaseTitle = () => {
    const title = document.querySelector('#aux-title')
    title.classList.add('hide')
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
    const truncDate = `${year}-${String(month).padStart(2, '0')}-01`
    new ExpenseCard(truncDate, expensesMonth)
    new SavingCard(truncDate, savings)
}

const addChart = () => {
    const chartCanvas = document.querySelector('#expense-chart')
    startChart(chartCanvas)
}

const updateExpenseTable = (month, year) => {
    const expDetails = document.querySelector('#details-expenses')
    expDetails.innerHTML = ''

    const truncDate = `${year}-${String(month).padStart(2, '0')}-01`
    const expTable = new ExpenseTypeTable(expDetails, truncDate)
}

const updateSavingTable = () => {
    const savDetails = document.querySelector('#details-savings')
    const savTable = new SavingBalanceTable(savDetails)
}
