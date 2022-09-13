"""
Given the root of a binary search tree, and an integer k,
return the kth smallest value of all the values of the nodes in the tree.

"""
from typing import  Optional
from trees.easy.tree import TreeNode,tree

class Solution:
    def kth_smallest_helper(self, root: Optional[TreeNode], k: int, val: int) -> tuple[int,int]:
        if root is None:
            return k, val
        k, val = self.kth_smallest_helper(root.left, k, val)
        k -= 1
        if k == 0:
            return k, root.val
        else:
            return self.kth_smallest_helper(root.right, k, val)

    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        k, val = self.kth_smallest_helper(root, k, -1)
        return val

#Test
test_root = tree([3,1,4,None,2])
print(Solution().kth_smallest(test_root,1)) # 1

test_root = tree([5,3,6,2,4,None,None,1])
print(Solution().kth_smallest(test_root,3)) # 3

"""
same as above but  iterative, stack based solution

Time complexity: O(H + k) where H is a tree height. 
This complexity is defined by the stack, which contains at least H + k elements,
 since before starting to pop out one has to go down to a leaf. 
 This results in O(logN+k) for the balanced tree and O(N+k) for completely unbalanced tree 
 with all the nodes in the left subtree.
Space complexity: O(H) to keep the stack, where H is a tree height. 
That makes O(N) in the worst case of the skewed tree, and O(logN) in the average case of the balanced tree.

"""


class Solution:
    def kth_smallest(self, root, k):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right

print("---------------------")
#Test
test_root = tree([3,1,4,None,2])
print(Solution().kth_smallest(test_root,1)) # 1

test_root = tree([5,3,6,2,4,None,None,1])
print(Solution().kth_smallest(test_root,3)) # 3

