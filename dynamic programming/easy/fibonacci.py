"""
simple fibonacci sequence impl

"""
from typing import  Optional
class Solution:
    def fib(self, n: int, dp :Optional[list[int]]=None) -> int:
        if dp is None:
            dp = [-1] * (n + 1)
            dp[0] = 0
        if n ==1:
            dp[n] = 1
            return 1
        if dp[n] != -1:
            return dp[n]
        else:
            dp[n] = self.fib(n-1,dp) + self.fib(n-2,dp)
            return dp[n]