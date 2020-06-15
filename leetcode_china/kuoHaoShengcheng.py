from typing import List

"""
https://leetcode-cn.com/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/

题解：方法一：深度优先遍历
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.val = value


class Solution:

    def generateTree(self, n):
        left, right = '(', ')'
        all_kuohao = list('()' * n)
        # 1 当前节点：左右节点都大于0，允许分支
        # 2 当前节点：左节点大于0，产生做分支
        # 3 当前节点：有节点大于左节点，产生右分支
        # 4 当前节点：左右节点都是0，结束分支


    def generateParenthesis(self, n: int) -> List[str]:
        left_kuohao, right_kuohao = "(", ')'
        if n == 0:
            return []
        if n:
            all_kuohao = list('()' * n)
            # 左括号和右括号的数量都大于0，产生分支
            if all_kuohao.count(left_kuohao) > 0 and all_kuohao.count(right_kuohao) > 0:
                if left_kuohao in all_kuohao:

            if all_kuohao.count(left_kuohao) == 0 and all_kuohao.count(right_kuohao) == 0:
                # 停止分支
                pass
