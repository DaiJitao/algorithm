def demo33(nums, target):
    if not nums:
        return -1

    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        if target == nums[0]:
            return 0
        else:
            return -1

    left = 0
    n = len(nums)
    right = n - 1

    if nums[left] > nums[right]:  # 存在旋转
        while left < right:
            midd = (right + left) // 2
            if nums[midd] == target:
                return midd

            if nums[0] <= nums[midd]:
                # 有序部分
                if nums[0] <= target < nums[midd]:
                    right = midd - 1
                else:
                    left = midd + 1
            else:# 无序部分
                if nums[midd] < target <= nums[n-1]:
                    left = midd + 1
                else:
                    right = midd - 1

        return -1

    else:
        # 不旋转
        pass


if __name__ == '__main__':
    nums = [11, 13, 14, 15, 1, 2, 4, 5, 9]
    target = 2
    res = demo33(nums, target)
    print(res)
