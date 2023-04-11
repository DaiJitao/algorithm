from typing import List


def filter(res):
    pass


def demo518(nums, target):
    if nums is None:
        return None

    n = len(nums)
    res = []
    path = []

    def backtracing(startIndex):
        if sum(path) > target:
            return

        if sum(path) == target:
            res.append(path[:])
            return

        for i in range(startIndex, n):
            if sum(path) <= target:
                path.append(nums[i])
            backtracing(0)
            path.pop()

    backtracing(0)
    print(res)


def demo518(coins, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(target + 1):
        for coin in coins:
            if coin <= i:
                continue

if __name__ == '__main__':
    nums = [1, 2, 5]
    target = 5
    demo518(nums, target)
