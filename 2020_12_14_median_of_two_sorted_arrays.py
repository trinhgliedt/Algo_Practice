# Leetcode
# Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# Follow up: The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# Example 3:

# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# Example 4:

# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# Example 5:

# Input: nums1 = [2], nums2 = []
# Output: 2.00000
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # :type nums1: List[int]
        # :type nums2: List[int]
        # :rtype: float
        median = 0
        arr = nums1 + nums2
        arr.sort()
        print(arr)
        if len(arr)%2 == 0:
            median = (arr[int(len(arr)/2)] + arr[int(len(arr)/2)-1])/2
        else: 
            median = arr[int(len(arr)/2)]
        return median

s = Solution()
nums1 = [1,3]; nums2 = [2]
print(s.findMedianSortedArrays(nums1, nums2))
nums1 = [1,2]; nums2 = [3,4]
print(s.findMedianSortedArrays(nums1, nums2))
nums1 = [0,0]; nums2 = [0,0]
nums1 = []; nums2 = [1]
print(s.findMedianSortedArrays(nums1, nums2))
nums1 = [2]; nums2 = []
print(s.findMedianSortedArrays(nums1, nums2))
