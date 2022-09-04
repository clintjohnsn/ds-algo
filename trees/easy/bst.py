# TODO: basic bst operations - insert, delete

"""
simple insert
guaranteed that element does not exist, do not balance the tree after

"""
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def bfs(self):
        q = deque()
        output = list()
        q.append(self)
        while q:
            node = q.popleft()
            if node:
                output.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                output.append(node)
        return output
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        else:
            if val < root.val:
                root.left = self.insertIntoBST(root.left,val)
            else:
                root.right = self.insertIntoBST(root.right,val)
            return root

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)

root = Solution().insertIntoBST(root,5)
print(root.bfs())