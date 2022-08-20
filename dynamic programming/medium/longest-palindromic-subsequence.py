"""
https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/
 length of the longest palindromic subsequence 
 “BBABCBCAB”, then the output should be 7 as “BABCBAB” is the longest palindromic subsequence in it
 2^n subsequences, O(n) to check if palindrome

 DP

Every single character is a palindrome of length 1
L(i, i) = 1 for all indexes i in given sequence

IF first and last characters are not same
If (X[i] != X[j])  L(i, j) =  max{L(i + 1, j),L(i, j - 1)} 

If there are only 2 characters and both are same
Else if (j == i + 1) L(i, j) = 2  

If there are more than two characters, and first and last 
characters are same
Else L(i, j) =  L(i + 1, j - 1) + 2 

basic recursive 
def lps(seq,i,j):
    if i == j:
        return 1
    if i + 1 == j and seq[i]==seq[j]:
        return 2
    if seq[i] == seq[j]:
        return 2 + lps(seq,i+1,j-1)
    else:
        return max(lps(seq,i+1,j),lps(seq,i,j-1))

"""
# memoization
# Time Complexity: O(n^2)
def lps(seq,i,j,mem):
    if i == j:
        mem[i][j] = 1
        return 1
    if i + 1 == j and seq[i]==seq[j]:
        mem[i][j] = 2
        return 2
    if mem[i][j] != -1:
        return mem[i][j]
    if seq[i] == seq[j]:
        mem[i][j] =  2 + lps(seq,i+1,j-1,mem)
        return mem[i][j]
    else:
        mem[i][j] = max(lps(seq,i+1,j,mem),lps(seq,i,j-1,mem))
        return mem[i][j]


# driver
seq = "GEEKSFORGEEKS"
n = len(seq)
mem = [[-1]*(n+1) for i in range(n+1)]
print("The length of the LPS is", lps(seq, 0, n - 1,mem))


"""
this is same as lcs
The idea used here is to reverse the given input string and check the length of the longest common subsequence. 
That would be the answer for the longest palindromic subsequence.
"""

# import lcs
# L = [[None]*(n+1) for i in range(n+1)]
# print ("Length of palidromic subsequence is ", lcs.lcs(seq,seq[::-1], L) )

