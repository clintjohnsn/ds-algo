"""
LeetCode 567: Permutation in a String
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.


Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

"""

class Solution:
    def __init__(self):
        self.charrray = [0]*26

    def anagram(self,s1:str, s2:str, i:int, j:int):
        for k in range(len(self.charrray)):
            self.charrray[k] = 0
        for c in s1:
            self.charrray[ord(c)-ord("a")] +=1
        for k in range(i,j+1):
            self.charrray[ord(s2[k]) - ord("a")] -=1
            if self.charrray[ord(s2[k]) - ord("a")] < 0:
                return False
        for k in range(len(self.charrray)):
            if self.charrray[k] !=0:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False
        for i in range(len(s2)-n+1):
            if self.anagram(s1,s2,i,i+n-1):
                return True
        return False

    def isAnagram(self,ar1: list[int], ar2:list[int]) -> bool:
        for i in range(len(ar1)):
            if ar2[i] != ar1[i]:
                return False
        return True

    def checkInclusionSW(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False
        s1array = [0] * 26
        charray = [0] * 26
        for c in s1:
            s1array[ord(c)-ord("a")] +=1
        for i in range(n):
            charray[ord(s2[i]) - ord("a")] +=1
        if self.isAnagram(charray,s1array):
            return True
        for i in range(n,len(s2)):
            charray[ord(s2[i-n]) - ord("a")] -= 1
            charray[ord(s2[i]) - ord("a")] += 1
            if self.isAnagram(charray, s1array):
                return True
        return False



print(Solution().checkInclusionSW("ab","eidbaooo"))
print(Solution().checkInclusionSW("ab","eidboaoo"))
print(Solution().checkInclusionSW("adc","dcda"))