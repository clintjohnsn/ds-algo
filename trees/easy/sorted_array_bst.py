"""
Leetcode 108
Convert Sorted Array to Binary Search Tree
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node
never differs by more than one.


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

"""
from typing import Optional
from trees.easy.tree import TreeNode

class Solution:
    def sorted_array_to_BST(self, nums: list[int], start:int=None, end:int=None) -> Optional[TreeNode]:
        if start is None or end is None:
            start = 0
            end = len(nums)
        if start < end:
            mid = (start + end)//2
            root = TreeNode(nums[mid])
            root.left = self.sorted_array_to_BST(nums,start,mid)
            root.right = self.sorted_array_to_BST(nums,mid+1,end)
            return root
        return None

# Test
test_root = Solution().sorted_array_to_BST([-10,-3,0,5,9])
test_root = Solution().sorted_array_to_BST([1,3])
