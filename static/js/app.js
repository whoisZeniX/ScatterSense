Chart.defaults.color = '#a8a29e';
Chart.defaults.borderColor = 'rgba(168, 162, 158, 0.1)';

document.addEventListener('DOMContentLoaded', function () {
    loadChartData();
});

function loadChartData() {
    fetch("/chart-data")
        .then(function (res) {
            return res.json();
        })
        .then(function (data) {
            if (!data) return;

            if (data.time_distribution) {
                renderTimeChart(data.time_distribution);
            }
            if (data.task_distribution) {
                renderTaskChart(data.task_distribution);
            }
            if (data.energy_trend) {
                renderEnergyChart(data.energy_trend);
            }
        });
}

function renderTimeChart(data) {
    var ctx = document.getElementById("timeChart");
    if (!ctx) return;

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: Object.keys(data),
            datasets: [{
                label: 'Sessions',
                data: Object.values(data),
                backgroundColor: 'rgba(255, 255, 255, 0.5)',
                borderColor: '#ffffff',
                borderWidth: 1
            }]
        },
        options: {
            plugins: { legend: { labels: { color: '#e7e5e4' } } },
            scales: {
                y: { grid: { color: 'rgba(168, 162, 158, 0.1)' } },
                x: { grid: { color: 'rgba(168, 162, 158, 0.1)' } }
            }
        }
    });
}

function renderTaskChart(data) {
    var ctx = document.getElementById("taskChart");
    if (!ctx) return;

    new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: Object.keys(data),
            datasets: [{
                data: Object.values(data),
                backgroundColor: [
                    'rgba(255, 255, 255, 0.8)',
                    'rgba(168, 162, 158, 0.7)',
                    'rgba(87, 83, 78, 0.7)',
                    'rgba(214, 211, 209, 0.7)'
                ],
                borderColor: 'transparent'
            }]
        },
        options: {
            plugins: { legend: { display: false } }
        }
    });
}

function renderEnergyChart(data) {
    if (!data || data.length === 0) return;
    var ctx = document.getElementById("energyChart");
    if (!ctx) return;

    var labels = [];
    for (var i = 0; i < data.length; i++) {
        labels.push(i + 1);
    }

    new Chart(ctx, {
        type: "line",
        data: {
            labels: labels,
            datasets: [{
                label: 'Energy',
                data: data,
                borderColor: '#ffffff',
                backgroundColor: 'rgba(255, 255, 255, 0.1)',
                tension: 0.3,
                fill: true
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    max: 10,
                    grid: { color: 'rgba(168, 162, 158, 0.1)' }
                },
                x: { display: false }
            },
            plugins: { legend: { display: false } }
        }
    });
}
