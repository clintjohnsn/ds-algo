# Leetcode: 541. Reverse String II
# https://leetcode.com/problems/reverse-string-ii/

# Given an array, reverse every sub-array formed by consecutive k elements.
# T = int(input())
# for _ in range(T):
#     n= int(input())
#     ar = [int(x) for x in input().split()]
#     k = int(input())
#     aux = []
#     res = []
#     for i,x in enumerate(ar):
#         aux.append(x)
#         if len(aux) == k:
#             aux.reverse()
#             res+=aux
#             aux = []
#     if len(aux) > 0:
#         aux.reverse()
#         res+=aux
#     for i in res:
#         print(i,end=" ")
#     print()

 # this must be atleast ~O(nk) time complexity
 # and ~O(n) space complexity

 #can do better with O(n) time and O(1) space complexity

T = int(input())
for _ in range(T):
    n= int(input())
    ar = [int(x) for x in input().split()]
    k = int(input())
    i  = 0
    for i in range(0,n,k):
        left = i
        right = min(i + k -1,len(ar) -1)
        while(left<right):
            ar[left] ,ar[right] = ar[right],ar[left]
            left +=1
            right -=1
    print(ar)
