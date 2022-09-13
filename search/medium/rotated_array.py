"""
Leetcode 33

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
 such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
  For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not

"""


class Solution:
    def largest(self, nums:list[int], start: int, end:int) -> int:
        if start < end:
            if nums[start] > nums[end-1]:
                mid = (start + end ) //2
                maxval = max(nums[start],nums[mid], nums[end-1])
                minval = min(nums[start],nums[mid], nums[end-1])
                if nums[mid] == maxval:
                    if nums[mid-1] < nums[mid] > nums[mid+1]:
                        return mid
                    else:
                        return self.largest(nums, mid+1, end)
                elif nums[mid] == minval:
                    return self.largest(nums,start, mid)
            else:
                return end-1
        else:
            return -1

    def binary_search(self, nums:list[int], target:int, start:int, end:int) -> int:
        if start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return self.binary_search(nums, target, mid + 1, end)
            else:
                return self.binary_search(nums,target,start,mid)
        return -1

    def search(self, nums: list[int], target: int) -> int:
        largest = self.largest(nums, 0 , len(nums))
        if largest == -1:
            return largest
        if nums[largest] == target:
            return largest
        index = self.binary_search(nums, target, 0, largest)
        if index == -1:
            index = self.binary_search(nums,target, largest+1,len(nums))
        return index


#Test
print(Solution().search([4,5,6,7,0,1,2],0)) #4
print(Solution().search([4,5,6,7,0,1,2],3)) #-1
print(Solution().search([1],0)) #-1

