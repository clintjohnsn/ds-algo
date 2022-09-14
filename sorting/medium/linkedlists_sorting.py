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


"""
QUICKSORT

But the worst-case time complexity is O(n^2)
variations of the quick sort like randomized quicksort are not efficient for the linked list because unlike arrays,
 random access in the linked list is not possible in O(1) time. 
 can use head or last for O(1) time, but not efficient - incase of already sorted lists
"""

class Solution:
    def print(self, head: ListNode) -> None:
        temp = head
        while temp:
            print(temp.val, end=' ')
            temp = temp.next

    def find_pivot(self, head:ListNode, last: ListNode):
        """
        pick a pivot and rearrange so that elements before pivot < pivot and after > pivot
        :param head: begin
        :param last: end (inclusive)
        :return: before pivot node
        """
        pivot = head
        temp = head
        before_pivot = None
        while temp and temp != last:
            if temp.val > last.val:
                temp = temp.next
            else:
                pivot.val, temp.val = temp.val, pivot.val
                before_pivot = pivot
                pivot = pivot.next
                temp = temp.next
        pivot.val, last.val = last.val, pivot.val
        return before_pivot,pivot


    def quicksort(self,head:ListNode,last:ListNode):
        """
        quicksort linked list implementation
        :param head: (head from which to begin)
        :param last: (inclusive)
        :return: None (inplace sorting)
        """
        if head is None or head.next is None or last is None or head == last:
            return
        before_pivot,pivot = self.find_pivot(head,last)
        self.quicksort(head, before_pivot)
        if pivot and pivot != last and pivot.next and pivot.next != last:
            self.quicksort(pivot.next, last)

    def sort(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # in place sorting
        if not head:
            return head
        temp = head
        while temp.next:
            temp = temp.next
        last = temp
        self.quicksort(head,last)
        return head



# Tests
test = ListNode(-1)
test.next = ListNode(5)
test.next.next = ListNode(3)
test.next.next.next = ListNode(4)
test.next.next.next.next = ListNode(0)

s = Solution()
test = s.sort(test)
s.print(test)

print()
test = ListNode(3)
test.next = ListNode(4)
test.next.next = ListNode(1)
s = Solution()
test = s.sort(test)
s.print(test)

print()
test = ListNode(1)
test.next = ListNode(2)
test.next.next = ListNode(3)
test.next.next.next = ListNode(4)

s = Solution()
test = s.sort(test)
s.print(test)
print()


"""
MERGE SORT

for linked lists merge sorts possible with O(1) space

"""


class Solution:
    def print(self, head: ListNode) -> None:
        temp = head
        while temp:
            print(temp.val, end=' ')
            temp = temp.next

    def merge(self, l1:ListNode, l2:ListNode) -> ListNode:
        dummy = ListNode()
        head = dummy
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1:
            head.next = l1
        elif l2:
            head.next = l2
        return dummy.next

    def sort(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        head = self.sort(head)
        mid = self.sort(mid)
        return self.merge(head,mid)





# Tests
print("--------------------------")

test = ListNode(-1)
test.next = ListNode(5)
test.next.next = ListNode(3)
test.next.next.next = ListNode(4)
test.next.next.next.next = ListNode(0)

s = Solution()
test = s.sort(test)
s.print(test)

print()
test = ListNode(3)
test.next = ListNode(4)
test.next.next = ListNode(1)
s = Solution()
test = s.sort(test)
s.print(test)

print()
test = ListNode(1)
test.next = ListNode(2)
test.next.next = ListNode(3)
test.next.next.next = ListNode(4)

s = Solution()
test = s.sort(test)
s.print(test)


