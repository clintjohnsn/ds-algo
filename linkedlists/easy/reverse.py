# reverse a linked list

# METHOD 1 using stack
# TODO: impl
# Store the nodes(values and address) in the stack until all the values are entered.
# Once all entries are done, Update the Head pointer to the last location(i.e the last value).
# Start popping the nodes(value and address) and store them in the same order until the stack is empty.
# Update the next pointer of last Node in the stack by NULL.
# Time Complexity: O(n) 
# Auxiliary Space: O(n)

# METHOD 2:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    # Time Complexity: O(n) 
    # Auxiliary Space: O(1)
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    # Time Complexity: O(n) 
    # Auxiliary Space: O(n)
    # not tail recursive
    def recursive_reverse(self, head):
        # empty, single, or end of list
        if head is None or head.next is None:
            return head
        # rest is the head of the reversed list
        rest = self.recursive_reverse(head.next)
        # head.next pointing to last el, make current head the last element
        head.next.next = head
        head.next = None
        # return the head of reversed list
        return rest

    def reverse_tail_recursive(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)

    def reverseUtil(self, curr, prev):
        # If last node mark it head
        if curr.next is None:
            self.head = curr
            # Update next to prev node
            curr.next = prev
            return
        # Save curr.next node for recursive call
        next = curr.next
        # And update next
        curr.next = prev
        self.reverseUtil(next, curr)
 
    # stack push T O(1)
    def stack_push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    # append list T O(n)
    def append(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' '),
            temp = temp.next
 
    

# Driver code
llist = LinkedList()
llist.append(20)
llist.append(4)
llist.append(15)
llist.append(85)
print("list:")
llist.printList()
llist.reverse()
print()
print("reversed:")
llist.printList()
print()
print("recursive reversed:")
llist.head = llist.recursive_reverse(llist.head)
llist.printList()
print()
print("tail recursive reversed:")
llist.reverse_tail_recursive()
llist.printList()