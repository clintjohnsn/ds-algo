"""
Leetcode 844

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".


Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


s= "bxj##tw" t = "bxo#j##tw"
output = true
"""

"""
T = O(n), S= O(n)
n is the number of letters in s or t
"""
from collections import  deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = deque()
        for c in s:
            if c != "#":
                stack.appendleft(c)
            elif stack:
                stack.popleft()
        snew = "".join(stack)
        stack.clear()
        for c in t:
            if c != "#":
                stack.appendleft(c)
            elif stack:
                stack.popleft()
        return snew == "".join(stack)

print(Solution().backspaceCompare("ab#c","ad#c"))
print(Solution().backspaceCompare("ab##","c#d#"))
print(Solution().backspaceCompare("a#c","b"))
print(Solution().backspaceCompare("#a##c","##b#c"))
print(Solution().backspaceCompare("bxj##tw","bxo#j##tw"))

"""
trying S = O(1) solution

does not work for this case:
s= "bxj##tw" t = "bxo#j##tw"
output = true
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        while i > 0 and j > 0:
            while s[i] != "#" and t[j] != "#":
                if s[i] != t[j]:
                    return False
                else:
                    i -= 1
                    j -= 1
            cs = 0
            while s[i] == "#":
                cs += 1
                i -= 1
            while cs > 0:
                i -= 1
                cs -= 1
            ct = 0
            while t[j] == "#":
                ct += 1
                j -= 1
            while ct > 0:
                j -= 1
                ct -= 1
        while i > 0:
            cs = 0
            if s[i] != "#":
                return False
            while s[i] == "#":
                cs += 1
                i -= 1
            while cs > 0:
                i -= 1
                cs -= 1
        while j > 0:
            ct = 0
            if t[j] != "#":
                return False
            while t[j] == "#":
                ct += 1
                j -= 1
            while ct > 0:
                j -= 1
                ct -= 1
        return True


print("----------------")
print(Solution().backspaceCompare("ab#c","ad#c"))
print(Solution().backspaceCompare("ab##","c#d#"))
print(Solution().backspaceCompare("a#c","b"))
print(Solution().backspaceCompare("#a##c","##b#c"))
print(Solution().backspaceCompare("bxj##tw","bxo#j##tw")) # fail

