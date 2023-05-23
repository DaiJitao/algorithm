from typing import List, Optional


def demo(nums, target):
    "pass 判断条件"

    n = len(nums)
    left = 0
    right = n - 1
    while left <= right:
        mid = left + (right-left) // 2

