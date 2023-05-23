from typing import List, Optional

"""
两个字符序列的最长公共子序列
"""


def demo(s1, s2):
    if s1 is None or len(s1) == 0:
        return 0
    if s2 is None or len(s2) == 0:
        return 0

    """
    dp[i][j] 代表S1[:i] s2[:j] 的最长公共子序列的长度；
    """
    n1 = len(s1)
    n2 = len(s2)
    print(n1, n2)
    inner = [0] * (n2)
    dp = [inner[:] for _ in range(n1)]
    dp[0][0] = 1 if s1[0] == s2[0] else 0
    maxp = 0
    print(dp)


    for i in range(1, n1):
        for j in range(1, n2):
            print(i, j)
            if s1[i] == s2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i-1][j])

            if dp[i][j] > maxp:
                maxp = dp[i][j]


    print(maxp)


if __name__ == '__main__':
    s1 = 'asdeeee'
    s2 = 'asdfe'
    demo(s1, s2)
