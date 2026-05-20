"""
Same Binary Tree
Hints

Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.
Example:
Input: p = [1,2,3], q = [1,2,3]

Output: true

Input: p = [4,7], q = [4,null,7]

Output: false

Input: p = [1,2,3], q = [1,3,2]

Output: false

"""

from typing import Optional

from BST_inorder_traversal import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if p is None and q is None:
                return True

            if p is None or q is None:
                return False

            if p.val != q.val:
                return False

            return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p, q)
