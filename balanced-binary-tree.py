# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, root):
        if not root:
            return 0

        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))


class Solution2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            isBalanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)
            return [isBalanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]