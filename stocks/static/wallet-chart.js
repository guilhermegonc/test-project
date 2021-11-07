const startChart = () => {
    const chartCanvas = document.querySelector('#wallet-chart')
    const walletLabels = Object.keys(chart)
    const walletValues = Object.values(chart)
    var relativeWallet = walletValues.map(num => ((num - 1) * 100).toFixed(2))
    var zeros = walletValues.map(() => 0)
    const color = walletValues[walletValues.length - 1] >= 1 ? 'rgb(113, 218, 97)' : 'rgb(208, 68, 26)'
    new Chart(chartCanvas, {
        type: 'line',
        data: {
            labels: walletLabels,
            datasets: [{
                type: 'line',
                backgroundColor: color,
                borderColor: color,
                pointBackgroundColor: color,
                pointBorderColor: 'rgba(0, 0, 0, 0)',
                data: relativeWallet,
                tension: 0,
                fill: false,
            },{
                type: 'line',
                backgroundColor: 'rgba(0, 0, 0, 0.4)',
                borderColor: 'rgba(0, 0, 0, 0.4)',
                pointBackgroundColor: 'rgba(0, 0, 0, 0.4)',
                pointBorderColor: 'rgba(0, 0, 0, 0)',
                borderWidth: 1,
                data: zeros,
                tension: 0,
                fill: false,
            }]
        },
        options: {
            layout: {
                padding: {
                    left: 0,
                }
            },
            elements: {
                point:{
                    radius: 1
                }
            },
            scales: {
                xAxes: [{
                    gridLines: {display: false},
                    ticks: {display: false},
                    gridLines: {drawBorder: false, display: false}
                }],
                yAxes: [{
                    ticks: {display: false, beginAtZero: false},
                    gridLines: {drawBorder: false, display: false}
                }]
            },
            legend: true,
            aspectRatio: 4,
        }
    })
}
