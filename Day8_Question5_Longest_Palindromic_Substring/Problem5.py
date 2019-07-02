# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

# Brute forced it. Very slow run time. Lets see if we can make if faster with 1 loop instead
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        longest_length = 0
        for letter in s:
            temp = letter
            if temp == temp[::-1] and len(temp)>longest_length:
                    longest = temp
                    longest_length = len(temp)
            for nletter in s[1:]:
                temp += nletter
                if temp == temp[::-1] and len(temp)>longest_length:
                    longest = temp
                    longest_length = len(temp)
            s = s[1:]
        return longest

# much better result by counting indexes.         
class Solution:
    def longestPalindrome(self, s):
        longest = []
        mid_left = 1
        mid_right = 2
        if s == s[::-1]:
            return s
        for i in range(0, len(s)):
            longest.append(s[i])
            while True:
                try:
                    if (s[i] == s[i+1]):
                        if (s[i-mid_left:i+mid_right+1] == s[i-mid_left:i+mid_right+1][::-1]) and (s[i-mid_left:i+mid_right+1] != ""):
                            longest.append(s[i-mid_left:i+mid_right+1])
                            mid_left += 1
                            mid_right += 1
                        else:
                            longest.append(s[i]+s[i+1])
                            break
                    else:
                        break
                except:
                    break
            mid_left = 1
            mid_right = 2
            while True:
                try:
                    if (s[i-mid_left:i+mid_right] == s[i-mid_left:i+mid_right][::-1]) and (s[i-mid_left:i+mid_right]!= ""):
                        longest.append(s[i-mid_left:i+mid_right])
                        mid_left += 1
                        mid_right += 1
                    else:
                        break
                except:
                    break
        longest = sorted(longest, key=len)
        return longest[-1]

