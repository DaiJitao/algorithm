from typing import List, Optional


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums is None:
            return 0

        n = len(nums)
        pmax, pmin = max(nums), min(nums)
        """
        通过hash存储一下，存在继续，不存在找到下个值:这样做会超出时间限制
        """
        temp = dict()
        for i in nums:
            temp[i] = 1

        maxlen = 0
        res = 0
        for i in range(pmin, pmax + 1):
            if i in temp:
                maxlen += 1
                if res < maxlen:
                    res = maxlen
            else:
                maxlen = 0

        return res


# ------------------
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        hash_dict = dict()
        res = 0
        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)
                length = left + 1 + right
                hash_dict[num] = length
                res = max(res, length)
                hash_dict[num-left] = length
                hash_dict[num+right] = length

        return res


if __name__ == '__main__':
    nums = [100, 2, 3, 43, 44, ]
    res = Solution().longestConsecutive(nums)
    print(res)
