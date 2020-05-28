from typing import List

"""
https://leetcode-cn.com/problems/unique-paths/

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 and n == 0:
            return 0
        if m == 0 and n != 0:
            return 1
        if m != 0 and n == 0:
            return 1
        if m == 1 and n == 1:
            return 2

        all = [[0] * n] * m  # (m列 n行)
        all[0][0] = 0
        for i in range(1, n):
            all[0][i] = 1
        for i in range(1, m):
            all[i][0] = 1

        for col in range(1, m):
            for row in range(1, n):
                all[col][row] = all[col-1][row] + all[col][row-1]
        return all[m-1][n-1]

if __name__ == '__main__':
    m,n = 7,3
    solution = Solution()
    print(solution.uniquePaths(m,n))
