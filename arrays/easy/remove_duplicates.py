"""

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place
such that each unique element appears only once. The relative order of the elements should be kept the same.

 if there are k elements after removing the duplicates, 
 then the first k elements of nums array should hold the final result.
 
 return k
 no extra space allowed
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                j +=1
                nums[j] = nums[i]
        return j + 1

nums = [1,1,2,3,4,4,4]
k = Solution().removeDuplicates(nums)
print(nums[:k])