# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        res = 0
        while stack:
            top, h = stack.pop()
            res = max(res, h)
            if top.left:
                stack.append((top.left, h + 1))
            if top.right:
                stack.append((top.right, h + 1))

        return res


class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
