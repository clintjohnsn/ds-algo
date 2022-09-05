"""
Leetcode 424

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mem = [0] * 26
        longest = 0
        if len(s) == 1:
            return 1
        i,j = 0,0
        while j < len(s):
            mem[ord(s[j])-ord("A")] +=1
            if (j-i+1) - max(mem) <= k:
                longest = max(longest,j-i+1)
                j+=1
            else:
                mem[ord(s[j]) - ord("A")] -= 1
                mem[ord(s[i])-ord("A")] -=1
                i+=1
        return longest

#
print(Solution().characterReplacement("ABAB",2)) # 4
print(Solution().characterReplacement("AABABBA",1)) #4
print(Solution().characterReplacement("ABBB",2)) # 4
print(Solution().characterReplacement("AABBB",0)) # 3
print(Solution().characterReplacement("ABCDE",1)) # 2

