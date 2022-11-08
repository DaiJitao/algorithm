def demo162(nums):
    n = len(nums)
    if n == 0:
        return None

    if n < 3:
        return None
    left = 0
    right = n - 1
    i = int(n / 2)
    while i > 0 and i < (n - 1):
        i = left + int((right - left) / 2)
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return i

        elif nums[i] > nums[i - 1] and nums[i] <= nums[i + 1]:
            left = i

        elif nums[i] < nums[i - 1] and nums[i] >= nums[i + 1]:
            right = i


if __name__ == '__main__':
    nums = [17, 16, 24, 14, 11, 6, 5, 11, 3, 2, 1]
    res = demo162(nums)
    print(res)
