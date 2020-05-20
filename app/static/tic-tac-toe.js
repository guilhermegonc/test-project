let createBoard = () => {
    let mainDiv  = document.querySelector('#game')
    
    for (let i = 0; i<3; i++) {
        let row = createRow()
        row.id = `row-${i+1}`

        mainDiv.appendChild(row)
    }
}

let createRow = () => {
    let newRow = document.createElement('div')
    newRow.classList.add('row')

    for (let i=0; i<3; i++ ){
        let square = createSquare()
        newRow.appendChild(square)
    }

    return newRow
}

let createSquare = () => {
    let newSquare = document.createElement('div')
    newSquare.classList.add('square')
    newSquare.classList.add('shadow')

    
    return newSquare
}

