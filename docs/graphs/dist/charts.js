function addData(chart, label, datas) {
    /** 
     * Add a new label and datapoint (x,y) to chart object  
     * 
     * @param {Chart} chart Chart object.
     * @param {string} label Our datetime label (x value).
     * @param {double} datas Power value for our label (y value).
     * 
     * Note: This function assumes our chart has only one dataset. 
     *  If there are multiple you must use dataset[0].data. etc. 
     */
    if (checkData(chart, label)) {
        chart.data.labels.splice(0, 1)
        chart.data.labels.push(label);
        chart.data.datasets.forEach((dataset) => {
            dataset.data.splice(0, 1);
            dataset.data.push(datas);
        });
        chart.update();
        console.log("Chart has been updated with ", label, datas)
    }
    else {
        console.log("Chart has not been updated")
    }
}

function checkData(chart, label) {
    /**
     * Checks the Chart to see if the new label is a new point or not. 
     * 
     * @param {Chart} chart Chart object. 
     * @param {string} label Our datetime label. 
     * 
     * @return {Boolean} returns True if we have a new point, false otherwise. 
     */

    var index = chart.data.labels.length
    var last_label = chart.data.labels[index - 1]

    console.log(last_label)
    console.log(label)

    if (last_label == label) {
        console.log("no update")
        return false
    }

    return true
}

function createGauge(val_id, maxval_id, id) {
    /**
     * Creates a Gauge.
     * 
     * @param {double} val_id HTML id where our value gauge is set to. 
     * @param {double} maxval_id HTML id for our Maximum value of gauge.
     * @param {string} id HTML ID for our gauge element.
     * 
     * @return {Gauge} returns Gauge object.
     */

    // Get values 
    var val = document.getElementById(val_id).value
    var max_val = document.getElementById(maxval_id).value
    console.log("Element ", id, "has a val of ", val, "and max value of ", max_val)
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

function createChart(dates, pwr_vals, future_pwr, maxerr_pwr, minerr_pwr, id, lbl_title, x_axis, y_axis) {
    /**
     * Creates a chart for EV Data. 
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
     * @return {Chart} returns chart object.
     */
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

function createTestChart(id, x_axis, main, max_err, min_err) {
    /**
     * Creates a chart for with Error Bars.  
     * 
     * @param {string} id String of the Element ID in HTML.
     * @param {Array} x_axis Array of dates for our chart. 
     * @param {Array} main Array of power for our chart.
     * @param {Array} max_err Array of positive error bar for our chart.
     * @param {Array} min_err Array of negative error bar for our chart.
     *
     * @return {Chart} Returns the chart object. 
     */
    var ctx_Test = document.getElementById(id).getContext('2d');

    var myChart = new Chart(ctx_Test, {
        type: 'line',
        data: {
            labels: x_axis,
            datasets: [{
                label: 'Power Consumption',
                data: main,
                backgroundColor: 'rgba(215, 135, 48, 0.4)',
                borderColor: '#D78730',
                fill: 'false',
            }, {
                label: 'Max Power Error',
                data: max_err,
                backgroundColor: 'rgba(155, 194, 229, 0.4)',
                borderColor: '#73C2E5',
                fill: '-1',
            }, {
                label: 'Min Power Error',
                data: min_err,
                backgroundColor: 'rgba(155, 194, 229, 0.4)',
                borderColor: '#73C2E5',
                fill: '-2',
            }]
        },
        options: {
            title: {
                display: true,
                text: 'Sample Data',
                fontColor: '#0C5784',
                fontSize: 22,
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Time',
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
                        labelString: 'Power (kW)',
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


function createCarChart(dates, totalcars, chargedcars, id, title, x_axis, y_axis) {
    /**
     * Creates a chart for number of cars.
     * 
     * @param {string} id string of element ID in HTML.
     * @param {Array} dates Array of dates for our chart. 
     * @param {Array} totalcars Array of total cars within the EV parkade. 
     * @param {Array} chargedcars Array of cars that are done charginh in EV parkade. 
     * @param {string} title Title of our chart. 
     * @param {string} x_axis Label for our x_axis. 
     * @param {string} y_axis Label for our y_axis
     * 
     * @return {Chart} Returns chart object 
     */
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

function createBarChart(dates, values, powercap, id, title, x_axis, y_axis) {
    /**
     * Creates a chart for number of cars.
     * 
     * @param {string} id string of element ID in HTML.
     * @param {Array} dates Array of dates for our chart. 
     * @param {Array} values Array of vals for our bar chart 
     * @param {double} powercap Double val that represents the max power we want to avoid.
     * 
     * @return {Chart} Returns chart object 
     */
    var ctx = document.getElementById(id).getContext('2d');

    var pwrcap = []
    for (var x in x_axis) {
        pwrcap.push(powercap)
    }

    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: dates,
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