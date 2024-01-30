"""
Leetcode 167

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

You may not use the same element twice.

sorted array, no extra space to be used

"""

"""
If extra space can be used, then simply store the index of integers in a dict in the first pass
then in the 2nd pass, check if the  target-current_num (!= current_num) is present in the dict/set
"""


"""
no extra space solution
use the fact that the array is sorted
"""

class Solution:
  def twoSum(self, numbers: list[int], target: int) -> list[int]:
      i,j = 0,len(numbers)-1
      while i<j:
        if numbers[i] + numbers[j] == target:
          return [i+1,j+1]
        elif numbers[i] + numbers[j] > target:
          j-=1
        else:
          i+=1

numbers = [2,7,11,15]
target = 9
print(Solution().twoSum(numbers,target))


"""
duplicate elements allowed
if you store the indexes in the dict instead, then need a dict (of lists of indexes) for duplicates, 
but dict will still be O(N) space
only works if there is only one solution
"""

"""
dict storing count of appearances solution (suboptimal)
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        p = dict()
        for num in nums:
          p[num] = p.get(num,0) + 1 # count of appearance
        for i in range(len(nums)):
            if p.get(target - nums[i],0) > 0:
              if nums[i] != target - nums[i] or ( nums[i] == target - nums[i] and p.get(target - nums[i],0) > 1):
                for j in range(i+1, len(nums)):
                    if nums[j] == target - nums[i]:
                        return [i,j]


numbers = [2,7,11,15]
target = 9
print(Solution().twoSum(numbers,target))


"""
case where multiple solutions exist, duplicates exist and solution set cant be duplicate
t = 7
numbers = [1,6,2,3,6,1,0,1,6]
ans = [[1,6],[3,4]] or [[6,1],[3,4]]
refer to three sum problem
will need to process solution set with sets

"""