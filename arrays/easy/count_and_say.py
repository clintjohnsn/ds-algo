"""
LeetCode 38
https://leetcode.com/problems/count-and-say/description/

say '445666' -> 2 fours, 1 five and 3 sixes -> 241536

count from 1 to n, and 'say' each number. only output the final number's 'say' value

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

"""

class Solution:
    def say(self,s:str)->str:
        ans = list()
        if len(s) == 0: # empty string
            return ""
        if len(s) == 1: # 1 char string
            return "1" + s[0]
        count = 1
        for i in range(1,len(s)):
            if s[i-1] == s[i]: #keep same number as before, keep counting
                count+=1
            else:
                ans.append(count) # different number, log down counts
                ans.append(s[i-1])
                count = 1
        ans.append(count) # finish up the count of last element
        ans.append(s[-1])
        return "".join([str(x) for x in ans]) # return ans string


    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.say(self.countAndSay(n-1)) # recursively call for n-1 ... 1

print(Solution().countAndSay(4))