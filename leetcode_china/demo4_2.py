def get_midd(nums):
    n = len(nums)
    if n % 2 == 0:  # 偶数
        i = n // 2
        return (nums[i] + nums[i - 1]) / 2
    else:
        i = n // 2
        return nums[i]


def demo(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    if n1 == 0 and n2 == 0:
        return []
    if n1 == 0 or n2 == 0:
        return get_midd(nums1 if n2 == 0 else nums2)

    n = n1 + n2
    if n % 2 == 0:  # 偶数
        k = n // 2  # 第k个数，即小标为k-1(inde=k-1)即为所求;第k个小的数，前面有k-1个数
        
    else:
        pass
