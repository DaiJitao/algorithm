def demo15(nums):
    n = len(nums)
    if n <= 2:
        return []
    if n == 3:
        if sum(nums) == 0:
            return nums
        else:
            return []

    res = []
    nums = sorted(nums)

    for i in range(n):

        if nums[i] > 0:
            return res

        if i > 0 or nums[i] == nums[i-1]:
            continue

        left = i + 1
        right = n -1
        while left < right:
            while left < right and nums[right] == nums[right-1]:
                right -= 1
            while left < right and nums[left] == nums[left+1]:
                left += 1

            target = sum(nums[i] + nums[left] + nums[right])
            if target == 0:
                res.append([i, left, right])
                left -= 1
                right += 1
            if target < 0:
                left += 1
            elif target > 0:
                right -= 1

    return res


if __name__ == '__main__':
    pass


