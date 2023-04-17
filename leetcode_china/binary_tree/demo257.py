from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []

        res = []
        path = ''

        def dfs(root):
            if root is None:
                return

            if root.left is None and root.right is None:
                res.append(path + str(root.val))
                return

            dfs(root.left, path + str(root.val) + '->')
            dfs(root.right, path + str(root.val) + '->')

        dfs(root)
        return res
