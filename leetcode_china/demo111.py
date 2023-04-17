from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def getDepth(root: TreeNode):
            if root is None:
                return 0

            leftdepth = getDepth(root.left)  # 0
            rightdepth = getDepth(root.right)  # 1
            # 右子树不为空，左子树为空
            if root.left is None and root.right is not None:
                return 1 + rightdepth
            # 左子树不为空，右子树为空
            if root.left is not None and root.right is None:
                return leftdepth + 1

            return min(leftdepth, rightdepth)

        return getDepth(root)
