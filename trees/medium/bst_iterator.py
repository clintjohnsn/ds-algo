"""
Leetcode 173
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class.
The root of the BST is given as part of the constructor.
The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer,
 otherwise returns false.
int next() Moves the pointer to the right,
then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number,
the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid.
That is, there will be at least a next number in the in-order traversal when next() is called.

Space optimized solution = O(height) ~ O(log n)
"""
from typing import Optional
from trees.easy.tree import TreeNode,tree


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = list()
        temp = root
        while temp:
            self.stack.append(temp)
            temp = temp.left

    def next(self) -> int:
        node = self.stack.pop()
        temp = node.right
        while temp:
            self.stack.append(temp)
            temp = temp.left
        return node.val

    def hasNext(self) -> bool:
        if self.stack:
            return True
        else:
            return False



# Driver
root = tree([7, 3, 15, None, None, 9, 20])
itr = BSTIterator(root)

while itr.hasNext():
    print(itr.next(), end=" ")