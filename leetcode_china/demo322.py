

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        dp[i][j] 表示在【0-i]进行选取，使其总数为j,所达到的硬币最少的个数为dp[i][j]

        """