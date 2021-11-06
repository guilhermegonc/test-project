const startChart = () => {
    const chartCanvas = document.querySelector('#wallet-chart')
    const walletLabels = Object.keys(chart)
    const walletValues = Object.values(chart)
    new Chart(chartCanvas, {
        type: 'line',
        data: {
            labels: walletLabels,
            datasets: [{
                type: 'line',
                backgroundColor: 'rgb(113, 218, 97)',
                borderColor: 'rgb(113, 218, 97)',
                pointBackgroundColor: 'rgb(113, 218, 97)',
                pointBorderColor: 'rgba(0, 0, 0, 0)',
                data: walletValues,
                tension: 0.5,
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
