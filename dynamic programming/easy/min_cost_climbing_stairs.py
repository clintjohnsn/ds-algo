"""
Leetcode 746

You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
 Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.


Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6

"""

from typing import Optional
class Solution:
    def minCostClimbingStairs(self, cost: list[int], n:Optional[int]=None, dp:Optional[list[int]]=None) -> int:
        if n is None:
            n = len(cost)
            cost.append(0)
            self.minCostClimbingStairs(cost,n,dp)
        if dp is None:
            dp = [-1] * (n+1)
        if dp[n] != -1:
            return dp[n]
        if n == 0:
            dp[0] = cost[0]
            return dp[0]
        if n == 1:
            dp[1] = cost[1]
            return dp[1]
        dp[n] = cost[n] + min(self.minCostClimbingStairs(cost,n-2,dp), self.minCostClimbingStairs(cost,n-1,dp))
        return dp[n]

print(Solution().minCostClimbingStairs([10,15,20]))
print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
