# Leetcode: 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

 # finding the k smallest numbers/ k largest numbers in a list or array; kth number is called the kth order statistic
# https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/
 # METHOD 1: sort and get ar[k-1] element -> O(nlogn)

# METHOD 2: partial selection sort
# a partial selection sort yields a simple selection algorithm which takes O(kn) time.
# or just call and remove max(ar) k times -> ar should not have duplicates, also O(kn)

# METHOD 3: HEAPSELECT/ Priority queue
# Time complexity of this solution is O(n + kLogn).
# O(n) for building the heap, then k times getting the min value -> O(klogn)

ar = [1,42,5,7,3,8,84,32,76,37,83]
k = 5
# import heapq
# print(heapq.nsmallest(k,ar))
# print(heapq.nlargest(k,ar))

# variation
# use min heap to have min of the largest k or PriorityQueue<Integer> minHeap = new PriorityQueue<>();
# Min Heap MH of the first k elements (arr[0] to arr[k-1]) of the given array  O(k*log(k))
# For each element, after the kth element (arr[k] to arr[n-1]), compare it with root of MH.
# ) If the element is greater than the root then make it root and call heapify for MH 
# ……b) Else ignore it.  O((n-k)*log(k))
# getting k largest -> O(k*log(k))
# total = O(k*log(k) + (n-k)*log(k) + k*log(k)) =? O((n +k)*logk)

# k largest impl
# import heapq
# def heap(arr, size, k):
#     minHeap = []
#     for i in range(k):
#         minHeap.append(arr[i])
#     heapq.heapify(minHeap)
#     for i in range(k, size):
#         if minHeap[0] > arr[i]:
#             continue
#         else:
#             # pop head
#             heapq.heappop(minHeap)
#             heapq.heappush(minHeap,arr[i])
#     for i in range(k):
#         print(heapq.heappop(minHeap),end=' ')
# heap(ar,len(ar),k)
# for k smallest, can push negative of the numbers( -1 * arr[i])

# METHOD 4: QUICKSELECT

# Choose a pivot number.
# if K is lesser than the pivot_Index then repeat the step.
# if K == pivot_Index : Print the array (low to pivot to get K-smallest elements and (n-pivot_Index) to n for K-largest elements)
# if  K > pivot_Index : Repeat the steps for right part.
# The worst-case time complexity of this version is O(n2) and the average time complexity is O(n).

import random
def partition(ar,start,end):
    n = end - start + 1
    # Selecting the random pivot index
    pivotInd =  (int((random.random()*1000000))%n)
    pivot = ar[pivotInd];
    print(pivotInd,pivot)
    i = start -1
    j = start
    for j in range(start,end):
        if (ar[j] < pivot):
            i+=1
            ar[i], ar[j] = ar[j], ar[i]
    i+=1
    ar[i], ar[pivotInd] = ar[pivotInd] ,ar[i]
    return i

def quickselect(ar,k,i,j):
    pivot = partition(ar,i,j)
    print(ar,k,i,j,pivot)
    if pivot == k-1:
        return ar[:k]
    if pivot > k-1:
        return quickselect(ar,k,i,j)
    else:
        return quickselect(ar,k,pivot+1,j)

print(quickselect(ar,k,0,len(ar)-1)[:k])


# Method 5(Creating a BST and Getting K greatest Elements):
# In this approach, we will create a Binary Search Tree and then we will print K greatest elements of it.
# TODO: BST