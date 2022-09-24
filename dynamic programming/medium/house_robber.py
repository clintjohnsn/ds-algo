"""
Leetcode 198
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
 and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""

"""
recursive approach

"""
counter = {}
counter["recursive"] = 0
counter["memoized"] = 0

class Solution:
    def rob(self, nums: list[int], i: int = 0) -> int:
        counter["recursive"] += 1
        if i >= len(nums):
            return 0
        return max(nums[i] + self.rob(nums, i+2), self.rob(nums, i+1))


print(Solution().rob([2, 7, 9, 3, 1]))  # 12
print(Solution().rob([1, 2, 3, 1])) # 4
print("----")


"""
memoized

"""

class Solution:
    def rob(self, nums: list[int], i: int = 0, mem: list[int]=None) -> int:
        counter["memoized"] += 1
        if not mem:
            mem = [-1] * len(nums)
        if i >= len(nums):
            return 0
        if mem[i] != -1:
            return mem[i]
        mem[i] = max(nums[i] + self.rob(nums, i+2,mem), self.rob(nums, i+1,mem))
        return mem[i]

print(Solution().rob([2, 7, 9, 3, 1]))  # 12
print(Solution().rob([1, 2, 3, 1])) # 4
print("----")

"""
bottom up approach
TODO
"""
print(counter)

