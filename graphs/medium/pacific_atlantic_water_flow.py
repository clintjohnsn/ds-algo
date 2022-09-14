class Solution:

    def dfs(self,heights: list[list[int]], i: int, j: int, pacific: bool=False, atlantic: bool= False) -> tuple[bool,bool]:
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
            pacific, atlantic = self.dfs(heights,n_i,n_j,pacific,atlantic)
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
                pacific, atlantic = self.dfs(heights, i, j)
                if pacific and atlantic:
                    output.append([i-1, j-1])
        return output


heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(Solution().pacific_atlantic(heights))
