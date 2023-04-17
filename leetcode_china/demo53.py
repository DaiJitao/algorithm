from typing import List, Optional
import sys

def demo(nums):
    if nums is None:
        return None
    n = len(nums)
    if n <= 1:
        return 0 if n == 0 else nums[0]

    """
    dp【i] 代表从【0， i]中选取一个 达到最大值；
    
    dp[i] = 
    if dp[i-1] + nums[i] > dp[i-1]:
        dp[i-1] + nums[i]
    else:
        dp[i] =  nums[i]
    """
    dp = [0] * (n + 1)
    dp[0] = nums[0]
    pmax = -sys.maxsize
    for i in range(n + 1):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])

