"""
Leetcode 617

Merge Two Binary Trees
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped
while the others are not.
You need to merge the two trees into a new binary tree.
The merge rule is that if two nodes overlap,
then sum node values up as the new value of the merged node.
 Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.


Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Input: root1 = [1], root2 = [1,2]
Output: [2,2]
"""

from trees.easy.tree import tree,TreeNode, print_tree
from typing import Optional
class Solution:
    def merge_trees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        temp = None
        if not root1 and not root2:
            return temp
        if root1 and not root2:
            temp = TreeNode(root1.val)
        elif root2 and not root1:
            temp = TreeNode(root2.val)
        elif root1 and root2:
            temp = TreeNode(root1.val + root2.val)
        temp.left = self.merge_trees(root1.left if root1 else None, root2.left if root2 else None)
        temp.right = self.merge_trees(root1.right if root1 else None, root2.right if root2 else None)
        return temp


# Test
root1 = tree([1,3,2,5])
root2 = tree([2,1,3,None,4,None,7])
root = Solution().merge_trees(root1, root2)
print_tree(root)

root1 = tree([1])
root2 = tree([1,2])
root = Solution().merge_trees(root1, root2)
print_tree(root)