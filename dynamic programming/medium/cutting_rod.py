"""

Given a rod of length n inches and an array of prices that includes prices 
of all pieces of size smaller than n. Determine the maximum value obtainable
 by cutting up the rod and selling the pieces.
  For example, if the length of the rod is 8 and the values of different pieces 
  are given as the following, then the maximum obtainable value is 22 
  (by cutting in two pieces of lengths 2 and 6) 

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

ans: 2 pieces 2,6 => 22

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 3   5   8   9  10  17  17  20

ans:  8 pieces of 1 => 24
"""
from collections import defaultdict


counter = [0] # count no of invocations
ar1 = [1, 5, 8, 9, 10, 17, 17, 20]
ar2 = [3, 5, 8, 9, 10, 17, 17, 20]

def cut(n:int,price:list[int])->int:
  counter[0] +=1
  if n == 0:
    return 0
  val = price[n-1]
  for i in range(1,n):
    val = max(val,cut(i,price) + cut(n-i,price))
  return val

counter[0] = 0
print(cut(len(ar1),ar1))
print("no of invocations", counter[0])
counter[0] = 0
print(cut(len(ar2),ar2))
print("no of invocations", counter[0])

"""
memoization

"""
print("memoized: ")

def cut(n:int, price: list[int], dp: list[int])->int:
  counter[0] +=1
  if n == 0:
    return 0
  if dp[n]:
    return dp[n]
  val = price[n-1]
  for i in range(1,n):
    val = max(val,cut(i,price,dp) + cut(n-i,price,dp))
  dp[n] = val
  return val

def memoized_cut(price: list[int]) -> int:
  n = len(price)
  dp = [None] * (n+1)
  return cut(n,price,dp)

counter[0] = 0
print(memoized_cut(ar1))
print("no of invocations", counter[0])
counter[0] = 0
print(memoized_cut(ar2))
print("no of invocations", counter[0])

"""
# TODO
Other methods
- bottom up
- knapsack based

https://www.geeksforgeeks.org/cutting-a-rod-dp-13/?ref=lbp
"""