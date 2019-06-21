# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Attempt 1
class IndicesPicker:
    def __init__(self, input_list, target):  #attributes for input and target
        self.input_list = input_list
        self.target = target

    # target is the sum we need to reach between two numbers from the list.
    # we can iterate through the list twice to add the two numbers to see if they are equal to target.
    # However, we can't have the iteration add on itself, so it needs to skip the index of the first iteration.

    def find_ind(self):
        for a in self.input_list:
            for b in self.input_list:
                if b == a:
                    continue
                elif a+b==self.target:
                    print(self.input_list.index(a), self.input_list.index(b))

# instance1 = IndicesPicker([1,2,3,4,5], 6)
# instance1.find_ind()


# LeetCode Solution Format:

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for a in nums:
            for b in nums:
                if b == a:
                    continue  # this is to skip over self.
                elif a+b==target:
                   return [nums.index(a), nums.index(b)]

# failed. Did not consider duplicates.

# LeetCode Solution Format:
# Solution from LeetCode user zk584807419
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        my_dict={} # this is so that we can keep track of index even after removing it.
        for a in range(len(nums)):
            if target-nums[a] not in my_dict.keys():
                my_dict[nums[a]] = a
            else:
                return [my_dict[target-nums[a]], a]
                
instance1 = Solution()
print(instance1.twoSum([5,3,6,5,3], 6))

# logic. We scan a range of indices that is equal to length of list. 0-4. since the only way for dupes to happen is if the entry is equal, if the number is already in the
# dict, we dont need to add it again, therefore skipping it.
