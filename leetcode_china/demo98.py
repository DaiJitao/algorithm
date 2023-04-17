from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        res = []
        def inOrderTravel(root:TreeNode):
            if root is None:
                return

            inOrderTravel(root.left)
            res.append(root.val)
            inOrderTravel(root.right)


        inOrderTravel(root)
        for index  in range(1, len(res)):
            if res[index-1] >= res[index]:
                return False
        return True
