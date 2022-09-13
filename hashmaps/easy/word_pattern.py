"""
Leetcode 290
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        hm1 = dict()
        hm2 = dict()
        for i in range(len(pattern)):
            if hm1.get(s[i], None) is None and hm2.get(pattern[i],None) is None:
                hm1[s[i]] = pattern[i]
                hm2[pattern[i]] = s[i]
            else:
                if hm1.get(s[i],None) != pattern[i] or  hm2.get(pattern[i],None) != s[i]:
                    return False
        return True

print(Solution().wordPattern("abba","dog cat cat dog")) # True
print(Solution().wordPattern("abba","dog dog dog dog")) # False
print(Solution().wordPattern("abba","dog cat cat fish")) # False
