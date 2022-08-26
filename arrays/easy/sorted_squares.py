"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

"""
# T = O(N), S = O(N)
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        negatives = [abs(num) for num in nums if num < 0]
        positives = [num for num in nums if num >= 0]
        negatives.reverse()
        # merge
        i,j,k = 0,0,0
        while i<len(negatives) and j <len(positives):
            if negatives[i] <= positives[j]:
                nums[k] = negatives[i]
                i+=1
            else:
                nums[k] = positives[j]
                j+=1
            k += 1
        if i == len(negatives):
            while j < len(positives):
                nums[k] = positives[j]
                j += 1
                k += 1
        if j == len(positives):
            while j < len(positives):
                nums[k] = negatives[i]
                i += 1
                k += 1
        nums =[num**2 for num in nums]
        return nums

nums = [-4,-1,0,3,10]
s = Solution().sortedSquares(nums)
print(s)