"""


Given an array arr[] of n integers, find the rotation that maximizes the sum of the value of i*arr[i] where i varies from 0 to n-1.

Input: arr[] = {8, 3, 1, 2}
Output: 29
Explanation: Lets look at all the rotations,
{8, 3, 1, 2} = 8*0 + 3*1 + 1*2 + 2*3 = 11
{3, 1, 2, 8} = 3*0 + 1*1 + 2*2 + 8*3 = 29
{1, 2, 8, 3} = 1*0 + 2*1 + 8*2 + 3*3 = 27
{2, 8, 3, 1} = 2*0 + 8*1 + 3*2 + 1*3 = 17

print the sum

rotation takes O(n), calculating sum takes O(n), n rotations exist
naive - T O(n^2)

if array is a rotated sorted  array, then the best sum is for rotation = 0

# method 1
from the first sum, get the next sum
0*a[0] + 1a[1] + 2a[2] + 3a[3]... (n-1)a[n-1]                           = s1
         0a[1] + 1a[2] + 2a[3] ...(n-2)a[n-1] + (n-1)a[0]               = s2
                 0a[2] + 1a[3] .. (n-3)a[n-1] + (n-2)a[0] + (n-1)a[1]   = s3

s1 - s2 = a[1] + a[2] + a[3] ...a[n-1] - (n-1)a[0]
s2 = s1 - (a[1] + a[2] .. a[n-1]) + (n-1)a[0])
29 = 11 - (3 + 1 + 2) + 3*8 = 11 -6 + 24

s2-s3 = a[2] + a[3]... a[n-1] + a[0] + (n-1)a[1] =(a[0] + a[2] + a[3].. a[n-1]) + (n-1)a[1]
s3 = s2 - (a[0] + a[2] + a[3]...) + (n-1)a[1]
27 = 29 - (8 + 1 + 2) + 3*3 = 29 - 11 + 9

s4 = 17 = 27 - (8+3+2) + 3 *1 = 27 - 13 + 3

T = O(N), S = O(1)

"""
from typing import List
def msr(ar:List[int])->int:
    s:int = sum(ar)
    n:int = len(ar)
    maxsum:int = 0
    for i in range(n):
        maxsum+=i*ar[i]
    for i in range(n):
        k:int = s - ar[i]
        maxsum = max(maxsum,maxsum-k+(n-1)*ar[i])
    return maxsum

ar1 = [8, 3, 1, 2]
ar2 = [ 3, 2, 1]
print(msr(ar1))
print(msr(ar2))


