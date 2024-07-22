"""
LeetCode 189: Rotate Array
https://leetcode.com/problems/rotate-array/

Given an array, rotate the array to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

if k > n, k = k % n -> max k = n

with O(N) space, simply copy values in the right position in T = O(N)
with O(k) space, similar
O(1) space solutions:L
1. naive: rotate k times, one by one T = O(N^2)
"""

# T = O(N*k) S = O(K)

def rotate(nums: List[int], k: int) -> None:
  k = k % len(nums)
  if k > 0:
    aux = nums[len(nums)-k:]
    for i in range(len(nums)-k-1,-1,-1):
      nums[i+k] = nums[i]
    for i in range(k):
      nums[i] = aux[i]

"""
juggling
instead of moving one by one, divide the array into different sets where the number of sets is equal to the GCD of N and d (say X. So the elements which are X distance apart are part of a set) and rotate the elements within sets by 1 position to the left. 

Calculate the GCD between the length and the distance to be moved.
The elements are only shifted within the sets.
We start with temp = arr[0] and keep moving arr[I] to arr[I+d] and finally store temp at the right place.
Time complexity : O(N) , S O(1)
"""
"""
Reverse method

Time Complexity: O(N)
Auxiliary Space: O(1)

Reverse the whole array 
Then reverse the last ‘d’ elements and 
Then reverse the first (N-d) elements.
"""
class Solution:
    def reverse(self,nums: list[int],i:int,j:int):
        while i<j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1

            
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        # reverse whole array
        self.reverse(nums,0,len(nums)-1)
        # reverse first k values
        self.reverse(nums,0,k-1)
        # reverse the remaining n-k values
        self.reverse(nums,k,len(nums)-1)
        

"""
python has collections.deque which has a rotate method
"""