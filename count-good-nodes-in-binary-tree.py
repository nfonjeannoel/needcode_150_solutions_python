# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0

        def dfs(node, maxVal):
            if not node:
                return
            nonlocal res
            if node.val >= maxVal:
                res += 1
            dfs(node.left, max(maxVal, node.val))
            dfs(node.right, max(maxVal, node.val))

        dfs(root, root.val)
        return res


class Solution2:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)


from collections import deque


class Solution3:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()

        q.append((root, -float('inf')))

        while q:
            node, maxval = q.popleft()
            if node.val >= maxval:
                res += 1

            if node.left:
                q.append((node.left, max(maxval, node.val)))

            if node.right:
                q.append((node.right, max(maxval, node.val)))

        return res
