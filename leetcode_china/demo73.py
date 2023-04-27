from typing import List, Optional


def demo(x, y):
    if x is None or y is None:
        return 0
    n1, n2 = len(x), len(y)
    if n1 == 0 and n2 != 0:
        return n2
    elif n1 != 0 and n2 == 0:
        return n1
    elif n1 == 0 and n2 == 0:
        return 0

    """
    if x[i] == y[j]:
        dp[i][j] = dp[i-1][j-1] 
    else:
        # 增,删
        if x[i] == '' or y[i] == '' :
            dp[i][j] = min(dp[i-1][j]  + 1, dp[i][j-1]  + 1)
        if x[i] ！= '' and y[i] != '' and x[i] ！= y[j]:
            dp[i][j] = dp[i-1][j-1]  + 1
        
    dp[0][0] = 0 if isEqual else 1
    
    """
