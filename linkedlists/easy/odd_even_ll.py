"""
Leetcode: 328. Odd Even Linked List
https://leetcode.com/problems/odd-even-linked-list/

Given the head of a singly linked list,
 group all the nodes with odd indices together followed by the nodes with even indices

 Note that the relative order inside both the even and odd groups should remain as it was in the input.

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

input: head = [1,2,3,4,5]
Output: [1,3,5,2,4
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def odd_even(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head
        # 3 or more elements
        odd = head
        even = head.next
        even_head = even
        while odd and even:
            odd.next = even.next
            odd = odd.next
            if odd:
                even.next = odd.next
                even = even.next
        odd = head
        while odd.next:
            odd = odd.next
        odd.next = even_head
        return head

    def print(self,head:ListNode) -> None:
        temp = head
        while temp:
            print(temp.val,end=' ')
            temp = temp.next

#Driver
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

Solution().odd_even(head)
Solution().print(head)