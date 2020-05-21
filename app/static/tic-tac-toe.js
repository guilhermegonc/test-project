let xNext = true
let gameOn = true
let rounds = 0

let createBoard = () => {
    let mainDiv  = document.querySelector('#game')
    createTitle(mainDiv)

    for (let i = 0; i<3; i++) {
        let row = createRow(i)
        mainDiv.appendChild(row)
    }

}

let createTitle = (boardDiv) => {
    let scoreInfo = document.createElement('h1')
    
    scoreInfo.id = 'game-title'
    scoreInfo.classList.add('s1')
    scoreInfo.classList.add('p-12')
    scoreInfo.classList.add('light')
    scoreInfo.innerText = 'Tic tac toe'
    
    boardDiv.appendChild(scoreInfo)
}

let createRow = (r) => {
    let newRow = document.createElement('div')
    let identifier = `r${r}`

    newRow.classList.add('row')
    newRow.id = identifier

    for (let i=0; i<3; i++ ){
        let square = createSquare(r, i)
        newRow.appendChild(square)
    }

    return newRow
}

let createSquare = (r, c) => {
    let newSquare = document.createElement('div')
    let identifier = `s${(r*3)+(c+1)}`

    newSquare.id = identifier
    newSquare.classList.add('square')
    newSquare.classList.add('shadow')
    newSquare.onclick = function(){isGameOver(identifier)}
    newSquare.innerText = "-"

    return newSquare
}

let isGameOver = (nextRound) => gameOn?alreadyMarked(nextRound):null

let alreadyMarked = (identifier) => {
    let squareToMark = document.querySelector(`#${identifier}`)
    squareToMark.innerText == "-"?addMark(squareToMark):null
}

let addMark = (piecePosition) => {
    piecePosition.innerText = xNext?'x':'o'
    rounds ++
    checkBoard()
}

let checkBoard = () => {
    let values = []
    let rawValues = document.querySelectorAll('.square')
    for (let i=0; i<rawValues.length; i++) {
        let answers = rawValues[i].innerText
        values.push(answers)
    }   
    checkWinner(values)
}

let checkWinner = (piecesPosition) => {
    let wCond = [
        [0, 1, 2],
        [0, 3, 7],
        [0, 4, 8],
        [1, 4 ,7],
        [2, 5, 8],
        [2, 4, 6],
        [3, 4, 5],
        [6, 7, 8]
    ]

    for (i=0; i<wCond.length; i++) {
        let pos1 = piecesPosition[wCond[i][0]]
        let pos2 = piecesPosition[wCond[i][1]]
        let pos3 = piecesPosition[wCond[i][2]]
        
        if (pos1 != "-") {
            let isWinner = pos1==pos2 & pos1==pos3
            isWinner?congratulate():null
        }
    }
    let itsTie = isBoardFull()
    itsTie?endGame():changePlayer()
}

let isBoardFull = () => rounds==9?true:false

let congratulate = () => {
    gameOn = false
    let feedback = document.querySelector('#game-title')
    let winner = xNext?'x':'o'

    feedback.innerText = `Vencedor! ${winner}`
    mainDiv.append(feedback)
}

let changePlayer = () => xNext = xNext?false:true

let endGame = () => {
    gameOn = false
    let mainDiv = document.querySelector('#game')
    let feedback = document.createElement('h1')

    feedback.innerText = 'Fim de jogo!'
    mainDiv.append(feedback)
}
