def demo77(n, _sum, k):
    nums = range(1, n + 1)
    path = []
    res = []

    def backtracking(nums, k):
        if len(path) == k and sum(path) == _sum:
            res.append(path[:])
            return

        for index, i in enumerate(nums):
            path.append(i)
            backtracking(nums[index + 1:], k)
            path.pop()

    backtracking(nums, k)
    return res


if __name__ == '__main__':
    n = 10
    res = demo77(n, 3)
    print(res)
