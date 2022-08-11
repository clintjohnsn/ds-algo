# Given an array A your task is to tell at which position the equilibrium first occurs
# in the array. Equilibrium position in an array is a position such that
# the sum of elements below it is equal to the sum of elements after it.
# print the position at which the elements are at equilibrium if no equilibrium point exists print -1.

# def equi(ar):
#     for i,x in enumerate(ar):
#         if sum(ar[:i]) == sum(ar[i+1:]):
#             print(i+1)
#             break
#     else:
#         print(-1)

# T-O(N) S-O(1)
# def equi(ar):
#     s = sum(ar)
#     rs = 0
#     for i,x in enumerate(ar):
#         if s-rs-x==rs:
#             print(i)
#             break
#         rs+=x
#     else:
#         print(-1) 

# cumulative sum
# T-O(N), S-O(N)
def equi(ar):
    ls = [0] * len(ar)
    rs = [0] * len(ar)
    for i,x in enumerate(ar):
        ls[i] = ls[i-1] + x
    for i,x in enumerate(reversed(ar)):
        rs[i] = rs[i-1] + x
    rs.reverse()
    for i in range(len(ls)):
        if ls[i] == rs[i]:
            print(i)
            break;
    else:
        print(-1)


# T = int(input())
# for _ in range(T):
#     n = int(input())
#     ar = [int(x) for x in input().split()]
#     equi(ar)
    
a1 = [-7,1,5,2,-4,3,0]
a2 = [1,2,3]
equi(a1)
equi(a2)

# Input: A[] = {-7, 1, 5, 2, -4, 3, 0} 
# Output: 3 
# 3 is an equilibrium index, because: 
# A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

# Input: A[] = {1, 2, 3} 
# Output: -1 