"""

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        sol = list()
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    sol.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif -(nums[j] + nums[k]) > nums[i]:
                    j += 1
                else:
                    k -= 1
        f = set()
        # every solution will already be sorted, since i,j,k is sorted
        # just need to remove duplicate solution sets
        for t in sol:
            f.add(tuple(t))
        return [list(item) for item in f]


nums = [-1, 0, 1, 2, -1, -4]
nums2 = [3, 0, -2, -1, 1, 2]
print(Solution().threeSum(nums2))

"""
Leetcode 16
3 sum closest

Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


"""


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = float("-inf")
        min_diff = float("inf")
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                diff = target - s
                if diff == 0:
                    return s
                min_diff = min(min_diff, abs(diff))
                if min_diff == abs(diff):
                    closest = s
                if diff > 0:
                    j += 1
                else:
                    k -= 1
        return closest

print("--------")
print(Solution().threeSumClosest([-1,2,1,-4],1)) # 2
