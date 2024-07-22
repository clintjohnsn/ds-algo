"""
Leetcode 191
https://leetcode.com/problems/number-of-1-bits/

Hamming weight
Number of 1 Bits
takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type.
In this case, the input will be given as a signed integer type.
 It should not affect your implementation,
 as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation.
Therefore, in Example 3, the input represents the signed integer. -3.

Input: n = 00000000000000000000000000001011 (11)
Output: 3

Input: n = 00000000000000000000000010000000 (128)
Output: 1

Input: n = 11111111111111111111111111111101 (-3)
Output: 31
"""


class Solution:
    def hamming_weight(self, n: int) -> int:
        weight = 0
        while n:
            weight +=1
            n = n & n-1
        return weight

    def inbuilt_hamming_weight(self,n:int):
        return bin(n).count('1')


print(Solution().hamming_weight(11))
print(Solution().hamming_weight(128))
# print(Solution().hammingWeight(-3)) # wont work, but input will be unsigned int

print(Solution().inbuilt_hamming_weight(11))
print(Solution().inbuilt_hamming_weight(128))
