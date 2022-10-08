"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays
and you may return the result in any order.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9] or [9,4]

"""

"""
set intersection doesnt work here because of existence of duplicates.
set intersection is simply checking if present in the other set, so takes O(n) time

brute force solution is O(n^2), as checking for presence is O(n) itself

Approach 1
using hashmaps, reduce time to O(n) but space increases to O(n)
Time: O(M + N)
Space: O(min(M, N))
 
"""
from collections import  defaultdict

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2,nums1)
        hm = defaultdict(int)
        for num in nums1:
            hm[num] += 1
        output = []
        for num in nums2:
            if hm[num] > 0:
                hm[num] -=1
                output.append(num)
        return output

print(Solution().intersect( [1,2,2,1],[2,2] )) # [2,2]
print(Solution().intersect( [4,9,5],[9,4,9,8,4])) # [9,4]

"""
Approach 2
sort, then use two pointers.
T = O(MlogM + NlogN, S = O(1)
better if arrays are already sorted, O(n) time and O(1) space 

"""


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) ->list[int]:
        nums1.sort()
        nums2.sort()
        ans = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans

print("------------")
print(Solution().intersect( [1,2,2,1],[2,2] )) # [2,2]
print(Solution().intersect( [4,9,5],[9,4,9,8,4])) # [9,4]

"""
If neither nums1 nor nums2 fits into the memory, 
we split the numeric range into numeric sub-ranges that fit into the memory.
We modify Approach 1 to count only elements which belong to the given numeric sub-range.
We process each numeric sub-ranges one by one, util we process all numeric sub-ranges.

For example:
Input constraint:
1 <= nums1.length, nums2.length <= 10^10.
0 <= nums1[i], nums2[i] < 10^5
Our memory can store up to 1000 elements.
Then we split numeric range into 
numeric sub-ranges [0...999], [1000...1999], ..., [99000...99999],
 then call Approach 1 to process 100 numeric sub-ranges.

"""