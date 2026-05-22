"""
Balanced Binary Tree
Easy Topics Company Tags
Hints

Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Input: root = [1,2,3,null,null,4]

Output: True

Input: root = [1,2,3,null,null,4,null,5]

Output: false


Input: root = []

Output: true
"""

from typing import Optional

from BST_inorder_traversal import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def dfs(node):
            if node is None:
                return True

            leftCount = dfs(node.left)
            rightCount = dfs(node.right)

            if abs(leftCount - rightCount) > 1:
                self.balanced = False

            return max(leftCount, rightCount) + 1

        self.balanced = True

        dfs(root)
        return self.balanced
