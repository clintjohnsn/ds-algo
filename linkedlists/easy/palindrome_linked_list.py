
from typing import Optional
"""
Leetcode 234
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.



"""
"""
can use a stack
 or get a reversed list and compare
 or convert into doubly linked list and iterate from both ends
 time - O(n)
 space - O(n)
"""

"""
O(n) time and O(1) space
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def print(self, head: Optional[ListNode]):
        temp = head
        while temp:
            print(temp.val, end=' ')
            temp = temp.next

    def is_equal(self, l1head: ListNode, l2head: ListNode) -> bool:
        temp1 = l1head
        temp2 = l2head
        while temp1 and temp2:
            if temp1.val != temp2.val:
                return False
            temp1 = temp1.next
            temp2 = temp2.next
        return temp1 == temp2

    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        temp = head
        prev = None
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
            if prev and temp and prev.val == temp.val and self.is_equal(prev, temp):
                return True
            if prev and temp and temp.next and prev.val == temp.next.val and self.is_equal(prev, temp.next):
                return True
        return False


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
print(Solution().is_palindrome(head))

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
print(Solution().is_palindrome(head))

"""
improved above method, 
since palindrome will be exactly split in half, 
don't need to check at every repetition, instead,
find the middle and reverse 

finding the middle => either find the length and divide by two O(n)
or two pointer (fast and slow) technique
fast is twice the speed of slow

"""


class Solution:

    def is_palindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
