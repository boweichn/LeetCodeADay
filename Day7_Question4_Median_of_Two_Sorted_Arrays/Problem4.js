// There are two sorted arrays nums1 and nums2 of size m and n respectively.

// Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

// You may assume nums1 and nums2 cannot be both empty.

// Example 1:

// nums1 = [1, 3]
// nums2 = [2]

// The median is 2.0
// Example 2:

// nums1 = [1, 2]
// nums2 = [3, 4]

// The median is (2 + 3)/2 = 2.5

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */

var findMedianSortedArrays = function(nums1, nums2) {
    const arrSum = arr => arr.reduce((a,b) => a + b, 0);
    const numberSorter = (a, b) => a - b;
    var combined = nums1.concat(nums2).sort(numberSorter),
        lengthOf = combined.length,
        median = 0.0
    if (combined == []){
        return median
    } else if (lengthOf%2 == 0){
        median = arrSum(combined.slice((lengthOf/2)-1,(lengthOf/2)+1))/2
    } else {
        median = parseFloat(combined[Math.floor(lengthOf/2)])
    }
    return median
};

