const setupPage = () => {
    addControls()
    writePageTitle(date.getMonth()+1, date.getFullYear())
    setupCards(date.getMonth()+1, date.getFullYear())
    addDetails()
}

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
