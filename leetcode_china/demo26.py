def demo26(nums):
    """
    思路1：
    数组转换为链表，就地删除；
    空间复杂度 O(1)
    时间复杂度 O(n)

    思路2：

    :return:
    """
    n = len(nums)
    p = 0
    q = 1
    while q < n:
        if nums[p] == nums[q]:
            q += 1
        else:
            p += 1
            nums[p] = nums[q]
            q += 1

    return nums[:p + 1]


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 2, 2, 3, 4, 5, 5, 6, 7, 7]
    res = demo26(nums)
    print(res)
