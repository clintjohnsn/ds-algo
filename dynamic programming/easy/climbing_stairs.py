"""
Leetcode 70

https://leetcode.com/problems/climbing-stairs/


You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""

from typing import Optional

class Solution:
    def climbStairs(self, n: int, dp:Optional[list[int]]=None) -> int:
        if dp is None:
            dp = [-1] * (max(n,1)+1)
            dp[0] = dp[1] = 1
        if dp[n] != -1:
            return dp[n]
        else:
            dp[n] = self.climbStairs(n - 1,dp) + self.climbStairs(n - 2,dp)
            return dp[n]

print(Solution().climbStairs(3))
print(Solution().climbStairs(34))