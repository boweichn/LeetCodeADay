// Given a string, find the length of the longest substring without repeating characters.

// Example 1:

// Input: "abcabcbb"
// Output: 3 
// Explanation: The answer is "abc", with the length of 3. 
// Example 2:

// Input: "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
// Example 3:

// Input: "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3. 
//              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    var longest = "",
        prev_letter = "",
        length_list = 0;
    for (var i=0; i<s.length; i++) {
        prev_letter = s[i]
        if (!(longest.includes(s[i]))) {
            longest += prev_letter
        } else {
            if (longest.length >= length_list) {
                length_list = longest.length
            }
            longest = longest.split("")
            longest.splice(0,longest.indexOf(s[i])+1)
            longest = longest.join("")+s[i]
        }
    } return Math.max(length_list, longest.length)
};