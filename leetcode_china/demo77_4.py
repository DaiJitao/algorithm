from typing import List


def demo77(n, k):
    if n == 0 or k == 0:
        return []

    path = []
    res = []

    arr = list(range(1, n + 1))
    print(arr)

    def backtracing(arr):
        if len(path) == k:
            res.append(path[:])
            return

        for index, i in enumerate(arr):
            path.append(i)
            backtracing(arr[index + 1:])
            path.pop()

    backtracing(arr)
    return res


if __name__ == '__main__':
    n = 10
    k = 2
    res = demo77(n, k)
    print(res)
