"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

from typing import List


class Solution1(object):
    def max_sumarray(self, array):
        size = len(array)
        if size == 1:
            return array[0]
        f = [0] * size
        f[0] = array[0]
        for i in range(1, size):
            f[i] = max(f[i - 1] + array[i], array[i])
        return max(f)


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0:
            return ""
        if len(s) > 1000:
            return "error"
        if len(s) == 1:
            return s


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]

        dp[0] = nums[0]
        for i in range(1, size):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


if __name__ == "__main__":
    l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution();
    s = solution.maxSubArray(l)
    print(s)
    solution = Solution1()
    s = solution.max_sumarray(l)
    print(s)
