// dashboard.js
// Fetch the data from Flask endpoint
fetch('/data')
.then(response => response.json())
.then(data => {
    // Hourly Chart
    const hourlyCtx = document.getElementById('hourlyChart').getContext('2d');
    const hourlyChart = new Chart(hourlyCtx, {
        type: 'bar',
        data: {
            labels: data.hourly.labels,
            datasets: [{
                label: 'Event frequency per Hour',
                data: data.hourly.datasets[0].data,
                backgroundColor: 'rgba(14, 132, 32, 0.2)',
                borderColor: 'rgba(14, 132, 32, 1)',
                borderWidth: 1
            }]
        },
        options: {
            maintainAspectRatio: false,
            responsive: true
        }
    });

    // Daily Chart
    const dailyCtx = document.getElementById('dailyChart').getContext('2d');
    const dailyChart = new Chart(dailyCtx, {
        type: 'bar',
        data: {
            labels: data.daily.labels,
            datasets: [{
                label: 'Event frequency per Day',
                data: data.daily.datasets[0].data,
                backgroundColor: 'rgba(249, 155, 17, 0.2)',
                borderColor: 'rgba(249, 155, 17, 1)',
                borderWidth: 1
            }]
        },
        options: {
            maintainAspectRatio: false,
            responsive: true
        }
    });

    // Weekly Chart
    const weeklyCtx = document.getElementById('weeklyChart').getContext('2d');
    const weeklyChart = new Chart(weeklyCtx, {
        type: 'bar',
        data: {
            labels: data.weekly.labels,
            datasets: [{
                label: 'Event frequency per Week',
                data: data.weekly.datasets[0].data,
                backgroundColor: 'rgba(199, 22, 43, 0.2)',
                borderColor: 'rgba(199, 22, 43, 1)',
                borderWidth: 1
            }]
        },
        options: {
            maintainAspectRatio: false,
            responsive: true
        }
    });

    // Extract peak and low values for hourly, daily, and weekly data
    const peakAndLow = (data) => {
        const peakIndex = data.indexOf(Math.max(...data));
        const lowIndex = data.indexOf(Math.min(...data));
        return {
            peakIndex,
            peakValue: data[peakIndex],
            lowIndex,
            lowValue: data[lowIndex]
        };
    };

    // Hourly Peak and Low
    const hourlyPeakLow = peakAndLow(data.hourly.datasets[0].data);
    document.getElementById('peak-hour').textContent = `Peak: Hour ${hourlyPeakLow.peakIndex}`;
    document.getElementById('low-hour').textContent = `Low: Hour ${hourlyPeakLow.lowIndex}`;

    // Daily Peak and Low
    const dailyPeakLow = peakAndLow(data.daily.datasets[0].data);
    document.getElementById('peak-day').textContent = `Peak: ${data.daily.labels[dailyPeakLow.peakIndex]}`;
    document.getElementById('low-day').textContent = `Low: ${data.daily.labels[dailyPeakLow.lowIndex]}`;

    // Weekly Peak and Low
    const weeklyPeakLow = peakAndLow(data.weekly.datasets[0].data);
    document.getElementById('peak-week').textContent = `Peak: Week ${weeklyPeakLow.peakIndex + 1}`;
    document.getElementById('low-week').textContent = `Low: Week ${weeklyPeakLow.lowIndex + 1}`;
});
