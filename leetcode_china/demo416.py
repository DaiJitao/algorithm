from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if nums is None or len(nums) <= 1:
            return False

        n = len(nums)
        _sum = sum(nums)
        if _sum % 2 == 1:
            return False

        """
        dp[j]: 容量为j的背包数组和最大值为j
        """
        target = _sum // 2
        dp = [0] * (target + 1)
        for i in nums:
            for j in range(target, -1, -1):
                if i <= j:
                    dp[j] = max(dp[j], dp[j - i] + i)

        if dp[target] == target:
            return True
        return False



if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    res = Solution().canPartition(nums)
    print(res)


