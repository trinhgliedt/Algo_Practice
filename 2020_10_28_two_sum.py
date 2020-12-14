# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:

# 2 <= nums.length <= 105
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
def twoSum(nums, target):
    result = []
    for j in range (len(nums)):
        for i in range(1, len(nums)):
            anchor = nums[j]
            if ((anchor + nums[i]) == target and i != j):
                result.append(j)
                result.append(i)
                return result
nums = [2,7,11,15]; target = 9;
nums1 = [3,2,4]; target1 = 6;
nums2 = [3,3]; target2 = 6;
nums3 = [2,5,5,11]; target3 = 10;
print(twoSum(nums, target))
print(twoSum(nums1, target1))
print(twoSum(nums2, target2))
print(twoSum(nums3, target3))