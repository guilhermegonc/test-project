const startChart = (chartCanvas, barColors, chartBudget, chartRealized) => {
    new Chart(chartCanvas, {
        type: 'bar',
        data: {
            labels: ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D',],
            datasets: [{
                type: 'line',
                backgroundColor: 'rgba(221, 221, 221)',
                data: chartBudget,
                tension: 0,
                fill: false,
            },{
                type: 'bar',
                backgroundColor: barColors,
                data: chartRealized,
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
            legend: false,
            aspectRatio: 2,
        }
    })
}
