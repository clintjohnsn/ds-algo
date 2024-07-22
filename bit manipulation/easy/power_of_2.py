"""
Leetcode 231
https://leetcode.com/problems/power-of-two/

Power of Two
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

-2^31 <= n <= 2^31 - 1

 Input: n = 1
Output: true (2^0)

Input: n = 16
Output: true (2^4)


Input: n = 3
Output: false
"""

"""

-2^31 <= n <= 2^31 - 1
but, negative numbers can only be a power of negative 2

power of two pattern -  00...0100..0
"""
class Solution:
    def is_power_of_two(self, n: int) -> bool:
        if n < 0 :
            return False
        sum = 0
        for i in range(32):
            sum += n & 1
            n = n >> 1
        return sum == 1


print(Solution().is_power_of_two(1))
print(Solution().is_power_of_two(16))
print(Solution().is_power_of_two(3))
print(Solution().is_power_of_two(-16))
print("------")
"""

pow(2, x) == 1 << x

pow(2,x) like  0..100...0
pow(2, x) - 1 like 00..11..1
pow(2, n) & (pow(2, n) - 1) == 0
If m is not a power of two, then the binary form of m contains more than one 1
so m & m - 1 > 0
00...1..1.. & 00...1..011. = 00..1..0..


negative numbers also contain more than one 1,
except for smallest negative number -> better to add condition 

"""

class Solution(object):
    def is_power_of_two(self, n):
        return n and not (n & n - 1)

print(Solution().is_power_of_two(1))
print(Solution().is_power_of_two(16))
print(Solution().is_power_of_two(3))
print(Solution().is_power_of_two(-16))

"""
class Solution {
    public boolean isPowerOfTwo(int n) {
        return n > 0 && (n & n - 1) == 0;
    }
}
"""