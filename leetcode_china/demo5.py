# 找出是一个中心点还是两个中心点
def extend(s, left, right):
    result = ""
    while left >= 0 and right < len(s) and s[left] == s[right]:
        result = s[left: right+1]

        left -= 1
        right += 1

    return result


def demo5(s):
    if len(s) <= 1:
        return s

    result = ''
    for i in range(len(s)):

        # 以一个点为中心扩散
        tmp = extend(s, i, i)
        if len(tmp) > len(result):
            result = tmp

        # 处理偶数情况
        tmp = extend(s, i, i + 1)
        if len(tmp) > len(result):
            result = tmp

    return result


if __name__ == '__main__':
    s = '1234'
    print(demo5(s))
