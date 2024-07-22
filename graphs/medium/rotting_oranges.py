"""
Leetcode 994
https://leetcode.com/problems/rotting-oranges/

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Input: grid =   [[2,1,1],
                [1,1,0],
                [0,1,1]]
Output: 4

Input: grid =   [[2,1,1],
                [0,1,1],
                [1,0,1]]
Output: -1
bottem left cant be reached

Input: grid = [[0,2]]
Output: 0, no fresh oranges
"""
class Solution:
    def any_fresh(self,grid:list[list[int]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return True
        return False

    def get_neighbours(self,grid:list[list[int]], i:int, j:int) -> list[tuple[int]]:
        output = list()
        xs = [0,0,1,-1]
        ys =[1,-1,0,0]
        for k in range(len(xs)):
            x = i + xs[k]
            y = j + ys[k]
            if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == 1:
                output.append((x,y))
        return output

    def rotting_oranges(self, grid: list[list[int]]) -> int:
        rotten = list()
        if not self.any_fresh(grid):
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i,j))
        count = -1
        while rotten:
            count += 1
            next = list()
            for i,j in rotten:
                grid[i][j] = 2
            for i,j in rotten:
                neighbours = self.get_neighbours(grid,i,j)
                if neighbours:
                    next.extend(neighbours)
            rotten = next
        if self.any_fresh(grid):
            return -1
        else:
            return count
# Driver
grid1= [[2,1,1],[1,1,0],[0,1,1]]
grid2 = [[2,1,1],[0,1,1],[1,0,1]]
grid3 = [[0, 2]]
grid4 = [[2,2],
         [1,1],
         [0,0],
         [2,0]]
print(Solution().rotting_oranges(grid1))
print(Solution().rotting_oranges(grid2))
print(Solution().rotting_oranges(grid3))
print(Solution().rotting_oranges(grid4))















