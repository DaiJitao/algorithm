from typing import List, Optional

"""
对一个有n个元素的数组，求最大的连续子数组的和，并求其开始、结束下标。
"""
import numpy as np


def demo(nums):
    """
    dp[i] 代表以i结尾的最大连续子数组
    dp[i] = dp[i-1] + nums[i] if dp[i-1] > 0
    = nums[i] else
    :param nums:
    :return:
    """
    end, start = 0, 0
    dp = [0] * (len(nums) + 1)
    maxdp = -np.inf
    dp[0] = nums[0]
    starts = []
    for i in range(1, len(nums)):
        if dp[i-1] + nums[i] > nums[i]:
            tmp = dp[i-1] + nums[i]
        else:
            starts.append(start)
            tmp = nums[i]

        dp[i] = tmp
        if dp[i] > maxdp:
            end = i
            start = starts[0]
            maxdp = dp[i]


    print(maxdp)
    return start, end


if __name__ == '__main__':
    nums = [-9, -1, 2, 3, -1]
    p1, p2 = demo(nums)
    print(p1, p2)
