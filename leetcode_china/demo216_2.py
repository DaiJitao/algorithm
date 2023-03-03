from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))

        res = []
        path = []
        def backtracking(nums, k):
            if len(path) == k and sum(path) == n:
                res.append(path[:])
                return

            for index, i in enumerate(nums):
                path.append(i)
                backtracking(nums[index+1:], k)
                path.pop()

        backtracking(nums, k)


        return res

if __name__ == '__main__':
    res = Solution().combinationSum3(k=4, n=1)
    print(res)