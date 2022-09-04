"""
Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island
variation of the standard problem: “Counting the number of connected components in an undirected graph”. 
"""

class Graph:
  def __init__(self, row, col, g):
    self.ROW = row
    self.COL = col
    self.graph = g

  def isSafe(self, i, j, visited):
    return (i >= 0 and i < self.ROW and
            j >= 0 and j < self.COL and
            not visited[i][j] and self.graph[i][j]==1)
            
  def DFS(self, i, j, visited):
    rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1];
    colNbr = [-1,  0,  1, -1, 1, -1, 0, 1];
    visited[i][j] = True
    for k in range(8):
        if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
            self.DFS(i + rowNbr[k], j + colNbr[k], visited)

  def countIslands(self):
    visited = [[False]*self.COL for _ in range(self.ROW)]
    count = 0
    for i in range(self.ROW):
        for j in range(self.COL):
            # If a cell with value 1 is not visited yet,
            # then new island found
            if visited[i][j] == False and self.graph[i][j] == 1:
                # Visit all cells in this island
                # and increment island count
                self.DFS(i, j, visited)
                count += 1
    return count

graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]
 
m = len(graph)
n = len(graph[0])
 
g = Graph(m,n, graph)
 
print ("Number of islands is:")
print (g.countIslands())

# Time complexity: O(mn)
# Auxiliary Space: O(mn)

"""
Leetcode 200
count no of islands
horizontal + vertical connection only

"""
class Solution:
    def dfs(self, grid: list[list[str]], i: int, j: int):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == "1":
            grid[i][j] = "0"
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i, j + 1)
            self.dfs(grid, i, j - 1)

    def numIslands(self, grid: list[list[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)
        return count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid))