"""
LeetCode 724

Given an array A your task is to tell at which position the equilibrium first occurs
in the array. Equilibrium position in an array is a position such that
the sum of elements below it is equal to the sum of elements after it.
print the position at which the elements are at equilibrium if no equilibrium point exists print -1.


The pivot index is the index where 
the sum of all the numbers strictly to the left of the index is equal to
the sum of all the numbers strictly to the index's right.


Input: A[] = {-7, 1, 5, 2, -4, 3, 0} 
Output: 3 
3 is an equilibrium index/pivot index, because: 
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

Input: A[] = {1, 2, 3} 
Output: -1


"""

"""
Brute force approach

check if left sum = right sum at every index

"""
def bruteforce(ar):
    for i,x in enumerate(ar):
        if sum(ar[:i]) == sum(ar[i+1:]):
            print(i+1)
            break
    else:
        print(-1)



"""
Make 2 cumulative sum arrays from left and right and reverse the right. 
The index where the cumulative sums is the required index
T-O(N) S-O(1) Solution

"""
def equi_best(ar):
    s = sum(ar) # 1st pass
    rs = 0 # running sum 
    for i,x in enumerate(ar): # 2nd pass
        if s-rs-x==rs:
            print(i)
            break
        rs+=x
    else:
        print(-1) 

# cumulative sum
# T-O(N), S-O(N) solution
def equi(ar):
    ls = [0] * len(ar) # left cumulative sums
    rs = [0] * len(ar) # right cumulative sums
    for i,x in enumerate(ar):
        ls[i] = ls[i-1] + x
    for i,x in enumerate(reversed(ar)):
        rs[i] = rs[i-1] + x
    rs.reverse()
    for i in range(len(ls)):
        if ls[i] == rs[i]:
            print(i)
            break;
    else:
        print(-1)


    
a1 = [-7,1,5,2,-4,3,0]
a2 = [1,2,3]
equi(a1)
equi(a2)

 