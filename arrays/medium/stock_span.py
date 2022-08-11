# https://www.geeksforgeeks.org/the-stock-span-problem/
# The stock span problem is a financial problem where we have a series of n daily price quotes 
# for a stock and we need to calculate the span of the stock’s price for all n days.
#  The span Si of the stock’s price on a given day i is defined as the maximum number of
#  consecutive days just before the given day, for which the price of the stock on the current day 
#  is less than its price on the given day. 

#  Input: N = 7, price[] = [100 80 60 70 60 75 85]
# Output: 1 1 1 2 1 4 6
# Explanation: Traversing the given input span for 100 will be 1, 80 is smaller than 100 so the span is 1, 60 is smaller than 80 so the span is 1, 70 is greater than 60 so the span is 2 and so on. Hence the output will be 1 1 1 2 1 4 6.

# Method , using stack, T- O(n), S= O(n)
# We see that S[i] on the day i can be easily computed if we know the closest day preceding i, 
# such that the price is greater than on that day than the price on the day i. let’s call it h(i)
# The span is now computed as S[i] = i – h(i)
# we use a stack as an abstract data type to store the days i, h(i), h(h(i)) (positions of the days) 
# we need the positions of the h(i)
# for i, if i < previous height, S[i] = 1, else we need the height that stopped the prev height, 
# as values less than prev height will not stop i 

# Time Complexity: O(n). It seems more than O(n) at first look. If we take a closer look, we can observe that every element of the array is added and removed from the stack at most once. So there are total 2n operations at most. Assuming that a stack operation takes O(1) time, we can say that the time complexity is O(n).
# Auxiliary Space: O(n) in the worst case when all elements are sorted in decreasing order.

# using simple python list as stack, but with a top value so that push pop operations are T = O(1)
def stock_span(ar,size):
    # init
    span = [None] * size
    stack = [None]* size
    # first value
    top = 0 # 1 element in stack
    stack[top] = 0 # position of first value 
    span[0] = 1
    for i in range(1,size):
        while top >=0 and ar[i] > ar[stack[top]]:
            top-=1
        if top == -1: # empty stack
            span[i] = i + 1
        else:
            span[i] = i - stack[top]
        top+=1
        stack[top] = i
    return span

# driver
ar1 =  [100, 80, 60, 70, 60, 75, 85] # 1 1 1 2 2 4 6
ar2 = [10, 4, 5, 90, 120, 80] # 1 1 2 4 5 1 
print(stock_span(ar1,len(ar1)))
print(stock_span(ar2,len(ar2)))
