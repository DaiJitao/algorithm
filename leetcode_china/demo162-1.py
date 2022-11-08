def demo162(nums):
    if nums is None:
        return
    n = len(nums)
    if n <= 2:
        return

    left = 0
    right = n - 1
    midd = left + (right - left) // 2
    while 1 < midd < n - 1:
        if nums[midd - 1] < nums[midd] > nums[midd + 1]:
            return midd

        elif nums[midd - 1] <= nums[midd] <= nums[midd + 1]:
            left = midd

        elif nums[midd - 1] >= nums[midd] >= nums[midd + 1]:
            right = midd

        midd = left + (right - left) // 2


if __name__ == '__main__':
    nums = [1, 2, 1, 3, 4, 5, 3, 4, 2]
    nums = [17, 16, 24, 14, 11, 6, 5, 11, 3, 2, 1]
    res = demo162(nums)
    print(res)
