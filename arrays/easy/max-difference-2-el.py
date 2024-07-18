# Leetcode 2016 

# https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/
# find Maximum difference between two elements such that larger element appears after the smaller number

def maxDiff(arr, arr_size):
    max_diff = arr[1] - arr[0]
    min_element = arr[0]

    for i in range( 1, arr_size ):
        if (arr[i] - min_element > max_diff):
            max_diff = arr[i] - min_element

        if (arr[i] < min_element):
            min_element = arr[i]
    return max_diff

# Time Complexity : O(n)
# Auxiliary Space : O(1)
