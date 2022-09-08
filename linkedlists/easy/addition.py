"""

Add two numbers represented by linked lists
List1: 5->6->3 // represents number 563 
List2: 8->4->2 // represents number 842 
Output: 
Resultant list: 1->4->0->5 // represents number 1405 

Method 1
- Traverse the two linked lists in order to add preceding zeros in case a list is having lesser digits than the other one.
- Start from the head node of both lists and call a recursive function for the next nodes.
- Continue it till the end of the lists.
- Creates a node for current digits sum and returns the carry.
- uses recursive stack memory
   
Method 1.1 can also use a stack
- loop through both, adding to stack
- pop from both stacks, add and push to result stack
    - maintain carry
    - when one stack is empty, loop through remaining elements in the other stack

Time Complexity: O(m + n), where m and n are numbers of nodes in first and second lists 
Space Complexity: O(m + n) (for output)

only two numbers = carry will just be 1

Method 2
reverse the two lists, add and carry over

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # append at end O(n)
    def append(self,node):
        if self.head == None:
            self.head = node
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = node

    # push at head like stack O(1)
    def push(self,node):
        if self.head == None:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
        print()
    
    def set_number(self,number):
        while(number):
            self.append(Node(number  % 10))
            number = number//10
        self.reverse()

    def length(self):
        l = 0
        temp = self.head
        while temp is not None:
            l+=1
            temp = temp.next
        return l

    # helper function to add zeros to the front
    def _add_zeros_(self,n):
        if n == 0:
            return
        while(n > 0 ):
            self.push(Node(0))
            n -=1         
    
    # recursive helper function used in add     
    def _add_helper_(self,xh,yh,result):
        if xh is None:
            return 0
        sum = xh.data + yh.data + self._add_helper_(xh.next,yh.next,result)
        node = Node(sum%10)
        result.push(node)
        return sum//10

    # add self to another and return sum
    def add(self,y):
        # add zeros in front
        diff = self.length() - y.length()
        y._add_zeros_(diff) if diff > 0 else self._add_zeros_(diff) 

        result = LinkedList()
        # recursive function to add
        self._add_helper_(self.head, y.test, result)
        return result

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
    
    # sum two lists and set sum to self
    def add_using_reverse(self,x,y):
        x.reverse()
        y.reverse()
        xh = x.test
        yh = y.test
        carry = 0 
        while xh is not None and yh is not None:
            node = Node((xh.data + yh.data + carry) % 10)
            carry = (xh.data + yh.data + carry)//10
            self.append(node)
            xh = xh.next
            yh = yh.next
        while xh is not None:
            node = Node((xh.data + carry) % 10)
            carry = (xh.data + carry)//10
            self.append(node)
            xh = xh.next
        while yh is not None:
            node = Node((yh.data + carry) % 10)
            carry = (yh.data + carry)//10
            self.append(node)
            yh = yh.next
        if carry !=0:
            self.append(Node(carry))
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
print("sum: ")
result = xl.add(yl)
result.printlist()
sum_list = LinkedList()
sum_list.add_using_reverse(xl,yl)
print("sum using reverse: ")
sum_list.printlist()

