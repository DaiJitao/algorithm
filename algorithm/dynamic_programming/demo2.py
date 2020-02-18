"""一个数组不相邻数组最大值"""

import numpy as np
def solution(n, data):
    if n == 2:
        return max(data)
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = data[0]
    for i in range(2, n):
        f[i] = max(f[i - 1], data[i] + f[i - 2])

    return f[i]


def randomn(n):
    s = [0] * n
    s[0] = 1
    for i in range(1, n):
        temp = (314159269 * s[i - 1] + 453806245)
        M = np.power(2,31)
        t = np.mod(temp, M)
        print(t)

def max_sum_fun(array):
    """连续最大子数组的和"""

    if array:
        max_sum = 0
        f = [0] * len(array)
        f[0] = array[0]
        for i in range(1,len(array)):
            f[i] = max(0, f[i-1]+array[i])
            if f[i] > max_sum:
                max_sum = f[i]

    return max_sum


if __name__ == '__main__':
    data = [12, 6, 4, 11, 23, 10, 8, 5, 14, 13, 15, 14, 5, 7, 21, 22, 9, 10]
    data = [12, 3, 0, 0, 2, 2, 0, 0, 9, 0, 1, 100]
    res = solution(n=len(data), data=data)
    array = [1,7,-7,-9,21,11,4,9,23,-3]
    print(max_sum_fun(array))
