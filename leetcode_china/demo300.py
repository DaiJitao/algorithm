def demo300(nums):
    if nums is None:
        return []
    n = len(nums)
    if n == 1:
        return 1

    """
    dp[j]:代表从[0,j]中任选一个元素，得到的最长序列的长度为dp[j]
    分两种情况讨论：
    第一，选取一个元素
    if num[j] > num[j-1]: dp[j] = d[j-1] + 1
    第二，不选取元素
    if num[j] <= num[j-1]: dp[j] = dp[j-1]  
    
    """
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n):
        if nums[i] > nums[i-1]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]

    return dp[n-1]

if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    res = demo300(nums)
    print(res)
