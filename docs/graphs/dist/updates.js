/**
 * Adds a single point onto the chart by slicing the oldest point and pushing then newest (a shift to the left)
 * 
 * @param {Chart} chart chart object.
 * @param {string} label Our datetime label (x value).
 * @param {double} datas Power value for our label (y value).
 */
function addData(chart, label, datas) {
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

/**
 * 
 * @param {Chart} chart chart object to check for. 
 * @param {string} label datetime label (x val).
 * 
 * @returns {boolean} Returns true if there is a new label, false otherwise.
 */
function checkData(chart, label) {

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

/**
 * Helper function to update our chart. 
 * 
 * @param {Chart} chart Chart object.
 * @param {Array} curr_x Current/Historical timestamps. 
 * @param {Array} curr_y Current/Historical power values.
 * @param {Array} pred_x Predicted timestamps. 
 * @param {Array} pred_y Predicted power values.
 * @param {Array} pred_max Predicted maximum error value. 
 * @param {Array} pred_min Predicted minimum error value. 
 * 
 */
function addDataChart(chart, curr_x, curr_y, pred_x, pred_y, pred_max, pred_min) {
   
    //create the new arrays that will have null values so that total sizes are equal to the label size 
    var timestamp = curr_x
    var evpwr = curr_y
    var predictedpwr = []
    var predictedmax = []
    var predictedmin = []
    for (var x in curr_x) {
        predictedpwr.push(null)
        predictedmax.push(null)
        predictedmin.push(null)
    }
    for (var x in pred_x) {
        timestamp.push(pred_x[x])
        evpwr.push(null)
        predictedpwr.push(pred_y[x])
        predictedmax.push(pred_max[x])
        predictedmin.push(pred_min[x])
    }

    chart.data.datasets[0].data = evpwr
    chart.data.datasets[1].data = predictedpwr
    chart.data.datasets[2].data = predictedmax
    chart.data.datasets[3].data = predictedmin
    chart.data.labels = timestamp
    chart.update();
}