# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# using the string style is very simple. 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            if str(x) == str(x)[::-1]: # literally if str is equal to the reverse of string
                return True
            else:
                return False
        else:
            return False

# after doing js. I found that the above solution is very "wordy"

# refactor

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if ((str(x) == str(x)[::-1]) and (x>=0)) else False


# problem also wanted a solution without str conversion. Did not know how to do it, but online solution is as follows:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        rev=0
        while(x>0):
            dig=x%10
            rev=rev*10+dig
            x=x//10
        if(temp==rev):
            return True
        else:
            return False

# Program Explanation
# 1.	User must first enter the value of the integer and store it in a variable.
# 2.	The value of the integer is then stored in another temporary variable.
# 3.	The while loop is used and the last digit of the number is obtained by using the modulus operator.
# 4.	The last digit is then stored at the one’s place, second last at the ten’s place and so on.
# 5.	The last digit is then removed by truly dividing the number with 10.
# 6.	This loop terminates when the value of the number is 0.
# 7.	The reverse of the number is then compared with the integer value stored in the temporary variable.
# 8.	If both are equal, the number is a palindrome.
# 9.	If both aren’t equal, the number isn’t a palindrome.
# 10.	The final result is then printed.