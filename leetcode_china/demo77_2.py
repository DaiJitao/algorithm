from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0:
            return None

        nums = range(1, n + 1)

        path = []
        res = []

        def backtracking(nums):

            if len(path) == k:
                res.append(path[:])
                return

            for index, i in enumerate(nums):
                path.append(i)
                backtracking(nums[index + 1:])
                path.pop()

        backtracking(nums)
        return res


# def demo77(n, size=2):
#     if n == 0:
#         return None
#
#     nums = range(1, n + 1)
#
#     path = []
#     res = []
#
#     def backtracking(nums, k):
#
#         if len(path) == k:
#             res.append(path[:])
#             return
#
#         for index in range(n):
#             path.append(nums[index])
#             backtracking(nums[index + 1:])
#             path.pop()
#
#
#     backtracking(nums, size)
#     return res


if __name__ == '__main__':
    res = Solution().combine(10, 2)
    print(res)
