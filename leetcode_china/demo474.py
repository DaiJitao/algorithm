from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if strs is None or len(strs) == 0:
            return None

        mydict = {}
        size = len(strs)
        for s in strs:
            pm = sum([1 for i in s if i == 0])
            pn = sum([1 for i in s if i == 1])
            mydict[s] = (pm, pn)

        inner = [0] * size
        mrow = [0] * (m + 1)
        ncol = [0] * (n + 1)
        dp = [[ncol[:] for _ in mrow][:] for _ in inner]
        for i in range(1, size):
            s = strs[i]
            pm, pn = mydict[s]
            for j in range(1, m + 1):
                for k in range(1, n + 1):
                    if pm <= j and pn <= k:
                        dp[i][j][k] = dp[i - 1][j - pm][k - pn]
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]

        return dp[size - 1][m][n]


if __name__ == '__main__':
    res = ["10", "0001", "111001", "1", "0"]
    # 5:0, 3:1
    res = Solution().findMaxForm(res, m=5, n = 3)
    print(res)
