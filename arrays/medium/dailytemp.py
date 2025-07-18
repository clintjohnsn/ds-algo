"""
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait 
after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

"""

# using monotonic stack
# Time Complexity: O(n). It seems more than O(n) at first look. If we take a closer look, 
# we can observe that every element of the array is added and removed from the stack at most once. 
# So there are total 2n operations at most. Assuming that a stack operation takes O(1) time,
#  we can say that the time complexity is O(n).
# Auxiliary Space: O(n) in the worst case when all elements are sorted in decreasing order.
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stk, out = [], []
        for i in range(len(temperatures)-1,-1,-1):
            while(stk and temperatures[stk[-1]]<= temperatures[i]):
                stk.pop()
            out.append(stk[-1] - i if stk else 0)
            stk.append(i)
        out.reverse()
        return out
