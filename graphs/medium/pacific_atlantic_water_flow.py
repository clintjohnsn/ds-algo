"""
Leetcode 417
https://leetcode.com/problems/pacific-atlantic-water-flow/

Pacific Atlantic Water Flow


There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
The Pacific Ocean touches the island's left and top edges,
 and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells.
You are given an m x n integer matrix heights where heights[r][c]
represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly
 north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height.
  Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes
that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

"""


"""

brute forced, bfs approach
 -> TLE
"""

class Solution:

    def bfs(self, heights: list[list[int]], i: int, j: int, pacific: bool=False, atlantic: bool= False) -> tuple[bool, bool]:
        height = heights[i][j]
        heights[i][j] = float("inf")
        moves_i = [0,0,1,-1]
        moves_j = [1,-1,0,0]
        neighbours = [(i + moves_i[k], j + moves_j[k]) for k in range(4)]
        reachable = list()
        for n_i,n_j in neighbours:
            if heights[n_i][n_j] == -1:
                pacific = True
            elif heights[n_i][n_j] == -2:
                atlantic = True
            elif heights[n_i][n_j] <= height and (not atlantic or not pacific):
                reachable.append((n_i,n_j))
        for n_i,n_j in reachable:
            pacific, atlantic = self.bfs(heights, n_i, n_j, pacific, atlantic)
        heights[i][j] = height
        return pacific,atlantic


    def pacific_atlantic(self, heights: list[list[int]]) -> list[list[int]]:
        output = list()
        m, n = len(heights), len(heights[0])
        # new matrix
        # -1 = pacific, -2 = atlantic
        for row in heights:
            row.insert(0, -1)
            row.append(-2)
        heights.insert(0, [-1] * (n+2))
        heights.append([-2] * (n+2))
        m += 2
        n += 2
        for i in range(1,m-1):
            for j in range(1,n-1):
                pacific, atlantic = self.bfs(heights, i, j)
                if pacific and atlantic:
                    output.append([i-1, j-1])
        return output


heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
print(Solution().pacific_atlantic(heights))

"""
dfs approach

start at pacific/atlantic ends and dfs to inwards
"""
class Solution:

    def dfs(self, heights: list[list[int]], pacific:list[list[bool]], i: int, j: int) -> None:
        pacific[i][j] = True
        moves_i = [0,0,1,-1]
        moves_j = [1,-1,0,0]
        neighbours = [(i + moves_i[k], j + moves_j[k]) for k in range(4)]
        for n_i,n_j in neighbours:
            if 0 <= n_i < len(heights) and 0 <= n_j < len(heights[0]) \
                    and heights[n_i][n_j] >= heights[i][j] and not pacific[n_i][n_j]:
                self.dfs(heights,pacific,n_i,n_j)

    def pacific_atlantic(self, heights: list[list[int]]) -> list[list[int]]:
        output = list()
        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        pacific[0] = [True] * n
        for i in range(m):
            pacific[i][0] = True
        atlantic[m-1] = [True] * n
        for i in range(m):
            atlantic[i][n-1] = True
        for i in range(m):
            for j in range(n):
                if pacific[i][j]:
                    self.dfs(heights,pacific,i,j)
        for i in range(m):
            for j in range(n):
                if atlantic[i][j]:
                    self.dfs(heights, atlantic, i, j)
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    output.append([i,j])
        return output

print("------------------------------------")
heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(Solution().pacific_atlantic(heights)) # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
print(Solution().pacific_atlantic([[1]])) #  [[0,0]]
print(Solution().pacific_atlantic([[10,10,10],[10,1,10],[10,10,10]])) #  [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]

