"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Input: root = [1,2,3,4,5], subRoot = [2,4,5]

Output: true


Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]

Output: false
"""

from collections import deque
from typing import Optional

from BST_inorder_traversal import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if subRoot is None and root is None:
            return True
        if subRoot is None or root is None:
            return False

        def dfs(p, q):
            if p is None and q is None:
                return True

            if p is None or q is None:
                return False

            if p.val != q.val:
                return False

            return dfs(p.left, q.left) and dfs(p.right, q.right)

        if subRoot:
            q = deque()
            q.append(root)

            while q:
                queLength = len(q)
                for i in range(queLength):
                    node = q.popleft()
                    if node:
                        if node.val == subRoot.val:
                            if dfs(node, subRoot):
                                return True
                        q.append(node.left)
                        q.append(node.right)
        return False
