from typing import List, Optional

# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0
        n = len(prices)
        if n <= 1:
            return 0
        start = 0
        end = 1
        res = 0
        while k:
            if prices[start] > prices[end]:
                start += 1
                end += 1
            elif prices[start] <= prices[end] and (end + 1) < n and prices[end] <= prices[end + 1]:
                end += 1
            else:
                res += (prices[end] - prices[start])
                start = end + 1
                end = start + 1

            if start >= n or end >= n:
                break
        return res

# 解法2，找窗口内最大值和最小值
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0
        n = len(prices)
        if n <= 1:
            return 0
        start = 0
        end = 1
        res = 0
        while k:
            pass

    def getMax(self, start_idx, prices):


if __name__ == '__main__':
    prices = [2, 4, 1]
    prices = [2,2,5]
    s = Solution()
    res = s.maxProfit(2, prices)
    print(res)

