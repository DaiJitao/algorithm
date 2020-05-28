"""
https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
提示：
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0:
            return None
        if len(nums2) == 0:
            return None
        size1 = len(nums1)
        size2 = len(nums2)
        if size2 <= size1:
            pass