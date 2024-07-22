"""
LeetCode: 7. Reverse Integer
https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Input: x = -123
Output: -321

- 12 //10 = -2
-12 % 10 = 8


python has no int limits
Time Complexity: O(log(x)). There are roughly log10(x) digits in x.
Space Complexity: O(1)
"""

class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        negative = x < 0
        x = abs(x)
        while x != 0 and ans <= (2 ** 31) - 1:
            ans *= 10
            ans += x % 10
            x = x // 10
        ans = -1 * ans if negative else ans
        return ans if -2 ** 31 <= ans <= (2 ** 31) - 1 else 0

print(Solution().reverse(-123))


"""
java - if system has max 32 bit integers

if rev > intmax/10, overflow
if rev < intmin/10, underflow
if rev == intmax/10, if pop > 7, overflow ( intmax =  2147483647) (-2 ^31 -1 )
if rev == intmin/10, if pop < -8, underflow ( intmin =  -2147483648) ( -2 ^31)



class Solution {
    public int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > Integer.MAX_VALUE/10 || (rev == Integer.MAX_VALUE / 10 && pop > 7)) return 0;
            if (rev < Integer.MIN_VALUE/10 || (rev == Integer.MIN_VALUE / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
}

"""