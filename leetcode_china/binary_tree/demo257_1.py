from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        stack = [root.val]
        res = []
        path_stack = [root.val]
        while stack:
            curr = stack.pop()
            path = path_stack.pop()
            if curr.left == None and curr.right == None:
                res.append(path)

            if curr.right is not None:
                stack.append(curr.right)
                path_stack.append(path + ' ' + curr.right.val)

            if curr.left is not None:
                stack.append(curr.left)
                path_stack.append(path + " " + curr.left.val)


        return res
