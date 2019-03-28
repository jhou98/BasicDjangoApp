/**
 * 
 * @param {double} val_id HTML id where our value gauge is set to.
 * @param {double} maxval_id HTML id for our Maximum value of gauge.
 * @param {string} id HTML ID for our gauge element.
 * 
 * @returns {Gauge} returns a Gauge object. 
 */
function createGauge(val_id, maxval_id, id) {
    // Get values 
    var val = document.getElementById(val_id).value
    var max_val = document.getElementById(maxval_id).value
    //Gauge Code 
    var gauge = Gauge(
        document.getElementById(id), {
            max: max_val,
            dialStartAngle: 90,
            dialEndAngle: 0,
            value: 0,
            label: function (value) {
                return Math.round(value * 1000) / 1000;
            } //allows us to have 3 decimal point accuracy 
        }
    );
    // Set value and animate (value, animation duration in seconds)
    gauge.setValueAnimated(val, 3)
    return gauge
}

/**
 * Creates a chart for either building or ev along with predicted values. 
 * 
 * @param {Array} dates Array of dates for our chart. 
 * @param {Array} pwr_vals Array of power for our chart.
 * @param {Array} future_pwr Array of future values for our chart. 
 * @param {Array} maxerr_pwr Array of max error for future values.
 * @param {Array} minerr_pwr Array of min error for future values.
 * @param {string} id HTML element id. 
 * @param {string} lbl_title Title of the chart.
 * @param {string} x_axis Title for x-axis of the chart.
 * @param {string} y_axis Title for y-axis of the chart. 
 * 
 * @returns {Chart} Chart object. 
 */
function createChart(dates, pwr_vals, future_pwr, maxerr_pwr, minerr_pwr, id, lbl_title, x_axis, y_axis) {
    var ctx = document.getElementById(id).getContext('2d');


    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                label: 'EV Consumption',
                data: pwr_vals,
                spanGaps: false,
                backgroundColor: 'rgba(155, 194, 229, 0.4)',
                borderColor: '#73C2E5',
            }, {
                label: 'Predicted Consumption',
                data: future_pwr,
                spanGaps: false,
                backgroundColor: 'rgba(155, 194, 229, 0.4)',
                borderColor: '#73C2E5',
                fill: false,
                borderDash: [10, 10]
            }, {
                label: 'Max',
                data: maxerr_pwr,
                spanGaps: false,
                backgroundColor: 'rgba(215, 135, 48, 0.4)',
                borderColor: '#D78730',
                borderWidth: 1,
                fill: '-1',
                pointRadius: 0,
            }, {
                label: 'Min',
                data: minerr_pwr,
                spanGaps: false,
                backgroundColor: 'rgba(215, 135, 48, 0.4)',
                borderColor: '#D78730',
                borderWidth: 1,
                fill: '-2',
                pointRadius: 0,
            }]
        },
        options: {
            title: {
                display: true,
                text: lbl_title,
                fontColor: '#0C5784',
                fontSize: 25,
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: x_axis,
                        fontColor: '#0C5784',
                        fontSize: 20
                    },
                    ticks: {
                        fontColor: '#0C5784'
                    },
                    gridLines: {
                        color: '#0C5784',
                        display: true
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: y_axis,
                        fontColor: '#0C5784',
                        fontSize: 20,
                    },
                    ticks: {
                        beginAtZero: true,
                        fontColor: '#0C5784'
                    },
                    gridLines: {
                        color: '#0C5784',
                        display: true
                    }
                }],
            },
            legend: {
                labels: {
                    fontColor: '#0C5784'
                }
            },
        }
    });
    return myChart
}

/**
 * Creates a chart with EV power, Building Power, and Total Power. 
 * Assumes that the datetime for EV and Building power are the same. 
 * 
 * @param {Array} dates array of datetime.  
 * @param {Array} ev_pwr array of ev power values.  
 * @param {Array} bd_pwr array of building power values. 
 * @param {string} id Element id in HTMl. 
 * @param {string} title title of the chart.  
 * @param {string} x_axis label of x-axis.  
 * @param {string} y_axis label of y-axis. 
 */
function createComboChart1(dates, ev_pwr, bd_pwr, id, title, x_axis, y_axis) {

    var ctx = document.getElementById(id).getContext('2d');

    var total_pwr = [] 
    for (var x in dates){
        total_pwr.push(ev_pwr[x]+bd_pwr[x])
    }
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                label: 'EV Power',
                data: ev_pwr,
                backgroundColor: 'rgba(155, 194, 229, 0.4)',
                borderColor: '#73C2E5',
                fill: 'zero',
            }, {
                label: 'Building Power',
                data: bd_pwr,
                backgroundColor: 'rgba(215, 135, 48, 0.4)',
                borderColor: '#D78730',
                fill: '-1',
            }, {
                label: 'Total Power',
                data: total_pwr,
                backgroundColor: 'rgba(91, 122, 139, 0.4)',
                borderColor: '#5B7A8B',
                fill: '-1',
            }]
        },
        options: {
            title: {
                display: true,
                text: title,
                fontColor: '#0C5784',
                fontSize: 22,
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: x_axis,
                        fontColor: '#0C5784',
                        fontSize: 20,
                    },
                    ticks: {
                        fontColor: '#0C5784'
                    },
                    gridLines: {
                        color: '#0C5784',
                        display: true
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: y_axis,
                        fontColor: '#0C5784',
                        fontSize: 20,
                    },
                    ticks: {
                        beginAtZero: true,
                        fontColor: '#0C5784'
                    },
                    gridLines: {
                        color: '#0C5784',
                        display: true
                    }
                }],
            },
            plugins: {
                filler: {
                    propagate: true
                }
            },
            legend: {
                labels: {
                    fontColor: '#0C5784'
                }
            },
        }
    });
    return myChart
}

/**
 * Creates a chart for number of cars.
 * 
 * @param {Array} dates Array of dates for our chart. 
 * @param {Array} totalcars Array of total cars within the EV parkade. 
 * @param {Array} chargedcars Array of cars that are done charginh in EV parkade. 
 * @param {string} id Element ID in HTML. 
 * @param {string} title Title of our chart. 
 * @param {string} x_axis Label for our x_axis. 
 * @param {string} y_axis Label for our y_axis
 * 
 * @returns {Chart} Returns chart object.
 */
function createCarChart(dates, totalcars, chargedcars, id, title, x_axis, y_axis) {

    var ctx = document.getElementById(id).getContext('2d');

    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                label: 'Total Connected Vehicles',
                data: totalcars,
                backgroundColor: 'rgba(215, 135, 48, 0.4)',
                borderColor: '#D78730',
                fill: '1',
                stepped: true,
            }, {
                label: 'Charged Vehicles',
                data: chargedcars,
                backgroundColor: 'rgba(155, 194, 229, 0.4)',
                borderColor: '#73C2E5',
                stepped: true,
            }]
        },
        options: {
            title: {
                display: true,
                text: title,
                fontColor: '#0C5784',
                fontSize: 22,
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: x_axis,
                        fontColor: '#0C5784',
                        fontSize: 20,
                    },
                    ticks: {
                        fontColor: '#0C5784'
                    },
                    gridLines: {
                        color: '#0C5784',
                        display: true
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: y_axis,
                        fontColor: '#0C5784',
                        fontSize: 20,
                    },
                    ticks: {
                        beginAtZero: true,
                        fontColor: '#0C5784'
                    },
                    gridLines: {
                        color: '#0C5784',
                        display: true
                    }
                }],
            },
            plugins: {
                filler: {
                    propagate: true
                }
            },
            legend: {
                labels: {
                    fontColor: '#0C5784'
                }
            },
        }
    });
    return myChart
}

/**
 * Creates a bar chart for the power consumption of EV, Building and total.  
 *
 * @param {Array} locations Array of locations for our chart. 
 * @param {Array} values Values corresponding to power at each location. 
 * @param {double} powercap A cap value that you wish to avoid hitting.  
 * @param {string} id Element ID in HTML.
 * @param {string} title Title of our chart. 
 * @param {string} x_axis Label for our x_axis.
 * @param {string} y_axis Label for our y_axis. 
 * 
 * @returns {Chart} Returns a chart object. 
 */
function createBarChart(locations, values, powercap, id, title, x_axis, y_axis) {
   
    var ctx = document.getElementById(id).getContext('2d');

    var pwrcap = []
    for (var x in x_axis) {
        pwrcap.push(powercap)
    }

    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: locations,
            datasets: [{
                label: 'EV Power Consumption',
                data: values,
                backgroundColor: [
                    'rgba(155, 194, 229, 0.4)',
                    'rgba(215, 135, 48, 0.4)',
                    'rgba(91, 122, 139, 0.4)',
                ],
                borderColor: [
                    '#73C2E5',
                    '#D78730',
                    '#5B7A8B'
                ],
                borderWidth: 3
            }, {
                type: 'line',
                label: 'Power Cap',
                data: pwrcap,
                backgroundColor: 'rgba(48, 48, 52, 0.4)',
                borderColor: '#303034',
                borderWidth: 4,
                fill: 'false'
            }],
        },
        options: {
            title: {
                display: true,
                text: title,
                fontColor: '#0C5784',
                fontSize: 22,
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: x_axis,
                        fontColor: '#0C5784',
                        fontSize: 20,
                    },
                    ticks: {
                        fontColor: '#0C5784'
                    },
                    gridLines: {
                        color: '#0C5784',
                        display: true
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: y_axis,
                        fontColor: '#0C5784',
                        fontSize: 20,
                    },
                    ticks: {
                        beginAtZero: true,
                        fontColor: '#0C5784'
                    },
                    gridLines: {
                        color: '#0C5784',
                        display: true
                    }
                }]
            },
            legend: {
                labels: {
                    fontColor: '#0C5784',
                }
            },
        }
    });
    return myChart
}