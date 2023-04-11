from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return nums

        n = len(nums)
        raw_nums = nums[:]
        for i in range(n):
            p = (i + k) % n
            nums[p] = raw_nums[i]

        return nums

if __name__ == '__main__':
    res = Solution().rotate(nums = [1,2,3,4,5,6,7], k = 3)
    print(res)