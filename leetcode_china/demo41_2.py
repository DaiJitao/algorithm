from typing import List, Optional


class Solution(object):

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def demo(self, nums):
        if nums is None:
            return None

        n = len(nums)
        """放到合理的位置
        假设nums[i] 为 元素 value
        value 所在的下标应为 value-1 才合理: value = nums[value-1]    
        """
        for i in range(n):
            value = nums[i]
            # 应为下标
            index = value - 1
            while index >= 0 and index < n and nums[index] != value:
                self.swap(nums, index, i)
                value = nums[i]
                index = value - 1

        for index, e in enumerate(nums):
            if index + 1 == e:
                continue
            else:
                return index + 1

        return nums[-1] + 1

if __name__ == '__main__':
    nums = [3,4,-1, 1, 2 , 6]
    nums = [1, 2, 0]
    s = Solution().demo(nums)
    print(s)


