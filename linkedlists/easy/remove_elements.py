"""
leetcode 203
https://leetcode.com/problems/remove-linked-list-elements/

Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val, and return the new head.

"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        temp = head.next
        prev = head
        while temp:
            if temp.val == val:
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next
        return head

