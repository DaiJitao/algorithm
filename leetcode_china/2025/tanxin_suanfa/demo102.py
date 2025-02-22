# -*- coding: utf-8 -*-
# @Author  : NLPCoder
# @Time    : 2025/2/22 14:15
# @Function: 


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return

        res = []
        que = []
        que.append(root)
        while len(que) > 0:

            index = len(que) - 1
            inner = []
            while index >= 0:
                node = que.pop()
                inner.append(node.val)
                if que[-1].left != None:
                    que.insert(0, node.left)
                if que[-1].right != None:
                    que.insert(0, node.right)

                index -= 1
            res.append(inner)

        return res


