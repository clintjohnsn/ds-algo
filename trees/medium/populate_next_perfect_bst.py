"""
Leetcode 116
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

"""

"""
level order traversal
"""

from collections import deque
from typing import Optional
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return  root
        dq = deque()
        dq.append([root])
        while dq:
            level = list()
            prev = None
            for node in dq.popleft():
                if prev:
                    prev.next = node
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                prev = node
            if level:
                dq.append(level)
        return root

