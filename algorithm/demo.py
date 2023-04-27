from typing import List, Optional

"""
给你一个排序（升序）数组，从里面找出来一个数。
时间复杂度为O(log n),但是如果有重复的数，最坏情况下退化成O(n)
其实重复的数组依然可以继续使用二分查找，只是需要判断一下边界即可。
"""

def demo(nums, value):
    if nums is None:
        return None

    n = len(nums)
    left = 0
    right = n - 1

    while left <= right:
        mid = left + (right - left) // 2
        if value < nums[mid]:
            right = mid - 1
        elif value > nums[mid]:
            left = mid + 1
        else:
            if (mid - 1 >= 0 and nums[mid - 1] != value) and (mid + 1 <= n - 1 and nums[mid + 1] != value):
                return mid

            while mid + 1 <= n - 1 and nums[mid + 1] == value:
                mid += 1

            return mid


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 8, 8]
    value = 8
    print(demo(nums, value))
