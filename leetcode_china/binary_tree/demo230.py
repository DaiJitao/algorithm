from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if k <= 0 or root is None:
            return None

        res = []

        def middTravel(root: TreeNode):
            if root == None:
                return

            middTravel(root.left)
            res.append(root.val)
            middTravel(root.right)

        return res[k - 1]
