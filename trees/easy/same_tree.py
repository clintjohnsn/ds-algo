"""
Leetcode 100

Given the roots of two binary trees p and q, write a function to check if they are the same or not.


"""
from trees.easy.tree import  TreeNode,tree
from typing import  Optional

class Solution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q:
            if p.val != q.val:
                return False
            else:
                return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
        return False


"""
Leetcode 101

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Input: root = [1,2,2,3,4,4,3]
            1
          2   2
      3    4 4   3
Output: true

Input: root = [1,2,2,null,3,null,3]
            1
        2       2
           3        3
Output: false
"""

class Solution:
    def is_symmetric_helper(self, a: TreeNode, b: TreeNode) -> bool:
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val == b.val:
            return self.is_symmetric_helper(a.left,b.right) and self.is_symmetric_helper(a.right, b.left)

    def is_symmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_symmetric_helper(root,root)


#Test
r1 = tree([1,2,2,3,4,4,3])
print(Solution().is_symmetric(r1)) # True
r2 = tree([1,2,2,None,3,None,3])
print(Solution().is_symmetric(r2)) # False

class Solution:

    def is_symmetric_iterative(self, root: Optional[TreeNode]) -> bool:
        stack = list()
        stack.append((root,root))
        while stack:
            a,b = stack.pop()
            if not a and not b:
                continue
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            stack.extend([(a.left,b.right),(a.right,b.left)])
        return True

#Test
print(Solution().is_symmetric_iterative(r1)) # True
print(Solution().is_symmetric_iterative(r2)) # False
