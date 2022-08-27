"""
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Input:
            1
    3        2         4
5       6
Output: [1,3,5,6,2,4]

"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorderHelper(self, node:Node, output:list[int]):
        if not node:
            return
        output.append(node.val)
        if node.children:
            for child in node.children:
                self.preorderHelper(child,output)

    def preorder(self, root: Node) -> list[int]:
        output = list()
        self.preorderHelper(root,output)
        return output



""""
Input:
            1
    3        2         4
5       6
Output: [1,3,5,6,2,4]
"""
root = Node(1)
three = Node(3)
two = Node(2)
four = Node(4)
root.children = [three,two,four]
five = Node(5)
six = Node(6)
three.children = [five,six]

print(Solution().preorder(root))