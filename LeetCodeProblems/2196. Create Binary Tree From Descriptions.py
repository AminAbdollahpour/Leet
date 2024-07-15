# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from idlelib.tree import TreeNode
from typing import List, Optional


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]):
        nodes = {}
        childern = set()
        for parent, child, is_left in descriptions:
            childern.add(child)
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
        for par,chi,left in descriptions:
            if par not in childern:
                return nodes[par]
