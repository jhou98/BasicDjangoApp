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