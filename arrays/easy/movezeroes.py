"""
Leetcode 283
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 T - O(N), S=O(1)
"""
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        i = 0
        while i + zeroes < len(nums):
          if nums[i+zeroes] == 0:
            zeroes +=1
          else:
            nums[i] = nums[i+zeroes]
            i+=1
        while i < len(nums):
          nums[i] = 0
          i +=1

#Driver
nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
print(nums)