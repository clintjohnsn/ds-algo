#EASY
n,m,k = [int(x) for x in input().split()]
a = []
for _ in range(n):
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

