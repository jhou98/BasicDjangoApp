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
    var evpwr = curr_y.slice(0)
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
            var predicted_length = result.data.length - 1
            for (var x in result.data) {
                predicted_date.push((result.data[predicted_length - x][0]).slice(0, 16))
                predicted_val.push(result.data[predicted_length - x][1])
                predicted_max.push(result.data[predicted_length - x][2])
                predicted_min.push(result.data[predicted_length - x][3])
            }
            //Add most recent datapoint into our chart
            addDataChart(chart, timestamps, pwr, predicted_date, predicted_val, predicted_max, predicted_min)
        },
        error: function (err_data) {
            console.log("error", err_data)
        }
    });
}

/**
 * This function updates our Building Chart. 
 * 
 * @param {Chart} chart Chart object.  
 * @param {Gauge} daily_gauge Gauge referring to our daily gauge. 
 * @param {Gauge} monthly_gauge Gauge referring to our monthly gauge. 
 * @param {string} bd_url URL to obtain historical building data in JSON format. 
 * @param {string} pred_url URL to obtain predicted building data in JSON format.  
 * 
 * @returns {Array} returns an array of building power that can be used. 
 */
function updateBuildingData(chart, daily_gauge, monthly_gauge, bd_url, pred_url) {
    var retval = []
    $.ajax({
        url: bd_url,
        type: "GET",
        async: false,
        success: function (data) {
            console.log("polling next building point")
            var result = JSON.parse(data)
            var date = []
            var power = []
            //length (as our objects are in Most recent->least recent)
            var length = result.data.length - 1
            for (var x in result.data) {
                //slice the ISO-Format String 
                //YYYY-mm-ddTHH:MM:SS.DDDZ -> YYYY-mm-ddTHH:MM:SS
                date.push(result.data[length - x][0].slice(0, 16))
                power.push(result.data[length - x][1])
            }
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