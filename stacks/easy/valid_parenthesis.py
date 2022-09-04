"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.


"""
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        mp = dict()
        mp['{'] = '}'
        mp['('] = ')'
        mp['['] = ']'
        for c in s:
            if stack and mp.get(stack[-1], None) == c:
                stack.pop()
            else:
                stack.append(c)
        if stack:
            return False
        else:
            return True

print(Solution().isValid("[]{([])}{{}}[{}]"))
print(Solution().isValid("[{]"))