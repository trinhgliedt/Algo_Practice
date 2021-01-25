# There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red
# costs[1][2] is the cost of painting house 1 with color green, and so on… Find the minimum cost to paint all houses.

# Note:
# All costs are positive integers.

# Example:

# Input: [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
# Minimum cost: 2 + 5 + 3 = 10.

# Solution 1
# Dynamic programming, using red, blue, green to represent the minimum cost of the current location, traversing costs, the state transition equation is:

# red = min(blue, green) + r
# blue = min(red, green) + b
# green = min(ren, blue) + g
# 1
# 2
# 3
# Note that the three variables need to be updated at the same time.
# Time: O(n)
# Space: O(1)
class Solution:
    def minCost(self, costs: 'List[List[int]]') -> 'int':
        red, blue, green = 0, 0, 0
        for r, b, g in costs:
            red, blue, green = min(blue, green) + \
                r, min(red, green) + b, min(red, blue) + g

        return min(red, blue, green)


Solution 2
# The generalized version of Solution 1. The base case returns 0 when costs is empty, defines dp to represent the current minimum cost, traverses costs, and the state transition equation:

# dp[j] = costs[i][j] + min(pre[:j] + pre[j+1:])
# 1
# Means, dp[j] = the cost of taking j in this step + the minimum cost of j in the previous step

# Code


class Solution:
    def minCost(self, costs: 'List[List[int]]') -> 'int':
        # base case
        if not costs:
            return 0

        dp = costs[0][:]
        for i in range(1, len(costs)):
            # get the previous minimum cost
            pre = dp[:]
            for j in range(len(costs[0])):
                dp[j] = costs[i][j] + min(pre[:j] + pre[j+1:])

        return min(dp)
