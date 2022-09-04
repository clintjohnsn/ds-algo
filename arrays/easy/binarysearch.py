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

"""

class Solution:
    def binarysearch(self, nums: list[int], i: int, j: int, target: int, index:int) -> int:
        if i < j:
            k = (j + i) // 2
            if nums[k] == target:
                return k
            elif nums[k] < target:
                index = k+1
                return self.binarysearch(nums, k + 1, j, target,index)
            else:
                index = k
                return self.binarysearch(nums, i, k-1, target,index)
        else:
            return index

    def searchInsert(self, nums: list[int], target: int) -> int:
        return self.binarysearch(nums, 0, len(nums)-1, target, 0)

s = Solution()
# print(s.searchInsert(nums,target))
# print(s.searchInsert([1,2,3,4,5,6],target))
print(s.searchInsert([1,3,5,6],7))