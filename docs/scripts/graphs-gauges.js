function createGauge(val_id, maxval_id, id) {
    /**
     * Creates a Gauge.
     * 
     * @param {double} val_id HTML id where our value gauge is set to. 
     * @param {double} maxval_id HTML id for our Maximum value of gauge.
     * @param {string} id HTML ID for our gauge element.
     * 
     */

    // Get values 
    var val = document.getElementById(val_id).value
    var max_val = document.getElementById(maxval_id).value
    //Gauge Code 
    var gauge = Gauge(
        document.getElementById(id), {
            max: max_val,
            dialStartAngle: 90,
            dialEndAngle: 0,
            value: 0
        }
    );
    // Set value and animate (value, animation duration in seconds)
    gauge.setValueAnimated(val, 3)
}


function createEVChart(x_axis, y_axis) {
    /**
     * Creates a chart for EV Data. 
     * 
     * @param {Array} x_axis Array of dates for our chart. 
     * @param {Array} y_axis Array of power for our chart.
     */
    var ctx_ev = document.getElementById("myChartEV").getContext('2d');
    document.get

    var myChartEV = new Chart(ctx_ev, {
        type: 'line',
        data: {
            labels: x_axis,
            datasets: [{
                label: 'Power Consumption',
                data: y_axis,
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255,99,132,1)',
            }]
        },
        options: {
            title: {
                display: true,
                text: 'EV Charging Stations'
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Time'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Power'
                    },
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}

function createBuildingChart(x_axis, y_axis) {
    /**
     * Creates a chart for Building Data.
     * 
     * @param {Array} x_axis Array of dates for our chart. 
     * @param {Array} y_axis Array of power for our chart.
     */
    var ctx_building = document.getElementById("myChartBuilding").getContext('2d');

    var myChartBuilding = new Chart(ctx_building, {
        type: 'line',
        data: {
            labels: x_axis,
            datasets: [{
                label: 'Power Consumption',
                data: y_axis,
                backgroundColor: 'rgba(255, 99, 132, 0)',
                borderColor: 'rgba(255,99,132,1)',
            }]
        },
        options: {
            title: {
                display: true,
                text: 'Building Data'
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Time'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Power'
                    },
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}

function createTestChart(x_axis, main, max_err, min_err) {
    /**
     * Creates a chart for with Error Bars.  
     * 
     * @param {Array} x_axis Array of dates for our chart. 
     * @param {Array} main Array of power for our chart.
     * @param {Array} max_err Array of positive error bar for our chart.
     * @param {Array} min_err Array of negative error bar for our chart
     */
    var ctx_Test = document.getElementById("myChartTest").getContext('2d');
    var presets = window.chartColors;
    var utils = Samples.utils;

    var myChartBuilding = new Chart(ctx_Test, {
        type: 'line',
        data: {
            labels: x_axis,
            datasets: [{
                label: 'Power Consumption',
                data: main,
                backgroundColor: utils.transparentize(presets.red),
                borderColor: presets.red,
                fill: 'false',
            }, {
                label: 'Max Power Error',
                data: max_err,
                backgroundColor: utils.transparentize(presets.blue),
                borderColor: presets.blue,
                fill: '-1',
            }, {
                label: 'Min Power Error',
                data: min_err,
                backgroundColor: utils.transparentize(presets.blue),
                borderColor: presets.blue,
                fill: '-2',
            }]
        },
        options: {
            title: {
                display: true,
                text: 'Sample Data'
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Time'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Power'
                    },
                    ticks: {
                        beginAtZero: true
                    }
                }]
            },
            plugins: {
                filler: {
                    propagate: true
                }
            }
        }
    });
}