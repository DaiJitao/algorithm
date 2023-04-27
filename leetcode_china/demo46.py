from typing import List, Optional


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return None
        n = len(nums)

        path = []
        res = []
        def backtracing(nums, skipIindex):
            if len(path) == n:
                res.append(path[:])
                return

            for index, i in enumerate(nums):
                path.append(i)
                tmp = nums[:index] + nums[index+1:]
                backtracing(tmp, skipIindex=i)
                path.pop()


        backtracing(nums, skipIindex=None)
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return None
        n = len(nums)

        path = []
        res = []
        used = [False] * n
        def backtracing(nums, used):
            if len(path) == n:
                res.append(path[:])
                return

            for index, i in enumerate(nums):
                if used[index] == True:
                    continue
                path.append(i)
                used[index] = True
                backtracing(nums, used)
                path.pop()
                used[index] = False


        backtracing(nums, used)
        return res

if __name__ == '__main__':
    nums = [1, 2, 3]
    # nums = [1, 0]
    r = Solution().permute(nums)
    print(r)