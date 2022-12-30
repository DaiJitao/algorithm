def demo31(nums):
    if nums is None or len(nums) <= 1:
        return []

    # 从右往左找
    n = len(nums)
    i = 0
    for idx in range(n - 1, 0, -1):
        i = idx - 1
        j = idx
        if nums[i] < nums[j]:
            for k in range(n - 1, j - 1, -1):  # 从右边往左边遍历
                if nums[k] > nums[i]:
                    nums[i], nums[k] = nums[k], nums[i]
                    break
            break

    if i > 0:
        p1 = nums[:i + 1]
        p2 = nums[i + 1:][::-1]
        p1.extend(p2)
        return p1
    else:
        return nums[::-1]


if __name__ == '__main__':
    nums = [1, 2, 3, 8, 5, 7, 6, 4]
    nums = [1, 2, 3, 8, 6, 4, 5, 7]
    nums = [1, 2, 3, 8, 6, 4, 7, 5]
    nums = [1, 2, 3, 8, 6, 5, 4, 7]
    print(nums)
    f = demo31(nums)
    print(f)
