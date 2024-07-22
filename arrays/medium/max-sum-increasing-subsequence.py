# Leetcode: 300
# Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
# Given an array of n positive integers. Write a program to find the sum of maximum sum subsequence of the given array
# such that the integers in the subsequence are sorted in increasing order.

# TODO: this


def increasing_subseq(arr):
    s = arr[0]
    gs = s
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
                s= arr[i]
        else:
            s+=arr[i]
        gs = max(gs,s)
    return gs

a = [1,2,3,4,3,5,6,3,1,9,3]

print(increasing_subseq(a))