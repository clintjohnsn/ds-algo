"""

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Input: nums = [4,1,5,2,3]
Output: true
1,2,3

"""
nums = [4,1,5,2,3]
nums2 = [2,1,5,0,4,6]

class Solution:
    def increasingSub(self, nums:list[int], i:int, k:int, val:int):
        if k == 0:
            return True
        if i == len(nums):
            return False
        if nums[i] > val:
            return self.increasingSub(nums,i+1,k-1,nums[i]) or self.increasingSub(nums,i+1,k,val)
        else:
            return self.increasingSub(nums,i+1,k,val)

    def increasingTriplet(self, nums: list[int]) -> bool:
        return self.increasingSub(nums,0,3,float("-inf"))

    # memoize
    #
    def increasingSubMem(self, mem:list[int], nums: list[int], i: int, k: int):
        if k == 0:
            return True
        if i == len(nums):
            return False
        if nums[i] > mem[k]:
            return self.increasingSubMem(mem, nums, i + 1, k - 1) or self.increasingSubMem(mem, nums, i + 1, k)
        else:
            return self.increasingSubMem(mem, nums, i + 1, k)

    def increasingTripletMem(self, nums: list[int]) -> bool:
        mem = [0] * 3
        return self.increasingSubMem(mem, nums, 0, 2)


print(Solution().increasingTriplet([4,1,5,2,3]))
print(Solution().increasingTriplet([2,1,5,0,4,6]))
print(Solution().increasingTriplet([6,5,4,3,2]))
print(Solution().increasingTriplet([1,2,3,4,5]))
print(Solution().increasingTriplet([1,5,0,4,1,3]))


