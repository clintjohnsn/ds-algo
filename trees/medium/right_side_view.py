"""
Leetcode 199
Given the root of a binary tree,
imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.


Input: root = [1,2,3,null,5,null,4]
            1
        2       3
          5       4

Output: [1,3,4]

"""

"""
bfs solution
T = O(N)
S = O(N)
"""
from trees.easy.tree import tree,TreeNode
from typing import  Optional

class Solution:
    def right_side_view(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return list()
        out = list()
        q = list()
        q.append(root)
        while q:
            new = list()
            out.append(q[-1].val)
            for node in q:
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            q = new
        return out

# Test
r1 = tree( [1,2,3,None,5,None,4])
print(Solution().right_side_view(r1)) # [1,3,4]
r2 = tree([])
print(Solution().right_side_view(r2)) #[]
r3 = tree([1,None,3])
print(Solution().right_side_view(r3)) # [1,3]

"""
dfs solution

"""
