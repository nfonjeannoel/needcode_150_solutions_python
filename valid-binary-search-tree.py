# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None

        def inOrder(node):
            if not node:
                return True

            if not inOrder(node.left):
                return False
            nonlocal prev
            if prev != None and node.val <= prev:
                return False
            prev = node.val
            return inOrder(node.right)

        return inOrder(root)


class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, left, right):
            if not node:
                return True

            if not (left < node.val < right):
                return False

            return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)

        return isValid(root, float('-inf'), float('inf'))
