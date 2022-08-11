# Given an unsorted array of non-negative integers, find a continuous sub-array which adds to a given sum.
def subarray_sum(arr,s):
    rs = 0
    i,j = 0,0
    while rs!=s and j<len(arr):
        if rs > s:
            rs -= arr[i]
            i+=1
        if rs < s:
            rs += arr[j]
            j+=1
    if rs == s:
        return i,j-1
    else:
        return -1,-1


arr = [1,0,2,7,5,3,9,3,0,4]
print(subarray_sum(arr,15))