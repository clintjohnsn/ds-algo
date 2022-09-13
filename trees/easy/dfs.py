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

def iterative_postorder(root):
    pass

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