def demo4(nums1, nums2):
    m, n = len(nums1), len(nums2)
    if m == n == 0:
        return None

    if m == 0:
        if n % 2 == 1:
            return nums2[n // 2]
        else:
            return (nums2[n // 2] + nums2[n // 2 - 1]) / 2
    if n == 0:
        if m % 2 == 1:
            return nums1[m // 2]
        else:
            return (nums1[m // 2 - 1] + nums1[m // 2]) / 2

    def get_K_element(k):
        index1 = 0
        index2 = 0
        while True:
            if index1 == m:
                pass
            if index2 == index2:
                pass

            newIndex1 = min(k // 2 - 1, m - 1)
            newIndex2 = min(k // 2 - 1, n - 1)
            if nums1[newIndex1] <= nums2[newIndex2]:
                k = k - newIndex1 - index1 + 1
                index1 = newIndex1 + 1
            else:
                k = k - newIndex2 - index2 + 1
                index2 = newIndex2 + 1

    totalLen = n + m
    if totalLen % 2 == 1:  # 奇数
        k = totalLen // 2

    else:  # 偶数
        pass
