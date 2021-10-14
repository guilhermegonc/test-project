const addExpensesTable = div => {
    const html = new ExpensesTable(div)
}

const addRecurringTable = div => {
    const html = new RecurringTable(div)
    const info = document.querySelector('#info')
    const text = `No dia 01 de cada mês, as despesas recorrentes "ativas" são adicionadas às suas "despesas" com o ícone ⏱. É possível EDITAR e REMOVÊ-LAS normalmente.\nPara evitar que esses custos sejam adicionados novamente no próximo mês, basta inativá-los por aqui.`

    info.addEventListener('click', function(){
        const modal = addModal()
        createTitle(modal, 'Recorrentes')
        createParagraph(modal, text)
    })
}

const addGoalsTable = div => {
    const html = new GoalsTable(div)
}

const addSavingsTable = div => {
    const html = new SavingsTable(div)
}