from typing import List


def demo674(nums):
    """
    最长连续递增子序列
    dp[j] 代表以j结尾的最长连续序列
    if nums[j] > nums[j-1]:
    dp[j] = dp[j-1]+nums[j]

    if nums[j] <= nums[j-1]:
    dp[j] = nums[j]
    :param nums:
    :return:
    """
    if nums is None:
        return nums
    if len(nums) <= 1:
        return len(nums)

    dp = [0] * (len(nums) + 1)
    dp[0] = 1
    pmax = 0
    for j in range(1, len(nums)):
        if nums[j] > nums[j - 1]:
            dp[j] = dp[j - 1] + 1
        else:
            dp[j] = 1

        pmax = max(dp[j], pmax)

    return pmax


if __name__ == '__main__':
    nums = [1, 3, 5, 4, 7]
    nums = [2, 2, 2, 2]
    res = demo674(nums)
    print(res)
