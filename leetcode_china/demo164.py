import math


def demo164(nums):
    if nums is None:
        return None

    n = len(nums)
    if n <= 1:
        return 0
    if n == 2:
        return abs(nums[0]-nums[1])

    pmax, pmin = max(nums), min(nums)
    arr = [-1] * (pmax + 1)
    for index in nums:
        arr[index] = 1

    temp = None
    first_flag = 0
    max_inter = 0
    print(arr)
    for index, value in enumerate(arr):
        if value == 1:
            if first_flag == 0:
                temp = index
                first_flag += 1
            else:
                if max_inter < index - temp:
                    max_inter = (index- temp)

                temp = index

    return max_inter

if __name__ == '__main__':
    nums = [11, 12, 9, 10, 1, 4, 5]
    res = demo164(nums)
    print(res)


