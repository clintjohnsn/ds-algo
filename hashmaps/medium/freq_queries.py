# You are given q queries. Each query is of the form two integers described below:
# -  1x: Insert x in your data structure.
# -  2y: Delete one occurence of y from your data structure, if present.
# -  3z: Check if any integer is present whose frequency is z exactly . If yes, print 1 else 0

# Operation   Array   Output
# (1,1)       [1]
# (2,2)       [1]
# (3,2)                   0
# (1,1)       [1,1]
# (1,1)       [1,1,1]
# (2,1)       [1,1]
# (3,2)                   1

# o/p = [0,1]

from collections import defaultdict

def ins(D,x):
    D[x] +=1
    
def delt(D,x):
    if D[x] > 0:
        D[x] -=1
    else:
        D[x] = 0


def freqQuery(queries):
    ans = []
    S = defaultdict(int)
    F = defaultdict(int)
    for f,x in queries:
        if f == 1:
            delt(F,S[x])
            ins(S,x)
            ins(F,S[x])     
        if f == 2:      
            delt(F,S[x])
            delt(S,x)
            ins(F,S[x])
        if f == 3:
            ans.append(1 if F[x] > 0 else 0 )
    return ans