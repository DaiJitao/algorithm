# -*- coding: utf-8 -*-
# @Author  : NLPCoder
# @Time    : 2025/2/22 20:58
# @Function: 


from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]: