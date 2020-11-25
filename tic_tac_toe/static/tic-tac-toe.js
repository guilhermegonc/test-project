let xNext = true
let gameOn = true
let rounds = 0

const createGame = () => {
    const mainDiv = document.querySelector('#game')    

    createTitle(mainDiv)
    createBoard(mainDiv)
    addResetButton(mainDiv)
    addReturnButton(mainDiv)
}

const createTitle = mainDiv => {
    const scoreInfo = document.createElement('h1')
    
    scoreInfo.id = 'game-title'
    scoreInfo.classList.add('s3')
    scoreInfo.classList.add('light')
    scoreInfo.classList.add('txt-center')
    scoreInfo.innerText = 'Tic tac toe'
    mainDiv.appendChild(scoreInfo)
}

const createBoard = mainDiv => {
    const gameBoard = document.createElement('div')
    
    gameBoard.id = 'gameBoard'
    gameBoard.classList.add('m-b-24')
    mainDiv.appendChild(gameBoard)

    for (let i=0; i<3; i++) {
        const row = createRow(i)
        gameBoard.appendChild(row)
    }
}

const createRow = row => {
    const newRow = document.createElement('div')
    const identifier = `r${row}`
    
    newRow.classList.add('row')
    newRow.id = identifier

    for (let i=0; i<3; i++) {
        const square = createSquare(row, i)
        newRow.appendChild(square)
    }

    return newRow
}

const createSquare = (row, column) => {
    const newSquare = document.createElement('div')
    const squareNumber = (row * 3)+(column + 1)
    const identifier = `s${squareNumber}`
    
    newSquare.id = identifier
    newSquare.classList.add('square')
    newSquare.classList.add('shadow')
    newSquare.onclick = () => isGameOver(newSquare.id)
    newSquare.innerText = '-'

    return newSquare
}

const isGameOver = nextRound => gameOn ? alreadyMarked(nextRound) : null

const alreadyMarked = identifier => {
    const squareToMark = document.querySelector(`#${identifier}`)
    squareToMark.innerText == '-' ? addMark(squareToMark) : null
}

const addMark = piecePosition => {
    piecePosition.innerText = xNext ? 'x' : 'o'
    rounds++
    checkBoard()
}

const checkBoard = () => {
    const rawValues = document.querySelectorAll('.square')
    let values = []
    
    for (let rawValue of rawValues) {
        const answers = rawValue.innerText
        values.push(answers)
    }   
    
    checkWinner(values)
}

const checkWinner = boardPieces => {
    const winConditions = [
        [0, 1, 2], [0, 3, 6], [0, 4, 8], [1, 4 ,7], 
        [2, 5, 8], [2, 4, 6], [3, 4, 5],[6, 7, 8]
    ]

    for (let winPosition of winConditions) {
        const pieces = [
            boardPieces[winPosition[0]],
            boardPieces[winPosition[1]],
            boardPieces[winPosition[2]]
        ]

        if (pieces[0] != '-' && 
            pieces[0] == pieces[1] && 
            pieces[0] == pieces[2]) 
            return congratulate()
    }

    isBoardFull() ? endGame() : changePlayer()
}

const isBoardFull = () => rounds==9

const congratulate = () => {
    const feedback = document.querySelector('#game-title')
    const winner = xNext ? 'X' : 'O'

    feedback.innerText = `${winner} venceu`
    gameOn = false
}

const changePlayer = () => xNext = xNext ? false : true

const endGame = () => {
    gameOn = false
    const feedback = document.querySelector('#game-title')
    feedback.innerText = 'Fim de jogo'
}

const addResetButton = mainDiv => {
    const resetBtn = document.createElement('div')

    resetBtn.classList.add('btn')
    resetBtn.classList.add('m-b-12')
    resetBtn.classList.add('txt-center')
    resetBtn.classList.add('shadow')
    resetBtn.innerText = 'Resetar jogo'
    resetBtn.onclick = () => reset(mainDiv)
    mainDiv.appendChild(resetBtn)
}

const reset = mainDiv => {
    mainDiv.innerHTML = ''
    xNext = true
    gameOn = true
    rounds = 0
    
    createGame()
}

const addReturnButton = mainDiv => {
    const returnBtn = document.createElement('a')

    returnBtn.classList.add('btn')
    returnBtn.classList.add('shadow')
    returnBtn.classList.add('light')

    returnBtn.innerText = 'Voltar'
    returnBtn.href = '/'
    mainDiv.appendChild(returnBtn)
}