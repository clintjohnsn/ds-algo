"""
Leetcode 543
https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

        1
    2       3
4       5
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def height(self, root: Optional[TreeNode], diameter:int=0) -> int:
        if not root:
            return -1,0
        else:
            left, ld = self.height(root.left, diameter)
            right, rd = self.height(root.right,ld)
            height = 1 + max(left,right)
            diameter = max(diameter,ld,rd, left + 2 + right)
            return height, diameter

    def diameter_of_binary_tree(self, root: Optional[TreeNode]) -> int:
        height, diameter = self.height(root)
        return diameter,height

# Driver
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right  = TreeNode(5)
print(Solution().diameter_of_binary_tree(root))

