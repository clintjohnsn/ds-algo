"""

Leetcode 112 (easy)
Given the root of a binary tree and an integer targetSum, return true
if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""
from __future__ import annotations
from typing import Optional
from trees.easy.tree import tree, TreeNode


class Solution:
    def has_path_sum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        if not root:
            return False
        # current node reduces to 0, and is a leaf node
        if target_sum - root.val == 0 and not root.left and not root.right:
            return True
        return self.has_path_sum(root.left, target_sum - root.val) or \
               self.has_path_sum(root.right,target_sum - root.val)


# Driver
test_root = tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
print(Solution().has_path_sum(test_root, 22))  # true
test_root = tree([1, 2, 3])
print(Solution().has_path_sum(test_root, 5))  # false
test_root = tree([])
print(Solution().has_path_sum(test_root, 0))  # false
print("-------------------------------------")

"""
Leetcode 113 (medium)
Given the root of a binary tree and an integer targetSum,
 return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
Each path should be returned as a list of the node values, not node references.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

"""
import  copy
class Solution:
    def get_paths_helper(self, root: Optional[TreeNode], target_sum: int, paths:list[list[int]], path: list[int] = None) -> None:
        if not root:
            return
        if not path:
            path = list()
        # current node reduces to 0, and is a leaf node
        path.append(root.val)
        if target_sum - root.val == 0 and not root.left and not root.right:
            paths.append(copy.deepcopy(path))
        self.get_paths_helper(root.left, target_sum - root.val, paths,path)
        self.get_paths_helper(root.right,target_sum - root.val,paths,path)
        path.pop()

    def get_paths(self,root: Optional[TreeNode], target_sum: int):
        paths = list()
        self.get_paths_helper(root,target_sum,paths)
        return paths
# test
test_root = tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
print(Solution().get_paths(test_root, 22))  # [[5,4,11,2],[5,8,4,5]]
test_root = tree([1,2,3])
print(Solution().get_paths(test_root, 5))  # []
test_root = tree([1,2])
print(Solution().get_paths(test_root, 0))  # []
print("-------------------------------------")

"""
Leetcode 437 (medium)

Given the root of a binary tree and an integer targetSum,
 return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf,
 but it must go downwards (i.e., traveling only from parent nodes to child nodes).

        1
    2       -2
4      3  x     7
paths with 6 = 3
2,4
1,2,3
1,-2,7

simpler problem : arrays/medium/subarray_sum

"""

import copy
from collections import defaultdict


class Solution:
    def path_sum(self, root: Optional[TreeNode],
                 target_sum: int,
                 count: int = 0,
                 running_sum: int = 0,
                 cumulative_sum: defaultdict = None) -> int:
        if not root:
            return count
        if not cumulative_sum:
            cumulative_sum = defaultdict(int)
            cumulative_sum[0] = 1
        running_sum = running_sum + root.val
        if cumulative_sum[running_sum - target_sum] > 0:
            count += cumulative_sum[running_sum - target_sum]
        cumulative_sum[running_sum] += 1

        count = self.path_sum(root.left, target_sum, count, running_sum, copy.deepcopy(cumulative_sum))
        count = self.path_sum(root.right, target_sum, count, running_sum, copy.deepcopy(cumulative_sum))
        return count

    def path_sum2(self, root: Optional[TreeNode],
                  target_sum: int,
                  count: int = 0,
                  running_sum: int = 0,
                  cumulative_sum: defaultdict = None) -> int:
        if not root:
            return count
        if not cumulative_sum:
            cumulative_sum = defaultdict(int)
            cumulative_sum[0] = 1
        running_sum = running_sum + root.val
        if cumulative_sum[running_sum - target_sum] > 0:
            count += cumulative_sum[running_sum - target_sum]
        cumulative_sum[running_sum] += 1
        count = self.path_sum2(root.left, target_sum, count, running_sum, cumulative_sum)
        count = self.path_sum2(root.right, target_sum, count, running_sum, cumulative_sum)
        cumulative_sum[running_sum] -= 1
        return count


# Test
root1 = tree([1, 2, -2, 4, 3, None, 7])
print(Solution().path_sum2(root1, 6))  # 3

root2 = tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
print(Solution().path_sum2(root2, 8))  # 3

root3 = tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
print(Solution().path_sum2(root3, 22))  # 3
