from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        最小值肯定从1开始；
        :param nums:
        :return:
        """
        pmax = max(nums)
        if pmax <= 0:
            return 1

        myset = set(nums)
        for i in range(1, pmax + 1):
            if i not in myset:
                return i

        return pmax + 1



