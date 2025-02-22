# -*- coding: utf-8 -*-
# @Author  : NLPCoder
# @Time    : 2025/2/22 12:59
# @Function: 


from typing import List, Optional
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        f = [0] * len(nums)
        f[0] = nums[0]
        maxnum = min(nums)
        for i in range(1, len(nums)):
            f[i] = max(f[i-1] + nums[i], nums[i])
            if f[i] > maxnum: maxnum = f[i]

        return maxnum

if __name__ == '__main__':
    nums = [5,4,-1,7,8]
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [-2,-1]
    s = Solution()
    print(s.maxSubArray(nums))

