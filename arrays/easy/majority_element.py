"""
Leetcode 169. Majority Element

The majority element is the element that appears more than ⌊n/2⌋ times.
even number n , eg 6 - > 6//2 > 3  atleast 4 times
odd number n, eg 7,  > 7//2 > 3  atleast 4
You may assume that the majority element always exists in the array.

"""

"""
simple approach - O(N) space
T = O(N)
hashmap
"""
from collections import defaultdict
class Solution:
    def majority_element(self, nums: list[int]) -> int:
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1
        key, val = max(hm.items(), key=lambda x: x[1])
        return key

test = [2,2,1,1,1,2,2] #2
print(Solution().majority_element(test))

"""
challenge = reduce space complexity
"""

"""
Divide and conquer
If we know the majority element in the left and right halves of an array, 
we can determine which is the global majority element in linear time (check which has higher count (2*N)) 

Time complexity : O(nlogn)
Space = O(log n)
"""

class Solution:
    def majority_element(self, nums, lo=0, hi=None):
        def majority_element_rec(lo, hi):
            if lo == hi:
                return nums[lo]
            mid = (hi-lo)//2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)
            if left == right:
                return left
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)
            return left if left_count > right_count else right
        return majority_element_rec(0, len(nums)-1)

print(Solution().majority_element(test))

"""
O(1) Space
sorting based = T =  O(nlogn)
if majority element is minimum, then the first n//2 + 1 elements are it
if majority element is max, then the last n//2 + 1 elements are it
-> majority element will always be at n//2 + 1

"""

class Solution:
    def majority_element(self, nums):
        nums.sort()
        return nums[len(nums)//2]

print(Solution().majority_element(test))


"""
TODO: bit manipulation
If an element majority_element occurs more than n//2 times, 
then there are at least n//2 elements of identical values with num at each bit.
That is, we can reconstruct the exact value of num by combining the most frequent value (0 or 1) at each bit.

Starting from the least significant bit, we enumerate each bit to determine which value is the majority at this bit, 0 or 1, and put this value to the corresponding bit of the result.
Finally, we end up with the most least significant bit of all elements and return the result

Time complexity : O(n * logC) where C is the max possible value
Space = O(1)

"""

"""
Randomization
a random array index is likely to contain the majority element
an expected-constant number of iterations
on average, T = O(N)
space = O(1)

"""
import random

class Solution:
    def majority_element(self, nums):
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate

print(Solution().majority_element(test))


"""
Boyer-Moore Voting Algorithm

+1 for every majority element, -1 for non-majority element

maintain a count, which is incremented whenever we see an instance of our current candidate 
for majority element and decremented whenever we see anything else.
 Whenever count equals 0, we effectively forget about everything in nums up to the current index 
 and consider the current number as the candidate for majority element
 
it is impossible to discard more majority elements than minority elements
 T = O(N)
 S = O(1)
 
 may need a second pass to confirm if existence of majority element is not assured.
"""
class Solution:
    def majority_element(self, nums):
        count = 0
        majority = nums[0]
        for num in nums:
            if count == 0:
                majority = num
            if num == majority:
                count += 1
            else:
                count -= 1
        return majority

print(Solution().majority_element(test))
print("---------------------")

"""
challenge  = Given an integer array of size n, find all elements that appear more than ⌊n/3⌋ times.

[x,y,z] = no majority ( 3//3 = 1)
[x,x,y] = x (2 > 3//3) 
[x,x,y,y,z] = x,y (2 > 5//3)
[x,x,y,y,z,z] = no majority (6//3 = 2)

at max, 2 such elements may exist

"""

"""
Boyer-Moore variation

for n//2, problem, another way of thinking is to form tuples of 2 different elements each time,
 and any leftover may be the majority

[1,1,2,3,1] -> (1,2), (1,3) means 1 is cancelled out by 2 and 3 in two occasions. 
The left over is last: "1" and can be rechecked if it really is majority element.

for n//3, We cancel out excess elements by forming triplets.

1,1,1,1,1,1,2,2,2,3,3,3,4,4,3

(1, 2, 3), (1, 2, 3), (1, 2, 3), (1, 4, 3)
 remaining - one 4 and two 1s
 1 and 4 may be majority

second pass to confirm, gives 1 as the only majority element

"""

class Solution:
    def majority_element(self, nums):
        y,z = None,None
        cy,cz = 0,0
        for num in nums:
            if cy == 0 and num != z:
                y = num
                cy += 1
            elif cz == 0 and num != y:
                z = num
                cz += 1
            elif num == y:
                cy += 1
            elif num == z:
                cz += 1
            else:
                # a triplet can be formed
                cy -= 1
                cz -=1
        output = list()
        if nums.count(y) > len(nums) // 3:
            output.append(y)
        if nums.count(z) > len(nums) // 3:
            output.append(z)
        return output


test = [1,1,1,1,1,1,2,2,2,3,3,3,4,4,3] # 1
print(Solution().majority_element(test))
print(Solution().majority_element([1,2])) # 1,2
print(Solution().majority_element([1])) # 1
print(Solution().majority_element([1,2,1]))  # 1
print(Solution().majority_element([1,2,3])) # none