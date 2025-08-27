# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append('N')
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(',')
        self.i = 0

        def dfs():
            if vals[self.i] == 'N':
                self.i += 1
                return

            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec2:
    # Serialize a tree into a string
    def serialize(self, root):
        if not root:
            return ""

        res = []
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)  # enqueue left child (can be None)
                q.append(node.right)  # enqueue right child (can be None)
            else:
                res.append("N")  # null marker

        # Remove trailing N's (not needed for reconstruction)
        while res and res[-1] == "N":
            res.pop()

        return ",".join(res)

    # Deserialize string back into a tree
    def deserialize(self, data):
        if not data:
            return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        q = deque([root])
        i = 1  # pointer for child values

        while q and i < len(values):
            parent = q.popleft()

            # Left child
            if values[i] != "N":
                parent.left = TreeNode(int(values[i]))
                q.append(parent.left)
            i += 1

            # Right child
            if i < len(values) and values[i] != "N":
                parent.right = TreeNode(int(values[i]))
                q.append(parent.right)
            i += 1

        return root
