"""
Leetcode 77
Combinations
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
ie return all nCk combinations

You may return the answer in any order.

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

"""


class Solution:
    def combine_helper(self, n: int, k: int, out:list[list[int]], combination: list[int])->None:
        if k == 0:
            out.append(combination)
            return
        elif n == 0:
            return
        else:
            self.combine_helper(n-1,k-1,out,combination+[n])
            self.combine_helper(n-1,k,out,combination)

    def combine(self, n: int, k: int) -> list[list[int]]:
        out, combination  = list(), list()
        self.combine_helper(n,k,out,combination)
        return out


# test
print(Solution().combine(4,2))
print(Solution().combine(1,1))












