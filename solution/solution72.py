# encoding=utf8
import sys

"""https://leetcode.cn/problems/edit-distance/solution/zi-di-xiang-shang-he-zi-ding-xiang-xia-by-powcai-3/
"""

class Solution:
    def minDistance(self, arr1: str, arr2: str) -> int:
        n1 = len(arr1)
        n2 = len(arr2)
        if n1 == 0:
            return n2
        if n2 == 0:
            return n1
    
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]  # 列
        for i in range(1, n2 + 1):
            dp[0][i] = dp[0][i - 1] + 1
    
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] + 1
    
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if arr1[i - 1] == arr2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
    
        return dp[-1][-1]
        
        
        
        
def demo74(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]  # 列
    for i in range(1, n2 + 1):
        dp[0][i] = dp[0][i - 1] + 1
    
    for i in range(1, n1 + 1):
        dp[i][0] = dp[i - 1][0] + 1
    
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if arr1[i - 1] == arr2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
    
    return dp[-1][-1]


if __name__ == '__main__':
    arr1 = 'abe'
    arr2 = 'acfg'
    
    word1 = "horse"
    word2 = "ros"
    res = demo74(word1, word2)
    print(res)
