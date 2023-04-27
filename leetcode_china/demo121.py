from typing import List, Optional
import math
import numpy as np

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if nums is None:
            return 0
        n = len(prices)
        if n == 1:
            return 0

        minprice = np.inf
        maxplus = 0
        for i in prices:
            if i < minprice:
                minprice = i
                continue

            if (i - minprice) > maxplus:
                maxplus = i - minprice

        return maxplus

if __name__ == '__main__':
    nums = [7,1,5,3,6,4]
    nums = [7,6,4,3,1]
    res = Solution().maxProfit(prices=nums)
    print(res)