const addModal = () => {
    const content = document.querySelector('div.flex-container.bg')
    const modal = document.createElement('div')
    modal.classList.add('modal-bg')

    const modalBox = document.createElement('div')
    modalBox.classList.add('modal')
    modalBox.classList.add('shadow')

    content.appendChild(modal)
    modal.appendChild(modalBox)

    addCloseBtn(modal)
    return modalBox
}

const addCloseBtn = modal => {
    const content = document.querySelector('.modal')
    
    const closeIcon = document.createElement('i')
    closeIcon.classList.add('material-icons')
    closeIcon.classList.add('menu-icon')
    closeIcon.classList.add('fl-r')
    closeIcon.innerText = 'close'
    content.appendChild(closeIcon)
    closeIcon.addEventListener('click', function(){close()})    
}

const close = () => {
    let modal = document.querySelector('.modal-bg')
    modal.remove()
}

const createTitle = (content, text) => {
    const title = document.createElement('h3')
    title.classList.add('s6', 'txt-center', 'm-b-24')
    title.innerText = text

    content.appendChild(title)
}

const createParagraph = (content, text) => {
    const paragraph = document.createElement('p')
    paragraph.classList.add('light-gray', 'm-b-24', 'txt-center')
    paragraph.innerText = text

    content.appendChild(paragraph)
}

const adjustSideScroll = () => {
    document.querySelector('.default-margin-bg').classList.add('scroll')
}

