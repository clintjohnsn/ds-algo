"""
Leetcode 153
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Given the sorted rotated array nums of unique elements, return the minimum element of this array.
Input: nums = [3,4,5,1,2]
Output: 1
"""


class Solution:
    def find_min(self, nums: list[int], start:int=None, end:int=None) -> int:
        if start is None or end is None:
            start = 0
            end = len(nums)-1
        if start <= end:
            if nums[start] > nums[end]:
                mid = (start + end) // 2
                if nums[mid] == max(nums[end],nums[start],nums[mid]):
                    return self.find_min(nums,mid + 1,end)
                if nums[mid] == min(nums[end],nums[start],nums[mid]):
                    if nums[mid] == min(nums[mid],nums[mid-1], nums[mid+1]):
                        return nums[mid]
                    return self.find_min(nums,start,mid-1)
            else:
                return nums[start]
        return -1

print(Solution().find_min([3,4,5,1,2])) # 1
print(Solution().find_min([4,5,6,7,0,1,2])) #0
print(Solution().find_min([11,13,15,17])) # 11
print(Solution().find_min([1])) # 1

print()
print("------------")

"""
above solution passes all test cases, but

if nums[start] < nums[end], ans = nums[start] is this always true??

"""



"""
inflection point solution

an inflection point is where all elements to the left of the point  are greater than nums[0]
and all elements to the right of the point are less than nums[0]

[4,5,6,7,^,0,1,2]

"""

class Solution:
    def find_min(self, nums: list[int]) -> int:
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]
        # left pointer
        left = 0
        # right pointer
        right = len(nums) - 1
        # if the last element is greater than the first element then there is no rotation.
        # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
        # Hence the smallest element is first element. A[0]
        if nums[right] > nums[0]:
            return nums[0]
        while right >= left:
            # Find the mid element
            mid = (left + right) // 2
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                left = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            else:
                right = mid - 1

print(Solution().find_min([3,4,5,1,2])) # 1
print(Solution().find_min([4,5,6,7,0,1,2])) #0
print(Solution().find_min([11,13,15,17])) # 11
print(Solution().find_min([1])) # 1

print()
print("------------")


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
        """
        TODO: convert largest to inflection point method
        """
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

