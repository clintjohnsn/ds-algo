# Given an array of size n-1 and given that there are numbers from
 # 1 to n with one missing, the missing number is to be found.
 # buckets
T = int(input())
for _ in range(T):
    n = int(input())
    ar = [int(x) for x in input().split()]
    aux = [0] * (n+1)
    for i in ar:
        aux[i] = 1
    for i in range(1,len(aux)):
        if aux[i] != 1:
            print(i)
            break
