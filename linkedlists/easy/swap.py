"""
Swap Kth node from beginning with Kth node from end in a Linked List

Input: 1 -> 2 -> 3 -> 4 -> 5, K = 2
Output: 1 -> 4 -> 3 -> 2 -> 5 
Explanation: The 2nd node from 1st is 2 and 
2nd node from last is 4, so swap them.

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # push at head like stack O(1)
    def push(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
        print()

    def size(self)->int:
        l = 0
        temp = self.head
        while temp:
            l +=1
            temp = temp.next
        return l

    def swap(self,k):
        n = self.size()
        temp = self.head
        c = 0
        ptr1,ptr2,pptr1,pptr2 = None, None,None, None
        while temp:
            c +=1
            if c == k-1:
                pptr1 = temp
            if c == k:
                ptr1 = temp
            if c == n-k:
                pptr2 = temp
            if c == n-k+1:
                ptr2 = temp
            temp = temp.next
        temp = ptr1.next
        ptr1.next = ptr2.next
        ptr2.next = temp
        pptr1.next = ptr2
        pptr2.next = ptr1


ll = LinkedList()
for i in range(5,0,-1):
    ll.push(i)
k = 2
ll.print_list()
ll.swap(k)
ll.print_list()