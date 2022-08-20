"""
"https://www.geeksforgeeks.org/edit-distance-dp-5/?ref=gcse
Given two strings str1 and str2 and below operations that can be performed on str1. 
Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.  

Insert
Remove
Replace

Input:   str1 = "geek", str2 = "gesek"
Output:  1
We can convert str1 into str2 by inserting a 's'.

Input:   str1 = "sunday", str2 = "saturday"
Output:  3
Last three and first characters are same.  We basically
need to convert "un" to "atur".  This can be done using
below three operations. 
Replace 'n' with 'r', insert t, insert a

 display all the words in a dictionary that are near proximity to a given wordincorrectly spelled word.

---------------------------
let X(0...m) , Y(0..n)  be strings
let E(X(0,m),Y(0,n)) be the edit distance
 
 E(X(i,m),Y(j,n)) =  E(X(i+1,m),Y(j+1,n)) ; if X[i]=Y[j]
                  =  min(
                        1 + E(X(i+1,m),Y(j,n)),
                        1 + E(X(i,m),Y(j+1,n)),
                        1 + E(X(i+1,m),Y(j+1,n))
                        ) ;                 if X[i] !] Y[j]

---------------------------------------------

# basic recursive
def edit_distance(X,i,m,Y,j,n):
    if i > m and j >n:
        return 0
    if j > n:
        return m-i + 1
    if i > m:
        return n-j + 1
    if X[i] == Y[j]:
        return edit_distance(X,i+1,m,Y,j+1,n)
    else:
        return 1 + min(edit_distance(X,i+1,m,Y,j,n),edit_distance(X,i,m,Y,j+1,n), edit_distance(X,i+1,m,Y,j+1,n))


## driver
X = "sunday"
Y = "saturday" # ans - 3
X2 = "voldemort"
Y2 = "dumbledore" # ans - 7 edit distance
print(edit_distance(X,0,len(X)-1,Y,0,len(Y)-1))
print(edit_distance(X2,0,len(X2)-1,Y2,0,len(Y2)-1))
"""
# ---------------------------------------
# memoization

def edit_distance(X,Y):
    m = len(X)-1
    n = len(Y) - 1
    mem = [[None] * (n + 1) for _ in range(m + 1)]
    # start from end, lesser arguments
    ans = ed(X,m,Y,n,mem)
    # print(mem)
    return ans

def ed(X,m,Y,n,mem):
    if mem[m][n] is not None:
        return mem[m][n]
    else:
        if m<0 and n<0:
            mem[m][n] = 0
        elif m<0 and n>=0:
            mem[m][n] = n + 1
        elif m>=0 and n<0:
            mem[m][n] = m + 1
        else:
            if X[m] == Y[n]:
                mem[m][n] = ed(X,m-1,Y,n-1,mem)
            else:
                mem[m][n] = 1 + min(ed(X,m-1,Y,n,mem),ed(X,m,Y,n-1,mem), ed(X,m-1,Y,n-1,mem))
        return mem[m][n]
        
# driver
X = "sunday"
Y = "saturday" # ans - 3
X2 = "voldemort"
Y2 = "dumbledore" # ans - 7 edit distance
print(edit_distance(X,Y))
print(edit_distance(X2,Y2))

"""
TODO: bottom up approach
"""