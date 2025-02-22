from typing import List, Optional

"""
https://leetcode.cn/problems/assign-cookies/description/
"""


class Solution:
    # g 孩子； s 饼干
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0 or len(g) == 0:
            return 0

        num = 0
        g.sort()
        s.sort()
        index = len(s) - 1  # 饼干
        for i in g[::-1]:
            if (index >= 0 and s[index] >= i):
                num += 1
                index -= 1

        return num


if __name__ == '__main__':
    g = [1, 2, 3]
    s = [3]
    fun = Solution().findContentChildren
    print(fun(g, s))
    # for i in range(9, -1, -1):
    #     print(i)
