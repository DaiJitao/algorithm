from typing import List, Optional

"""
逝水无痕
给定一个长度为n的数组，找出其中出现次数大于数组长度1/2的那个数， 该数肯定存在;
"""


class Solution1:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]

        temp = nums[0]
        count = 0
        for i in nums:
            if i == temp:
                count += 1
            else:
                count -= 1
                if count == 0:
                    temp = i
                    count += 1

        return temp


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return
        n = len(nums)
        if n == 1:
            return nums[0]

        count = 0
        for i in nums:
            if count == 0:
                temp = i
                count += 1

            else:
                if temp != i:
                    count -= 1
                else:
                    count += 1
        return temp


if __name__ == '__main__':
    nums = [1, 2, 6, 6, 6, 6, 6, 6, 2, 2, 3, 4, 5, 6, 6, 6, 6, 7, 6, 1]
    nums = [1, 1, 1, 2, 2]
    print(len(nums))
    res = Solution1().majorityElement(nums)
    print(res)
