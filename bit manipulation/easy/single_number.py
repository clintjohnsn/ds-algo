"""
Leetcode 136
https://leetcode.com/problems/single-number/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Input: nums = [4,1,2,1,2]
Output: 4

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
"""

"""
len(nums) is odd

T = O(n)
S = O(1)

"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        bit = 1
        x = 1
        single = 0
        while bit <= 128:
            ones,zeroes = 0,0
            for num in nums:
                if x & num == x:
                    ones += 1
                else:
                    zeroes += 1
            if ones % 2 == 1:
                single = single | x
            bit += 1
            x = x << 1
        return single


print(Solution().singleNumber([4,1,2,1,2]))
print(Solution().singleNumber([1,2,1,4,2]))
print(Solution().singleNumber([2,2,1]))
# doesnt work for negative python integers
print(Solution().singleNumber([-1]))
print(Solution().singleNumber([-1,-1,-2]))
print("--------------")

"""
T = O(nlogn)
S = O(nlogn)

"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        x = 1
        while nums:
            if len(nums) == 1:
                break
            ones,zeroes = list(),list()
            for num in nums:
                if x & num == x:
                    ones.append(num)
                else:
                    zeroes.append(num)
            if len(ones) % 2 == 1:
                nums = ones
            else:
                nums = zeroes
            x = x << 1
        return nums[0]


print(Solution().singleNumber([4,1,2,1,2]))
print(Solution().singleNumber([1,2,1,4,2]))
print(Solution().singleNumber([2,2,1]))
print(Solution().singleNumber([-1]))
print(Solution().singleNumber([-1,-1,-2]))
print("--------------")


"""
T = O(n)
S = O(1)

xor
 
 1 ^ 1 == 0 and 0 ^ 0 == 0
 
xor is associative and commutative
if all nums are xored all the same ones will evaluate to 0 and 0^single_number = single_number.
 
"""
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        xor = 0
        for num in nums:
            xor = xor ^ num
        return xor

print(Solution().singleNumber([4,1,2,1,2]))
print(Solution().singleNumber([1,2,1,4,2]))
print(Solution().singleNumber([2,2,1]))
print(Solution().singleNumber([-1]))
print(Solution().singleNumber([-1,-1,-2]))
