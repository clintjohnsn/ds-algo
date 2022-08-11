# Maximum of all subarrays of size k
# Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.
# Sliding Window Maximum - print max vals for every window of size k

# METHOD 1
# T = int(input())
# for _ in range(T):
#     n,k = [int(x) for x in input().split()]
#     ar = [int(x) for x in input().split()]
#     for i in range(0,len(ar)-k+1):
#         print(max(ar[i:i+k]),end=" ")
#     print()
# O(nk)

# METHOD 2
#  can be done in O(n) time and O(k) space using deque
T = int(input())
for _ in range(T):
    n,k = [int(x) for x in input().split()]
    ar = [int(x) for x in input().split()]
    ans = []
    aux = []
    # put first k elements in the aux array
    # idea is to only care about the biggest fish in the pond
    # any numbers coming before the largest number in the window is useless
    for i in range(k):
        while aux and ar[i] >= ar[aux[-1]]:
            aux.pop()
        aux.append(i)
    ans.append(ar[aux[0]])

    #for the rest of the elements from k to n
    for i in range(k,n):
        #move the Window
        # determine if aux[0] is out of window
        if i - k + 1> aux[0]:
            aux = aux[1:]
        #put in the elements
        while aux and ar[i] >= ar[aux[-1]]:
            aux.pop()
        aux.append(i)
        ans.append(ar[aux[0]])
    for i in ans:
        print(i,end=" ")
    print()

# Q) Sum of minimum and maximum elements of all subarrays of size k:
# maintain another aux (dequeue?) array with minimums
