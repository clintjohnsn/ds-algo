# given matrix of n*m, 
# add an integer d to a square submatrix of size s 
# starting at row r and column c 

n,m,k = [int(x) for x in input().split()] # input n,m, and k values 
a = []
for _ in range(n): # construct n*m matrix
    a.append([int(x) for x in input().split()])

for _ in range(k):
    r,c,s,d = [int(x) for x in input().split()]
    r -= 1
    c -= 1
    for i in range(r,r + s):
        for j in range(c,c + s):
            a[i][j] += d

for i in range(n):
    for j in range(m):
        print(a[i][j],end=" ")
    print()

# TODO : Submatrix sum DP problem
