# Given an array of integers nums sorted in ascending order
# find the starting and ending position of a given target value
# if target is not found, return [-1,-1]
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Input: nums = [], target = 0
# Output: [-1,-1]

class Solution(object):
    def getLeftPosition(self, nums, target):
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = left+(right-left)//2
            if (nums[mid] == target):
                if (mid-1 >= 0 and nums[mid-1] != target) or mid == 0:
                    return mid
                right = mid-1
            elif (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def getRightPosition(self, nums, target):
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = left+(right-left)//2
            if (nums[mid] == target):
                if (mid+1 < len(nums) and nums[mid+1] != target) or mid == len(nums)-1:
                    return mid
                left = mid+1
            elif (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.getLeftPosition(nums, target)
        right = self.getRightPosition(nums, target)
        return [left, right]


s = Solution()
nums1 = [5, 7, 7, 8, 8, 10]
print(s.searchRange(nums1, 8))
nums2 = [5, 7, 7, 8, 8, 10]
print(s.searchRange(nums2, 6))
