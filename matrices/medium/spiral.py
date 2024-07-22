"""
Leetcode 54
https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.

Input:
matrix =    [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]]
Output:     [1,2,3,4,8,12,11,10,9,5,6,7]

"""

"""
T O(mn)
S O(1)
"""
from typing import Optional


class Solution:
    def spiralOrder(self, matrix: list[list[int]],
                    start_i: int = 0, start_j: int = 0,
                    m: Optional[int] = None, n: Optional[int] = None,
                    output: Optional[list[int]] = None) -> list[int]:
        if not matrix or not matrix[0]:
            return list()
        if not output:
            output = list()
        if not m or not n:
            m = len(matrix)
            n = len(matrix[0])
        i, j = start_i, start_j
        if start_i >= m or start_j >= n:
            return output
        if j < n:
            while j < n:
                output.append(matrix[i][j])
                j += 1
            j -= 1
            i += 1
        if i < m:
            while i < m:
                output.append(matrix[i][j])
                i += 1
            i -= 1
            j -= 1
            if j >=start_j:
                while j >= start_j:
                    output.append(matrix[i][j])
                    j -= 1
                j += 1
                i -= 1
                while i > start_i:
                    output.append(matrix[i][j])
                    i -= 1
                i += 1
            return self.spiralOrder(matrix, start_i + 1, start_j + 1, m - 1, n - 1, output)
        return output


# Driver

m1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
m2 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12]]
print(Solution().spiralOrder(m1))
print(Solution().spiralOrder(m2))
print(Solution().spiralOrder([[1]]))
print(Solution().spiralOrder([[]]))
print(Solution().spiralOrder([[1,2,3]]))
print(Solution().spiralOrder([[1], [2], [3]]))

"""
TODO: 
https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
"""


"""
Leetcode 59
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
"""
from collections import deque

class Solution:
    def print(self,mat:list[list[int]])->None:
        for i in range(len(mat)):
            print()
            for j in range(len(mat[i])):
                print(mat[i][j],end='   ')


    def spiralFill(self,mat:list[list[int]],nums:deque[int], start:int, n:int)->None:
        if not nums or start > n:
            return
        for i in range(start,n+1):
            if nums:
                mat[start][i] = nums.popleft()
        for i in range(start+1,n+1):
            if nums:
                mat[i][n] = nums.popleft()
        for i in range(n-1,start-1,-1):
            if nums:
                mat[n][i] = nums.popleft()
        for i in range(n-1,start,-1):
            if nums:
                mat[i][start] = nums.popleft()
        self.spiralFill(mat, nums, start+1, n-1)


    def generateMatrix(self, n: int) -> list[list[int]]:
        mat = [[0] * n for _ in range(n)]
        nums = deque(range(1,n*n+1))
        self.spiralFill(mat,nums,0,n-1)
        return mat

print("-----------")
mat = Solution().generateMatrix(3)
Solution().print(mat)
print()
print("-----------")
mat = Solution().generateMatrix(5)
Solution().print(mat)
print("-----------")
mat = Solution().generateMatrix(6)
Solution().print(mat)
