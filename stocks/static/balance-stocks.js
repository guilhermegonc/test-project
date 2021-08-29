const balanceWallet = stocks => {
    addListener(stocks)
}

const addListener = stocks => {
    let btn = document.querySelector('#balance div')
    btn.addEventListener("click", function() {
        distributeBalance(stocks)
    })
}

const distributeBalance = stocks => {
    val = getBalance()
    for (s in stocks) {
        console.log(stocks[s])
    }
}

const getBalance = () => {
    let balance = document.querySelector('#balance input')
    let val = balance.value
    return parseInt(val)
}