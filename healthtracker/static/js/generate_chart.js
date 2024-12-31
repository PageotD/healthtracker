// Get user name from URL parameter
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const username = urlParams.get('username');
console.log(username);

// Declare a global variable for userUUID
let userUUID;

// Function to get user ID from API
async function getUserID(username) {
    try {
        const response = await fetch(`/user/${username}`);
        const data = await response.json();
        return data.user_id;
    } catch (error) {
        console.error('Error retrieving user ID:', error);
        throw error;
    }
}

// Function to add weight data for the user
function add_weight_data() {
    if (userUUID) {
        console.log(`Using UUID in add_weight_data: ${userUUID}`);
        fetch(`/weight/${userUUID}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                measurement_datetime: document.getElementById('measurement_Date').value,
                weight_value: document.getElementById('weight').value
            })
        })
            .then(response => {
                if (response.ok) {
                    console.log('Weight data added successfully');
                    plot_weight_chart(); // Refresh the chart after adding data
                } else {
                    console.error('Error adding weight data:', response.statusText);
                }
            })
            .catch(error => console.error('Error adding weight data:', error));
    } else {
        console.error("UUID not available!");
    }
}

// Function to add weight data for the user
function add_calories_data() {
    if (userUUID) {
        console.log(`Using UUID in add_calories_data: ${userUUID}`);
        fetch(`/calories/${userUUID}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                measurement_datetime: document.getElementById('calories_measurement_Date').value,
                calories_value: document.getElementById('calories').value
            })
        })
            .then(response => {
                if (response.ok) {
                    console.log('calories data added successfully');
                    plot_calories_chart(); // Refresh the chart after adding data
                } else {
                    console.error('Error adding calories data:', response.statusText);
                }
            })
            .catch(error => console.error('Error adding calories data:', error));
    } else {
        console.error("UUID not available!");
    }
}


// Function to add weight data for the user
function add_sleep_data() {
    if (userUUID) {
        console.log(`Using UUID in add_sleep_data: ${userUUID}`);
        fetch(`/sleep/${userUUID}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                start_datetime: document.getElementById('start_sleep_measurement_Date').value,
                end_datetime: document.getElementById('end_sleep_measurement_Date').value
            })
        })
            .then(response => {
                if (response.ok) {
                    console.log('Sleep data added successfully');
                    plot_sleep_chart(); // Refresh the chart after adding data
                } else {
                    console.error('Error adding sleep data:', response.statusText);
                }
            })
            .catch(error => console.error('Error adding sleep data:', error));
    } else {
        console.error("UUID not available!");
    }
}

// Function to add weight data for the user
function add_activity_data() {
    if (userUUID) {
        console.log(`Using UUID in add_activity_data: ${userUUID}`);
        fetch(`/activity/${userUUID}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                start_datetime: document.getElementById('start_activity_measurement_Date').value,
                end_datetime: document.getElementById('end_activity_measurement_Date').value
            })
        })
            .then(response => {
                if (response.ok) {
                    console.log('Activity data added successfully');
                    plot_activity_chart(); // Refresh the chart after adding data
                } else {
                    console.error('Error adding activity data:', response.statusText);
                }
            })
            .catch(error => console.error('Error activity weight data:', error));
    } else {
        console.error("UUID not available!");
    }
}

// Function to plot the weight chart
function plot_weight_chart() {
    if (!userUUID) {
        console.error('UUID not available for plotting chart!');
        return;
    }

    console.log(`Using UUID in plot_weight_chart: ${userUUID}`);

    // Fetch weight data from the API
    fetch(`/weight/${userUUID}`)
        .then(response => response.json())
        .then(data => {
            const chartLabels = data.date; // Array of dates
            const chartValues = data.weight; // Array of weights (with null for missing values)
            const minWeight = Math.min(...chartValues.filter(value => value !== null))-1.;
            const maxWeight = Math.max(...chartValues.filter(value => value !== null))+1.;

            // Remove any existing chart canvas to prevent overlap
            const oldCanvas = document.getElementById('weightChart');
            if (oldCanvas) {
                oldCanvas.remove();
            }

            // Create a new canvas for the chart
            const newCanvas = document.createElement('canvas');
            newCanvas.id = 'weightChart';
            document.getElementById('weight-chart-container').appendChild(newCanvas);

            // Configure and render the chart
            const ctx = newCanvas.getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: chartLabels,
                    datasets: [{
                        label: 'Weight Over Time',
                        data: chartValues,
                        borderColor: 'rgb(147, 51, 234)',
                        backgroundColor: 'rgba(147, 51, 234, 0.2)',
                        borderWidth: 1.5,
                        tension: 0.1, // Smooth line
                        spanGaps: true // Skip gaps for null values
                    }]
                },
                options: {
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Date'
                            }
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Weight (kg)'
                            },
                            min: Math.round(minWeight),
                            max: Math.round(maxWeight), // Set the maximum value to maxWeight
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error fetching weight data:', error));
}

// Function to plot the weight chart
function plot_calories_chart() {
    if (!userUUID) {
        console.error('UUID not available for plotting chart!');
        return;
    }

    console.log(`Using UUID in plot_calories_chart: ${userUUID}`);

    // Fetch weight data from the API
    fetch(`/calories/${userUUID}`)
        .then(response => response.json())
        .then(data => {
            const chartLabels = data.date; // Array of dates
            const chartValues = data.calories; // Array of weights (with null for missing values)
            const minCalories = Math.min(...chartValues.filter(value => value !== null))-1.;
            const maxCalories = Math.max(...chartValues.filter(value => value !== null))+1.;

            // Remove any existing chart canvas to prevent overlap
            const oldCanvas = document.getElementById('caloriesChart');
            if (oldCanvas) {
                oldCanvas.remove();
            }

            // Create a new canvas for the chart
            const newCanvas = document.createElement('canvas');
            newCanvas.id = 'caloriesChart';
            document.getElementById('calories-chart-container').appendChild(newCanvas);

            // Configure and render the chart
            const ctx = newCanvas.getContext('2d');
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: chartLabels,
                    datasets: [{
                        label: 'Calories Over Time',
                        data: chartValues,
                        borderColor: 'rgb(255, 235, 59)',
                        backgroundColor: 'rgba(255, 235, 59, 0.2)',
                        borderWidth: 1.5,
                        tension: 0.1, // Smooth line
                        spanGaps: true // Skip gaps for null values
                    }]
                },
                options: {
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Date'
                            }
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Calories (kCal)'
                            },
                            min: 0,
                            // max: Math.round(maxCalories), // Set the maximum value to maxWeight
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error fetching weight data:', error));
}

function plot_sleep_chart() {
    if (!userUUID) {
        console.error('UUID not available for plotting chart!');
        return;
    }

    console.log(`Using UUID in plot_sleep_chart: ${userUUID}`);

    // Fetch sleep data from the API
    fetch(`/sleep/${userUUID}`)
        .then(response => response.json())
        .then(data => {
            const chartLabels = data.date;
            const chartValues = data.duration;

            // Remove any existing chart canvas to prevent overlap
            const oldCanvas = document.getElementById('sleepChart');
            if (oldCanvas) {
                oldCanvas.remove();
            }

            // Create a new canvas for the chart
            const newCanvas = document.createElement('canvas');
            newCanvas.id = 'sleepChart';
            document.getElementById('sleep-chart-container').appendChild(newCanvas);

            // Configure and render the chart
            const ctx = newCanvas.getContext('2d');
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: chartLabels,
                    datasets: [{
                        label: 'Sleep Over Time',
                        data: chartValues,
                        borderColor: 'rgb(29, 78, 216)',
                        backgroundColor: 'rgb(29, 78, 216, 0.2)',
                        borderWidth: 1.5,
                        tension: 0.1, // Smooth line
                        spanGaps: true // Skip gaps for null values
                    }]
                },
                options: {
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Date'
                            }
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Duration (hours)'
                            }
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error fetching sleep data:', error));
}

function plot_activity_chart() {
    if (!userUUID) {
        console.error('UUID not available for plotting chart!');
        return;
    }

    console.log(`Using UUID in plot_activity_chart: ${userUUID}`);

    // Fetch sleep data from the API
    fetch(`/activity/${userUUID}`)
        .then(response => response.json())
        .then(data => {
            const chartLabels = data.date;
            const chartValues = data.duration;

            // Remove any existing chart canvas to prevent overlap
            const oldCanvas = document.getElementById('activityChart');
            if (oldCanvas) {
                oldCanvas.remove();
            }

            // Create a new canvas for the chart
            const newCanvas = document.createElement('canvas');
            newCanvas.id = 'activityChart';
            document.getElementById('activity-chart-container').appendChild(newCanvas);

            // Configure and render the chart
            const ctx = newCanvas.getContext('2d');
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: chartLabels,
                    datasets: [{
                        label: 'Activity Over Time',
                        data: chartValues,
                        borderColor: 'rgb(0, 200, 83)',
                        backgroundColor: 'rgba(0, 200, 83,0.2)',
                        borderWidth: 1.5,
                        tension: 0.1, // Smooth line
                        spanGaps: true // Skip gaps for null values
                    }]
                },
                options: {
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Date'
                            }
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Duration (hours)'
                            }
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error fetching activity data:', error));
}

// Initialize the application
getUserID(username)
    .then(user_id => {
        userUUID = user_id[0];
        console.log(`UUID stored: ${userUUID}`);
        document.getElementById('user-id').textContent = userUUID; // Display user ID
        plot_weight_chart(); // Plot the chart after fetching the UUID
        plot_calories_chart();
        plot_sleep_chart();
        plot_activity_chart();
    })
    .catch(error => {
        console.error('Error initializing application:', error);
    });
