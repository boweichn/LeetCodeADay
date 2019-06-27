# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = sorted(nums1+nums2)
        length_of_combined = len(combined)
        median = float(0)
        if combined == []:
            return 0.0
        elif len(combined)%2 == 0:
            median = sum(combined[int((length_of_combined/2)-1):int((length_of_combined/2)+1)])/2
        else:
            median = float(combined[(len(combined)//2)])
        return median