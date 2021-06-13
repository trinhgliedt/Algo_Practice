# https://leetcode.com/problems/contains-duplicate/
# #
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
from typing import List
from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # method 1: use counter: This method is faster than using set like in method 2
        map = Counter(nums)
        # print(map)
        for val in map.values():
            if val > 1:
                return True
        return False

        # method 2: use set
        return len(set(nums)) < len(nums)


s = Solution()
print(s.containsDuplicate([1, 2, 3, 1]))
print(s.containsDuplicate([1, 2, 3, 4]))
print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
