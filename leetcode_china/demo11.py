def demo11(height):
    """双循环"""
    m = len(height)
    if m <= 1:
        return 0
    if m == 2:
        return max(height)

    _max = 0
    for j in range(m - 1):
        for i in range(j + 1, m):
            w = (i - j)
            h = min(height[j], height[i])
            if _max < w * h:
                _max = w * h

    return _max


# 双指针
def demo11(height):
    """
    水槽的面积取决于短板，若要移动短板，面积可能变大也可能变小；但是，移动长板，面积一定变小，不会给予变大的机会；
    :param height:
    :return:
    """
    m = len(height)
    if m <= 1:
        return 0
    if m == 2:
        return max(height)

    i = 0
    j = m - 1
    res = 0
    while i < j:
        left = height[i]
        right = height[j]
        if left < right:
            res = res if res > (j - i) * left else (j - i) * left
            i += 1
        else:
            res = res if res > (j - i) * right else (j - i) * right
            j -= 1

    return res


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # height = [1, 1]
    res = demo11(height)
    print(res)
