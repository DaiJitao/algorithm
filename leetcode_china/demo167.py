def demo167(nums, target):
    if nums == None or len(nums) == 0:
        return None

    n = len(nums)
    if n == 1:
        return None

    left = 0
    right = n - 1
    while left < right:
        _sum = nums[left] + nums[right]
        if _sum > target:
            right -= 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

        elif _sum < target:
            left += 1
            while left < right and nums[left] == nums[left + 1]:
                left += 1
        else:
            return [left + 1, right + 1]

if __name__ == '__main__':
    nums = [2, 3, 4, 15]
    target = 7
    res = demo167(nums, target)
    print(res)