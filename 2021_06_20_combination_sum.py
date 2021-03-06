# https://leetcode.com/problems/combination-sum/
# Medium
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
# Example 4:

# Input: candidates = [1], target = 1
# Output: [[1]]
# Example 5:

# Input: candidates = [1], target = 2
# Output: [[1,1]]


# Constraints:

# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500
from typing import List


class Solution:
    def solution(self, candidates, ans, cur, target, index, sum):
        # we need to keep track of:
        # 1. The current array and its sum
        # 2. Out last index (position of our last candidate). So that we can pop and try a new branch.
        if sum == target:
            ans.append(cur[:])
        elif sum < target:
            n = len(candidates)
            for i in range(index, n):
                cur.append(candidates[i])
                self.solution(candidates, ans, cur,
                              target, i, sum+candidates[i])
                # current candidate was already added to cur above. Below we are popping it to try a new branch
                cur.pop()
            return

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        self.solution(candidates, ans, cur, target, 0, 0)

        return ans
