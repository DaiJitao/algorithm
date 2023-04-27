from typing import List, Optional
import numpy as np

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """

        :param root:
        :return:
        """
        if root is None:
            return None

        """分析：
        1 左 + 根 + 右
        2 左 + 根
        3 右 + 根
        4 根
        5 左
        6 右
        """
        self.max_sum = -np.inf
        def dfs_max(root:TreeNode):
            if root is None:
                return

            left_max = dfs_max(root.left)
            right_amx = dfs_max(root.right)
            self.max_sum = max(self.max_sum, left_max + root.val + right_amx, left_max, right_amx)
            return max(root.val + left_max, root.val + right_amx, root.val)

        dfs_max(root)
        return max(self.max_sum, )