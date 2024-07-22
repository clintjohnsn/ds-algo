"""
Leetcode 110
https://leetcode.com/problems/balanced-binary-tree/

 height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def height(self, root: Optional[TreeNode], diff:int=0) -> tuple[int, int]:
        if not root:
            return -1, diff
        else:
            lh, diff = self.height(root.left, diff)
            rh, diff = self.height(root.right, diff)
            return 1 + max(lh, rh), max(diff, abs(lh - rh))

    def is_balanced(self, root:Optional[TreeNode]) -> bool:
        tree_height, diff = self.height(root)
        print(tree_height,diff)
        return not diff > 1

"""

Test
              1
        2           22
    3      x    x       33
 4   x                x    4

"""


root = TreeNode(1)
root.left = two = TreeNode(2)
root.right = twentytwo = TreeNode(22)
two.left = three = TreeNode(3)
twentytwo.right = thirtythree = TreeNode(33)
three.left = TreeNode(4)
thirtythree.right = TreeNode(4)
print(Solution().is_balanced(root))

"""
less cool solutions
1. make height calculations in every isbalance call
2. modify height method to return invalid height (-1) if not balanced

"""


def is_balanced(root):
    if root is None:
        return True
    # Compute height of left subtree
    lh = is_balanced(root.left)
    # If left subtree is not balanced,
    if lh == -1:
        return -1
    rh = is_balanced(root.right)
    if rh == -1:
        return -1
    if (abs(lh - rh) > 1):
        return -1
    # If we reach here means tree is
    # height-balanced tree, return height
    else:
        return max(lh, rh) + 1

print(is_balanced(root))