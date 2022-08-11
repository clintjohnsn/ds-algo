# Add two numbers represented by linked lists
# List1: 5->6->3 // represents number 563 
# List2: 8->4->2 // represents number 842 
# Output: 
# Resultant list: 1->4->0->5 // represents number 1405 

# Method 1
# Traverse the two linked lists in order to add preceding zeros in case a list is having lesser digits than the other one.
# Start from the head node of both lists and call a recursive function for the next nodes.
# Continue it till the end of the lists.
# Creates a node for current digits sum and returns the carry.
# can also use a stack

# Time Complexity: O(m + n), where m and n are numbers of nodes in first and second lists 
# Space Complexity: O(m + n) (for output)

# only two numbers = carry will just be 1

# Method 2
# reverse the two lists, add and carry over

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,node):
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
    
    def set_number(self,number):
        while(number):
            self.push(Node(number  % 10))
            number = number//10
        self.reverse()
    # reverse
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def add_using_reverse(self,x,y):
        x.reverse()
        y.reverse()
        xh = x.head
        yh = y.head
        carry = 0 
        while xh is not None and yh is not None:
            node = Node((xh.data + yh.data + carry) % 10)
            carry = (xh.data + yh.data + carry)//10
            self.push(node)
            xh = xh.next
            yh = yh.next
        while xh is not None:
            node = Node((xh.data + carry) % 10)
            carry = (xh.data + carry)//10
            self.push(node)
            xh = xh.next
        while yh is not None:
            node = Node((yh.data + carry) % 10)
            carry = (yh.data + carry)//10
            self.push(node)
            yh = yh.next
        if carry !=0:
            self.push(Node(carry))
        self.reverse()

x = 1238
y = 397
xl = LinkedList()
yl = LinkedList()
xl.set_number(x)
yl.set_number(y)
print("x: ")
xl.printlist()
print("y: ")
yl.printlist()
sum_list = LinkedList()
sum_list.add_using_reverse(xl,yl)
print("sum: ")
sum_list.printlist()
