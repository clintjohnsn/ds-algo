"""
Leetcode 62
There is a robot on an m x n grid.
The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n,
return the number of possible unique paths that the robot can take to reach the bottom-right corner.


Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

"""

class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * (n+1) for _ in range(m+1)]
        if m <=0 or n<=0:
            return 0
        if m == 1 or n == 1:
            return 1
        else:
            return self.uniquePathsHelper(m,n,dp)


    def uniquePathsHelper(self, m: int, n: int, dp:list[list[int]]) -> int:
        if m <=0 or n<=0:
            return 0
        if dp[m][n] != -1:
            return dp[m][n]
        if m == 1 or n == 1:
            dp[m][n] = 1
            return 1
        else:
            dp[m][n] = self.uniquePathsHelper(m-1,n,dp) + self.uniquePathsHelper(m,n-1,dp)
            return dp[m][n]


print(Solution().uniquePaths(3,7))
print(Solution().uniquePaths(3,2))
print(Solution().uniquePaths(4,2))
print(Solution().uniquePaths(23,12)) # even this will take too long if not memoized

