# https://www.geeksforgeeks.org/maximum-sum-subsequence/
# Given an array arr[] of positive numbers, the task is to find the maximum sum of a subsequence 
# with the constraint that no 2 numbers in the sequence should be adjacent in the array.

# eg
# Input: arr[] = {5, 5, 10, 100, 10, 5}
# Output: 110
# Explanation: Pick the subsequence {5, 100, 5}
# input: arr[] = {3, 2, 7, 10}
# Output: 13
# Explanation: The subsequence is {3, 10}. This gives sum = 13.
# Input: arr[] = {3, 2, 5, 10, 7}
# Output: 15
# Explanation: Pick the subsequence {3, 5, 7}. The sum is 15.


# let S[ar(0,n-1)] be max sum subsequence function then
# S[ar(i,j)] = max(
#                   ar[i] + S[ar(i+2,j)], if we include ar[i]
#                   S[ar(i+1,j)], otherwise
#                  )

# ----------------------------

# basic recursive method
# def mss(ar,i,j):
#     print("ïnvoked")
#     if i == j:
#         return ar[i]
#     if i + 1 == j:
#         return max(ar[i],ar[j]) 
#     return max(ar[i] + mss(ar,i+2,j), mss(ar,i+1,j))

# driver
# a1 = [5, 5, 10, 100, 10, 5] # 110
# a2 = [3, 2, 7, 10] # 13
# a3 = [3, 2, 5, 10, 7] #15 
# print(mss(a1,0,len(a1)-1))
# print(mss(a2,0,len(a2)-1))
# print(mss(a3,0,len(a3)-1))

# ----------------------------

# memoization
# j is not changing
def mss_single_array(ar):
    n = len(ar)
    mem = [None] * n
    s = mss(ar,0,n,mem)
    # print(mem)
    return s  

def mss(ar,i,n,mem):
    if mem[i] is not None:
        return mem[i]
    if i == n-1:
        mem[i] = ar[i]
    elif i + 1 == n-1:
        mem[i] = max(ar[i],ar[i+1])
    else:
        mem[i]= max(ar[i] + mss(ar,i+2,n,mem), mss(ar,i+1,n,mem))
    return mem[i]

# driver
a1 = [5, 5, 10, 100, 10, 5] # 110 
a2 = [3, 2, 7, 10] # 13 
a3 = [3, 2, 5, 10, 7] #15  
print(mss_single_array(a1))
print(mss_single_array(a2))
print(mss_single_array(a3))

# ----------------------------
