import random
import sys
# A sorting algorithm is said to be stable if two objects with equal
# or same keys appear in the same order in sorted output as they appear in the input array to be sorted.

# TimSort is a sorting algorithm based on Insertion Sort and Merge Sort.
# A stable sorting algorithm works in O(n Log n) time
# Used in Java’s Arrays.sort() as well as Python’s sorted() and sort().
# First sort small pieces using Insertion Sort, then merges the pieces using merge of merge sort.
def timsort(ar):
    ar.sort()
    # ¯\_(ツ)_/¯


# every time in the loop, the largest element is swapped to the end of the list. 
# next time, the loop runs till before where we left the last element
# works without swapped being tracked, just slightly better if we track swapped information (early exit)
def bubblesort(ar):
    for i in range(len(a)):
        swapped = False
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1],a[j]
                swapped = True
        if not swapped:
            break
    #O(n2) -> worst case when array is reverse sorted
    # O(n) -> best case when array is sorted
    #stable sort

# recursive bubblesort
# void bubbleSort(int arr[], int n)
# {
#     // Base case
#     if (n == 1)
#         return;
#
#     // One pass of bubble sort. After
#     // this pass, the largest element
#     // is moved (or bubbled) to end.
#     for (int i=0; i<n-1; i++)
#         if (arr[i] > arr[i+1])
#             swap(arr[i], arr[i+1]);
#
#     // Largest element is fixed,
#     // recur for remaining array
#     bubbleSort(arr, n-1);


# select the smallest and put in the first slot, start from second slot next time, and so on.
# very similar to bubble, except there is no swapping at every comparison
def selectionsort(ar):
    for i in range(len(ar)-1):
        smal = i
        for j in range(i+1,len(ar)):
            if ar[j] < ar[smal]:
                smal = j
        if smal != i:
            a[i],a[smal] = a[smal],a[i]
    # never make more than n swaps. good when memory write is costly
    # O(n2)
    # not stable

# keep sorted and unsorted array
# insert every element from the unsorted array in its right place in the sorted array
def insertionsort(ar):
    for i in range(1,len(ar)):
        j = i - 1
        temp = ar[i]
        while j>=0 and ar[j] > temp:
            ar[j+1] = ar[j]
            j -=1
        if j != i-1:
            ar[j+1] = temp
    # stable sort
    # W: O(n2)  B- O(n)
    # no of elements small or array is almost sorted
    # Binary Insertion sort: reduce the number of comparisons, use binary search to
    #  find the proper location to insert the selected item at each iteration
    #  O(log i) (at ith iteration)
    #  still has a running worst case running time of O(n2) because of the series
    # of swaps required for each insertion - even if you find the right location to insert, you still have to shift
    # the rest of the elements


# QUICKSORT
# 1. bring pivot to appropriate postion such that left of pivot is lesser than and right of pivot is greater than the pivot
# 2. recursively call quicksort on left and right parts

# worst case O(n2)
# average case O(nLogn)

# not stable. However any sorting algorithm can be made stable by considering indexes as comparison parameter.

# As per the broad definition of in-place algorithm it qualifies as an in-place sorting algorithm as 
# it uses extra space only for storing recursive function calls but not for manipulating the input.

# Most practical implementations of Quick Sort use randomized version. 
# The randomized version has expected time complexity of O(nLogn).
#  The worst case is possible in randomized version also, but worst case doesn’t occur 
#  for a particular pattern (like sorted array) and randomized Quick Sort works well in practice.

# Quick Sort is also a cache friendly sorting algorithm as it has good locality of reference when used for arrays.

# Quick Sort is also tail recursive, therefore tail call optimizations is done.

def partition(ar,start,end):
    pivot = ar[end];
    i = start -1
    j = start
    for j in range(start,end):
        if (ar[j] < pivot):
            i+=1
            ar[i], ar[j] = ar[j], ar[i]
    i+=1
    ar[i], ar[end] = ar[end] ,ar[i]
    return i


def quicksort(ar,start=None,end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(ar) - 1
    if (start< end):
        pivot_index = partition(ar,start,end)
        quicksort(ar,start,pivot_index-1)
        quicksort(ar,pivot_index+1,end)


# merge two contiguos sorted sub arrays
# end of the array is non inclusive  
def merge(ar,start,mid,end):
    temp = []
    i = start
    j = mid
    while(i<mid and j<end):
        if ar[i] <= ar[j]:
            temp.append(ar[i])
            i+=1
        else:
            temp.append(ar[j])
            j+=1
    while(i<mid):
        temp.append(ar[i])
        i+=1
    while(j<end):
        temp.append(ar[j])
        j+=1
    ar[start:end]= temp

def mergesort(ar,start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(ar)
    if start+1>=end:
        return
    else:
        mid = (end+start)//2
        mergesort(ar,start,mid)
        mergesort(ar,mid,end)
        merge(ar,start,mid,end)
        return ar


try:
    runfunc = sys.argv[1]
    n = int(sys.argv[2])
except:
    print("usage :python3 sorting.py <sort method> <no of elements>")
    print("sort methods :\n1.timsort \n2. bubblesort \n3.insertionsort \n4.selectionsort \n5.quicksort \6.mergesort")
    exit(0)

funclist = {"bubblesort":bubblesort, "timsort":timsort, "insertionsort":insertionsort,
 "selectionsort":selectionsort, "quicksort":quicksort,"mergesort":mergesort}

#main
a = list(range(n))
random.shuffle(a)
print(a)
funclist[runfunc](a)
print(a)

