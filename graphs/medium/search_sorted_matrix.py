"""

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

"""
matrix = [[1, 2, 5, 7],
         [10, 11, 16, 20],
         [23, 30, 34, 60]]


class Solution:
    def rowsearch(self,matrix: list[list[int]], target: int, i: int, start:int, end:int):
        while start <= end:
            mid = (start + end) //2
            if matrix[i][mid] == target:
                return True
            if matrix[i][mid] < target:
                start = mid + 1
            else:
                end = mid -1
        return False

    def columnsearch(self, matrix: list[list[int]], target: int, start: int, end: int):
        mid = start
        while start <= end:
            mid = (start + end) // 2
            if matrix[mid][0] > target:
                end = mid -1
            if matrix[mid][0] <= target:
                if mid + 1 <= end and matrix[mid+1][0] > target:
                    return mid
                else:
                    start = mid + 1
        return mid

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        column = self.columnsearch(matrix,target,0,m-1)
        return self.rowsearch(matrix,target,column,0,n-1)

print(Solution().searchMatrix(matrix,34))