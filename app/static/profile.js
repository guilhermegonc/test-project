const destroyConfirmation = () => {
    const btn = document.querySelector('#exclusion')
    btn.addEventListener('click', function() {
        const modal = addModal()
        createTitle(modal, 'Excluir conta')
        createParagraph(modal, 'Digite "DELETAR" no campo abaixo.')
        addForm(modal)
    })
}

const addForm = modal => {
    const inp = document.createElement('input')
    modal.appendChild(inp)
    addBtn(modal, inp)
}

const addBtn = (modal, inp) => {
    const div = document.createElement('div')
    div.classList.add('btn', 'shadow', 'danger')
    div.innerText = 'Confirmar'
    div.href = '/'
    modal.appendChild(div)
    div.addEventListener('click', function(){
        inp.value == 'DELETAR' ? destroyUser() : close()
    })
}

const destroyUser = () => {
    location.href = '/'
}