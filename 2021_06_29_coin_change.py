# https://leetcode.com/problems/coin-change/
# Medium
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.


# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
# Example 4:

# Input: coins = [1], amount = 1
# Output: 1
# Example 5:

# Input: coins = [1], amount = 2
# Output: 2


# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0

        if min(coins) > amount:
            return -1

        INT_MAX = 1 << 32

        dp = [INT_MAX] * (amount+1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min((dp[i-coin] + 1), dp[i])

        return dp[amount] if dp[amount] != INT_MAX else -1


s = Solution()
print(s.coinChange([1, 2, 5], 11))
