# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        prev_letter = ""
        length_list = 0
        for letter in s:
            prev_letter = letter
            if (letter not in longest):
                longest += prev_letter
            else:
                if len(longest) >= length_list:
                    length_list = len(longest)
                longest = longest[longest.index(letter)+1:]+letter    
        return max(length_list, len(longest))