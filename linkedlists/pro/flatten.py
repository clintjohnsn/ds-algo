"""
Leetcode 430. Flatten a Multilevel Doubly Linked List
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/


Given a linked list where every node represents a linked list and contains two pointers of its type: 

Pointer to next node in the main list (we call it right pointer) 
Pointer to a linked list (we call it the down pointer)
All linked lists are sorted

flatten this ds into a linked list. resultant linked list should also be sorted

eg

Input:  5 -> 10 -> 19 -> 28
        |     |     |     |
        7     20    22    35
        |           |      |
        8           50     40
        |                   |
        30                 45

Output: 5->7->8->10->19->20->22->28->30->35->40->45->50

# Method 1
Recursively call to merge the current linked list with the next linked list
If the current linked list is empty or there is no next linked list then return the current linked list (Base Case)
Start merging the linked lists, starting from the last linked list

Time Complexity: O(N * N * M) – where N is the no of nodes in the main linked list and M is the no of nodes in a single sub-linked list 
Explanation: As we are merging 2 lists at a time,

After adding the first 2 lists, the time taken will be O(M+M) = O(2M).
Then we will merge another list to above merged list -> time = O(2M + M) = O(3M).
Then we will merge another list -> time = O(3M + M).
We will keep merging lists to previously merged lists until all lists are merged.
Total time taken will be O(2M + 3M + 4M + …. N*M) = (2 + 3 + 4 + … + N) * M
Using arithmetic sum formula: time = O((N * N + N – 2) * M/2)
The above expression is roughly equal to O(N * N * M) for a large value of N
Auxiliary Space: O(N*M) – because of the recursion. 
The recursive functions will use a recursive stack of a size equivalent to a total number of elements in the lists, which is N*M.

# Method 2
Create a priority queue(Min-Heap) and push the head node of every linked list into it 
(main chain element are the head nodes of side chain and the min of the side chains )
While the priority queue is not empty, extract the minimum value node from it (get next min val) 
and if there is a down node linked to the minimum value node then push it into the priority queue (next candidate for min val)
Also, print the value of the node every time after extracting the minimum value node

Time Complexity: O(N * M * log(N)) – where N is the no of nodes in the main linked list (reachable using the next pointer) 
and M is the no of nodes in a single sub-linked list (reachable using a bottom pointer).
Auxiliary Space: O(N) – where N is the no of nodes in the main linked list (reachable using the next pointer).

similar to traversing through O(mn) and adding to a ll T = O(mn) S =O(mn), then sorting this list, T = O(mnlog(mn)), 
only that elements are popped immediately, leading to efficient time and space complexities

"""
import heapq
# Method 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.down = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # push into side chain
    def push_side_chain(self,side_head,value):
        temp = side_head
        while temp.down is not None:
            temp = temp.down
        node = Node(value)
        temp.down = node
    
    # push at head like stack O(1)
    def push(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node
        return node

    def print_list_whole(self):
        temp = self.head
        while(temp):
            self.print_side_chain(temp)
            temp = temp.next

    def print_side_chain(self,side_head):
        temp = side_head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.down
        print()

    # recursive reverse print
    # def print_list(self,temp):
    #     if temp:
    #         self.print_list(temp.next)
    #         print(temp.data, end=' ')

    
    def merge(self,ch1,ch2):
        """
        used in method 1 flatten
        merge chain1 chain2 into chain 1
        """
        rh = ch1
        prev = None
        while ch1 and ch2:
            if ch1.data <= ch2.data:
                prev = ch1
                ch1 = ch1.down
            else:
                node = Node(ch2.data)
                node.down = prev.down
                prev.down = node
                prev = node
                ch1 = node.down
                ch2 = ch2.down
        while ch1:
            prev = ch1
            ch1 = ch1.down
        while ch2:
            node = Node(ch2.data)
            prev.down = node
            prev = prev.down
            ch2 = ch2.down
        return rh
    
    def flatten(self):
        """
        method 1
        result in chain 1
        """
        rh = self.head
        if rh is None:
            return rh
        temp = self.head.next
        while temp:
            rh = self.merge(rh,temp)
            temp = temp.next
        return rh
    
    def heap_flatten(self):
        """
        method 2
        https://docs.python.org/3/library/heapq.html
        """
        heap = []
        temp = self.head
        while temp:
            heapq.heappush(heap,(temp.data,temp))
            temp = temp.next
        while heap:
            data, temp = heapq.heappop(heap)
            print(data,end=' ')
            if temp.down:
                heapq.heappush(heap,(temp.down.data,temp.down))


# Driver
# make the required linked list
inpt = [[5,7,8,30],[10,20],[19,22,50],[28,35,40,45]]
ll = LinkedList()
for values in reversed(inpt):
    side_head = ll.push(values[0])
    for i in range(1,len(values)):
        ll.push_side_chain(side_head,values[i])
print("linked list: ")
ll.print_list_whole()
print("heap based flattening: ")
ll.heap_flatten()
print()
print("method 1 flattening (changes original linked list): ")
result = ll.flatten()
ll.print_side_chain(result)

# ----------------------------
# alt implementation, method 1

# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.right = None
#         self.down = None
 
 
# class LinkedList():
#     def __init__(self):
 
#         # head of list
#         self.head = None
 
#     # Utility function to insert a node at beginning of the
#     #   linked list
#     def push(self, head_ref, data):
 
#         # 1 & 2: Allocate the Node &
#         # Put in the data
#         new_node = Node(data)
 
#         # Make next of new Node as head
#         new_node.down = head_ref
 
#         # 4. Move the head to point to new Node
#         head_ref = new_node
 
#         # 5. return to link it back
#         return head_ref
 
#     def printList(self):
 
#         temp = self.head
#         while(temp != None):
#             print(temp.data, end=" ")
#             temp = temp.down
 
#         print()
 
#     # An utility function to merge two sorted linked lists
#     def merge(self, a, b):
#         # if first linked list is empty then second
#         # is the answer
#         if(a == None):
#             return b
 
#         # if second linked list is empty then first
#         # is the result
#         if(b == None):
#             return a
 
#         # compare the data members of the two linked lists
#         # and put the larger one in the result
#         result = None
 
#         if (a.data < b.data):
#             result = a
#             result.down = self.merge(a.down, b)
#         else:
#             result = b
#             result.down = self.merge(a, b.down)
 
#         result.right = None
#         return result
 
#     def flatten(self, root):
 
#         # Base Case
#         if(root == None or root.right == None):
#             return root
#         # recur for list on right
 
#         root.right = self.flatten(root.right)
 
#         # now merge
#         root = self.merge(root, root.right)
 
#         # return the root
#         # it will be in turn merged with its left
#         return root
 
 
# # Driver's code
# if __name__ == '__main__':
#     L = LinkedList()
 
#     '''
#     Let us create the following linked list
#             5 -> 10 -> 19 -> 28
#             |    |     |     |
#             V    V     V     V
#             7    20    22    35
#             |          |     |
#             V          V     V
#             8          50    40
#             |                |
#             V                V
#             30               45
#     '''
#     L.head = L.push(L.head, 30)
#     L.head = L.push(L.head, 8)
#     L.head = L.push(L.head, 7)
#     L.head = L.push(L.head, 5)
 
#     L.head.right = L.push(L.head.right, 20)
#     L.head.right = L.push(L.head.right, 10)
 
#     L.head.right.right = L.push(L.head.right.right, 50)
#     L.head.right.right = L.push(L.head.right.right, 22)
#     L.head.right.right = L.push(L.head.right.right, 19)
 
#     L.head.right.right.right = L.push(L.head.right.right.right, 45)
#     L.head.right.right.right = L.push(L.head.right.right.right, 40)
#     L.head.right.right.right = L.push(L.head.right.right.right, 35)
#     L.head.right.right.right = L.push(L.head.right.right.right, 20)
 
#     # Function call
#     L.head = L.flatten(L.head)
 
#     L.printList()
