"""
713. Subarray Product Less Than K

Given an array of integers nums and an integer k, 
return the number of contiguous subarrays where the product of 
all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106

"""

"""
For each j, let opt(j) be the smallest i so that 
nums[i] * nums[i+1] * ... * nums[j] is less than k. opt is an increasing function.
"""

"""
Key Observations:

The problem requires counting valid subarrays, not returning the actual subarrays.
The values in the nums array are positive.
"""

"""
Sliding Window Approach:
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1: return 0
        i, j  = 0, 0
        p = 1
        count = 0
        while(j < len(nums)):
            p *= nums[j]
            while(p >= k and i <= j):
                p //= nums[i]
                i +=1
            count+= j- i + 1
            j+=1
        return count  

    def alt(self, nums: list[int], k: int) -> int:
        # Handle edge cases where k is 0 or 1 (no subarrays possible)
        if k <= 1:
            return 0

        total_count = 0
        product = 1

        # Use two pointers to maintain a sliding window
        left = 0
        for right, num in enumerate(nums):
            product *= num  # Expand the window by including the element at the right pointer

            # Shrink the window from the left while the product is greater than or equal to k
            while product >= k:
                product //= nums[left]  # Remove the element at the left pointer from the product
                left += 1

            # Update the total count by adding the number of valid subarrays with the current window size
            total_count += right - left + 1  # right - left + 1 represents the current window size

"""
Like  continuous_subarray_sum.py, but here a sliding window is used to maintain the product of the subarray.
"""

"""
Time & Space Complexity:
Time complexity: O(n)

The algorithm iterates through the input array nums using a single for loop. 
Inside the loop, there are nested operations for shrinking the window, 
but since left is incremented a total number of n times during the whole array traversal,
 each element in the array is visited at most twice.

The nested loop terminates when the product becomes less than k, 
and this can only happen at most n times total (once for each element).
 Therefore, the overall time complexity is 2n, which we describe as O(n).

Space complexity: O(1)
"""