"""
You are given the root of a binary tree root. Invert the binary tree and return its root.
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if  root is None:
            return None
        current = root
        temp = current.left
        current.left = current.right
        current.right = temp
        self.invertTree(current.left)
        self.invertTree(current.right)
        return root
