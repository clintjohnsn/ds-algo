"""
Leetcode 763 Partition Labels
given a string s.
We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order,
the resultant string should be s.

Return a list of integers representing the size of these parts.

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

"""

from collections import  defaultdict
class Solution:
    def partition_labels(self, s: str) -> list[int]:
        hm = defaultdict(int)
        output = list()
        j = -1
        for i in range(len(s)):
            hm[s[i]] = i
        index = -1
        for i in range(len(s)):
            if index == -1:
                index = hm[s[i]]
            if i == index:
                output.append(i - j)
                j = i
                index = -1
            elif hm[s[i]] > index:
                index = hm[s[i]]
        return output

# Test
print(Solution().partition_labels("ababcbacadefegdehijhklij")) #[9,7,8]
print(Solution().partition_labels("eccbbbbdec")) #[10]
print(Solution().partition_labels("eaaaabaaec")) #[9,1]
print(Solution().partition_labels("caedbdedda")) #[1,9]

"""
T = O(N)
S = O(1) (26 char max)
"""