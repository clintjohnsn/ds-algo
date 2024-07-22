"""
Leetcode 542
https://leetcode.com/problems/01-matrix/

01 matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
horizontal or vertical travelling allowed

Input: mat =    [[0,0,0],
                [0,1,0],
                [1,1,1]]

Output:         [[0,0,0],
                [0,1,0],
                [1,2,1]]

"""

"""
naive/bruteforce
"""
class Solution:

    def dist(self, mat: list[list[int]],out: list[list[int]], i: int, j: int):
        if 0 <= i < len(mat) and 0 <= j < len(mat[i]):
            if out[i][j] != -1:
                return out[i][j]
            if mat[i][j] == 0:
                out[i][j] = 0
                return 0
            elif mat[i][j] == 1:
                mat[i][j] = -1
                result = 1 + min(self.dist(mat,out, i+1, j),
                               self.dist(mat,out, i-1, j),
                               self.dist(mat,out, i, j+1),
                               self.dist(mat,out, i, j-1))
                mat[i][j] = 1
                # out[i][j] = result
                return result
        return float("inf")

    def nearestzero(self, mat: list[list[int]]) -> list[list[int]]:
        out = [[-1] * len(mat[0]) for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if out[i][j] == -1:
                    out[i][j] = self.dist(mat,out, i, j)
        return out


#Driver
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(Solution().nearestzero(mat))

mat2 = [[1,0,1,1,0,0,1,0,0,1],
        [0,1,1,0,1,0,1,0,1,1],
        [0,0,1,0,1,0,0,1,0,0],
        [1,0,1,0,1,1,1,1,1,1],
        [0,1,0,1,1,0,0,0,0,1],
        [0,0,1,0,1,1,1,0,1,0],
        [0,1,0,1,0,1,0,0,1,1],
        [1,0,0,0,1,1,1,1,0,1],
        [1,1,1,1,1,1,1,0,1,0],
        [1,1,1,1,0,1,0,0,1,1]]

mat2 = Solution().nearestzero(mat2)
for i in range(len(mat2)):
    print()
    for j in range(len(mat2[i])):
        print(mat2[i][j],end=' ')

"""
DP
"""

# TODO: implement DP solution