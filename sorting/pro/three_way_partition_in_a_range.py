"""
Leetcode 75. Sort Colors
https://leetcode.com/problems/sort-colors/

"""

arr = [2,3,4,1,19,24,23,12,15,13,14]
range_low = 10
range_high = 15

def three_way_partition(arr,low,high):
    start=0
    end = len(arr) -1
    i= 0
    while(i<len(arr) and i<=end):
        if arr[i]<low:
            arr[i],arr[start] = arr[start] ,arr[i]
            start+=1
            i+=1
        elif arr[i] >high:
            arr[i],arr[end] = arr[end], arr[i]
            end-=1
        else:
            i+=1
        print(arr)

three_way_partition(arr,range_low,range_high)
print(arr)
