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


import math


class Solution:
    def reverse(self, x: int) -> int:
        if x:
            str_x = str(x)
            if len(str_x) == 0:
                return x
            if x < 0:
                str_x = str(int(math.fabs(x)))
                x = int(str_x[::-1])
                return -1 * x
            str_x = str(x)
            return int(str_x[::-1])


# """ 字符串反转 """
def reverse(content, topN):
    '''
    蛮力法
    :param content:
    :return:
    '''
    t = content[:topN]
    return content[topN:] + t


# """ 字符串反转 """
def reverse2(content, topN):
    pass


def twoSum(nums, target):
    res_dict = dict()  # 建立字典
    for index, i in enumerate(nums):
        key = str(i)
        if key in res_dict:
            res_dict.get(key).append(index)
        else:
            res_dict.update({key: [index] })

    for index, i in enumerate(nums):
        plus = target - i  # 剩余的值
        otherKey = str(plus)
        indexLst = res_dict.get(otherKey)
        # indexLst.remove(index)
        s = indexLst.append(index)
    return s


if __name__ == "__main__1":
    l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    s = solution.reverse(-12333333333333339)
    s = reverse("abcdef", topN=3)
    print(s)

if __name__ == '__main__':
    t = [0,0,2,7,9]
    s = twoSum(t, 9)
    print(s)
