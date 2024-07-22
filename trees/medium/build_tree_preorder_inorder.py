"""
Leetcode: 105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
 and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
    3
9       20
     15     7

"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        root.left = self.buildTree(preorder,inorder[:root_index])
        root.right = self.buildTree(preorder,inorder[root_index+1:])
        return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Solution().buildTree(preorder,inorder)

"""
TODO: 
optimize this solution:
either use deque for preorder for O(1) pop or use indexing
use left and right indices on inorder array
use a hashmap to store the indexes of values instead of finding the index of the root

"""