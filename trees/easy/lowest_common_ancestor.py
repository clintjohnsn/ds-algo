"""
leetcode 235

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

the lowest common ancestor is defined between two nodes p and q
as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself)

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.


root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself

Input: root = [2,1], p = 2, q = 1
Output: 2
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            return self.lowestCommonAncestor(root,q,p)
        if root is None:
            return root
        if root.val == p.val and root.val == q.val:
            return root
        if p.val <= q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if q.val >= p.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        if p.val <= root.val <= q.val:
            return root

root = TreeNode(2)
root.left = TreeNode(1)
print(Solution().lowestCommonAncestor(root,root,root.left).val)