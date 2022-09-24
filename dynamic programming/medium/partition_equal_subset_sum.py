"""
Leetcode 416
Partition Equal Subset Sum

Given a non-empty array nums containing only positive integers,
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Input: nums = [2,2,1,1]
output: True

"""

"""
recursive approach
"""
from collections import  defaultdict
counter = defaultdict(int)

class Solution:
    def partition_helper(self, nums: list[int], i:int, s1:int, s2:int) -> bool:
        counter["recursive"] +=1
        if i == len(nums):
            return s1 == s2
        return self.partition_helper(nums, i+1, s1 + nums[i], s2) or self.partition_helper(nums, i+1, s1, s2 + nums[i])

    def can_partition(self, nums: list[int]) -> bool:
        return self.partition_helper(nums,0,0,0)


# Test
print(Solution().can_partition([1, 5, 11, 5])) # true
print(Solution().can_partition([1, 2, 3, 5])) # false
print(Solution().can_partition([2, 2, 1, 1])) # true
print("------------------")

"""
memoized
"""


class Solution:
    def partition_helper(self, mem: list[list[bool|None]], nums: list[int], i:int, s:int) -> bool:
        counter["memoized"] +=1
        if i == len(nums):
            return s == 0
        if mem[i][s] is not None:
            return mem[i][s]
        mem[i][s] = self.partition_helper(mem, nums, i+1, s + nums[i]) or self.partition_helper(mem, nums, i+1, s - nums[i])
        return mem[i][s]

    def can_partition(self, nums: list[int]) -> bool:
        max_sum = sum(nums)
        mem = [[None] * (2*max_sum) for _ in range(len(nums))]
        return self.partition_helper(mem,nums,0,0)




print(Solution().can_partition([1, 5, 11, 5])) # true
print(Solution().can_partition([1, 2, 3, 5])) # false
print(Solution().can_partition([2, 2, 1, 1])) # true

print("------------------")
print(counter)

"""
TODO further optimization

"""