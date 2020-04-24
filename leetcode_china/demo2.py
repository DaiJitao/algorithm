# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素
from typing import List


class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        dict_temp = {}
        set_temp = set()
        for i in nums:
            if i not in dict_temp:
                dict_temp.update({i: 1})
            else:
                dict_temp.update({i: dict_temp.get(i) + 1})

        for (i, c) in dict_temp.items():
            if c == 1:
                return i


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a = a ^ i
        return a


""" 区间合并：https://leetcode-cn.com/problems/merge-intervals/
"""


class Solution3(object):
    def merge(self, intervals: List[List[int]]):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 1:
            return intervals
        if len(intervals) == 0:
            return list()
        intervals.sort(key = lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged:
                merged.append(interval)
            elif merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged






if __name__ == '__main__':
    solution = Solution3()
    l = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]  # [[1,4],[4,5]] # [[1,3],[2,6],[8,10],[15,18]]
    s = solution.merge(l)
    print(s)
