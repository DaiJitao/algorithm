from typing import List, Optional


def swap(nums, i, j):
    # i = 4
    # j = 3
    nums[i], nums[j] = nums[j], nums[i]


def demo41(nums):
    if None is nums:
        return None

    if len(nums) == 1:
        if nums[0] <= 0:
            return 1
        elif nums[0] == 1:
            return 2
        else:
            return nums[0] - 1
    # 元素为 element, 对应下标应为 element-1 也即 num[i-1] = i
    for i in range(len(nums)):  # i为下标
        while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
            swap(nums, i, nums[i]-1)

    for i in range(len(nums)):
        if i != nums[i] - 1:
            return i+1


if __name__ == '__main__':
    nums = [-9, 10, 1, 3, 2, 6]
    res = demo41(nums)
    print(res)
