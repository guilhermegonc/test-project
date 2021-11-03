class PageData {
    constructor(){
        this.months = Object.keys(userFinances.months)
        this.step = this.updateStep(12)
        this.changeMonth()
        this.updateSavingTable()
        this.addNav('previous', false)
        this.addNav('next', true)
    }

    updateStep = step => {
        this.step = step
        this.date = this.months[step]
        this.month = this.parseDate()[1]
        this.year = this.parseDate()[0]
        return step
    }

    parseDate = () => {
        return this.date.split('-')
    }

    changeMonth = () => {
        this.clearCards()
        this.writePageTitle()
        this.setupCards()
        this.updateExpenseTable()
        this.updateChart()
    }

    clearCards = () => {
        const cards = document.querySelector('#summary')
        cards.innerHTML = ''
    }

    writePageTitle = () => {
        const monthDict = { 
            1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
            5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
            9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
        }
        const title = document.querySelector('#title-text')
        const text = `${monthDict[parseInt(this.month)]}\n${this.year}`
        title.innerText = text
        this.addSubtitle(text)
    }

    addSubtitle = text => {
        const title = document.querySelector('#aux-title')
        title.innerText = text
        const showMethod = this.fixTitle
        const hideMethod = this.releaseTitle
        document.addEventListener('scroll', function() {
            window.scrollY > 172 ? showMethod() : hideMethod()
        })
    }

    fixTitle = () => {
        const title = document.querySelector('#aux-title')
        title.classList.remove('hide')
    }

    releaseTitle = () => {
        const title = document.querySelector('#aux-title')
        title.classList.add('hide')
    }

    setupCards = () => {
        const div = document.querySelector('#summary')
        new ExpenseCard(div, this.date, userFinances.months)
        new SavingCard(div, this.date, userFinances.months)
    }

    updateChart = () => {
        const month = parseInt(this.month) - 1
        const chartCanvas = document.querySelector('#expense-chart')
        chartCanvas.innerHTML = ''
        let color
        const barColors = []
        for (let i = 0; i < 12; i++){
            color = i === month ? 'rgba(0,0,0)' : 'rgba(221, 221, 221)'
            barColors.push(color)
        }
        const budgetValues = this.loadYearBudget()
        const realizedValues = this.loadYearRealized()
        startChart(chartCanvas, barColors, budgetValues, realizedValues)
    }
    
    loadYearBudget = () => {
        const budget = []
        let truncDate, val
        for (let i = 1; i < 13; i++) {
            truncDate = `${this.year}-${String(i).padStart(2,'0')}-01`
            val = userFinances.months[truncDate].expenses.goal
            budget.push(val)
        }
        return budget
    }
    
    loadYearRealized = () => {
        const realized = []
        let truncDate, val
        for (let i = 1; i < 13; i++) {
            truncDate = `${this.year}-${String(i).padStart(2,'0')}-01`
            val = userFinances.months[truncDate].expenses.total
            realized.push(val)
        }
        return realized
    }

    updateExpenseTable = () => {
        const expDetails = document.querySelector('#details-expenses')
        expDetails.innerHTML = ''    
        let values = this.getExpenseCategories(this.date)
        new ExpenseTypeTable(expDetails, values)
    }

    getExpenseCategories = () => {
        const expenses = {}
        let classification = []
        let inBudget
        const categories = Object.keys(userFinances.averages)
        let avg, val
        for (let i = 0; i < categories.length; i++) {
            avg = userFinances.averages[categories[i]].toFixed(2)
            val = userFinances.months[this.date].expenses.categories[categories[i]]
            val = val === undefined ? '0.00' : val.toFixed(2)
            expenses[categories[i]] = `R$ ${val}<br>(R$ ${avg})`

        }
        return expenses
    }

    addColors = classification => {
        let cells = document.querySelectorAll('td')
        cells = [1,2,3,4,5,6]
        console.log(cells)
        const filterItems = cells.filter(item => cells.indexOf(item) != 2)
        console.log(cells)
    }
    
    updateSavingTable = () => {
        const savDetails = document.querySelector('#details-savings')
        let values = userFinances.savingsSum
        Object.keys(values).forEach((key, value) => {
            values[key] = `R$ ${values[key].toFixed(2)}`
        })
        new SavingBalanceTable(savDetails, values)
    }
    
    addNav = (id, inverse) => {
        const previous = document.querySelector(`#${id}`)
        const method = this.addMonth
        previous.addEventListener('click', function(){
            method(inverse)
        })
    }

    addMonth = direction => {
        direction = direction === true ? 1 : -1
        const newStep = this.step + (1 * direction)
        newStep > 0 && newStep < this.months.length ? this.updateStep(newStep) : null
        this.changeMonth()
    }
}
