# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def getDepth(node, depth):
            if node is None:
                return depth

            leftDepth = getDepth(node.left, depth + 1)
            rightDepth = getDepth(node.right, depth + 1)
            return max(leftDepth, rightDepth)

        right = getDepth(root.right, 0)
        left = getDepth(root.left, 0)
        diameter = max(right + left, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return diameter
