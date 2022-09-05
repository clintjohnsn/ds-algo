"""
Leetcode 409
Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
from collections import  defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = defaultdict(int)
        count = 0
        for c in s:
            hm[c] +=1
        for key,val in hm.items():
            hm[key] = val % 2
            count += 2 * (val//2)
        for val in hm.values():
            if val == 1:
                return count + 1
        return count

print(Solution().longestPalindrome("abccccdd"))
print(Solution().longestPalindrome("a"))