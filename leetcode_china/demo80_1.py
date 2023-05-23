from typing import List, Optional


def demo(nums):
    if nums is None or len(nums) == 0:
        return

    pre = nums[0]
    pcount = 0

    plus = 0
    for i, e in enumerate(nums):
        if e == pre:
            pcount += 1
        else:
            pcount = 1
            pre = e

        if pcount > 2:
            nums[i] = ''
            plus += 1

    print(nums, plus)
    return len(nums) - plus


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 5]
    demo(nums)
