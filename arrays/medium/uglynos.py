# Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
# The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11
# ugly numbers. By convention, 1 is included.
#
# Given a number n, the task is to find n’th Ugly number.

#METHOD 1: brute force
# def maxDivide( a, b ):
#     while a % b == 0:
#         a = a / b
#     return a
#
# def isUgly( no ):
#     no = maxDivide(no, 2)
#     no = maxDivide(no, 3)
#     no = maxDivide(no, 5)
#     return 1 if no == 1 else 0
#
# def getNthUglyNo( n ):
#     i = 1
#     count = 1 # ugly number count
#     while n > count:
#         i += 1
#         if isUgly(i):
#             count += 1
#     return i
#
# no = getNthUglyNo(150)
# print("150th ugly no. is ", no)
# ----------------------------------------------------------
# METHOD 2: DP - bottom up

# min of 3 sequence
# 1×2, 2×2, 3×2, 4×2, 5×2, 6x2, 8x2, 9x2, 10x2, 12x2 ...
# 1×3, 2×3, 3×3, 4×3, 5×3, 6x3, 8x3, 9x3, 10x3, 12x3 ...
# 1×5, 2×5, 3×5, 4×5, 5×5, 6x4, 8x4, 9x4, 10x4, 12x4 ...
# note: sequence itself is ugly no sequence not natural numbers
# create 3 factors, 3 index variables pointing to the ugly sequence, compare & get min of  3 sequence values to find which sequence progresses


# factors     2 3 5 
# index       0 0 0
# nextnos    [2 3 5]
# uglynos    [1]


n = int(input())
facs = [int(x) for x in input().split()]
k = len(facs) #k=3
indices = [0] * k
nextnos = [0] * k
uglynos = [1]

for i in range(1,n):
    nextnos = [uglynos[indices[x]] * facs[x] for x in range(k)]
    uglynos.append(min(nextnos))
    for i,x in enumerate(nextnos):
        if x == min(nextnos):
            indices[i] +=1

print(uglynos[-1])
#space = O(n)
# time = O(n) or O(nk) k =3
