"""
Leetcode 187
https://leetcode.com/problems/repeated-dna-sequences/

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings)
that occur more than once in a DNA molecule. You may return the answer in any order.

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        sset = set()
        output = set()
        for i in range(len(s)-9):
            if s[i:i+10] in sset:
                output.add(s[i:i+10])
            else:
                sset.add(s[i:i+10])
        return list(output)

"""
T = O(n), since pattern length is 10
S = O(n), n-10+1 windows
"""

# Test
print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(Solution().findRepeatedDnaSequences("AAAAAAAAAAA"))

"""
what if pattern length is m, m < n
using above naive approach, T = O(nm), S = O(n-m+1)

"""

"""
Rabin Karp algo

Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) 
that prints all occurrences of pat[] in txt[]. You may assume that n > m.

efficiently calculate hash values for all the substrings of size m of text - 
we must have a hash function which has the following property. 
Hash at the next shift must be efficiently computable from the current hash value and next character in text

https://cp-algorithms.com/string/string-hashing.html#calculation-of-the-hash-of-a-string
https://cp-algorithms.com/string/rabin-karp.html
https://www.programiz.com/dsa/rabin-karp-algorithm

improve no collision probability
just compute two different hashes for each string (by using two different d, and/or different k 
and compare these pairs instead

"""





"""


"""
