"""
LeetCode 73 : Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

"""

matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = [False] * len(matrix)
        columns = [False] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows[i] = True
                    columns[j] = True
        for i in range(len(matrix)):
            if rows[i]:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
        for j in range(len(matrix[0])):
            if columns[j]:
                for i in range(len(matrix)):
                    matrix[i][j] = 0

    def setZeroesInPlace(self, matrix: list[list[int]]) -> None:
        firstcolumn,firstrow = False,False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                firstcolumn = True
                break
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                firstrow = True
                break

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # use the first row and column as markers
        # if there is a real zero in the first row/column we need to mark those
        for i in range(1,len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1,len(matrix[i])):
                    matrix[i][j] = 0
        for j in range(1,len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1,len(matrix)):
                    matrix[i][j] = 0
        for i in range(len(matrix)):
            if firstcolumn:
                matrix[i][0] = 0
        for j in range(len(matrix[0])):
            if firstrow:
                matrix[0][j] = 0


Solution().setZeroesInPlace(matrix)
for row in matrix:
    print(row)