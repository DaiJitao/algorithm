from typing import List, Optional
import numpy as np
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -sys.maxsize - 1
        def max_tree(root: TreeNode):
            if root == None:
                return -sys.maxsize - 1

            max_left = max_tree(root.left)
            max_right = max_tree(root.right)
            self.max_sum = max(self.max_sum, max_left + root.val + max_right, max_left, max_right)
            return max(self.max_sum, root.val, max_left + root.val, max_left, root.val)

        new_max = max_tree(root)
        return max(self.max_sum, new_max)

def demo():
    """
    1 左 + 根 + 右
    2 左 + 根
    3 右 + 根
    4 根
    5 左
    6 右

    :return:
    """
