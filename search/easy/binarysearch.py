"""

search for index
"""

class Solution:
  def binarysearch(self,nums: list[int],i: int, j: int, target:int) -> int:
      if i < j:
          k = (j + i) // 2
          if nums[k] == target:
              return k
          elif nums[k] < target:
              return self.binarysearch(nums,k+1,j,target)
          else:
              return self.binarysearch(nums,i,k,target)
      else:
          return -1

  def search(self, nums: list[int], target: int) -> int:
      return self.binarysearch(nums,0,len(nums),target)
        
nums = [-1,0,3,5,9,12]
target = 9
s = Solution()
print(s.search(nums,target))
print(s.search([1,2,3,4,5,6],target))

"""
 sorted array of distinct integers and a target value, return the index if the target is found. 
 If not, return the index where it would be if it were inserted in order.

Input: nums = [1,3,5,6], target = 2
Output: 1

Input: nums = [1,3,5,6], target = 5
Output: 2
"""

class Solution:
  def binarysearch(self,nums: list[int],i: int, j: int, target:int) -> int:
      if i < j:
          k = (j + i) // 2
          if nums[k] == target:
              return k
          elif nums[k] < target:
              if k+1 >= len(nums) or nums[k+1] > target:
                  return k+1
              return self.binarysearch(nums,k+1,j,target)
          else:
              if k-1 < 0 or nums[k-1] < target:
                  return k
              return self.binarysearch(nums,i,k,target)
      else:
          return -1

  def searchInsert(self, nums: list[int], target: int) -> int:
      return self.binarysearch(nums,0,len(nums),target)

s = Solution()
print("---------")
print(s.searchInsert([1,3,5,6],2)) # 1
print(s.searchInsert([1,3,5,6],5)) # 2
print(s.searchInsert([1,3,5,6],0)) # 0
print(s.searchInsert([1,3,5,6],7)) #4

