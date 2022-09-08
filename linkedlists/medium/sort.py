"""
Sort a linked list


Input: [-1,5,3,4,0]
Output: [-1,0,3,4,5]

target:
T = O(n logn)
S = O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def print(self, head: ListNode) -> None:
        temp = head
        while temp:
            print(temp.val, end=' ')
            temp = temp.next

    def find_pivot(self, head:ListNode, last: ListNode):
        """
        find pivot and new last element
        :param head: begin
        :param last: end (non inclusive)
        :return: pivot,last nodes
        """
        # take last element as pivot
        if head is None or head.next is None or head == last or head.next == last:
            return head,head
        temp = head
        while temp and temp.next and temp !=last and temp.next != last:
            temp = temp.next
        pivot = temp
        # pivot the list
        temp = head
        prev = None
        while temp and temp.next != pivot:
            if temp.val < pivot.val and prev:
                prev.next = temp.next
                temp.next = head
                head = temp
                temp = prev.next
                if temp.next == pivot:
                    break
            else:
                prev = temp
                temp = temp.next
        # here, temp.next == pivot
        last = temp.next = pivot.next
        # place the pivot
        temp = head
        prev = None
        while temp and temp.val < pivot.val:
            prev = temp
            temp = temp.next
        if prev:
            prev.next = pivot
        else:
            head = pivot
        pivot.next = temp
        return pivot, last

    def quicksort(self,head:ListNode,last:ListNode):
        """
        quicksort linked list implementation
        :param head: (head from which to begin)
        :param last: non inclusive
        :return: None (inplace sorting)
        """
        # length 0 or 1
        if head is None or head.next is None:
            return
        # find pivot and last element (non inclusive)
        pivot,last = self.find_pivot(head,last)
        # divide and conquer
        if pivot and head != pivot != last:
            self.quicksort(head,pivot)
            self.quicksort(pivot.next,last)

    def sort(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # in place sorting
        self.quicksort(head,None)
        return head



# Driver
test = ListNode(-1)
test.next = ListNode(5)
test.next.next = ListNode(3)
test.next.next.next = ListNode(4)
test.next.next.next.next = ListNode(0)

s = Solution()
test = s.sort(test)
s.print(test)
