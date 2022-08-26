"""
Leetcode 19
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []


Input: head = [1,2], n = 2
Output: [2]
"""

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        print(length)
        pos = length - n + 1
        i = 0
        temp = head
        prev = None
        while temp and i < pos - 1:
            i += 1
            prev = temp
            temp = temp.next
        if prev:
            prev.next = temp.next
        else:
            head = temp.next
        return head
