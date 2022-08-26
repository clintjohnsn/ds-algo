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


def maxSubArray(self, nums: list[int]) -> int:
    s= float("-inf")
    maxsum = float("-inf")
    for i in range(len(nums)):
        s = max(nums[i],s+ nums[i])
        maxsum = max(maxsum,s)
    return maxsum

