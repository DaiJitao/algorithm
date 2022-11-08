def demo169(nums):
    prior = nums[0]
    count = 0
    for e in nums:
        if e == prior:
            count += 1
        else:
            count -= 1
            if count == 0:
                prior = e
                count = 1

    return prior


if __name__ == '__main__':
    rs = [3, 3, 2, 3, 3, 4, 4]
    rs = demo169(rs)
    print(rs)
