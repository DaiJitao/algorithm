from typing import List, Optional

"""
最长公共子序列: leetcode 1143
"""


def demo(x, y):
    if x is None or len(x) == 0:
        return 0
    if y is None or len(y) == 0:
        return 0

    """
    dp[i][j] 代表以x[i]和y[j]结尾的最长公共子序列
    if x[i] == y[j]: 
        dp[i][j] = dp[i-1][j-1]+1
    else:
        if x[i-1] == y[j]:
            dp[i][j] = dp[i-1][j]
        elif x[i] == y[j-1]:
            dp[i][j] = dp[i][j-1]
            
        dp[i][j] = max(dp[i-1][j], dp[i-1][j])
        
    res = max(pamx, dp[i][j])
    """


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 is None or text2 is None:
            return None
        n1 = len(text1)
        n2 = len(text2)
        if n1 == 0 or n2 == 0:
            return 0

        if n1 == 0 or n2 == 0:
            return 0
        if n1 == 1 and text1[0] in text2:
            return 1
        if n2 == 1 and text2[0] in text1:
            return 1

        row_num = n1 + 1
        col_num = n2 + 1

        cols = [0] * col_num
        dp = [cols[:] for _ in range(row_num)]
        if text1[0] == text2[0]:
            dp[0][0] = 1
        else:
            dp[0][0] = 0

        for j in range(1, n2 + 1):
            dp[0][j] = 1 if text1[0] in text2[:j + 1] else 0

        for i in range(1, n1):
            dp[i][0] = 1 if text2[0] in text1[:i + 1] else 0

        pmax = 0
        for i in range(1, n1):
            for j in range(1, n2):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

                pmax = max(pmax, dp[i][j])

        return pmax