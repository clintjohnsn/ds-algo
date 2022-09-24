"""
Leetcode 227

Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid.
 All intermediate results will be in the range of [-2^31, 2^31 - 1].

All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].
The answer is guaranteed to fit in a 32-bit integer.

"""


class Solution:
    def evaluate(self, a:int, op:str, b:int ) -> int:
        if op == "-":
            return a-b
        elif op == "+":
            return a+b
        elif op == "/":
            return a//b
        elif op == "*":
            return a * b
        else:
            raise Exception("operation not supported")

    def calculate(self, s: str) -> int:
        ops = dict()
        ops["-"] = 1
        ops["+"] = 1
        ops["/"] = 2
        ops["*"] = 2
        inp = list()
        n = list()
        slist = [c for c in s if c != " "]
        for c in slist:
            if c not in ops:
                n.append(c)
            else:
                inp.append("".join(n))
                inp.append(c)
                n.clear()
        if n:
            inp.append("".join(n))
        inp.reverse()
        stack = list()
        op_stack = list()
        for i in inp:
            if i not in ops:
                stack.append(int(i))
            else:
                while op_stack and ops[i] < ops[op_stack[-1]]:
                    val = self.evaluate(stack.pop(), op_stack.pop(), stack.pop())
                    stack.append(val)
                op_stack.append(i)
        while op_stack:
            val = self.evaluate(stack.pop(),op_stack.pop(),stack.pop())
            stack.append(val)
        return stack.pop()


# Test
print(Solution().calculate("3+2*2")) #7
print(Solution().calculate("3 / 2")) # 1
print(Solution().calculate("3 + 5 / 2")) # 5