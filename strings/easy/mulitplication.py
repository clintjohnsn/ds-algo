"""

Leetcode 43
https://leetcode.com/problems/multiply-strings/

Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

use only single digit addition/multiplication (simulate multiplication)
similar to linkedlists/easy/addition.py

Input: num1 = "123", num2 = "456"
Output: "56088"

            4 5 6
x           1 2 3
--------------
      1     3   6   8
      9     1   2   0
4     5     6   0   0
------------------------
5     6     0   8   8

"""
from collections import  deque
class Solution:
    def sum(self,sumlist:list[int],numlist:list[int]):
        if not sumlist or len(sumlist) < len(numlist):
            for _ in range(len(numlist)-len(sumlist)):
                sumlist.append(0)
        carry = 0
        for i in range(len(sumlist)):
            s = sumlist[i] + numlist[i] + carry
            sumlist[i] = s % 10
            carry = s // 10
        if carry !=0:
            sumlist.append(carry)
        return sumlist

    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            return self.multiply(num2,num1)
        n1 = [ord(c) - ord("0") for c in num1]
        n2 = [ord(c) - ord("0") for c in num2]
        n1.reverse()
        n2.reverse()
        temp1 = deque()
        sumlist = deque()
        for i in range(len(n1)):
            temp1.clear()
            carry = 0
            for j in range(len(n2)):
                temp1.append((n1[i]*n2[j] + carry) % 10)
                carry = (n1[i] * n2[j] + carry) // 10
            if carry != 0:
                temp1.append(carry)
            for _ in range(i):
                temp1.appendleft(0)
            self.sum(sumlist,temp1)
        sumlist.reverse()
        while sumlist and sumlist[0] == 0:
            sumlist.popleft()
        if not sumlist:
            return "0"
        return "".join([str(i) for i in sumlist])

print(Solution().multiply("123","456"))
print(Solution().multiply("123","0"))