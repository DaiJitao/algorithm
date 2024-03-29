# encoding=utf8
import sys


def yihuo(a, b):
    if a == b:
        return 0
    else:
        return


def demo137(arr):
    if len(arr) == 0:
        return None

    if len(arr) <= 3:
        return None

    lst = [0] * 32
    for v in arr:
        bin_v = bin(v)[2:]

        for j, e in enumerate(bin_v[::-1]):
            index = 31 - j
            lst[index] += int(e)

    lst = [str(i % 3) for i in lst]
    return int(''.join(lst), 2)


if __name__ == '__main__':
    arr = [2, 2, 2, 9, 6, 9, 6, 9, 56, 6]
    res = demo137(arr)
    print(res)
