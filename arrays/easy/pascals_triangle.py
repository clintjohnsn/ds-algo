"""
leetcode 118
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

"""


class Solution:
    def pascal(self, input:list[int]) -> list[list[int]]:
        output = list()
        for i in range(len(input)+1):
            if i -1 < 0:
                output.append(0 + input[i])
            elif i == len(input):
                output.append(input[i - 1] + 0)
            else:
                output.append(input[i-1] + input[i])
        return output


    def generate(self, numRows: int) -> list[list[int]]:
        output = list([[1]])
        p = [1]
        for i in range(numRows-1):
            p = self.pascal(p)
            output.append(p)
        return output

print(Solution().generate(5))