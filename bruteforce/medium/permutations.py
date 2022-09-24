"""
Leetcode 46
permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


class Solution:
    def permute_helper(self, nums:list[int], permutations: list[list[int]], perm: list[int]) -> None:
        if len(nums) == 0:
            permutations.append(perm)
        for num in nums:
            next = list(filter(lambda x:x!=num, nums))
            self.permute_helper(next, permutations, perm + [num])




    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations = list()
        perm = list()
        self.permute_helper(nums,permutations,perm)
        return permutations

print(Solution().permute([1,2,3]))  #[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(Solution().permute([0,1])) # [[0,1],[1,0]]
print(Solution().permute([1])) # [[1]]

