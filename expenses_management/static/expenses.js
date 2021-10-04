const createTable = () => {
    const table = document.createElement('table')
    table.id = 'expenses'
    table.classList.add('shadow', 'm-a')
    appendTable(table)
    loadExpenses()
    createInputBtn()
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
    createLoadBtn(table)
}

const createLoadBtn = div => {
    const td = document.createElement('td')
    const a = document.createElement('a')
    td.colSpan = 4
    td.id = 'expenses-btn'
    td.appendChild(a)

    a.classList.add('btn', 'light')
    a.innerText = 'Carregar mais antigas'
    
    div.appendChild(td)
    a.addEventListener('click', function() {
        loadExpenses()
    })
}

const loadExpenses = async() => {
    const start = counter * 50
    const end = start + 50
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
        row.id = `${expenses[i].name}-${i}`
        recurringDecoration = expenses[i].recurring === true ? '⏱' : ''
        valueDecoration = expenses[i].value > 0 ? 'red' : 'green'
        row.innerHTML = `
        <td class="s10 str main-column blue">${expenses[i].name}</td>
        <td class="s9 light-gray m-0 hide-mobile">${expenses[i].type}</td>
        <td class="s9 light-gray m-0 hide-mobile">${expenses[i].date}</td>
        <td class="s9 light-gray m-0 ${valueDecoration} t-right">R$ ${expenses[i].value.toFixed(2)} ${recurringDecoration}</td>
        `
        table.appendChild(row)
        table.insertBefore(row, btn)
    }
}

const createInputBtn = () => {
    const td = document.createElement('td')
    td.colSpan = 4
    td.id = 'input-btn'
    td.appendChild(a)

    const a = document.createElement('a')
    a.classList.add('btn', 'light')
    a.innerText = 'Nova despesa'
    
    const div = document.querySelector('#expenses')
    div.insertBefore(td, div.firstChild)
    a.addEventListener('click', function() {
        addInputModal()
    })
}