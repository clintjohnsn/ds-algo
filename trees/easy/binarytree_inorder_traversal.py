"""

Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self,root:Optional[TreeNode],output:list[int]):
        if not root:
            return
        if root.left:
            self.inorder(root.left,output)
        output.append(root.val)
        if root.right:
            self.inorder(root.right,output)

    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        output = list()
        self.inorder(root,output)
        return  output


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.left = Node(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(Solution().inorderTraversal(root))