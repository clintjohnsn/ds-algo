"""
bfs of tree
no of nodes n, no of edges =  n-1
 T = O(N) S = O(N)
"""
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 
def printLevelOrder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while(len(queue) > 0):
        print(queue[0].data)
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

from collections import deque
from typing import Optional
def levelOrder(root: Optional[Node]) -> list[list[int]]:
    if not root:
        return []
    order = list()
    dq = deque()
    dq.append([root])
    while dq:
        level = dq.popleft()
        order.append([node.data for node in level])
        nextlevel = list()
        for node in level:
            if node.left:
                nextlevel.append(node.left)
            if node.right:
                nextlevel.append(node.right)
        if nextlevel:
            dq.append(nextlevel)
    return order
# Driver 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
# root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

printLevelOrder(root)
print(levelOrder(root))


"""
n-ary tree level order traversal

"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from collections import deque
class Solution:
    def levelOrder(self, root: Node) -> list[list[int]]:
        dq = deque()
        output = list()
        if not root:
            return root
        dq.append([root])
        while dq:
            level = dq.popleft()
            output.append([node.val for node in level])
            nextlevel = list()
            for node in level:
                nextlevel.extend(node.children)
            if nextlevel:
                dq.append(nextlevel)
        return output