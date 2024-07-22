# LeetCode 155. Min Stack
# https://leetcode.com/problems/min-stack/

# Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull() and 
# an additional operation getMin() which should return minimum element from the SpecialStack. 
# All these operations of SpecialStack must be O(1).

# Consider the following SpecialStack
# 16  --> TOP
# 15
# 29
# 19
# 18

# When getMin() is called it should 
# return 15, which is the minimum 
# element in the current stack. 

# If we do pop two times on stack, 
# the stack becomes
# 29  --> TOP
# 19
# 18

# When getMin() is called, it should 
# return 18 which is the minimum in 
# the current stack.
# ------------------
# METHOD 1
#  Use two stacks: one to store actual stack elements and the other as an auxiliary stack to store minimum values.
# idea is that stacks will only pop in order, so can ignore larger elements and only keep smaller elements in the aux stack

# We can push only when the incoming element of the main stack is smaller than or equal to the top of the auxiliary stack. 
# Similarly during pop, if the pop-off element equal to the top of the auxiliary stack, remove the top element of the auxiliary stack.
# T = O(1), S = O(N)

# TODO: rewrite this

class stack:

  def __init__(self):
    self.array = []
    self.top = -1
    self.max = 100  

  def isEmpty(self):
    if self.top == -1:
      return True
    else:
      return False  
  
  def isFull(self):        
    if self.top == self.max - 1:
      return True
    else:
      return False   
  
  def push(self, data):
    if self.isFull():
      print('Stack OverFlow')
      return
    else:
      self.top += 1
      self.array.append(data)     

  def pop(self):  
    if self.isEmpty():
      print('Stack UnderFlow')
      return
    else: 
      self.top -= 1
      return self.array.pop()

class SpecialStack(stack):
  
  def __init__(self):
    super().__init__()
    self.Min = stack()  

  def push(self, x):
    if self.isEmpty():
      super().push(x)
      self.Min.push(x)
    else:
      super().push(x)
      # pop push is used to peek
      y = self.Min.pop()
      self.Min.push(y)
      if x <= y:
        self.Min.push(x)
      else:
        self.Min.push(y)  
  
  # SpecialStack's member method to  
  # remove an element from it. This 
  # method removes top element from 
  # min stack also. 
  def pop(self):
  
    x = super().pop()
    self.Min.pop()
    return x  
  
  # SpecialStack's member method 
  # to get minimum element from it.
  def getmin(self):
  
    x = self.Min.pop()
    self.Min.push(x)
    return x
  
# Driver code
# if __name__ == '__main__':
    
#   s = SpecialStack()
#   s.push(10)
#   s.push(20)
#   s.push(30)
#   print(s.getmin())
#   s.push(5)
#   print(s.getmin())

"""
simpler impl
"""


class MinStack:
    def __init__(self):
        self.stack = list()
        self.min = list()
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min:
            self.min.append(val)
        else:
            if val <= self.min[-1]:
                self.min.append(val)
    def pop(self) -> None:
        val = self.stack.pop()
        if self.min[-1] == val:
            self.min.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min[-1]


# --------------------------
# METHOD 2
# T - O(1) S- O(1)
# store element value as val * d + min; d = some random constant, min = min at the time of insertion
# value can be retrieved by element/d, min can be retrieved by element % d
# d should not be in the values

class SpecialStack2:

	def __init__(self):
		self.minm = -1
		SpecialStack.demoVal = 9999
		self.st = []

	def getMin(self):
		print("min is: ", self.minm)

	def push(self, val):
        #dont use len, T = O(n), store the top val instead
		if len(self.st) == 0 or val < self.minm:
			self.minm = val
		self.st.append(val*self.demoVal + self.minm)
		print("pushed: ", val)

	def pop(self):
		if len(self.st) == 0:
			print("stack underflow")
			return -1
		val = self.st.pop()
		if len(self.st) != 0:
			self.minm = val % self.demoVal
		else:
			self.minm = -1
		print("popped: ", val // self.demoVal)
		return val // self.demoVal

	def peek(self):
		return self.st[-1] // self.demoVal

# Driver Code
# if __name__ == "__main__":
# 	s = SpecialStack2()

# 	arr = [3, 2, 6, 1, 8, 5, 5, 5, 5]

# 	for i in range(len(arr)):
# 		s.push(arr[i])
# 		s.getMin()

# 	print("\n")
# 	for i in range(len(arr)):
# 		s.pop()
# 		s.getMin()
