"""

Leetcode 334
https://leetcode.com/problems/increasing-triplet-subsequence/

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Input: nums = [4,1,5,2,3]
Output: true
1,2,3

"""

"""
recursive solution
TODO: time and space complexity for this 
( > O(N) )
"""
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

print(Solution().increasingTriplet([4,1,5,2,3])) # True
print(Solution().increasingTriplet([2,1,5,0,4,6])) # True
print(Solution().increasingTriplet([6,5,4,3,2])) #False
print(Solution().increasingTriplet([1,2,3,4,5])) # True
print(Solution().increasingTriplet([1,5,0,4,1,3])) #True
print(Solution().increasingTriplet([1,5,0,4,2,1])) # False



"""
approach 2

T= O(N)
S = O(N)

track the minimum element reachable to the left of an element and the max element reachable to the right
"""

class Solution:

    def increasingTriplet(self, nums: list[int]) -> bool:
        left_min = [-1] * len(nums)
        right_max = [-1] * len(nums)
        left_min[0] = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < left_min[i-1]:
                left_min[i] = nums[i]
            else:
                left_min[i] =  left_min[i-1]
        right_max[len(right_max)-1] = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > right_max[i + 1]:
                right_max[i] = nums[i]
            else:
                right_max[i] = right_max[i + 1]
        for i in range(len(nums)):
            if left_min[i] < nums[i] < right_max[i]:
                return True
        return False


print("-------------")
print(Solution().increasingTriplet([4, 1, 5, 2, 3]))  # True
print(Solution().increasingTriplet([2, 1, 5, 0, 4, 6]))  # True
print(Solution().increasingTriplet([6, 5, 4, 3, 2]))  # False
print(Solution().increasingTriplet([1, 2, 3, 4, 5]))  # True
print(Solution().increasingTriplet([1, 5, 0, 4, 1, 3]))  # True
print(Solution().increasingTriplet([1, 5, 0, 4, 2, 1]))  # False

"""
O(1) space 
O(n) time

two variables holding possible i and j

"""

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        i,j = nums[0], float("inf")
        for k in range(1,len(nums)):
            if nums[k] < i:
                i = nums[k]
            elif nums[k] > j:
                return True
            elif i < nums[k] < j:
                j = nums[k]
        return False


print("-------------")
print(Solution().increasingTriplet([4, 1, 5, 2, 3]))  # True
print(Solution().increasingTriplet([2, 1, 5, 0, 4, 6]))  # True
print(Solution().increasingTriplet([6, 5, 4, 3, 2]))  # False
print(Solution().increasingTriplet([1, 2, 3, 4, 5]))  # True
print(Solution().increasingTriplet([1, 5, 0, 4, 1, 3]))  # True
print(Solution().increasingTriplet([1, 5, 0, 4, 2, 1]))  # False