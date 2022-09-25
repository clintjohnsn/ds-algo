"""
Leetcode 76
Minimum Window Substring

Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that every character in t (including duplicates)
 is included in the window. If there is no such substring, return the empty string "".

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

s and t consist of uppercase and lowercase English letters.
"""
from collections import  defaultdict

class Solution:
    def min_window(self, s: str, t: str) -> str:
        hm = defaultdict(int)
        for c in t:
            hm[c] -= 1
        i, j = 0,0
        subs = list()
        while i <= j and j < len(s):
            while j < len(s):
                if s[j] in hm.keys():
                    hm[s[j]] += 1
                    if all([value >= 0 for value in hm.values()]):
                        j += 1
                        break
                j += 1
            while i < j:
                if s[i] in hm.keys():
                    if hm[s[i]] - 1 < 0:
                        break
                    else:
                        hm[s[i]] -= 1
                i += 1
            if all([value >= 0 for value in hm.values()]):
                subs.append((j-i,i,j))
        if not subs:
            return ""
        m,i,j = min(subs)
        return s[i:j]

# Test
print(Solution().min_window("ADOBECODEBANC", "ABC")) # "BANC"
print(Solution().min_window("a", "a")) # "a"
print(Solution().min_window("a", "aa")) # ""
print(Solution().min_window("a", "b")) # ""
