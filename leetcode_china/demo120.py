from typing import List, Optional
import sys

"""
   2
  3 4
 6 5 7
4 1 8 3
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle is None or len(triangle) == 0:
            return
        n = len(triangle)
        if n == 1:
            return triangle[0][0]

        res = [0] * n
        res[0] = triangle[0][0]
        pmin = sys.maxsize
        pre_res = res[0]
        for row, arr in enumerate(triangle[1:]):
            for index, i in enumerate(arr):
                if index == 0:
                    temp = res[0]
                    res[0] = res[0] + i

                elif index == len(arr) - 1:
                    res[index] = i + pre_res

                else:
                    temp = res[index]
                    res[index] = min(pre_res, res[index]) + i

                pre_res = temp
                if row == n - 2:
                    if res[index] < pmin:
                        pmin = res[index]
        return pmin


if __name__ == '__main__':
    t = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    t = [[-1], [2, 3], [1, -1, -3]]
    res = Solution().minimumTotal(t)
    print(res)
