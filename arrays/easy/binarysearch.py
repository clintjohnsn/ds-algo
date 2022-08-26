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
