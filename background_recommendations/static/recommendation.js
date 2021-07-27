const getRecomendation = async() => {
    addFeedback()
    let uri = `/recomendations/2021-07-15`
    let response = await fetch(uri)
    responseDetails = await response.json()
    removeFeedback()
    console.log(responseDetails)
    return responseDetails
}

const addFeedback = () => {
    const waitingSection = document.querySelector('#message')
    const waitingMessage = document.createElement('p')
    
    waitingMessage.id = 'waiting-message'
    waitingMessage.classList.add('s8', 'p-12', 'token', 'light', 'txt-center', 'w-300', 'txt-center', 'm-a')    
    waitingMessage.innerText = 'Carregando análise'

    waitingSection.appendChild(waitingMessage)
}

const removeFeedback = () => {
    const waitingMessage = document.querySelector('#waiting-message')
    waitingMessage.remove()
}