"""
https://leetcode-cn.com/problems/longest-consecutive-sequence/
https://leetcode-cn.com/problems/longest-consecutive-sequence/
"""
from typing import List




class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            if (len(nums)) == 1:
                return 1

            mv = max(nums)
            for i in range(mv+1):
                d = {i: []}
            for i in nums:
                v = d.get(i)
                v.append(i)

        return 0
