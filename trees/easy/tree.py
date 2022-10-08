"""
simple tree utility functions for leetcode test cases
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree(bfs: list[int | None ]) -> TreeNode | None:
    """
    build a tree from a bfs array
    :param bfs: array
    :return: root
    """
    if not bfs:
        return None
    bfs = list(map(lambda x: TreeNode(x) if x is not None else None, bfs))
    i, j = 0, 1
    while j < len(bfs):
        if bfs[i] is not None:
            bfs[i].left = bfs[j]
            j += 1
            if j < len(bfs):
                bfs[i].right = bfs[j]
                j += 1
        i += 1
    return bfs[0]

from collections import  deque
def print_tree(root:TreeNode) -> None:
    """
    bfs representation of tree
    """
    if not root:
        return list()
    result = list()
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        result.append(node.val if node else None)
        if node:
            q.extend([node.left, node.right])
    print(result)