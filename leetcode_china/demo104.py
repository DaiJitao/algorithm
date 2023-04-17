from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def getDepth(root:TreeNode, depth:int=0):
            if root is None:
                return 0

            leftDepth = getDepth(root.left)
            rightDepth = getDepth(root.right)

            depth = max(leftDepth, rightDepth) + 1

            return depth

        depth = getDepth(root)
        return depth