"""
Leetcode 240

search for a value target in an m x n integer matrix.
This matrix has the following properties:

1. Integers in each row are sorted in ascending from left to right.
2. Integers in each column are sorted in ascending from top to bottom.

 Input: matrix = [[1,4,7,11,15],
                 [2,5,8,12,19],
                 [3,6,9,16,22],
                 [10,13,14,17,24],
                 [18,21,23,26,30]],

target = 5

Output: true
"""
from typing import Optional
class Solution:
    def search_matrix(self, matrix: list[list[int]], target: int, start_i:int=0, start_j:int=0,m:Optional[int]=None, n:Optional[int]=None) -> bool:
        if not matrix or not matrix[0]:
            # matrix = None or matrix = [] or matrix = [[]]
            return False
        if m is None or n is None:
            m = len(matrix)
            n = len(matrix[0])
        if start_i < m and start_j < n:
            i = (start_i + m) // 2
            j = (start_j + n) // 2
            if matrix[i][j] == target:
                return True
            elif target > matrix[i][j]:
                # not in left side matrix
                # look in bottom diagonal, bottom left and top right  matrix
                return self.search_matrix(matrix,target,i+1,j+1,m,n) or \
                       self.search_matrix(matrix,target,i+1,start_j,m,n-j) or \
                       self.search_matrix(matrix,target,start_i,j+1,m-i,n)
            else:
                # not in right side matrix
                # look in top diagonal, bottom left and top right matrix
                return self.search_matrix(matrix,target,start_i,start_j,m-i-1,n-j-1) or \
                       self.search_matrix(matrix,target,i,start_j,m,n-j-1) or \
                       self.search_matrix(matrix,target,start_i,j,m-i-1,n)
        return False


# Test
matrix1 = [[1, 4, 7, 11, 15],
          [2, 5, 8, 12, 19],
          [3, 6, 9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]]

matrix2 = [[1,4,7,11,15],
          [2,5,8,12,19],
          [3,6,9,16,22],
          [10,13,14,17,24],
          [18,21,23,26,30]]

# print(Solution().search_matrix(matrix1,5)) # true
# print(Solution().search_matrix(matrix2,20)) # false

matrix3 = [[1, 4, 7, 11],
          [2, 5, 8, 12],
          [3, 6, 9, 16],
          [10, 13, 14,11]]
print(Solution().search_matrix(matrix3,5)) # true

matrix4 = [[1, 4, 7],
          [2, 5, 8],
          [3, 6, 9]]
print(Solution().search_matrix(matrix4,1)) # true

matrix5 = [[1, 4],
          [2, 5]]
print(Solution().search_matrix(matrix5,1)) # true

print(Solution().search_matrix([[-1,3]],-1)) # true
