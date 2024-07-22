"""
LeetCode: 5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.
Input: s = "babad"
Output: "bab"
"aba" is also a valid answer.
Input: s = "cbbd"
Output: "bb"

"""

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) == 1:
#             return s
#         if len(s) == 2:
#             if s[0] == s[1]:
#                 return s
#             else:
#                 return s[0]
#         longest = 0
#         li,lj = -1,-1
#         M = [[None] * len(s) for _ in range(len(s))]
#         for i in range(len(s)-1):
#             for j in range(1,len(s)):
#                 if self.isPalindrome(M,s,i,j):
#                    if longest < j-i+1:
#                        longest = j-i+1
#                        li = i
#                        lj = j
#         return s[li:lj+1]
#
#     def isPalindrome(self, M:list[list[bool]] ,s:str, i:int,j:int) -> bool:
#         if not M[i][j] is None:
#             return M[i][j]
#         if i == j:
#             M[i][j] = True
#             return True
#         if i+1==j:
#             M[i][j] = s[i] == s[j]
#             return s[i] == s[j]
#         if i<j:
#             if s[i] == s[j]:
#                 M[i][j] = self.isPalindrome(M,s,i+1,j-1)
#             else:
#                 M[i][j] = False
#             return M[i][j]
#         else:
#             return False

# print(Solution().longestPalindrome("babad"))
# print(Solution().longestPalindrome("cbbd"))
# print(Solution().longestPalindrome("aaaa"))
# print(Solution().longestPalindrome("k"))


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        longest = 0
        li,lj = -1,-1
        M = dict()
        for i in range(len(s)-1):
            for j in range(1,len(s)):
                if self.isPalindrome(M,s[i:j+1]):
                   if longest < j-i+1:
                       longest = j-i+1
                       li = i
                       lj = j
        return s[li:lj+1]

    def isPalindrome(self, M:dict ,s:str) -> bool:
        if s in M:
            return M[s]
        if len(s) == 0:
            return True
        if len(s) == 1:
            M[s] = True
            return M[s]
        if s[0] == s[1]:
            if len(s) == 2:
                M[s] = True
            else:
                M[s] = self.isPalindrome(M,s[1:-1])
        else:
            M[s] = False
        return M[s]



print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("aaaa"))
print(Solution().longestPalindrome("k"))
