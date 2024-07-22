"""
Leetcode 14
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_word=  min(strs,key=lambda x:len(x))
        output = list()
        for i in range(len(min_word)):
            for s in strs:
                if s[i] != min_word[i]:
                    return "".join(output)
            output.append(min_word[i])
        return "".join(output)


print(Solution().longestCommonPrefix( ["flower","flow","flight"])) # "fl"
print(Solution().longestCommonPrefix( ["dog","racecar","car"])) # ""
print(Solution().longestCommonPrefix( ["cir","car"])) # "c"
