def demo300(nums):
    n = len(nums)
    if n == 0:
        return None
    elif n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1
    for j in range(0, n - 1):
        for i in range(j + 1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1]

    return dp[n - 1]


def demo172(n):
    p = 1
    for i in range(2, n + 1):
        p = p * i

    # print(p)
    return p


if __name__ == '__main__':
    for i in range(3, 21):
        print('{}={}'.format(i, demo172(i)))


