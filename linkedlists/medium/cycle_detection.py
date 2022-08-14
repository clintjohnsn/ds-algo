"""
Write a function that checks whether a given Linked List contains a loop 
and if the loop is present then removes the loop and returns true. 
If the list doesn’t contain a loop then it returns false. 
eg 1 -> 2- > 3- > 4- > 5-> 2 becomes  1->2->3->4->5->NULL.

detect cycle
Method 1
Traverse the list one by one and keep putting the node addresses in a Hash Table.
At any point, if NULL is reached then return false, 
if the next of the current nodes points to any of the previously stored nodes in  Hash then return true.
T:O(N) S:O(N)

Method 2
Add a visited flag
T:O(N) S O(N) (flag * n)

Method 3: Floyd’s Cycle-Finding Algorithm 
Traverse linked list using two pointers.
Move one pointer(slow_p) by one and another pointer(fast_p) by two.
If these pointers meet at the same node then there is a loop. 
If pointers do not meet then linked list doesn’t have a loop.

Time complexity: O(n). 
Only one traversal of the loop is needed.
Auxiliary Space: O(1). 

Fixing the loop
for method 1-2 the loop start point is easily available at detection
for floyd's algo, the slow_p/fast_p is at a random node in the loop

Count the number of nodes in the loop. Let the count be k.
Fix one pointer to the head and another to a kth node from the head.
Move both pointers at the same pace, they will meet at the loop starting node.
Get a pointer to the last node of the loop and make the next of it NULL.
T = O(n)

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


def floyd_detect_loop(list):
    slow_p = list.head
    fast_p = list.head
    while(slow_p and fast_p and fast_p.next):
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p == fast_p:
            return (True,slow_p)
    return (False,None)

def fix_loop(list):
    has_loop, node = floyd_detect_loop(list)
    if has_loop:
        # find length of loop
        temp = node
        length = 1
        while(temp.next is not node):
            length += 1
            temp = temp.next
        # set a pointer at dist of length from head
        ptr = list.head
        while(length>0):
            length -=1
            ptr = ptr.next
        # move the head pointer and ptr till they meet at start of loop
        temp = list.head
        while(temp is not ptr):
            temp = temp.next
            ptr = ptr.next
        # ptr is the start of the loop
        # find the prev node and set to null
        end = ptr
        while(end.next is not ptr):
            end = end.next
        if end.next is ptr:
            end.next = None

# # Driver
llist = LinkedList()
for i in range(5,0,-1):
    llist.push(i)
llist.print_list()

# # make a cycle
three = llist.head.next.next
temp = llist.head
while temp.next is not None:
    temp = temp.next
temp.next = three

## endless loop
## llist.print_list()

print(floyd_detect_loop(llist))
##  fix it
fix_loop(llist)
llist.print_list()
