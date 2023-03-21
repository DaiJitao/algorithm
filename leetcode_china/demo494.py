from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return None

        n = len(nums)
        _sum = sum(nums)
        x = (_sum + target) / 2

        dp = [0] * (target + 1)
        for i in nums:
            for j in range(target+1, -1, -1):
                if j >= i:
                    pass

