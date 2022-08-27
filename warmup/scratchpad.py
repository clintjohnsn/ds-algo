class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import  Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode()
        temp = result
        while l1 and l2:
            carry, l1, l2, temp = self.sum(carry, l1, l2, temp)
        while l1 and carry > 0:
            carry, l1, l2, temp = self.sum(carry, l1, l2, temp)
        if l1:
            temp.next = l1
            temp = temp.next
        while l2 and carry > 0:
            carry, l1, l2, temp = self.sum(carry, l1, l2, temp)
        if l2:
            temp.next = l2
            temp = temp.next
        if carry > 0:
            temp.next = ListNode(carry)
        result = result.next
        return result


    def sum(self, carry:int, l1: Optional[ListNode], l2:Optional[list], temp:ListNode):
        l1_val, l2_val = 0,0
        if l1:
            l1_val = l1.val
        if l2:
            l2_val = l2.val
        s = l1_val + l2_val + carry
        digit = s % 10
        carry = s // 10
        temp.next = ListNode(digit)
        temp = temp.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        return carry, l1, l2, temp


l1 = [2,4,3]
l2 = [5,6,4]