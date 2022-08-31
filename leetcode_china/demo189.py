def demo189(nums, k=0):
    n = len(nums)
    if n == 0 or k == 0:
        return nums
    p = k % n
    if p == 0:
        return nums
    temp = {}
    temp['v'] = nums[k]
    temp['index'] = k
    nums[k] = nums[0]
    nums[0] = None
    p = k
    isFinine = False if nums[0] is None else True
    for i in range(1, n-1):
        if temp['v'] == None:
            while not isFinine:
                k = (temp['index'] + p) % n  # 下一个位置
                t = nums[k]
                nums[k] = temp['v']
                temp['v'] = t
                temp['index'] = k

                isFinine = False if None in nums else True

    return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    d = demo189(nums, k=2)
    print(d)
