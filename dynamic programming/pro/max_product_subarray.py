"""
Leetcode 152
https://leetcode.com/problems/maximum-product-subarray/

Maximum Product Subarray

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product,
and return the product.

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

2 6 -12 -48
4 -8 -24 -48

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""

"""
brute force
every i,j pair
O(N^2)
"""

class Solution:
    def max_product(self, nums: list[int]) -> int:
        mp = float("-inf")
        for i in range(len(nums)):
            p = 1
            for j in range(i,len(nums)):
                p *= nums[j]
                mp = max(mp,p)
        return mp


"""
DP - bottom up
 2 values: the max cumulative product UP TO current element starting from SOMEWHERE in the past, 
 and the minimum cumuliative product UP TO current element 
 
 at each new element, u could either add the new element to the existing product, 
 or start fresh the product from current index
 if we see a negative number, the "candidate" for max should instead become the previous min product, 
 because a bigger number multiplied by negative becomes smaller,
 
T = O(N)
s = O(1)
"""
class Solution:
    def max_product(self, nums: list[int]) -> int:
        max_i = min_i = max_prod = nums[0]
        for i in range(1,len(nums)):
            max_i,min_i = max(nums[i], nums[i] * max_i, nums[i] * min_i), min(nums[i], nums[i] * max_i, nums[i] * min_i)
            max_prod = max(max_prod,max_i)
        return max_prod


# Test
# print(Solution().maxProduct([2,3,-2,4])) # 6
# print(Solution().maxProduct([-2,0,-1])) # 0
print(Solution().max_product([-4, -3, -2])) # 0



