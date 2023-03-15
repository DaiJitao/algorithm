from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == None or len(nums) < 3:
            return []

        nums.sort()

        res = []
        if nums[0] > 0:
            return []
        """
        nums[i] + nums[left] + nums[right]
        """
        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1
            while left < right:
                while left < right  and nums[left] == nums[left + 1]:
                    left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1

        return res


if __name__ == '__main__':
    res = [-1, 0, 1, 2, -1, -4]
    res = [0, 1, 1]
    p = Solution().threeSum(res)

    res.sort()
    print(res)
    print(p)
