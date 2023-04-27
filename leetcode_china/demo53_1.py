from typing import List, Optional
import sys


class Solution:
    def max_(self, nums, i, j):
        maxsize = 0
        index = 0
        for t_index, p in enumerate(nums):
            if t_index < i or t_index > j:
                break
            elif t_index >= i and t_index <= j:
                if maxsize < p:
                    maxsize = p
                    index = t_index

        return index, maxsize

    def canJump(self, nums: List[int]) -> bool:
        if nums is None:
            return False
        n = len(nums)
        if n == 1:
            True

        i = 0
        size = nums[i]
        # 从 [i+1, i+size]找最大值
        while size > 0 and i <= (n - 1):
            if (i + size) >= (n - 1):
                return True

            i, maxsize = self.max_(nums, i + 1, i + 1 + size)

        return False


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    res = Solution().canJump(nums)
    print(res)
