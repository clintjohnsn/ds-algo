"""
Leetcode 36

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: true


"""
# valid
board1 = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

#invalid
board2 = \
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["1",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

class Solution:

    def clear(self, numbers:list[int]):
        for i in range(len(numbers)):
            numbers[i] = 0

    def validBox(self,numbers:list[int], board:list[list[str]],i1:int,i2:int,j1:int,j2:int):
        self.clear(numbers)
        for i in range(i1,i2+1):
            for j in range(j1,j2+1):
                if board[i][j] != ".":
                    if numbers[int(board[i][j])-1] == 0:
                        numbers[int(board[i][j]) - 1] = 1
                    else:
                        return False
        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        numbers = [0] * 9
        # rows
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if numbers[int(board[i][j])-1] == 0:
                        numbers[int(board[i][j]) - 1] = 1
                    else:
                        return False
            self.clear(numbers)
        # columns
        for j in range(len(board[0])):
            for i in range(len(board)):
                if board[i][j] != ".":
                    if numbers[int(board[i][j])-1] == 0:
                        numbers[int(board[i][j]) - 1] = 1
                    else:
                        return False
            self.clear(numbers)
        # boxes
        return  self.validBox(numbers, board, 0, 2, 0, 2) and \
                self.validBox(numbers, board, 0, 2, 3, 5) and \
                self.validBox(numbers, board, 0, 2, 6, 8) and \
                self.validBox(numbers, board, 3, 5, 0, 2) and \
                self.validBox(numbers, board, 3, 5, 3, 5) and \
                self.validBox(numbers, board, 3, 5, 6, 8) and \
                self.validBox(numbers, board, 6, 8, 0, 2) and \
                self.validBox(numbers, board, 6, 8, 3, 5) and \
                self.validBox(numbers, board, 6, 8, 6, 8)

print(Solution().isValidSudoku(board1))
print(Solution().isValidSudoku(board2))































