# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Easy
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
from typing import List


class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [0]*n
        lowestPrice = prices[0]
        dp[0] = prices[0]-lowestPrice
        for i in range(1, n):
            if lowestPrice > prices[i]:
                lowestPrice = prices[i]
            dp[i] = max(dp[i-1], prices[i]-lowestPrice)
        return dp[-1]

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        buyPrice = float('inf')
        profit = 0
        for price in prices:
            if buyPrice > price:
                buyPrice = price
            else:
                profit = max(profit, price-buyPrice)

        return profit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))
print(s.maxProfit([1]))
