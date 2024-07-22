"""
Leetcode 238
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].

You must write an algorithm that runs in O(n) time and O(1) space and without using the division operation.
the output array does not count as extra space for space complexity analysis.)
"""

"""
with division operation, the problem is trivial

with O(n) space, two cumulative product arrays does the trick
as an optimization, we modify the input and output arrays themselves and use as space

"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = [i for i in nums]
        for i in range(n-2,-1,-1):
            output[i] = output[i+1] * output[i]
        for i in range(1,n):
            nums[i] = nums[i-1] * nums[i]
        for i in range(n):
            if i + 1 == n:
                output[i] = 1 * nums[i - 1]
            elif i - 1 ==-1:
                output[i] = output[i + 1] * 1
            else:
                output[i] = output[i+1] * nums[i-1]
        return output

print(Solution().productExceptSelf([1,2,3,4]))
print(Solution().productExceptSelf( [-1,1,0,-3,3]))

"""
do not modify input array
use a running cumulative product in a single variable
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = [i for i in nums]
        for i in range(n-2,-1,-1):
            output[i] = output[i+1] * output[i]
        cumulative = 1
        for i in range(n):
            if i + 1 == n:
                output[i] = 1 * cumulative
            else:
                output[i] = output[i+1] * cumulative
                cumulative = cumulative * nums[i]
        return output


print(Solution().productExceptSelf([1,2,3,4]))
print(Solution().productExceptSelf( [-1,1,0,-3,3]))