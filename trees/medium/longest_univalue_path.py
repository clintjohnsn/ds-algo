# Leetcode: 687
# https://leetcode.com/problems/longest-univalue-path/

from typing import  Optional
from trees.easy.tree import TreeNode,tree

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode], pathlength:int=0, longest: int =0 ) -> int:
        if not root or (not root.left and not root.right):
            return pathlength, longest
        left_pathlength, right_pathlength = 0,0
        if root.left:
            if root.val == root.left.val:
                left_pathlength, longest = self.longestUnivaluePath(root.left, pathlength +1,longest)
            else:
                left_pathlength, longest = self.longestUnivaluePath(root.left, 0, longest)
        if root.right:
            if root.val == root.right.val:
                right_pathlength, longest = self.longestUnivaluePath(root.right, pathlength +1, longest)
            else:
                right_pathlength, longest = self.longestUnivaluePath(root.right, 0, longest)
        if left_pathlength == 0:
            return right_pathlength, max(longest,right_pathlength)
        elif right_pathlength == 0:
            return  left_pathlength, max(longest,left_pathlength)
        else:
            if root.val == root.left.val == root.right.val:
                return max(left_pathlength,right_pathlength), \
                       max(left_pathlength,right_pathlength, left_pathlength + right_pathlength - 2 * pathlength, longest)
            else:
                return max(left_pathlength, right_pathlength), \
                       max(left_pathlength, right_pathlength, longest)




# Test
# tr = tree([5,4,5,1,1,None,5])
# print(Solution().longestUnivaluePath(tr)) # 2
tr = tree([4,4,4,4,4,None,5])
print(Solution().longestUnivaluePath(tr)) # 2