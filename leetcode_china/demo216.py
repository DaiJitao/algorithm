def demo77(_sum, k):
    nums = range(1, 10)
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
    res = demo77(9, 3)
    print(res)
