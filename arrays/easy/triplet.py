# Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.
arr = [3, 1, 4, 6, 5]

# T - O(n2), S -O(n)
def triplet(arr):
    mem = set()
    for el in arr:
        mem.add(el**2)
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if (arr[i]**2 + arr[j]**2 ) in mem:
                return [arr[i]**2, arr[j]**2, arr[i]**2 + arr[j]**2]
    return []

print(triplet(arr))

# O(n2), S- O(n)
# 1. sort
# 2. fix c = len -1, look up a & b in O(n) meet in the middle manner
# 3. decrement c, look up till before c


# if max(arr) < n
# T - O(max^2)
# S - O(max)

# import math
 
# def checkTriplet(arr, n):
#     maximum = 0
 
#     # Find the maximum element
#     maximum = max(arr)
 
#         # Hashing array
#     hash = [0]*(maximum+1)
 
#     # Increase the count of array elements
#     # in hash table
#     for i in range(n):
#         hash[arr[i]] += 1
 
#         # Iterate for all possible a
#     for i in range(1, maximum+1):
#         # If a is not there
#         if (hash[i] == 0):
#             continue
 
#         # Iterate for all possible b
#         for j in range(1, maximum+1):
#             # If a and b are same and there is only one a
#             # or if there is no b in original array
#             if ((i == j and hash[i] == 1) or hash[j] == 0):
#                 continue
 
#             # Find c
#             val = int(math.sqrt(i * i + j * j))
 
#             # If c^2 is not a perfect square
#             if ((val * val) != (i * i + j * j)):
#                 continue
 
#             # If c exceeds the maximum value
#             if (val > maximum):
#                 continue
 
#             # If there exists c in the original array,
#             # we have the triplet
#             if (hash[val]):
#                 return True
#     return False
 
