"""
Leetcode 394

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string],
 where the encoded_string inside the square brackets is being repeated exactly k times.
  Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid.
 Furthermore, you may assume that the original data does not contain any digits and that digits
 are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"

"""
from collections import deque

class Node:
    def __init__(self, mult:int):
        self.char = list()
        self.mult = mult

    def extend(self,clist:list[str]):
        self.char.extend(clist)

class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        stack.appendleft(Node(1))
        num = list()
        for i in range(len(s)):
            if s[i] == '[':
                multiplier = int("".join(num))
                num.clear()
                stack.appendleft(Node(multiplier))
            elif s[i] == ']':
                node = stack.popleft()
                if stack:
                    stack[0].extend(node.char * node.mult)
            elif ord("a") <= ord(s[i]) <= ord("z"):
                stack[0].extend([s[i]])
            else:
                num.append(s[i])
        return "".join(stack[0].char)



print(Solution().decodeString("3[a]2[bc]"))
print(Solution().decodeString("3[a2[c]]"))
print(Solution().decodeString("2[abc]3[cd]ef"))
print(Solution().decodeString("13[a]"))

