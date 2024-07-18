# LeetCode: 75. Sort Colors
# https://leetcode.com/problems/sort-colors/

# Write a program to sort an array of 0's,1's and 2's in ascending order.
# bucket sort
T = int(input())
for _ in range(T):
    n = int(input())
    ar = [int(x) for x in input().split()]
    bucket = [0] * 3
    for i in ar:
        bucket[i] += 1
    for i,x in enumerate(bucket):
        for _ in range(x):
            print(i,end=" ")
    print()
