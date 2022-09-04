"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


"""
from typing import  Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode],
                   min_limit: float = float("-inf"),
                   max_limit: float = float("inf")) -> bool:
        if not root:
            return True
        if min_limit < root.val < max_limit:
            return self.isValidBST(root.left, min_limit, root.val) \
                   and self.isValidBST(root.right, root.val, max_limit)
        return False

#Driver
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)
print(Solution().isValidBST(root))
