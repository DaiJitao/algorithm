from typing import List

"""
https://leetcode-cn.com/problems/container-with-most-water/
提示： 双指针方法
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        超出时间限制
        :param height:
        :return:
        '''
        if height:
            max_area = 0
            size = len(height)
            if size == 1: return max_area
            for i, h in enumerate(height[:-1]):
                for j in range(i + 1, size):
                    width = j - i
                    h_ = min(h, height[j])
                    if (width * h_) > max_area:
                        max_area = width * h_
            return max_area
        return None

if __name__ == '__main__':
    s = Solution()
    l = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea(l))