"""
Leetcode 2131
You are given an array of strings words.
 Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order.
 Each element can be selected at most once.

Return the length of the longest palindrome that you can create.
 If it is impossible to create any palindrome, return 0.

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.'


"""
from collections import  defaultdict
class Solution:
    def longest_palindrome(self, words: list[str]) -> int:
        repeated = defaultdict(int)
        tlp = defaultdict(int) # two letter palindromes
        length = 0
        for word in words:
            if word[0] == word[1]:
                repeated[word] +=1
            else:
                if tlp[word[::-1]] != 0:
                    tlp[word[::-1]] -= 1
                    length += 4
                else:
                    tlp[word] +=1
        for key,item in repeated.items():
            length += (item //2 ) * 4
            repeated[key] = item % 2
        for key,item in repeated.items():
            if item == 1:
                return length + 2
        return length

    def longest_palindrome_optimized(self, words: list[str]) -> int:
        """
        can be further optimized by using a 2d 26*26 matrix instead of dictionary
        :param words:
        :return:
        """
        hm = defaultdict(int)
        length = 0
        unpaired = 0
        for word in words:
            if word[0] == word[1]:
                if hm[word] > 0:
                    hm[word] -=1
                    unpaired -=1
                    length += 4
                else:
                    hm[word] +=1
                    unpaired +=1
            else:
                if hm[word[::-1]] > 0:
                    hm[word[::-1]] -= 1
                    length += 4
                else:
                    hm[word] +=1
        if unpaired > 0:
            return length + 2
        return length


# Test
t1 = ["lc","cl","gg"] # 6
t2 = ["ab","ty","yt","lc","cl","ab"] # 8  tylcclyt
t3 = ["cc","ll","xx", "xx"] # 6
t4 = ["ab", "cd"] # 0

print(Solution().longest_palindrome(t1))
print(Solution().longest_palindrome(t2))
print(Solution().longest_palindrome(t3))
print(Solution().longest_palindrome(t4))
print("-----------")

print(Solution().longest_palindrome_optimized(t1))
print(Solution().longest_palindrome_optimized(t2))
print(Solution().longest_palindrome_optimized(t3))
print(Solution().longest_palindrome_optimized(t4))