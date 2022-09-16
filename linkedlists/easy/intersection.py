"""
Leetcode 160
Given the heads of two singly linked-lists headA and headB,
return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

"""
from typing import  Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def get_intersection_node(self, head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
        if not head_a or not head_b:
            return head_a
        # find lengths
        len_a, len_b = 0,0
        temp = head_a
        while temp.next:
            len_a +=1
            temp = temp.next
        temp = head_b
        while temp.next:
            len_b += 1
            temp = temp.next
        ptr_a, ptr_b = head_a, head_b
        # traverse the longer one to until same length
        if len_a > len_b:
            k = len_a - len_b
            while ptr_a and k > 0:
                k -= 1
                ptr_a = ptr_a.next
        else:
            k = len_b - len_a
            while ptr_b and k > 0:
                k -= 1
                ptr_b = ptr_b.next
        # traverse remaining till meeting point
        while ptr_a and ptr_b:
            if ptr_a == ptr_b:
                return ptr_a
            else:
                ptr_a = ptr_a.next
                ptr_b = ptr_b.next
        return None