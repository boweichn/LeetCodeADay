// LeetCode Template

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// Taking from what we've learned in the Python version
var twoSum = function(nums, target) {
    var indexObj = {}
    for (var i=0; i<nums.length; i++){
        if (!(target-nums[i] in indexObj)){
            indexObj[nums[i]] = i
        } else {
            return [indexObj[target-nums[i]], i]
        }
    }
};