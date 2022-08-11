# largest sum contiguous subarray
# Given an array containing both negative and positive integers. Find the contiguous sub-array with maximum sum.

T = int(input())
for _ in range(T):
    summ = 0
    n = int(input())
    ar = [int(x) for x in input().split()]
    gmax =0
    maxtillhere=0
    for i in ar:
        # if zero element subarray allowed, all negative numbers should have ans = 0
        maxtillhere += i;
        if maxtillhere < 0:
            maxtillhere = 0
        else:
            gmax = max(maxtillhere,gmax)
    print(gmax)


# if all negative, zero element subarray now allowed, ans = max(arr)
# T = int(input())
# for _ in range(T):
#     summ = 0
#     n = int(input())
#     ar = [int(x) for x in input().split()]
#     gmax =0
#     maxtillhere=0
#     flag = False
#     for i in ar:
#         maxtillhere += i;
#         if maxtillhere < 0:
#             maxtillhere = 0
#         else:
#             flag = True
#             gmax = max(maxtillhere,gmax)
#     if flag:
#         print(gmax)
#     else:
#         print(max(ar))


# another method of solving all negative problem
# T = int(input())
# for _ in range(T):
#     summ = 0
#     n = int(input())
#     ar = [int(x) for x in input().split()]
#     gmax = ar[0]
#     maxtillhere= ar[0]
#     for i in ar[1:]:
#         maxtillhere = max(i,maxtillhere + i)
#         gmax = max(maxtillhere, gmax)
#     print(gmax)
