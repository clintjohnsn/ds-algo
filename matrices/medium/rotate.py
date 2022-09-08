"""

Leetcode 48

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

Input: matrix =
[[1,2,3],
[4,5,6],
[7,8,9]]
Output:
[[7,4,1],
[8,5,2],
[9,6,3]]

"""
# # driver
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
 
# Test case 2
mat2 = [ [1, 2, 3 ],
        [4, 5, 6 ],
        [7, 8, 9 ] ]
 
# Test case 3
mat3 = [ [1, 2 ],
        [4, 5 ] ]


class Solution:
    def rotate(self, matrix: list[list[int]], start_j:int=None, n:int=None) -> None:
        if not matrix or not matrix[0]:
            return
        if start_j is None:
            start_j, n = 0, len(matrix) - 1
        if start_j >= n:
            return
        j = start_j
        k = 0
        while j < n:
            temp = matrix[start_j+k][n]
            matrix[start_j+k][n] = matrix[start_j][j]
            matrix[start_j][j] = matrix[n - k][start_j]
            matrix[n - k][start_j] = matrix[n][n - k]
            matrix[n][n-k] = temp
            k+=1
            j+=1
        self.rotate(matrix, start_j + 1, n - 1)

    def print(self,matrix:list[list[int]])->None:
        for i in range(len(matrix)):
            print()
            for j in range(len(matrix)):
                print(matrix[i][j],end=' ')

#
Solution().rotate(mat)
Solution().print(mat)
print()
print("---------------- ")
Solution().rotate(mat2)
Solution().print(mat2)
print()
print("---------------- ")
Solution().rotate(mat3)
Solution().print(mat3)