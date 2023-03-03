

'''
dp[n] 代表到台阶n的总不同种的走法

dp[1] 1种走法
dp[2] 2种走法
dp[3] 1台阶 + 1 台阶 + 1台阶
      1台阶 + 2台阶
      2台阶 + 1台阶

dp[n] = dp[n-1] + dp[n-2]
'''

def f(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    if n == 0:
        return 0
    if n <= 2:
        return dp[n]
    i = 3
    while i <= n:
        dp[i] = dp[i - 1] + dp[i - 2]
        i += 1

    return dp[n]

print(f(5))