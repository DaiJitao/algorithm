from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 is None or text2 is None:
            return None
        n1 = len(text1)
        n2 = len(text2)
        if n1 == 0 or n2 == 0:
            return 0
        if n1 == 1 and text1[0] in text2:
            return 1
        if n2 == 1 and text2[0] in text1:
            return 1

        row_num = n1 + 1
        col_num = n2 + 1

        cols = [0] * col_num
        dp = [ cols[:] for _ in range(row_num)]
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


if __name__ == '__main__':
    text1 = "abcde"
    text2 = "ace"
    text1 = 'xaxx'
    text2 = 'a'
    res = Solution().longestCommonSubsequence(text1, text2)
    print(res)


def demo1143():
    """
    dp[i][j] 代表从a[0:i]，b[0:j]中选取的字符串的最长公共子序列的长度为dp[i][j]

    if a[i] == b[j]: d[i-1][j-1] + 1
    if a[i] != b[j]:

    :return:
    """
    pass
