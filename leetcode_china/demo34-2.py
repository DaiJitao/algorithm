from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        n = len(nums)
        if n == 0:
            return [-1, -1]

        left = 0
        right = n - 1
        while 0 <= left <= right < n:
            midd = (left + right) // 2

            if nums[midd] > target:
                right = midd - 1

            elif nums[midd] < target:
                left = midd + 1
            else:
                i, j = midd, midd
                while i >= 1 and nums[i] == nums[i - 1]:
                    i -= 1
                while j < (n - 1) and nums[j] == nums[j + 1]:
                    j += 1
                return [i, j]

        return [-1, -1]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    nums = [1, 4]
    target = 4
    res = Solution().searchRange(nums, target)
    print(res)
