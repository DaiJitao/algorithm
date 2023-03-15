from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        _sum = sum(stones)
        target = _sum // 2
        dp = [0] * (target + 1)
        for i, e in enumerate(stones):
            for j in range(target, -1, -1):
                if j >= stones[i]:
                    dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])

        print(dp)
        return _sum - dp[target] - dp[target]

if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    res = Solution().lastStoneWeightII(stones)
    print(res)