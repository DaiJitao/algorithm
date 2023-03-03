def f(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    if n <= 1:
        return
    i = 2
    while i <= n:
        dp[i] = dp[i - 1] + dp[i - 2]
        i += 1

    return dp[n]


if __name__ == '__main__':
    print(f(5))
