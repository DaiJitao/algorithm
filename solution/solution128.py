import math
from typing import List

"""
https://leetcode.cn/problems/longest-consecutive-sequence/solution/ha-xi-zui-qing-xi-yi-dong-de-jiang-jie-c-xpnr/
"""
class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums

        res = 0
        dic = set(nums)
        for x in dic:
            if x - 1 not in dic:
                y = x
                while y + 1 in dic: y += 1
                res = max(res, y - x + 1)

        return res


if __name__ == '__main__':
    arr = [1, 4, 7, 9, 10, 11, 2, 3, ]
    res = Solution().longestConsecutive(nums=arr)
    print(res)
