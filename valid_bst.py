"""
Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary search tree satisfies the following constraints:

    The left subtree of every node contains only nodes with keys less than the node's key.
    The right subtree of every node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees are also binary search trees.

Input: root = [2,1,3]

Output: true


Input: root = [1,2,3]

Output: false
"""

from collections import deque
from typing import Optional

from BST_inorder_traversal import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)

        while q:
            qLen = len(q)

            for i in range(qLen):
                parent = q.popleft()
                if parent:
                    if parent.left:
                        q.append(parent.left)
                        if parent.left.val >= parent.val:
                            return False
                    if parent.right:
                        q.append(parent.right)
                        if parent.right.val <= parent.val:
                            return False

        return True
