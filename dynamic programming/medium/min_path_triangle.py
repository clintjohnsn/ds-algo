"""
Leetcode 120
https://leetcode.com/problems/triangle/

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below.
 More formally, if you are on index i on the current row,
 you may move to either index i or index i + 1 on the next row.

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Input: triangle = [[-10]]
Output: -10

"""

"""

recursive solution
"""
from collections import  defaultdict
counter = defaultdict(int)

class Solution:
    def min_path(self, triangle: list[list[int]], i:int, j:int) -> int:
        counter["recursive"] +=1
        if i == len(triangle):
            return 0
        return triangle[i][j] + min(self.min_path(triangle,i+1,j), self.min_path(triangle,i+1,j+1))


    def minimumTotal(self, triangle: list[list[int]]) -> int:
        if not triangle or len(triangle[0]) > 1:
            return 0
        return self.min_path(triangle,0,0)

# Test
print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])) # 11
print(Solution().minimumTotal([[-10]])) # -10
print("--------------")

"""
memoized
"""

class Solution:
    def min_path(self, triangle: list[list[int]], i:int, j:int, dp:list[list[int]]) -> int:
        counter["memoized"] +=1
        if i == len(triangle):
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        dp[i][j] = triangle[i][j] + min(self.min_path(triangle,i+1,j,dp), self.min_path(triangle,i+1,j+1,dp))
        return dp[i][j]

    def minimumTotal(self, triangle: list[list[int]]) -> int:
        if not triangle or len(triangle[0]) > 1:
            return 0
        dp = [[-1] * len(triangle) for _ in range(len(triangle))]
        return self.min_path(triangle,0,0,dp)

# Test
print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])) # 11
print(Solution().minimumTotal([[-10]])) # -10
print("--------------")


""""
TODO: optimize
"""

print(counter)