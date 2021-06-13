# https://leetcode.com/problems/majority-element/

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -231 <= nums[i] <= 231 - 1
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = Counter(nums)
        for key, val in map.items():
            if val > len(nums)//2:
                return key

        # this method is slower than the method above
        m = {}
        for num in nums:
            # get value of key num in dict m: the 0 in the get func means if val doesn't exist then consider it 0
            m[num] = m.get(num, 0) + 1
        for num in nums:
            if m[num] > len(nums)//2:
                return num


s = Solution()
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement([3, 2, 3, 1, 3]))
