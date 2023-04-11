from typing import List
from typing import Optional
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
1 根 + 左 + 右
2 根 + 左
3 根 + 右
4 根
5 左
6 右
"""


class Solution:
    import sys
    def __init__(self):
        self.pamx = -sys.maxsize

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxGain(root: TreeNode):
            if root is None:
                return

            left = maxGain(root.left)
            right = maxGain(root.right)

            newmax = max(root.val + left + right, root.val + left, root.val+right, root.val, 0)
