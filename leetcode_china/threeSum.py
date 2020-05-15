from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums:
            res = []
            nums.sort()
            for index, i in enumerate(nums):
                target = -i
                if index >= 1 and i == nums[index - 1]:
                    continue
                j = index + 1
                k = len(nums) - 1  # 最后一个元素
                while (j < k):
                    if nums[j] + nums[k] == target:
                        res.append([index, j, k])
                        j += 1; k -= 1

                    elif nums[j] + nums[k] > target:
                        j += 1
                    else:
                        k -= 1


        return []
