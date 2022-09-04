"""
Leetcode 695

You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

"""

# ans = 6
grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]





class Solution:
    def getarea(self, grid:list[list[int]], i:int, j:int) -> int:
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        if grid[i][j] == 1:
            grid[i][j] = 0
            return 1 + self.getarea(grid,i+1,j) + self.getarea(grid,i-1,j) +\
                   self.getarea(grid,i,j+1) + self.getarea(grid,i,j-1)

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        maxarea = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    maxarea = max(maxarea,self.getarea(grid,i,j))
        return maxarea

print(Solution().maxAreaOfIsland(grid))