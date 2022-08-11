# Given an array, print the Next Greater Element (NGE) for every element. 
# The Next greater Element for an element x is the first greater element on the right side of x in the array.
#  Elements for which no greater element exist, consider the next greater element as -1. 

#  ar = [4, 5, 2, 25]
#  answer = [5,25,25,-1]

# method:
# similar to stock span 
# for i, if h(i) is the next greater element, maintain a stack i, h(i), h(h(i))
# start from reverse, maintain the greater element that stopped i 
# T:O(N) S:O(N)
def next_greater_element(ar):
    size = len(ar)
    stack = [ar[size-1]]
    ans = [-1] * size
    for i in range(size-2,-1,-1):
        while stack and ar[i] > stack[-1]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(ar[i])
    return ans

# driver
ar1 = [4, 5, 2, 25] # [5,25,25,-1]
ar2 =  [13, 7, 6, 12] # [-1,12,12,-1]
ar3 = [6,8,0,1,3] # [8, -1, 1, 3, -1]
ar4 = [11, 13, 21, 3] # [13,21,-1,-1]
print(next_greater_element(ar1))
print(next_greater_element(ar2))
print(next_greater_element(ar3))
print(next_greater_element(ar4))


