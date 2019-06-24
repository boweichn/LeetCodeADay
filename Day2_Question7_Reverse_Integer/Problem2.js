/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    var neg="-"+x.toString().substr("1").split("").reverse().join(""),
        pos=x.toString().split("").reverse().join("");
    if (x < 0){
        if (neg<=Math.pow(-2,31)) {
                return 0
        } else {
            return neg
        }
        
    } else {
        if (pos>=Math.pow(2,31)) {
            return 0
        } else {
            return pos   
        }
    }
    
};