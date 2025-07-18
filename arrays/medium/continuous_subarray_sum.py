"""

523. Continuous Subarray Sum
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
"""

"""
Similar to subarray_sum.py, but here we need to check if the sum is a multiple of k
"""

"""
 If the cumulative sum up to two indices is the same, 
 the sum of the elements lying in between those indices is zero. 
 Extending the same thought further, if the cumulative sum up to two indices, 
 say i and j is at a difference of k i.e. if sum[i] - sum[j] = k, 
 the sum of elements lying between indices i and j is k.

# 23  2  4  6  7
# 23 25  29 35 42 cumulatives
# if j - i = nk
# (j % k) - (i % k) = (nk % k) = 0
# (29 % 6) - (23 % 6) = 5 - 5 = 0
# or (42 % 6 = 0) - (0 % 6 = 0) = 0
# (j % k) - (nk % k = 0) = (i % k)
# j % k == i % k

"""

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        hm = {}
        rs = 0
        hm[0] = -1
        for i in range(len(nums)):
            rs += nums[i]
            if rs % k in hm and i-hm[rs%k] > 1:
                return True
            if rs % k not in hm:
                hm[rs % k] = i 
        return False

    # alt
    def checkSubarraySum2(self, nums, k):
        prefix_mod = 0
        mod_seen = {0: -1}

        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k

            if prefix_mod in mod_seen:
                # ensures that the size of subarray is at least 2
                if i - mod_seen[prefix_mod] > 1:
                    return True
            else:
                # mark the value of prefix_mod with the current index.
                mod_seen[prefix_mod] = i

        return False
    
"""
974. Subarray Sums Divisible by K
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
2 <= k <= 104

"""
from collections import defaultdict

class Solution2:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        hm = defaultdict(int)
        hm[0] = 1
        rs = 0
        count = 0
        for i, num in enumerate(nums):
            rs += num
            count += hm[rs % k]
            hm[rs % k] +=1
        return count



