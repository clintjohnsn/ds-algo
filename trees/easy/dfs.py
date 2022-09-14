"""
Depth First Traversals: 
(a) Inorder (Left, Root, Right)
(b) Preorder (Root, Left, Right) 
(c) Postorder (Left, Right, Root) 

Time Complexity: O(n) 
S = recursive stack memory = O(h) where h is the height of the tree.

"""
 
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
  
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=' ')
        inorder(root.right)
  
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val,end=' ')
  
def preorder(root):
    if root:
        print(root.val,end=' ')
        preorder(root.left)
        preorder(root.right)

def iterative_preorder(root):
    if root is None:
        return
    nodeStack = []
    nodeStack.append(root)
    while(len(nodeStack) > 0):
        node = nodeStack.pop()
        print (node.val, end=" ")
        # Note that right child is pushed first so that left is processed first
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)

def iterative_inorder(root):
    current = root
    stack = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        # BackTrack visit the Node at the top of the stack
        elif stack:
            current = stack.pop()
            print(current.val, end=" ")
            current = current.right
        else:
            break

def iterative_inorder_2(root):
    stack = []
    temp = root
    while True:
        while temp:
            stack.append(temp)
            temp = temp.left
        if stack:
            temp = stack.pop()
            print(temp.val, end=' ')
            temp = temp.right
        else:
            break

"""
iterative postorder
https://www.geeksforgeeks.org/iterative-postorder-traversal/?ref=lbp

postorder = reverse order of a preorder traversal, with right subtree processing before left subtree processing
D, R, L

                1
        2              3
    4       5       6       7
    
postorder = L,R,D = 4,5,2,6,7,3,1
reverse  = 1,3,7,6,2,5,4

use a stack to reverse the iterative preorder
iterative preorder itself uses a stack
"""


def iterative_postorder(root):
    stack = list()
    postorder = list()
    stack.append(root)
    while stack:
        node = stack.pop()
        postorder.append(node)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    while postorder:
        print(postorder.pop().val, end=' ')



# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("preorder")
preorder(root)
print()
print("iterative preorder")
iterative_preorder(root)
print()
print("inorder")
inorder(root)
print()
print("iterative inorder")
iterative_inorder(root)
print()
print("iterative inorder 2")
iterative_inorder_2(root)
print()
print("postorder")
postorder(root)
print()
print("iterative postorder")
iterative_postorder(root)