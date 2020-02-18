# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素
from typing import List


class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        dict_temp = {}
        set_temp = set()
        for i in nums:
            if i not in dict_temp:
                dict_temp.update({i: 1})
            else:
                dict_temp.update({i: dict_temp.get(i) + 1})

        for (i, c) in dict_temp.items():
            if c == 1:
                return i


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a = a ^ i
        return a






if __name__ == '__main__':
    solution = Solution()
    nums = [2, 1, 2, 1, 3]
    print(solution.singleNumber(nums))
