const addDetails = () => {
    const details = document.querySelector('#details')
    const chartCanvas = document.querySelector('#expense-chart')
    startChart(chartCanvas)
    new SavingBalanceTable(details)
}

const startChart = chartCanvas => {
    new Chart(chartCanvas, {
        type: 'bar',
        data: {
            labels: ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D',],
            datasets: [
                {
                    type: 'line',
                    backgroundColor: 'rgba(50, 72, 190)',
                    data: goalExpValues,
                    tension: 0,
                    fill: false,
                },{
                    backgroundColor: 'rgba(50, 72, 190)',
                    data: expenseValues,
                    tension: 0,
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                },
                xAxes: [{
                    gridLines: {display: false}
                }],
                yAxes: [{
                    ticks: {display: false},
                    gridLines: {drawBorder: false}
                }]
            },
            title: {
                display: true,
                text: 'Despesas',
            },
            legend: false,
            aspectRatio: 3,
        }
    })
}