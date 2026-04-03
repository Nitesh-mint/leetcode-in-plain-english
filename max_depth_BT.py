from typing import Deque, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1


node4 = TreeNode(4)

node2 = TreeNode(2)
node3 = TreeNode(3, left=node4)

root = TreeNode(1, left=node2, right=node3)

sol = Solution()
print(sol.maxDepth(root))
