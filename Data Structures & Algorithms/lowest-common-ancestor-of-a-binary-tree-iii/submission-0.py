"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen = set()

        pNode = p
        while pNode is not None:
            seen.add(pNode)
            pNode = pNode.parent

        qNode = q
        while qNode not in seen and qNode is not None:
            qNode = qNode.parent

        return qNode
        