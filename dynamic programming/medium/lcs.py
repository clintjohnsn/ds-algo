
"""
Longest common subsequence
https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
 A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 
 For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. 
used in:
1. File comparison. The Unix program "diff
2. Molecular biology. DNA sequences (genes)
3. Screen redisplay. Many text editors like "emacs" display part of a file on the screen,
updating the screen image as the file is changed. For slow dial-in terminals,
these programs want to send the terminal as few characters as possible to cause
it to update its display correctly. It is possible to view the computation of the
minimum length sequence of characters needed to update the terminal as being a sort of
common subsequence problem (the common subsequence tells you the parts of the display that
are already correct and don't need to be changed).

O(n) time to check if a subsequence is common to both the strings
 nC1 + nC2 + … nCn = 2^n - nC0
So a string of length n has 2^n-1 different possible subsequences.
brute force O(n * 2^n)


# --------------------------------------------------------------------------------
# METHOD 1:
# recursive, non DP, super inefficient, only prints length of lcs
# O(2^n)

# int lcs_length(char * A, char * B)
#   {
# if (*A == '\0' || *B == '\0') return 0;
# else if (*A == *B) return 1 + lcs_length(A+1, B+1);
# else return max(lcs_length(A+1,B), lcs_length(A,B+1));
#   }

"""

#python implementation of above
#
def lcs_length(a,b):
    if len(a)==0 or len(b)==0:
        return 0
    elif a[0]==b[0]:
        return 1+ lcs_length(a[1:],b[1:])
    else:
        return max(lcs_length(a[1:],b),lcs_length(a,b[1:]))

A = "AGGTAB"
B = "GXTXAYB"
print(lcs_length(list(A),list(B)))

# OR

def lcs(X, Y, m, n):
    if m == 0 or n == 0:
       return 0;
    elif X[m-1] == Y[n-1]:
       return 1 + lcs(X, Y, m-1, n-1);
    else:
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));

# # Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs(X , Y, len(X), len(Y)))

# better because a[1:] takes extra spaces ( and  possibly O(n) time as well?)

# --------------------------------------------------------------------------------

"""
METHOD 2:
DP - MEMOIZATION (TOP DOWN)
Time complexity of the above naive recursive approach is O(2^n) in worst case
and worst case happens when all characters of X and Y mismatch i.e., length of LCS is 0.
                 lcs("AXYT", "AYZX")
                       /            \
         lcs("AXY", "AYZX")            lcs("AXYT", "AYZ")
         /             \                 /               \
lcs("AX", "AYZX") lcs("AXY", "AYZ")   lcs("AXY", "AYZ") lcs("AXYT", "AY")
lcs(“AXY”, “AYZ”) is being solved twice.
1) Optimal Substructure and 2) Overlapping Substructure

Python recursion with MEMOIZATION / top down
O(mn)
"""
def lcs(X, Y, m, n, dp): 
    if (m == 0 or n == 0):
        return 0
    if (dp[m][n] != -1):
        return dp[m][n]
    if X[m - 1] == Y[n - 1]:
        dp[m][n] = 1 + lcs(X, Y, m - 1, n - 1, dp)
        return dp[m][n] 
    dp[m][n] = max(lcs(X, Y, m, n - 1, dp),lcs(X, Y, m - 1, n, dp))
    return dp[m][n]
 
# Driver code
X = "AGGTAB"
Y = "GXTXAYB"
m = len(X)
n = len(Y)
dp = [[-1 for i in range(n + 1)]for j in range(m + 1)]
print(f"Length of LCS is {lcs(X, Y, m, n, dp)}")
 
# bottom up
def lcs(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
 
    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]
 
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]

 
# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", lcs(X, Y) )

# printing lcs
# Traverse the 2D array starting from L[m][n]. Do following for every cell L[i][j] 
# If characters (in X and Y) corresponding to L[i][j] are same (Or X[i-1] == Y[j-1]), then include this character as part of LCS. 
# Else compare values of L[i-1][j] and L[i][j-1] and go in direction of greater value.

def lcs(X , Y, L):
    # find the length of the strings
    m = len(X)
    n = len(Y)
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]

def get_lcs(X,Y,L):
   m = len(X)
   n = len(Y)
   s = []
   while(m>0 and n>0):
      if X[m-1] == Y[n-1]:
         s.append(X[m-1])
         m-=1
         n-=1
      else:
         if L[m-1][n] >= L[m][n-1]:
            m-=1
         else:
            n-=1
   return "".join(reversed(s))

# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
# declaring the array for storing the dp values
m = len(X)
n = len(Y)
L = [[None]*(n+1) for i in range(m+1)]
print ("Length of LCS is ", lcs(X, Y, L) )
print(get_lcs(X,Y,L))