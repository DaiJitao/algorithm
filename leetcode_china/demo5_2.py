from typing import List


def demo5(s):
    if s is None:
        return None

    if len(s) <= 1:
        return 3

    # 中心扩展法
    n = len(s)
    max_s = s[0]

    for i in range(1, n - 1):
        leftindex = i - 1
        rightindex = i + 1
        res = s[i]


        if s[i] == s[rightindex]:
            res += s[rightindex]
            rightindex += 1
        elif s[i] == s[leftindex]:
            res = s[leftindex] + res
            leftindex -= 1

        while leftindex >= 0 and rightindex < n and s[leftindex] == s[rightindex]:
            res = s[leftindex] + res
            res = res + s[rightindex]
            leftindex -= 1
            rightindex += 1
            if leftindex < 0 or rightindex >= n:
                break


        if len(max_s) < len(res):
            max_s = res

    return max_s

if __name__ == '__main__':
    s = 'gcbcf'
    s = 'babad'
    s = 'fabbafff'
    s = 'ggggfff'
    s = '123456'
    res = demo5(s)
    print(res)

