"""
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
 In other words, given two integer arrays val[0..n-1] and wt[0..n-1] 
 which represent values and weights associated with n items respectively.
  Also given an integer W which represents knapsack capacity, 
  find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.
 You cannot break an item, either pick the complete item or don’t pick it (0-1 property).
 return the max value

basic recursive solution

Time Complexity: O(2n). 
As there are redundant subproblems.
Auxiliary Space :O(N) (recursive stack) 

"""
# ans = 100 + 120 = 220
val1 = [60, 100, 120]
wt1 = [10, 20, 30]
W1 = 50 

# ans = 60 + 180 = 240
val2 = [60, 120, 180]
wt2 = [10, 20, 30]
W2 = 40

val = [20,30,50,10,30,40,10,40,20,50,30,20,40,10,20,50]
wt =  [10,20,40,20,30,10,30,10,20,30,10,20,30,10,20,30]
W = 200

# counter to see the number of invocations
c = [0,0,0]

def K(n,W,val,wt,counter):
  c[counter]+=1
  if W <= 0 or n < 0:
    return 0
  if W - wt[n] <0 :
    return K(n-1,W,val,wt,counter)
  return max(
    K(n-1,W,val,wt,counter),
    val[n] + K(n-1,W-wt[n],val,wt,counter))


def knapsack(val,wt,W,counter):
  n = len(val)
  ans = K(n-1,W,val,wt,counter)
  print(ans)

# driver
print("recursive knapsack:")
knapsack(val1,wt1,W1,0)
knapsack(val2,wt2,W2,1)
knapsack(val,wt,W,2)
print(c)
"""
with memoization
Time Complexity: O(N*W). 
As redundant calculations of states are avoided.
Auxiliary Space: O(N*W) + O(N). 
The use of 2D array data structure for storing intermediate states and O(N) auxiliary stack space(ASS) has been used for recursion stack:
"""

from collections import defaultdict
c = [0,0,0]

def K(n,W,val,wt,mem,counter):
  c[counter] +=1
  if W <= 0 or n < 0:
    return 0
  if mem[n][W]!=-1:
    return mem[n][W]
  if W - wt[n] < 0 :
    mem[n][W]= K(n-1,W,val,wt,mem,counter)
  else:
    mem[n][W] = max(K(n-1,W,val,wt,mem,counter),val[n] + K(n-1,W-wt[n],val,wt,mem,counter))  
  return mem[n][W]

def mem_knapsack(val,wt,W,counter):
  n = len(val)
  # dict {n: {w: -1}}
  mem = defaultdict(lambda:defaultdict(lambda:-1))
  # other option is to have a 2d array thats W*n (every possible weight 1-W X 1-n)
  ans = K(n-1,W,val,wt,mem,counter)
  print(ans)

print("memoized knapsack:")
mem_knapsack(val1,wt1,W1,0)
mem_knapsack(val2,wt2,W2,1)
mem_knapsack(val,wt,W,2)
print(c)

"""
TODO: bottom up approach
"""