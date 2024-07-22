"""
leetcode 226
https://leetcode.com/problems/invert-binary-tree/

invert binary tree
invert and return root
invert => left child becomes right , right becomes left

"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        else:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.invert_tree(root.left)
            self.invert_tree(root.right)
            return root

# Test
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root = Solution().invert_tree(root)
print(root.val,root.left.val,root.right.val,root.right.left,root.right.right.val)
