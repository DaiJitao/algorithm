def demo201(left, right):
    """暴力解法：O(n) """
    while left < right:
        right &= (right - 1)

    return right

if __name__ == '__main__':
    left = 4
    right = 7
    res = demo201(left, right)
    print(res)


if __name__ == '__main__1':
    left = 1985
    right = 789456
    bin_right = bin(right)
    n = len(bin_right[2:])
    bin2num = {}
    for i in range(left, right + 1):
        pos = bin(i)[2:]
        plus = n - len(pos)
        if plus > 0:
            p = '0' * plus
        else:
            p = ''
        res = p + pos
        # 把每一位遍历一遍
        for i in range(n):
            if i in bin2num:
                bin2num[i].add(res[i])
            else:
                bin2num[i] = set(res[i])

    print(bin2num)
