"""
Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Input: root = [1,2,3,4,5,6,7]

Output: [[1],[2,3],[4,5,6,7]]

Example 2:

Input: root = [1]

Output: [[1]]

Example 3:

Input: root = []

Output: []
"""

from collections import deque
from typing import List, Optional

from BST_inorder_traversal import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        final_list = []

        while q:
            queueLength = len(q)
            child_list = []
            for i in range(queueLength):
                node = q.popleft()
                if node:
                    child_list.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if child_list:
                final_list.append(child_list)
        return final_list
