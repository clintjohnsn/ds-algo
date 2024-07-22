# Leetcode 560
# https://leetcode.com/problems/subarray-sum-equals-k/

# Given an unsorted array of non-negative integers, find a continuous sub-array which adds to a given sum.
def subarray_sum(arr,s):
    rs = 0
    i,j = 0,0
    while rs!=s and j<len(arr):
        if rs > s:
            rs -= arr[i]
            i+=1
        if rs < s:
            rs += arr[j]
            j+=1
    if rs == s:
        return i,j-1
    else:
        return -1,-1


arr = [1,0,2,7,5,3,9,3,0,4]
print(subarray_sum(arr,15))

"""
Leetcode 560
including negative numbers
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
Input: nums = [1,1,1], k = 2
Output: 2

-1000 <= nums[i] <= 1000
-107 <= k <= 107

above method wont work if negative numbers included

2. O(n2) time solution is to find every possible i,j pair (subarray) and find sum
find sum - to avoid O(n) time to find sum, either add or remove according to i,j similar to method 1
or keep an array of cumulative sum, then sum(i,j) = cumulativesum(j) - cumulativesum(i)

3. O(n) time solution using hashmap
O(n) space

 If the cumulative sum up to two indices is the same, 
 the sum of the elements lying in between those indices is zero. 
 Extending the same thought further, if the cumulative sum up to two indices, 
 say i and j is at a difference of k i.e. if sum[i] - sum[j] = k, 
 the sum of elements lying between indices i and j is k.
  
"""

from collections import  defaultdict
class Solution:
    def subarray_sum(self, nums: list[int], k: int) -> int:
        # hashmap containing number of times a cumulative sum occurs
        cumulative_sum = defaultdict(int)
        running_sum = 0
        cumulative_sum[0] = 1
        # number of sum ks found
        count = 0
        for num in nums:
            running_sum += num
            count += cumulative_sum[running_sum-k]
            cumulative_sum[running_sum] +=1
        return count


print(Solution().subarray_sum([1, 1, 1], 2)) # 2
print(Solution().subarray_sum([1, 2, 3], 3)) # 2
print(Solution().subarray_sum([1, -1, 0], 0)) # 3
print(Solution().subarray_sum([1], 0)) #0
















