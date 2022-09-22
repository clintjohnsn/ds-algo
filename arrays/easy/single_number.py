"""
Leetcode 136

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Input: nums = [4,1,2,1,2]
Output: 4

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
"""

"""
len(nums) is odd

"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        bit = 1
        x = 1
        single = 0
        while bit <= 64:
            ones,zeroes = 0,0
            for num in nums:
                if x & num == x:
                    ones += 1
                else:
                    zeroes -= 1
            if ones % 2 == 1:
                single = single | x
            bit += 1
            x = x << 1
        return single


# print(Solution().singleNumber([4,1,2,1,2]))
# print(Solution().singleNumber([1,2,1,4,2]))
# print(Solution().singleNumber([2,2,1]))
print(Solution().singleNumber([-1]))

