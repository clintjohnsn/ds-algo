"""

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

"""

# find max difference subset
# same as max-difference-2-el.py

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        m = 0
        dif = 0
        i = 0
        for j in range(1,len(prices)):
            if prices[j] < prices[i]:
                i = j
            else:
                dif = prices[j] - prices[i]
                m = max(m,dif)
        return m


prices = [7, 1, 5, 3, 6, 4]
prices2 = [7,6,4,3,1]
print(Solution().maxProfit(prices))

"""

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

"""

class Solution:
    def maxProfit2(self, prices: list[int]) -> int:
        mp = 0
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                mp += prices[i+1] - prices[i]
        return mp

print(Solution().maxProfit2(prices))


""""
Leetcode 123
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
TODO: this
"""
