def demo153(nums):
    n = len(nums)
    if n == 1:
        return nums
    elif n == 0:
        return None

    # 未发生旋转
    if nums[0] < nums[-1]:
        return nums[0]

    left = 0
    right = n - 1
    mid = left + int((right - left) / 2)
    while left < right and mid - 1 >= 0 and mid + 1 < n:
        if nums[mid - 1] > nums[mid] < nums[mid + 1]:
            return nums[mid]
        elif nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        elif nums[mid - 1] < nums[mid] < nums[mid + 1] and nums[mid] < nums[-1]:
            right = mid
        elif nums[mid - 1] < nums[mid] < nums[mid + 1] and nums[mid] > nums[-1]:
            left = mid
        else:
            raise Exception()

        mid = left + int((right - left) / 2)
