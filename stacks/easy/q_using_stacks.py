"""
Leetcode 232

Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

You must use only standard operations of a stack,
which means only push to top, peek/pop from top, size, and is empty operations are valid.

"""
"""
Approach #1 
whenever pushing, empty stack 1 into stack 2, push the element into stack 1, and empty stack 2 to stack 1

Push - O(n) per operation
Pop/Peek/Empty - O(1) per operation.


"""

"""
Approach 2
each operation is amortized O(1) time complexity
In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
Amortized analysis gives the average performance (over time) of each operation in the worst case.
The basic idea is that a worst case operation can alter the state in such a way that
 the worst case cannot occur again for a long time, thus amortizing its cost.

"""
class MyQueue:

    def __init__(self):
        self.read_stack = list()
        self.push_stack = list()

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        if self.read_stack:
            return self.read_stack.pop()
        while self.push_stack:
            self.read_stack.append(self.push_stack.pop())
        if self.read_stack:
            return self.read_stack.pop()
        else:
            raise Exception("empty")


    def peek(self) -> int:
        if self.read_stack:
            return self.read_stack[-1]
        while self.push_stack:
            self.read_stack.append(self.push_stack.pop())
        if self.read_stack:
            return self.read_stack[-1]
        else:
            raise Exception("empty")

    def empty(self) -> bool:
        return not self.read_stack and not self.push_stack
