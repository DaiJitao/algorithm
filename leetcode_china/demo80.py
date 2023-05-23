from typing import List, Optional

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None:
            return 0

        n = len(nums)
        temp = nums[0]
        tcount = 1

        i = 1
        e_count = 0
        while i < n:
            if temp == nums[i]:
                tcount += 1
            else:
                temp = nums[i]
                tcount = 1

            if tcount > 2:
                nums[i] = 'e'
                e_count += 1

            # n = len(new_nums)
            i += 1

        for i in range(e_count):
            nums.remove('e')

        return nums


if __name__ == '__main__':
    nums = [0, 0, 0, 0, 1, 1, 1, 2, 2]
    nums = [1, 1, 1, 2, 2, 3]
    p = Solution().removeDuplicates(nums)
    print(p)
