const createTable = () => {
    const table = document.createElement('table')
    table.id = 'expenses'
    table.classList.add('shadow', 'm-a')
    appendTable(table)
    loadExpenses()
}

const appendTable = table => {
    const div = document.querySelector('#expenses-list')
    div.appendChild(table)
    createHeader(table)
}

const createHeader = table => {
    const header = document.createElement('tr')
    header.innerHTML = `
        <th class="s10 main-column">Serviço</th>
        <th class="s10 hide-mobile">Tipo</th>
        <th class="s10 hide-mobile">Data</th>
        <th class="s10 t-right">Valor</th>
        `
    table.appendChild(header)
    addFirstRow(table)
}

const addFirstRow = (table) => {
    const row = document.createElement('tr')
    row.id = 'input-listener'
    row.innerHTML = `
        <td class="s10 str main-column gray">Adicionar serviço</td>
        <td class="s9 light-gray m-0 hide-mobile">-</td>
        <td class="s9 light-gray m-0 hide-mobile">-</td>
        <td class="s9 light-gray m-0 t-right">R$ 00,00</td>
        `
    table.appendChild(row)
    addInputListener(row.id)
    addLoadBtn(table)
}

const addInputListener = id => {
    const row = document.querySelector(`#${id}`)
    row.addEventListener('click', function(){
        new ExpenseModal()
    })
}

const addLoadBtn = div => {
    const td = document.createElement('td')
    td.colSpan = 4
    td.id = 'expenses-btn'

    const a = document.createElement('a')
    a.classList.add('btn', 'light')
    a.innerText = 'Carregar mais antigas'
    td.appendChild(a)
    
    div.appendChild(td)
    a.addEventListener('click', function() {
        loadExpenses()
    })
}

const loadExpenses = async() => {
    const start = counter * 20
    const end = start + 20
    const uri = `load-expenses?start=${start}&end=${end}`
    
    response = await fetch(uri)
    response = await response.json()
    expenses = expenses.concat(response.data)
    
    counter +=1
    populateTable(response.data)
}

const populateTable = expenses => {
    const table = document.querySelector('#expenses')
    const btn = document.querySelector('#expenses-btn')
    
    for (let i = 0; i < expenses.length; i++) {
        let row = document.createElement('tr')
        row.id = `expenses-${i+counter*20}`
        
        recurringDecoration = expenses[i].recurring === true ? '⏱' : ''
        valueDecoration = expenses[i].value > 0 ? 'red' : 'green'
        
        row.innerHTML = `
            <td class="s10 str main-column ${valueDecoration}">${expenses[i].name}</td>
            <td class="s9 light-gray m-0 hide-mobile">${expenses[i].type}</td>
            <td class="s9 light-gray m-0 hide-mobile">${expenses[i].date}</td>
            <td class="s9 light-gray m-0 ${valueDecoration} t-right">R$ ${expenses[i].value.toFixed(2)} ${recurringDecoration}</td>
            `
        table.appendChild(row)
        table.insertBefore(row, btn)
        row.addEventListener('click', function(){
            new ExpenseModal(expenses[i])
        })
    }
}
