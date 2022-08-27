class Solution:
    def say(self,s:str)->str:
        ans = list()
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return "1" + s[0]
        count = 1
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                count+=1
            else:
                ans.append(count)
                ans.append(s[i-1])
                count = 1
        ans.append(count)
        ans.append(s[-1])
        return "".join([str(x) for x in ans])


    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.say(self.countAndSay(n-1))

print(Solution().countAndSay(4))