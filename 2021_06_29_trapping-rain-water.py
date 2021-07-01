# https://leetcode.com/problems/trapping-rain-water/
# Hard
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9


# Constraints:

# n == height.length
# 0 <= n <= 3 * 104
# 0 <= height[i] <= 105
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left = [0]*n
        right = [0]*n

        answer = 0

        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(height[i], left[i-1])

        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])

        for i in range(0, n):
            answer += min(left[i], right[i])-height[i]

        return answer
