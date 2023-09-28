# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if not n:
            return None
        mid = (n - 1) // 2
        root = TreeNode(nums[mid])
        root.left = (self.sortedArrayToBST(nums[:mid]))
        root.right = (self.sortedArrayToBST(nums[mid + 1:]))
        return root

