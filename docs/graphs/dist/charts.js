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

function createChart(x_axis, y_axis, id, label_title) {
    /**
     * Creates a chart for EV Data. 
     * 
     * @param {Array} x_axis Array of dates for our chart. 
     * @param {Array} y_axis Array of power for our chart.
     * @param {string} id HTML element id. 
     * @param {string} label_title Title of the chart.
     *
     * @return {Chart} returns chart object.
     */
    var ctx = document.getElementById(id).getContext('2d');

    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: x_axis,
            datasets: [{
                label: 'Energy Consumption',
                data: y_axis,
                backgroundColor: 'rgba(155, 194, 229, 0.4)',
                borderColor: '#73C2E5',
            }]
        },
        options: {
            title: {
                display: true,
                text: label_title,
                fontColor: '#0C5784',
                fontSize: 25,
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Timestamp',
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
                        labelString: 'Energy (kWh)',
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
                        labelString: 'Power',
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