const populateField = (code) => {
    codeInput = document.querySelector('#id_code')
    codeInput.value = code
    codeInput.type = 'hidden'
    classifyTransaction('sell')
}

const classifyTransaction = (method) => {
    hiddenInput = document.querySelector('#id_action')
    hiddenInput.value = method    
}