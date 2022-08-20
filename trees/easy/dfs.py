"""
Depth First Traversals: 
(a) Inorder (Left, Root, Right)
(b) Preorder (Root, Left, Right) 
(c) Postorder (Left, Right, Root) 

Time Complexity: O(n) 
S = recursive stack memory = O(h) where h is the height of the tree.

 TODO: Morris Traversal
 https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
"""
 
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
  
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val,end=' ')
        printInorder(root.right)
  
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val,end=' ')
  
def printPreorder(root):
    if root:
        print(root.val,end=' ')
        printPreorder(root.left)
        printPreorder(root.right)

def iterativePreorder(root):
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
  
# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("preorder")
printPreorder(root)
print()
print("iterative preorder")
iterativePreorder(root)
print()
print("inorder")
printInorder(root)
print()
print("postorder")
printPostorder(root)