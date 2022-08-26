
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = dict()
        k = -1
        maxstr = 0
        for i in range(len(s)):
            if s[i] not in hm:
                hm[s[i]] = i
            else:
                k = max(k,hm[s[i]])
                hm[s[i]] = i
            maxstr = max(maxstr,i-k)
        return maxstr

print(Solution().lengthOfLongestSubstring("abba"))
print(Solution().lengthOfLongestSubstring("dvdf"))
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring(" "))