from typing import List, Optional

"""
对一个有n个元素的数组，求最大的连续子数组的和，并求其开始、结束下标。
数组的元素必然有正数也有负数才有意义，如果全是正数，那最大的子数组就是本身；如果全部为负数，应该是一个最大的元素。
"""
def demo(nums):
    if nums is None or len(nums) == 1:
       return None if  nums is None else nums[0]

    n  = len(nums)
    temp = 0
    maxp = 0
    startIndex = 0
    endIndex = 0
    ts = 0
    for i in range(n):
        temp += nums[i]

        if temp < 0:
            ts = i + 1
            temp = 0
        else:
            if temp > maxp:
                startIndex = ts
                endIndex = i
                maxp = temp

    print(maxp)
    return startIndex, endIndex


if __name__ == '__main__':
    nums = [4, -10, 9, 7, -2, 8, 6, -1, 11]
    print(demo(nums))