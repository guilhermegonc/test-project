const greetingSubmission = () => {
    const modal = addModal()
    createTitle(modal, 'Obrigado!')
    createParagraph(modal, 'Seu cadastro foi salvo. Se quiser remover seu nome daqui, basta clicar no card ao lado. Caso queira ter o nome removido de outras bases, entre em contato.')
}

const handleText = (id, original=null) => {
    const text = document.querySelector(`#p-${id}`)
    text.innerText = original == null ? 'Clique para deletar' : original
}
