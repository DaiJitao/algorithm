from typing import List, Optional

"""
  123
*   5
------

"""

class Solution():
    def multiply_str_n(self, string, n):
        s = string[::-1]
        pre = 0
        for i in s:
            out = int(i) * n
            if out > 10:
                out // 10

    def demo(self, nums1, nums2):
        if nums1 is None or nums2 is None:
            return None

        if len(nums2) == 0 or len(nums1) == 0:
            return None

        if nums1 == '0' or nums2 == '0':
            return '0'

        n1 = len(nums1)
        n2 = len(nums2)
        max_num = nums1
        short_num = nums2
        if n1 > n2:
            short_num = nums2
            max_num = nums1






