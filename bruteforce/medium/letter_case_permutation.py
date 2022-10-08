"""
# Leetcode 784
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Input: s = "3z4"
Output: ["3z4","3Z4"]

"""


class Solution:
    def permute(self, s:str,i:int, out:list[str],perm:list[str])->None:
        if i == len(s):
            out.append("".join(perm))
            return
        if ord("a") <= ord(s[i]) <= ord("z") or ord("A") <= ord(s[i]) <= ord("Z"):
            self.permute(s,i+1,out,perm+[s[i].lower()])
            self.permute(s,i+1,out,perm+[s[i].upper()])
        else:
            perm.append(s[i])
            self.permute(s,i+1,out,perm)


    def letter_case_permutation(self, s: str) -> list[str]:
        out, perm = list(), list()
        self.permute(s,0,out,perm)
        return out

# test
print(Solution().letter_case_permutation("a1b2"))
print(Solution().letter_case_permutation("3z4"))
