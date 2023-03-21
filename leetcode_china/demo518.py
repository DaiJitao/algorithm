
"""
题目： https://leetcode.cn/problems/coin-change-ii/
"""
from typing import  List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if coins is None or len(coins) == 0:
            return None

        b = len(coins)
        """
        dp[j] 达到价值为j的背包，共有d[j]种方法
        dp[0] = 0
        dp[1] = if j >= nums[i]
        """
