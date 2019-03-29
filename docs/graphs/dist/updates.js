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
    var timestamp = curr_x.slice(0)
    var val = curr_y.slice(0)
    var predictedpwr = []
    var predictedmax = []
    var predictedmin = []
    formatpredicted(curr_x, pred_x, pred_y, pred_max, pred_min, timestamp, val, predictedval, predictedmax, predictedmin)

    chart.data.datasets[0].data = val
    chart.data.datasets[1].data = predictedval
    chart.data.datasets[2].data = predictedmax
    chart.data.datasets[3].data = predictedmin
    chart.data.labels = timestamp
    chart.update();
}
/**
 * Updates our Chart that has predicted and historic power values. 
 * 
 * @param {Chart} chart Chart object. 
 * @param {Array} timestamps Array of date values.  
 * @param {Array} pwr Array of float values corresponding to power.  
 * @param {string} _url URL to obtain predicted JSON data from.  
 */
function updateChart(chart, timestamps, pwr, _url) {
    $.ajax({
        url: _url,
        type: "GET",
        success: function (data) {
            var result = JSON.parse(data)
            var predicted_date = []
            var predicted_val = []
            var predicted_max = []
            var predicted_min = []
            parsepredicted(predicted_date, predicted_val, predicted_max, predicted_min, result.data)
            //Add most recent datapoint into our chart
            addDataChart(chart, timestamps, pwr, predicted_date, predicted_val, predicted_max, predicted_min)
        },
        error: function (err_data) {
            console.log("error", err_data)
        }
    });
}

/**
 * This function updates our Chart and gauges.  
 * 
 * @param {Chart} chart Chart object.  
 * @param {Gauge} daily_gauge Gauge referring to our daily gauge. 
 * @param {Gauge} monthly_gauge Gauge referring to our monthly gauge. 
 * @param {string} bd_url URL to obtain historical building data in JSON format. 
 * @param {string} pred_url URL to obtain predicted building data in JSON format.  
 * 
 * @returns {Array} returns an array of building power that can be used. 
 */
function updateBuildingData(chart, daily_gauge, monthly_gauge, _url, pred_url) {
    var retval = []
    $.ajax({
        url: _url,
        type: "GET",
        async: false,
        success: function (data) {
            console.log("polling next building point")
            var result = JSON.parse(data)
            var date = []
            var power = []
            parsedata(date, power, result.data)
            //Update our EV gauge and Charts
            daily_gauge.setValue(result.data[0][1])
            monthly_gauge.setValue(result.data[0][1])
            updateChart(chart, date, power, pred_url)
            retval = power.slice(0)
        },
        error: function (err_data) {
            console.log("error", err_data)
        }
    });
    return retval
}

/**
 * Function updates a Chart without gauges. 
 * @param {Chart} chart Chart object. 
 * @param {string} _url string for URL to obtain historical data in JSON format. 
 * @param {string} pred_url string for URL to obtain predicted data in JSON format. 
 */
function updateData(chart, _url, pred_url) {
    $.ajax({
        url: _url,
        type: "GET",
        success: function (data) {
            console.log("polling next vehicle point")
            var result = JSON.parse(data)
            var date = []
            var val = []
            parsedata(date, val, result.data)
            //Update our EV gauge and Charts
            daily_gauge.setValue(result.data[0][1])
            monthly_gauge.setValue(result.data[0][1])
            updateChart(chart, date, val, pred_url)
        },
        error: function (err_data) {
            console.log("error", err_data)
        }
    });
}

/**
 * This function updates our Combo Chart. 
 * @note This assumes timestamps are equal and ev_pwr and bd_pwr have equal amount of points. 
 * 
 * @param {Chart} chart Chart object. 
 * @param {Array} timestamp Array of our date values. 
 * @param {Array} ev_pwr Array of our ev power values. 
 * @param {Array} bd_pwr Array of our building power values. 
 */
function updateComboData(chart, timestamp, ev_pwr, bd_pwr) {
    var total_pwr = []
    for (var x in timestamp) {
        total_pwr.push(ev_pwr[x] + bd_pwr[x])
    }
    console.log("updating combo data")
    console.log(timestamp)
    console.log(ev_pwr)
    chart.data.labels = timestamp
    chart.data.datasets[0].data = ev_pwr
    chart.data.datasets[1].data = bd_pwr
    chart.data.datasets[2].data = total_pwr
    chart.update();
}

/**
 * This function updates our Bar Data. 
 * 
 * @param {Chart} chart Chart object. 
 * @param {Array} power Power of ev charger, building, and total.
 */
function updateBarData(chart, power){
    chart.data.datasets[0].data = power
    chart.update(); 
    console.log("updating bar data")
}

/**
 * Function that helps us parse our predicted data 
 * @note Assumes that the data array is a 2d array where the second dimension corresponds
 * as follows: 
 *  - [0]: date
 *  - [1]: value
 *  - [2]: max 
 *  - [3]: min 
 * 
 * @param {Array} date array of dates 
 * @param {Array} val array of values 
 * @param {Array} max array of max error 
 * @param {Array} min array of min error 
 * @param {Array} data Data array to parse 
 */
function parsepredicted(date, val, max, min, data) {
    var length = data.length - 1
    for (var x in data) {
        date.push((data[length - x][0]).slice(0, 16))
        val.push(data[length - x][1])
        max.push(data[length - x][2])
        min.push(data[length - x][3])
    }
}

/**
 * Function that formats the predicted values with the current values 
 * 
 * @param {Array} curr_date array of current dates
 * @param {Array} pred_date array of predicted dates
 * @param {Array} pred_val array of predicted values 
 * @param {Array} pred_max array of predicted max error
 * @param {Array} pred_min array of predicted min error
 * @param {Array} date array of dates for our graph
 * @param {Array} val array of values for our graph
 * @param {Array} pred array of predictions for our graph
 * @param {Array} max array of max error for our graph
 * @param {Array} min array of min error for our graph 
 */
function formatpredicted(curr_date, pred_date, pred_val, pred_max, pred_min, date, val, pred, max, min) {
    for (var x in curr_date) {
        pred.push(null)
        max.push(null)
        min.push(null)
    }

    for (var y in pred_date) {
        date.push(pred_date[y])
        val.push(null)
        pred.push(pred_val[y])
        max.push(pred_max[y])
        min.push(pred_min[y])
    }
}

/**
 * Function that helps us parse our current data. 
 * @note Assumes that the data array is a 2d array where the second dimension corresponds
 * as follows: 
 *  - [0]: date
 *  - [1]: value
 * 
 * @param {Array} date Array of dates
 * @param {Array} val Array of values 
 * @param {Array} data Array of data to be parsed 
 */
function parsedata(date, val, data) {
    var length = data.length - 1
    for (var x in data) {
        date.push((data[length - x][0]).slice(0, 16))
        val.push(data[length - x][1])
    }
}