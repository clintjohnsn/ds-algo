# Given a linked list, write a function to reverse every k nodes 
# Input: 1->2->3->4->5->6->7->8->NULL, K = 3 
# Output: 3->2->1->6->5->4->8->7->NULL 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,node):
        # O(n), alternatively append on the head like a stack
        if self.head == None:
            self.head = node
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = node
    
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
        print()

    def reverse(self,node,k):
        count = 0
        prev = None
        while node is not None and count<k:
            next = node.next
            node.next = prev
            prev = node
            node = next
            count+=1
        # new head
        return prev

    # stack based
    # TODO use better stack and push operations, T = O(N) S = O(N + K)
    def group_reverse_stack(self,k):
        stack = []
        reversed = LinkedList()
        count = 0
        curr = self.head
        while curr is not None:
            stack.append(curr) # T=O(n); use real stack instead for O(1)
            count +=1
            if count == k:
                while count > 0:
                    node = stack.pop()
                    reversed.push(Node(node.data))
                    count -=1
            curr = curr.next
        while count > 0:
            node = stack.pop()
            reversed.push(Node(node.data))
            count -=1
        return reversed


# driver
k  = 3
ll = LinkedList()
for i in range(11):
    ll.push(Node(i))
print("list")
ll.printlist()
reversed = ll.group_reverse_stack(k)
print("group reversed,k ={}".format(k))
reversed.printlist()